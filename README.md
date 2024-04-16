# StreamArchiver

StreamArchiver is an efficient script for incrementally packing a directory into a tar file while deleting the source files on the fly, eliminating the need for extra temporary space required by traditional methods that keep both the tar and the source files during the process. This space-saving approach is particularly useful in storage-constrained environments. This approach is handy for environments with limited storage.

## Features
- Saves disk space by avoiding the need to duplicate files before archiving.
- Deletes files immediately after archiving if they have been successfully added to the tar archive.

## Prerequisites
You need Python 3.x installed on your machine to use StreamArchiver.

## Installation
To get started with StreamArchiver, clone this repository:
```
git clone https://github.com/yourgithubusername/StreamArchiver.git
cd StreamArchiver
python stream_archiver.py <source_directory> <output_tar_path>
```
Replace `<source_directory>` with the directory you want to archive, and `<output_tar_path>` with the desired tar file path.

## Warning
StreamArchiver is a basic script and hasn't been extensively tested. There is a potential risk of data loss. Use it cautiously, and always back up important data first.

## Contributing
Feel free to fork this repository, make improvements, and submit pull requests. Any contributions are welcome!

## License
StreamArchiver is open-source under the MIT License. See the LICENSE file for more details.

