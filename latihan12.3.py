nama_file = open("Masukkan nama file : ")
try:
    handle = open(nama_file)
except:
    print('File cannot be opened:', nama_file)
    exit()

for line in handle:
    words = line.split()