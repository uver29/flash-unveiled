1) Recovers only .jpg files.
2) Files(***.jpg) should be present in the root directory of a drive, not in any of the subdirectories
3) Filesystem of the drive partition should be FAT32
4) The disk should be defragmented

Preparing the drive:
* Mount the usb drive
* Format it with FAT32
* Copy the data in the drive
* Delete some of the data(including some ***.jpg files)

Recovering the files:
* Clone this repo or copy the flash-unveiled.py file
* Download the latest version of python (https://www.python.org/downloads/)
* Open the flash-unveiled file in idle
* From the toolbar at the top in idle, select "Run" menu and then select "Run... Customized" 
* Give the command line argument "\\\\.\\Harddisk*Partition*", replace the * by following these steps:
	* On the start menu type "diskpart" and press enter
	* Diskpart window appears
	* On the diskpart window type "list-disk" and press enter
	* It will list all the disks mounted to the computer
	* Choose your usb drive disk by typing "select disk n"
	* Here the value of n will give the first * value in "\\\\.\\Harddisk*Partition*"
	* Then type "list partition" and press enter
	* Select the partition number of the FAT32 of the drive
	* Here the partition number will give the second * value in "\\\\.\\Harddisk*Partition*"
	* Eg: "\\\\.\\Harddisk1Parttion1"
* After giving the command line argument, press enter and the program will start compiling and output some data on the console window
* If any of the files will be recovered they will be saved in the directory where flash-unveiled.py file is stored.

Note: The program only works for defragmented files. So format the usb drive before testing the program. Also it only recovers deleted files.
