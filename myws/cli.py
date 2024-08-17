import os
import sys
import json
import webbrowser
import subprocess
import argparse

WORKSPACE_DIR = os.path.join(os.path.expanduser("~"), ".workspace")

def save_workspace(name, apps, websites, paths):
    if not os.path.exists(WORKSPACE_DIR):
        os.makedirs(WORKSPACE_DIR)
    
    workspace = {
        "apps": apps,
        "websites": websites,
        "paths": paths
    }
    
    file_path = os.path.join(WORKSPACE_DIR, f"{name}.json")
    
    with open(file_path, "w") as f:
        json.dump(workspace, f)
    
    print(f"Workspace '{name}' saved successfully.")

def start_workspace(name):
    file_path = os.path.join(WORKSPACE_DIR, f"{name}.json")
    
    if not os.path.exists(file_path):
        print(f"Workspace '{name}' does not exist.")
        return
    
    with open(file_path, "r") as f:
        workspace = json.load(f)
    
    for app in workspace["apps"]:
        print(f"Starting application: {app}")
        subprocess.Popen([app])
    
    for website in workspace["websites"]:
        print(f"Opening website: {website}")
        webbrowser.open(website)
    
    for path in workspace.get("paths", []):
        print(f"Opening path in VS Code: {path}")
        if os.name == 'nt':  
            path = path.replace("/", "\\") 
        try:
            subprocess.Popen(["code", path], shell=True)
        except FileNotFoundError:
            print(f"Error: Could not open path '{path}' in VS Code.")

    print(f"Workspace '{name}' started.")

def main():
    parser = argparse.ArgumentParser(description="Manage workspaces.")
    subparsers = parser.add_subparsers(dest="command")
    
    # Subparser for the "save" command
    save_parser = subparsers.add_parser("save", help="Save a new workspace")
    save_parser.add_argument("name", help="Name of the workspace")
    save_parser.add_argument("-a", "--apps", nargs="*", default=[], help="Applications to open")
    save_parser.add_argument("-w", "--websites", nargs="*", default=[], help="Websites to open")
    save_parser.add_argument("-p", "--paths", nargs="*", default=[], help="Paths to open in editors")
    
    # Subparser for the "start" command
    start_parser = subparsers.add_parser("start", help="Start a workspace")
    start_parser.add_argument("name", help="Name of the workspace")
    
    args = parser.parse_args()
    
    if args.command == "save":
        save_workspace(args.name, args.apps, args.websites, args.paths)
    elif args.command == "start":
        start_workspace(args.name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
