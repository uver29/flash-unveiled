import sys
import os
import binascii
import codecs
# changes the location loc of cursor for reading the raw data file
def doseek(loc):
    if sys.platform == 'win32':
        # Windows raw disks can only be seeked to a multiple of the block size ie 512 bytes
        # quo = quotient, rem = remainder
        quo, rem = divmod(loc, 512)
        raw.seek(quo * 512)
        if rem:
            raw.read(rem)
    else:
        raw.seek(loc)
# converts n bytes of raw file data into INT32 - Little Endian form starting from location loc
def con_int(loc, n):
	doseek(loc)
	return(int.from_bytes(raw.read(n), byteorder = "little"))
# Function for finding the next cluster by reading the FAT
def fat(clu):
	nxt_clu = con_int(((res_sec*512)+((clu)*4)+(sec_per_fat*512)), 4)
	return(nxt_clu) 
def jpg(st_clu, size):
	st_byt = (st_clu_byt + ((st_clu-2)*sec_per_cl*512))
	raw.seek(st_byt)
	data = raw.read(size)
	data = codecs.encode(data, "hex_codec")
	data1 = data.decode("utf-8")
	data1 = binascii.a2b_hex(data1)
	raw.seek(st_byt)
	with open("imageLOC" + str(st_byt) + ".jpg", "wb") as image_file:
		image_file.write(data1)
		print("Recovered imageLOC", str(st_byt), ".jpg")
# Function for browsing files and sub-directories from Root directory
def dir_data(st_clu):
	# starting byte location
	st_byt = st_clu_byt + ((st_clu-2)*sec_per_cl*512)
	while(con_int(st_byt, 1)!=0):
		raw.seek(st_byt)
		# condition for a deleted file
		if(raw.read(1) == b"\xE5"):
			raw.seek(st_byt+8)
			# condition for .jpg file
			if(raw.read(3)== b"JPG"):
				raw.seek(st_byt)
				print("\nFound ", raw.read(8), ".jpg")
				jpg(con_int((st_byt+26), 2), con_int((st_byt+28), 4))
		st_byt = st_byt + 32
		if(st_byt == (st_clu_byt+((st_clu-1)*sec_per_cl*512))):
			st_clu = fat(st_clu)
			st_byt = st_clu_byt + ((st_clu-2)*sec_per_cl*512)
def main():
	print("\nVolume ID")
	print("\nJMP Instruction(hex)", raw.read(3))
	print("\nOEM = ", raw.read(8));
	print("\nBIOS Parameter Block and Extended BIOS Parameter Block Fields")
	print("More info at http://www.ntfs.com/fat-partition-sector.htm")
	print("Bytes per Sector = ", con_int(0xB, 2))
	print("Sectors Per Cluster = ", con_int(0xD, 1))
	print("Reserved Sectors = ", res_sec)
	print("Number of FAT's = ", no_fat)
	print("Root Entries(unused) = ", con_int(0x11, 2))
	print("Sectors(on small volume) = ", con_int(0x13, 2))
	print("Media Type(hex) = ", raw.read(1)) 
	print("Sectors per FAT(small volume) = ", con_int(0x16, 2))
	print("Sectors per Track = ", con_int(0x18, 2))	
	print("Number of Heads = ", con_int(0x1A, 2))
	print("Hidden Sectors = ", con_int(0x1C, 4))
	print("Sectors(on large volume) = ", con_int(0x20, 4))
	print("\nFAT32 Section")
	print("Sectors per FAT ", sec_per_fat)
	print("Extended Flags = ", con_int(0x28, 1))
	print("FAT mirroring disabled? = ", con_int(0x28, 1))
	print("Version(usually 0) = ", con_int(0x2A, 2))
	print("Root dir 1st cluster = ", con_int(0x2C, 4))
	print("FSInfo sector = ", con_int(0x30, 2))
	print("Backup boot sector = ", con_int(0x32, 2))
	print("(Reserved) = ", raw.read(12))
	doseek(0x40)
	print("\nBIOS drive(hex, HD=8x) = ", raw.read(1))
	print("(Unused) = ", con_int(0x41, 1))
	print("Ext. boot signature(29h) = ", raw.read(1))
	print("Volume serial number(hex) = ", raw.read(4))
	print("Volume serial number(decimal) = ", con_int(0x43, 4))
	print("Volume label = ", raw.read(7))
	doseek(0x52)
	print("File system = ", raw.read(5))
	doseek(0x1FE)
	print("\nSignature(55 AA) = ", raw.read(2))
	# Starting cluster is 2, root dir is located there
	dir_data(2)
if __name__ == '__main__':
	disk = sys.argv[1]
	#"\\\\.\\Harddisk*Partition*"
	raw = open(disk, "rb")
	# reserved sectors
	res_sec = con_int(0xE, 2)
	# number of FAT's
	no_fat = con_int(0x10, 1)
	# sectors per FAT
	sec_per_fat = con_int(0x24, 4)
	# sectors per cluster
	sec_per_cl = con_int(0xD, 1)
	# starting cluster location at byte level
	st_clu_byt = (res_sec+(no_fat*sec_per_fat))*512
	exit(main())
