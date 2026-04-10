import yaml as yaml
from pathlib import Path

# Helper script to generate Tree Map seen in README.md

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

# strips out container paths, keeps host side and keeps attribute of path
def strip_container_side_paths(mapping):
    for i, item in enumerate(mapping):
            flag = False
            host_mapping = ""
            for char in item:
                if char == ':':
                    flag = not flag
                if not flag:
                    host_mapping += char
            mapping[i] = host_mapping

# returns full list of paths used by stack 
def get_stack_paths(stack):

    stack_paths = list()

    for config in stack:
        
        compose = yaml.safe_load(stream=config)
        services = dict(compose["services"])

        for s, container in services.items():        

            vols = container.get("volumes")

            if vols != None:
                strip_container_side_paths(vols)

                for v in vols:
                    stack_paths.append(v)
    
    return stack_paths

# prints primary paths with folder emoji
def print_primary_paths(paths, primary_path):
    limit = len(primary_path)
    all_paths = list()
    for p in paths:
        if p[0:limit] == primary_path:
            mod_path = p.replace("/", "/📁 ") 
            all_paths.append(mod_path)

    for p in all_paths:
        print(p)

# Usage: python tree.py > primary_paths.txt; tree --fromfile -n  --noreport  primary_paths.txt
def main():
        path = "../stack/current/"
        primary_path = "/srv/stacks/"
        
        stack = get_stack(path)
        paths = get_stack_paths(stack)

        print_primary_paths(paths, primary_path)

if __name__ == "__main__":
        main()
