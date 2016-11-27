# FileUpdater

A Python File System Listener

## Problem:

I had two different directories. One was specific to all things published by my portfolio site and the other was specific to all things related to my resume. I wanted to keep these two directories distinct on my local drive; however, everytime I updated my resume, I also had to make sure I remembered to copy the latest one exported in PDF from a Word document to the public portfolio directory and properly rename it. This is a simply but unnecessarily tedious task. I figured all I needed to do is the have some event listener focus on a particular directory and copy the file over when a modification or file creation was detected.

## Requirements:

- Python 3.5+
- Watchdog
- GitPython You can install `Watchdog` and `GitPython` by running the following command:

  ```
  $ pip install -r requirements.txt
  ```

## How To Use:

This script was intended to be setup in the Windows Task Scheduler and executed at startup. To execute the script, navigate to the `src` directory and run the following command:

```
$ python FileUpdater.py -n <author_name> -e <author_email> -m <commit_message> -g <git_directory> -s <directory_to_watch> -d <destination_directories_01 destination_directories_02 ...> -p <pattern_matcher>
```

Example:

```
$ python FileUpdater.py -n "David Lam" -e "some_email@xyz.com" -m "updating cool file" -g \some\git\directory -s \some\directory\to\watch -d \directory\01 \directory\02 -p *.pdf *.xml *.json
```

### Arguments:
#### Required:
- directory_to_watch: A String of the path of the directory the script will listen to.
- destination_directories: A list of space separated Strings (must include at least 1) of the path to which to move the updated file(s) to. This can include a new name of the file if needed. For example: if a file was originally called `apple.pdf`, you could specify the path `/some_path/orange.pdf` to be the new name of the copied file.
- pattern_matcher: A list of space separated regular expression Strings (must include at least 1).

#### Optional:
- git_directory: A String of the path to the git directory the files will be moved to.
- author_name: A String of the author and committer of the update. Required only if git_directory argument provided.
- author_email: A String of the author and committer's email. Required only if git_directory argument provided.
- commit_message: A String of the message associated with the Git commit. Required only if git_directory argument provided.


