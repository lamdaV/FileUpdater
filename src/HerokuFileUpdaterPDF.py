import time
import shutil
import subprocess
import sys
import os.path
from git import Repo, Actor
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

"""
    HerokuFileUpdaterPDF watches for creations and modifications of pdf files at the scheduled source and moves them to the destination.

    Note: The destination should contain the new name Example: /path/some-new-name.pdf
"""


class HerokuFileUpdaterPDF(PatternMatchingEventHandler):
    patterns = ["*.pdf"]

    def __init__(self, author_name, author_email, message, git_directory, destinations):
        """
            Construct a HerokuFileUpdaterPDF.
        """
        super(HerokuFileUpdaterPDF, self).__init__()
        self.git_directory = git_directory
        self.destinations = destinations
        self.author_name = author_name
        self.author_email = author_email
        self.message = message

    def process(self, event):
        """
            Process files modified or created.

            event.event_type
                'modified' | 'created' | 'moved' | 'deleted'
            event.is_directory
                True | False
            event.src_path
                path/to/observed/file
        """
        # Print path and event type
        print(event.src_path, event.event_type)

        # Copy the file to the destination
        for destination in self.destinations:
            shutil.copy(event.src_path, destination)

        # Push to master
        self.git_process()

    def git_process(self):
        """
            Push update to git.
        """
        # Setup Repo.
        repo = Repo(self.git_directory)
        index = repo.index

        # Add files.
        index.add(self.destinations)

        # Commit.
        committer = Actor(self.author_name, self.author_email)
        index.commit(self.message, author=committer, committer=committer)

        # Push.
        for remote in repo.remotes:
            if (remote.name == "origin"):
                remote.push()
                break

    def on_modified(self, event):
        """
            If a file following the patterns defined is modified, execute the following code.
        """
        self.process(event)

    def on_created(self, event):
        """
            If a file following the patterns defined is created, execute the following code.
        """
        self.process(event)


def main():
    # Detect required arguments met.
    if (len(sys.argv) < 7):
        print("[ ERROR ] missing parameters")
        print(
            "HerokuFileUpdaterPDF.py author_name author_email /path/to/git/directory  /path/to/watch/directory /path/to/destination/directory...")
        return

    # Parse arguments from command line.
    author_name = sys.argv[1]
    author_email = sys.argv[2]
    message = sys.argv[3]
    git_directory = sys.argv[4]
    source_path = sys.argv[5]
    destinations = sys.argv[6:]

    # Run WatchDog with HerokuFileUpdaterPDF.
    observer = Observer()
    observer.schedule(HerokuFileUpdaterPDF(
        author_name, author_email, message, git_directory, destinations), source_path)
    observer.start()

    # Print some initial information.
    print("Observation starting...")
    print("Ctrl-C to stop")

    # Run indefinitely. Stop if Ctrl-C.
    try:
        while(True):
            time.sleep(1)
    except KeyboardInterrupt:
        # Print that it has started quitting information.
        print("Quitting...")
        observer.stop()

    observer.join()


if __name__ == "__main__":
    main()
