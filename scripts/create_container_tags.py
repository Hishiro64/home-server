import yaml as yaml
from pathlib import Path

# Helper script to generate container related tags seen in /root/srv/stacks/mailpit/data/tags.yaml
# The following doesn't work in Wud:
# - WUD_TRIGGER_SMTP_MAILPIT_TO=admin+notification+$${container.name}@server.home.arpa
# So this work around is used instead for Wud notifications to be tagged in mailpit
# Just append everything under "filters:" to existing rules

# returns entire stack as list object
def get_stack(path):
    stack = list()
    path = Path(path)
    for f in path.iterdir():
        if f.is_file() and f.suffix == ".yml":
            with f.open("r") as yml:
                config = yml.read()
                stack.append(config)
    return stack

# returns full list of container_names used by stack 
def get_stack_container_names(stack):

    stack_container_names = list()

    for config in stack:
        
        compose = yaml.safe_load(stream=config)
        services = dict(compose["services"])

        for s, container in services.items():        

            name = container.get("container_name")

            if name != None:
                stack_container_names.append(name)
    
    return stack_container_names

# Create and print tags
def print_container_tags(names):
    print("filters:")
    for name in names:
        words = name.split('-')
        tag_name = '-'.join(word.capitalize() for word in words)
        print(f'  - match: "Container: {name}"')
        print(f'    tags: {tag_name}')

# Usage: python create_container_tags.py > container_tags.yaml
def main():
        path = "../stack/current/"
        primary_path = "/srv/stacks/"
        
        stack = get_stack(path)
        names = get_stack_container_names(stack)

        print_container_tags(names)

if __name__ == "__main__":
        main()
