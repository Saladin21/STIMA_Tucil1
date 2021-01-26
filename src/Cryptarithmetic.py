#NIM / NAMA     : 13519187 / Ahmad Saladin
#Tanggal        : 20 Januari 2020
import time


def CtoInt(char, Tab, A):
#Fungsi untuk mengubah karakter menjadi angka sesuai dengan data yang ada pada matriks Tab dan array A
    #KAMUS LOKAL
    #i : integer
    #ALGORITMA
    if char == "" or char == " ":
        return 0
    else:
        i = 0
        while i < len(Tab[0]) and char != Tab[0][i]:
            i += 1
        return A[i]

def Test(MKata, Tab, First, A):
#Fungsi untuk melakukan test apakah jawaban yang dicoba sudah benar
    #KAMUS LOKAl
    #success : boolean
    #n, i, total, k : integer
    #ALGORITMA
    success = True
    n = len(MKata)
    i = 9
    total = 0

    for k in First:
        if CtoInt(k, Tab, A) == 0:
            success = False

    while i >= 0 and success:
        for j in range (n-1):
            total += CtoInt(MKata[j][i], Tab, A)
        if total % 10 != CtoInt(MKata[n-1][i], Tab, A):
            success = False
        else:
            total = total // 10
            i -= 1
    return success

def permutasi(n, hasil, First, MKata):
#Fungsi untuk membangkitkan permutasi n buah angka (n<= 10) lalu melakukan test
#apakah jawaban sudah sesuai
    #KAMUS LOKAl
    #success : boolean
    #n, i, total, k : integer
    #ALGORITMA
    global count
    global found
    global Tab
    if not found:
        if (n==0):
            count += 1
            if Test(MKata, Tab, First, hasil):
                found = True
                for k in range (len(Tab[0])):
                    Tab[1][k] = hasil[k]
        else:
            i = 0
            while not found and i <10:
                if i not in hasil and (i != 0 or (Tab[0][len(hasil)-n] not in First)):
                    hasil[len(hasil)-n] = i
                    permutasi(n-1, hasil, First, MKata)
                if not found:
                    i += 1
                hasil[len(hasil)-n] = -1

#KAMUS
#Tab : List of List
#n,a,b,c,d,e,f,g,h,i,j,k,l, count : integer
#found : boolean
#MKata : Matrix of character
#First, kata, kata1 : List of character
#ALGORITMA
Tab = [[],[0 for i in range (10)]]
n = 0


#Baca File kemudian disimpan dalam MKata
file = input("Masukkan nama file: ")
f = open("../test/"+file, "r")
MKata = []
First = []
kata = f.readline().strip("\n")
while kata != "":
    if kata[0] != "-" and kata[0] != "+":
        if kata.strip(" ")[0] not in First:
            First.append(kata.strip(" ")[0])
        kata1 = ["" for i in range (10)]
        
        j = 9
        for i in range(len(kata)-1, -1, -1):
            kata1[j] = kata[i]
            j -= 1
            if kata[i] not in Tab[0] and kata[i] != " ":
                if n < 9:
                    Tab[0].append(kata[i])
                    n += 1
                else:
                    print("Terdapat lebih dari 10 huruf yang berbeda")
        MKata.append(kata1)
    kata = f.readline().strip("\n").strip("+")
f.close()

#Mencatat waktu awal
start = time.time()
count = 0 #jumlah test yang dilakukan
found = False #jawaban sudah sesuai
#Melakukan permutasi kemudian mengetes apakah hasil permutasi merupakan jawaban yang sesuai
#Jika jawaban sudah sesuai loop berhenti

hasil = [-1 for i in range (len(Tab[0]))]
permutasi(len(Tab[0]), hasil, First, MKata)                                                 
                                                                                
if found:
    #Mencetak soal
    for k in range (len(MKata)-1):
        print()
        for l in range (10):
            if MKata[k][l] == "":
                print(" ", end="")
            else:
                print(MKata[k][l], end="")
        
    print("+")
    print(10*"-")
    for l in range(10):
        if MKata[len(MKata)-1][l] == "":
            print(" ", end="")
        else:
            print(MKata[len(MKata)-1][l], end="")
    print()
    print()

    #Mencetak Solusi
    print("solusi:")
    for k in range (len(MKata)-1):
        print()
        for l in range (10):
            if MKata[k][l] == "" or MKata[k][l] == " ":
                print(" ", end="")
            else:
                print(CtoInt(MKata[k][l], Tab, Tab[1]), end="")
        
    print("+")
    print(10*"-")
    for l in range(10):
        if MKata[len(MKata)-1][l] == "" or MKata[len(MKata)-1][l] == " ":
            print(" ", end="")
        else:
            print(CtoInt(MKata[len(MKata)-1][l], Tab, Tab[1]), end="")
    print()
    print()
    print("Ditemukan pada tes ke", count)
    print("Waktu yang dibutuhkan:", (time.time()-start), "detik")
else:
    print("Solusi tidak ditemukan")
input()
