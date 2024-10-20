import sys
import shutil
from pathlib import Path

def copy_file(file, dist):
    try:
        file_ext = file.suffix[1:]
        destination_folder = dist.joinpath(file_ext)

        if not destination_folder.exists():
            destination_folder.mkdir()

        destination = destination_folder.joinpath(file.name)
        shutil.copy(file, destination)
    except Exception as e:
        print(f"Error copying file {file.name}, details: {e}.")

def walk_through_folder(path, dist):
    try:
        if path.is_dir():
            for child in path.iterdir():
                if child.is_dir():
                    walk_through_folder(child, dist)
                else:
                    copy_file(child, dist)
    except FileNotFoundError as e:
        print(f"Folder or path doesn't exist, details: {e}.")
    except PermissionError as e:
        print(f"Permission denied, details: {e}.")
    except Exception as e:
        print(f"Error occured while processing the folder, details: {e}")

def main():
    try:
        folder_to_iterate = sys.argv[1]
    except IndexError:
        print("Folder to iterrate was not specified. Exiting.")
        sys.exit(1)

    current_dir = Path.cwd()
    path_to_folder = current_dir.joinpath(folder_to_iterate)

    if not path_to_folder.exists():
        print(f"Specified folder '{folder_to_iterate}' doesn't exist.")
        sys.exit(1)

    try:
        dist_folder = sys.argv[2]
    except IndexError:
        print("Destination folder was not spefied. Fallback to /dist.")
        dist_folder = "dist"
    
    destination_folder = current_dir.joinpath(dist_folder)
    
    if not destination_folder.exists():
        try:
            destination_folder.mkdir()
        except Exception as e:
            print(f"Error creating dist folder, details: {e}.")

    walk_through_folder(path_to_folder, destination_folder)

if __name__ == "__main__":
    main()
