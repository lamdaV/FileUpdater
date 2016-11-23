# FileUpdaterPDF
A Python File System Listener

# Problem:
I had two different directories. One was specific to all things published by my portfolio site and the other was specific to all things related to my resume. I wanted to keep these two directories distinct on my local drive; however, everytime I updated my resume, I also had to make sure I remembered to copy the latest one exported in PDF from a Word document to the public portfolio directory and properly rename it. This is a simply but unnecessarily tedious task. I figured all I needed to do is the have some event listener focus on a particular directory and copy the file over when a modification or file creation was detected.

# Requirements:
  * Python 3.5+
  * Watchdog
  * GitPython
You can install `Watchdog` and `GitPython` by running the following command:
```
  $ pip install -r requirements.txt
```
