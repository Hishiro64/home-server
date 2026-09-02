# 🍵 Migrating From Years Old Gitea Instance 

> [!CAUTION]
> Incomplete Draft, Don't Use.

This is for people who have a Gitea instance running for several years pinned on a tag.

Since then, environment variables have changed around and breaking changes have been introduced. Jumping to the latest stable on the existing stack could create *problems*. You could manually stagger update through each minor release, but that's a lot of reading on intermediate releases, room for error, and you'll be updating the compose file for each minor release, when only the last one is maintained.

A safer alternative would be to close off and slate the existing instance. Create a new compose file based on latest stable on a fresh new stack, then migrate every repository manually (or use a [Gitea Importer CLI](https://gitea.com/gitea/importer) when it's usable). This should cover most peoples use cases.

I'll be using `gitea:1.21.11` as an example. Since this is such an old release, Docs are not easily accessible. The compose file was edited from the example template at the time. If you need old docs, you can find them [here](https://dl.gitea.com/gitea/). They exist as tar archives, like the such: `gitea-docs-1.21.11.tar.gz`. The latest release at the time of writing is `gitea:1.27.3`. We'll be migrating to that. You should use target whatever is the latest stable.

## Slate the current Gitea instance

1. This is what is currently deployed on the compose project:

    ```yml
    version: "3"
    services:
      gitea:
        container_name: gitea
        image: gitea/gitea:1.21.11
        restart: always
        ports:
          - "10010:10010"
          - "2222:22"
        volumes:
          - /srv/stacks/gitea/data:/data
          - /etc/timezone:/etc/timezone:ro
          - /etc/localtime:/etc/localtime:ro
        environment:
          - APP_NAME=Gitea
          - GITEA__ui__DEFAULT_THEME=arc-green
          - USER_UID=1000
          - USER_GID=1000
          - GITEA__database__HOST=192.168.1.200:10010
          - GITEA__server__ROOT_URL=http://192.168.1.200:10010/
          - GITEA__server__HTTP_PORT=10010
          - GITEA__server__SSH_DOMAIN=192.168.1.200
          - GITEA__server__SSH_PORT=2222
          - GITEA__server__DOMAIN=192.168.1.200
          - GITEA__server__OFFLINE_MODE=true
          - GITEA__server__LFS_START_SERVER=true
          - GITEA__lfs__PATH=/data/lfs
          - GITEA__openid__ENABLE_OPENID_SIGNIN=false
          - GITEA__openid__ENABLE_OPENID_SIGNUP=false
          - GITEA__service__NO_REPLY_ADDRESS=noreply-gitea.192.168.1.200
          - GITEA__service__DEFAULT_KEEP_EMAIL_PRIVATE=true
          - GITEA__service__DISABLE_REGISTRATION=true
          - GITEA__service__DISABLE_REGISTER_EMAIL_CONFIRM=false
          - GITEA__service__DISABLE_ALLOW_ONLY_EXTERNAL_REGISTRATION=false
          - GITEA__mailer__ENABLED=false
        security_opt:
          - no-new-privileges:true
    ```

2. We want to first stop the container.

3. Make a backup of the data directory:
    ```bash
    sudo cp -a /srv/stacks/gitea /srv/stacks/samba/Serva/gitea.backup
    ```

4. Rename the existing mount:
    ```bash
    cd /srv/stacks ; sudo mv gitea/ old-gitea
    ```

5. Modify the stack with non-conflicting values:

    ```yml
    version: "3"
    services:
      old-gitea:
        container_name: old-gitea
        image: gitea/gitea:1.21.11
        restart: always
        ports:
          - "3001:3001"
          - "2223:22"
        volumes:
          - /srv/stacks/old-gitea/data:/data
          - /etc/timezone:/etc/timezone:ro
          - /etc/localtime:/etc/localtime:ro
        environment:
          - APP_NAME=Old-Gitea
          - GITEA__ui__DEFAULT_THEME=arc-green
          - USER_UID=1000
          - USER_GID=1000
          - GITEA__database__HOST=192.168.1.200:3001
          - GITEA__server__ROOT_URL=http://192.168.1.200:3001/
          - GITEA__server__HTTP_PORT=3001
          - GITEA__server__SSH_DOMAIN=192.168.1.200
          - GITEA__server__SSH_PORT=2223
          - GITEA__server__DOMAIN=192.168.1.200
          - GITEA__server__OFFLINE_MODE=true
          - GITEA__server__LFS_START_SERVER=true
          - GITEA__lfs__PATH=/data/lfs
          - GITEA__openid__ENABLE_OPENID_SIGNIN=false
          - GITEA__openid__ENABLE_OPENID_SIGNUP=false
          - GITEA__service__NO_REPLY_ADDRESS=noreply-gitea.192.168.1.200
          - GITEA__service__DEFAULT_KEEP_EMAIL_PRIVATE=true
          - GITEA__service__DISABLE_REGISTRATION=true
          - GITEA__service__DISABLE_REGISTER_EMAIL_CONFIRM=false
          - GITEA__service__DISABLE_ALLOW_ONLY_EXTERNAL_REGISTRATION=false
          - GITEA__mailer__ENABLED=false
        security_opt:
          - no-new-privileges:true
    ```
    #### More information
    These values have to be different since we don't want any existing workspace to point to the slated instance.
    
    For example with local repositories, inside of `.git/config`
    ```ini
    [remote "origin"]
        url = http://192.168.1.200:10010/Hishiro/test-repo # points to slate if port not changed
        fetch = +refs/heads/*:refs/remotes/origin/*
    ``` 
    Same thing goes for the mounts and identifiers for distinguishability. 

6. Run it and make sure it's still healthy. 

7. Now stop the container again. 

8. Remove the container.

9. In portainer, Under stack details -> Stack duplication / migration 

    ```
    Stack Name: old-gitea
    Select...: Server
    ```
    Then duplicate it.

10. Run the container

We should now have a separate stack called "old-gitea" running our slated Gitea instance with everything prefixed as "old". Any local repositories won't be able to contact remote. This puts a pause until Gitea and repository migrations are complete.

## Deploy a fresh Gitea instance on latest stable.

Under our stack called "gitea" we can now update our stack identically to how it was before. When creating this new compose, you only need to read up on the latest stable docs. 

1. Create the primary directories like before:

    ```bash
    cd /srv/stacks ; mkdir -p ./gitea/data
    ```

2. Update the compose file targeting latest stable:
    ```yml
    services:
      gitea:
        container_name: gitea
        image: docker.gitea.com/gitea:1.27.3
        restart: always
        ports:
          - "10010:3000"
          - "2222:22" # Change right hand to port 2222 paired with commenting in the ssh section in env
        volumes:
          - /srv/stacks/gitea/data:/data
          - /etc/timezone:/etc/timezone:ro
          - /etc/localtime:/etc/localtime:ro
        environment:
          - USER_UID=1000
          - USER_GID=1000
          # Added
          - APP_NAME=Tea
          # Enable this to migrate from slated Gitea instance
          - GITEA__migrations__ALLOW_LOCALNETWORKS=true
          # SMTP
          - GITEA__mailer__ENABLED=true
          - GITEA__mailer__PROTOCOL=smtp
          - GITEA__mailer__SMTP_ADDR=192.168.1.200
          - GITEA__mailer__SMTP_PORT=1025
          - GITEA__mailer__FROM=gitea@server.home.arpa
          - GITEA__mailer__USER=Gitea
          - GITEA__mailer__PASSWD=none
          # Mail
          - GITEA__service__ENABLE_NOTIFY_MAIL=true
          - GITEA__service__REGISTER_EMAIL_CONFIRM=false
          - GITEA__service__DEFAULT_KEEP_EMAIL_PRIVATE=false
          - GITEA__service__NO_REPLY_ADDRESS=users.noreply.gitea.server.home.arpa
          # openid
          - GITEA__openid__ENABLE_OPENID_SIGNIN=false
          - GITEA__openid__ENABLE_OPENID_SIGNUP=false
          # server
          - GITEA__server__OFFLINE_MODE=true
          - GITEA__server__LFS_START_SERVER=true
          # ssh
          #- GITEA__server__START_SSH_SERVER=true
          #- GITEA__server__SSH_LISTEN_PORT=2222
          #- GITEA__server__SSH_PORT=2222
    ```

3. Start the container

4. Do initial setup and create the administrator account. Use the same username and email as the slated instance.
 
You should now have a fresh instance of Gitea running on the latest stable. All endpoints like mounts and ports are the same.

## Migrate repositories

1. Inside of Gitea make a new migration.

2. Use either:
    ```python
    1. "Git - Migrate a repository only from any Git service." 
    or 
    2. "Gitea - Migrate data from gitea.com or other Gitea instances."
    ```

3. Then one by one migrate each repository from the slated instance. If it has LFS, then enable it for the repo. If it has Issues, Pull Requests, Releases, etc... make sure to use the Gitea migration specifically with an Access Token.


## Gitea Access Token

If you selected the latter you can use an Access Token to migrate the additional items. 

You can create one in: 

> User -> Settings -> Applications ->  Manage Access Tokens ->  Generate New Token

Select read for all the permissions and copy the token and use that during each repository migration.

## Delete the slated instance

You will have the slated instance and the new instances running alongside each other. If done correctly, everything should work as expected as if nothing has changed. You should not push or pull from the slated instance and only use the new one from here on. Then after some time, you should stop running the slated instance and either safely archive or permanently delete `old-gitea` and `gitea.backup`. 

From now on, regularly maintain the stack through every minor release to avoid having to go through all of this again. 




