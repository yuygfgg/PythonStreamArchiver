import os
import sys
import tarfile

def create_tar_archive(source_dir, output_tar_file):
    # Convert the output_tar_file path to an absolute path to avoid path confusion
    output_tar_file = os.path.abspath(output_tar_file)
    
    # Create a new tar file and open it for writing
    with tarfile.open(output_tar_file, "w") as tar:
        # Traverse the directory tree starting from source_dir
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                # Construct the full path of each file
                full_path = os.path.join(root, file)
                
                # Skip processing if the current file is the tar file itself
                if full_path == output_tar_file:
                    continue
                
                # Calculate the relative path to use within the tar archive
                arcname = os.path.relpath(full_path, start=source_dir)
                
                # Try to add the file to the tar archive
                try:
                    tar.add(full_path, arcname=arcname)
                    print(f"Added {full_path} to archive as {arcname}")
                except Exception as e:
                    print(f"Failed to add {full_path} to archive: {e}")
                    continue
                
                # Check if the file was successfully added to the tar file
                if arcname in tar.getnames():
                    # If added successfully, delete the file from the file system
                    try:
                        os.remove(full_path)
                        print(f"Deleted {full_path}")
                    except Exception as e:
                        print(f"Failed to delete {full_path}: {e}")
                else:
                    # If the file was not added to the tar, do not delete it
                    print(f"File {arcname} not found in archive, not deleting.")

# Entry point of the script
if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python file.py <source_directory> <output_tar_path>")
        sys.exit(1)
    
    # Collect command line arguments
    source_directory = sys.argv[1]
    output_tar_path = sys.argv[2]
    
    # Call the function to create the tar archive
    create_tar_archive(source_directory, output_tar_path)
