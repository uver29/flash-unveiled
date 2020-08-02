import sys
import os
import codecs

mp4_header = '66747970'
chunk_signatures = [b"ftyp", b"mdat", b"moov", b"pnot", b"udta", b"uuid", b"moof", b"free", b"skip", b"jP2 ", b"wide", b"load", b"ctab", b"imap", b"matt", b"kmat", b"clip", b"crgn", b"sync", b"chap", b"tmcd", b"scpt", b"ssrc", b"PICT"]
data = b''
file_num = 0

dd_image_name = sys.argv[1]

# recovered_files_directory = sys.argv[2]
# if os.path.isdir(recovered_files_directory):
#     print('The specified directory already exists. Create a new one.')
#     exit()
# os.makedirs(recovered_files_directory)


def save_data():
    global file_num
    with open("/home/uver/Desktop/new/video" + str(file_num) + ".mp4", "wb") as video_file:
        video_file.write(data)
    file_num += 1


def skip_and_save_chunk(offset):
    global data
    dd_image.seek(offset)
    size_bytes = dd_image.read(4)
    size = int.from_bytes(size_bytes, byteorder="big")
    print(size)
    # l = dd_image.read(10)
    # print(l)
    # data = data + l
    data = data + dd_image.read(size + 4)
    data1 = codecs.encode(data, "hex_codec")
    data1 = data1.decode("utf-8")
    # print(data1)
    print(offset + size + 4)
    return(offset + size + 4)


with open(dd_image_name, 'rb') as dd_image:
    current_offset = 0
    while True:

        dd_image_contents = dd_image.read(512)
        dd_image_contents = codecs.encode(dd_image_contents, "hex_codec")
        raw_bytes = dd_image_contents.decode("utf-8")

        if not raw_bytes:
            # save_data()
            # print('Scanned {} kilobytes'.format((num_of_sectors * 512) / 1024))
            break

        elif raw_bytes[8:16] == mp4_header:
            # print(current_offset)
            dd_image.seek(current_offset)
            data = b''
            data = data + dd_image.read(4)
            current_offset = skip_and_save_chunk(current_offset) + 4
            # exit()
            count = 0
            mp3_found = True
            while mp3_found:
                dd_image.seek(current_offset)
                first_byte = dd_image.read(1)
                chunk_signature_maybe = first_byte + dd_image.read(3)
                chunk_signature_found = False
                if chunk_signature_maybe == b'\x00\x00\x00\x00':
                    data = data + first_byte
                    current_offset += 1
                    print('a')
                    if current_offset > 2130633:
                        save_data()
                        exit()
                    # pass
                elif chunk_signature_maybe != b'\x00\x00\x00\x00':
                    for i in chunk_signatures:
                        if chunk_signature_maybe == i:
                            print('found chunk signature', i)
                            print('first: ', current_offset)
                            current_offset = skip_and_save_chunk(current_offset - 4)
                            print('second ', current_offset)
                            chunk_signature_found = True
                            if current_offset > 2130633:
                                save_data()
                                exit()
                            # save_data()
                            # exit()
                            break
                    if not chunk_signature_found:
                        # print('c')
                        data = data + first_byte
                        count += 1
                        if current_offset > 2130633:
                            save_data()
                            exit()
                        # if count > 5:
                        #     mp3_found = False
                        #     current_offset = (current_offset // 512) * 512
                        #     break
                        current_offset += 1

        else:
            current_offset += 512
