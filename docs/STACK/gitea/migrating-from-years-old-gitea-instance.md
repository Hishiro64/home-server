# 🍵 Migrating from Years Old Gitea Instance 

> [!CAUTION]
> Incomplete Draft, Don't reference.

This is for people who have a Gitea instance running for several years pinned on a tag.

Since then, environment variables have changed around and breaking changes have been introduced. Jumping directly to the latest stable on the existing stack could create *problems* which you don't want to find out since you're already reading this. The suggested approach would be to manually update through each minor release back to back, reviewing the changes and migration notes each time. This would mitigate the likelihood of unforeseen problems outside our control. You may be on a release that's a few years old, thus that route would be in advised. Outside of changelogs, docs are not readily accessible for very old releases. Successfully updating the compose file, reviewing each intermediate deployment, and sanity checking each time, may not be doable. It's also not worth you data and risking your infrastructure.

A safer alternative would be to close off and slate the existing instance. Create a new compose file based on latest stable on a fresh new stack, then migrate every repository manually (or use the [Gitea Importer CLI](https://gitea.com/gitea/importer) when it's usable). A repository and content migration should cover most peoples use cases. It would be wise to treat this migration as if you are switching git providers. For such a large jump, you will have to review everything from scratch anyway.

I'll be using `gitea:1.21.11` as an example. It's a little over 2 years old. Since this is an ancient release, Docs can be found as tar archives, like the such: `gitea-docs-1.21.11.tar.gz`. If you need old docs, you can find them [here](https://dl.gitea.com/gitea/). The compose file was edited from the example template at the time. We'll be migrating to the latest release, which at the time is `gitea:1.27.3`. Replace `1.27.3` with the current stable release on your end.

## Slate the Current Gitea Instance

We will mark our current instance to be slated by prefixing it with "old" and removing endpoint access.

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
    These values have to be different since we don't want any users or existing workspaces to get pointed to the slated instance. Nothing should have to change on any local repositories. Users should never be asked to change anything on their end.
    
    For example with local repositories, inside `.git/config`
    ```ini
    [remote "origin"]
        url = http://192.168.1.200:10010/Hishiro/test-repo # Expects this to be the up to date remote 
        fetch = +refs/heads/*:refs/remotes/origin/*
    ``` 
    Same thing goes for the mounts and identifiers for distinguishability. 

6. Run it and make sure it's still healthy. 

7. Now stop the container again. 

8. Remove the container.

9. Step only applies to Portainer, Under stack details -> Stack duplication / migration 

    ```
    Stack Name: old-gitea
    Select...: Server
    ```
    Then duplicate it. This is so it doesn't have a naming conflict with the compose project.

10. Run the container

We should now have a separate stack called "old-gitea" running our slated Gitea instance with everything prefixed as "old". Any local repositories won't be able to contact remote and users will see an "Unable to connect". This puts a pause until Gitea, user, and repository migrations are complete.

## Deploy a Fresh Gitea Instance on Latest Stable.

Under our stack called "gitea" we can now update our stack identically to how it was before. When creating this new compose, you only need to read up on the latest stable docs. 

1. Create the primary directories seen in the original compose file:

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
          # Enable this to migrate from a slated Gitea instance
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
 
You should now have a fresh instance of Gitea running on the latest stable. All endpoints like mounts and ports are the same. Now we have to migrate our data.

## Migrate Repositories

1. Inside Gitea make a new migration.

2. Use either:
    ```python
    1. "Git - Migrate a repository only from any Git service." 
    or 
    2. "Gitea - Migrate data from gitea.com or other Gitea instances."
    ```

3. Then one by one migrate each repository from the slated instance. If it has LFS, then enable it for the repo. If it has Issues, Pull Requests, Releases, etc... make sure to use the Gitea migration specifically with an Access Token.


## Gitea Access Token

If you selected the latter you can use an Access Token to migrate the additional items. 

You can create one from the Admin account in: 

> User -> Settings -> Applications -> Manage Access Tokens -> Generate New Token

Select read for all the permissions and copy the token and use that during each repository migration.

## Migrate users

Users are responsible for creating and managing their new credentials. 

## Delete the Slated Instance

Since you manage your own instance, you'll know where additional migration steps will need to be applied. Nevertheless, you will have the slated instance and the new instance running alongside each other. If done correctly, everything should work as expected as if nothing has changed. You should not push or pull from the slated instance and only use the new one from here on. Then after some observation interval, you should stop running the slated instance and either safely archive or permanently delete `old-gitea` and `gitea.backup`. 

From now on, regularly maintain the stack through every minor release to avoid having to go through all of this again. Refer to [Official docs](https://docs.gitea.com/installation/upgrade-from-gitea/) for the rest.