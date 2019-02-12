#HAK MILIK KELOMPOK BAGAS31 - TUGAS BESAR 1 STIMA 2019

#PROGRAM UNTUK FRONT-END II, FILE EKSTERNAL

#Library untuk menggunakan sys.argv
#Command akan berupa : py namafile.py fileinput.txt fileoutput.txt
import sys
import backend

# Inisialisasi list jawaban
listofanswer = ['0','0']

#Assign variabel yang berisi sys.argv(1), yaitu nama file eksternal yang ingin dibaca
fileinput = sys.argv[1]

#Membuka File Eksternal Input
inputtemp = open(fileinput, "r")  # File eksternal disiapkan untuk dibaca ("r")
# Memasukkan setiap data dari file eksternal ke dalam list/array, dengan pemisah berupa spasi/whitespace
inputlist = inputtemp.read().split(' ')

#Iterasi untuk mengubah tipe data dari string menjadi integer
for i in range(4):
    # Typecast setiap elemen list menjadi integer
    inputlist[i] = int(inputlist[i])

print(inputlist)  # Mencetak isi list ke layar, untuk test

# Menghitung list of integers
listofanswer = backend.solve24(inputlist)

#Assign variabel yang berisi sys.argv(2), yaitu nama file eksternal yang ingin ditulis
fileoutput = sys.argv[2]

#Membuka File Eksternal Output
# File eksternal disiapkan untuk ditulis ("w")
outputtemp = open(fileoutput, "w")

# Menulis keluaran ke file eksternal, ditest dengan string "4"
outputtemp.write(listofanswer[0])

#Menutup File Eksternal
inputtemp.close()  # Tutup file input
outputtemp.close()  # Tutup file output
