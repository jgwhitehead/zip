import zipfile
import os
import random
try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED

modes = { zipfile.ZIP_DEFLATED: 'deflated',
          zipfile.ZIP_STORED:   'stored',
          }

filename = "demofile.txt"
f = open(filename, "w")

wordfile = open("/usr/share/dict/words")
words = wordfile.readlines()

print(os.stat(filename).st_size)
while os.stat(filename).st_size < 1000000:
    print("writing")
    f.write(random.choice(words))

f.close()

print('creating archive')
zf = zipfile.ZipFile('zipfile_write_compression.zip', mode='w')
try:
    print('adding demofile.txt with compression mode', modes[compression])
    zf.write(filename, compress_type=compression)
    info = zf.getinfo(filename)
    print(info.file_size)
    print(info.file_size)


finally:
    print('closing')
    zf.close()
