# This module recursively lists all directories and files starting from a given path.
import os

# Recursively walks through the directory tree and collects file and directory paths.
def list_directory(path="."):
    # Attempt to walk through the directory structure and gather paths
    try:
        directory_contents = []
        for root, dirs, files in os.walk(path):
            for name in dirs:
                full_path = os.path.join(root, name)
                directory_contents.append(("DIR", full_path))
            for name in files:
                full_path = os.path.join(root, name)
                directory_contents.append(("FILE", full_path))
        return directory_contents
    except Exception as e:
        return [("ERROR", str(e))]

# Formats the directory listing for display with labels for files and directories.
def format_list(output):
    return "\n".join([f"[{kind}] {path}" for kind, path in output])

# Allows the script to be run as a standalone module from the command line.
if __name__ == "__main__":
    import sys
    # Get the target path from the command line arguments, default to current directory
    target_path = sys.argv[1] if len(sys.argv) > 1 else "."
    output = list_directory(target_path)
    # Print the formatted list of directory contents
    print(format_list(output))