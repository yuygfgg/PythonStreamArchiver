import os
import sys
import tarfile

def create_tar_archive(source_dir, output_tar_file):
    output_tar_file = os.path.abspath(output_tar_file)  # 获取 tar 文件的绝对路径
    with tarfile.open(output_tar_file, "w") as tar:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                full_path = os.path.join(root, file)
                if full_path == output_tar_file:
                    continue  # 如果文件是 tar 文件本身，则跳过不添加到归档中也不删除

                arcname = os.path.relpath(full_path, start=source_dir)
                try:
                    tar.add(full_path, arcname=arcname)
                    print(f"Added {full_path} to archive as {arcname}")
                except Exception as e:
                    print(f"Failed to add {full_path} to archive: {e}")
                    continue
                # 检查文件是否已经在 tar 归档中，再确认是否删除
                if arcname in tar.getnames():
                    try:
                        os.remove(full_path)
                        print(f"Deleted {full_path}")
                    except Exception as e:
                        print(f"Failed to delete {full_path}: {e}")
                else:
                    print(f"File {arcname} not found in archive, not deleting.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python file.py <source_directory> <output_tar_path>")
        sys.exit(1)
    
    source_directory = sys.argv[1]
    output_tar_path = sys.argv[2]
    create_tar_archive(source_directory, output_tar_path)