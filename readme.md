Flash Unveiled

A simple file recovery tool based on file carving method. Scans for headers of files and extracts the file raw bytes once it reaches the slack space.

It is a file carving program in Python that succesfully recovers the defragmented (continuous) files from a formatted drive. This program is independent of the file system and has support for 500+ file types. Although for recovering fragmented data a separate program for each file type is required. I did some research on JPEGs and MP4, and planned to use back propagation neural network for making the software. But being a beginner in ML I couldn't fully implement my ideas to code, and it is still under development.
But since most of the files in a drive are in continuous clusters or defragmented, so my program recovers most of the files, and also it doesn't matter if the drive is formatted from one file system to another or even if it is corrupted.

The GUI of this program is tested on linux, to run it on linux:
1) sudo python gui2.py
2) Browse and select the drive. Example: /dev/sdb1
3) Select the output path(make sure to name a new directory)
4) Click Scan
5) Click "OK" after a message appears that scan has started and wait. Messages would be printed on the terminal about the files being scaned.


To run the program in Windows, try the above method, if gui fails, then:
1) git checkout d30ea399c0077caab0c31c7c476275814f4ec1ad
2) python recover.py path/to/the/drive recovered/files/saving/path. Example recover.py /dev/sdb1 ~/Desktop/new_folder