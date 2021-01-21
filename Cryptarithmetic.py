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
        while i < 10 and char != Tab[0][i]:
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

#KAMUS
#Tab : List of List
#n,a,b,c,d,e,f,g,h,i,j,k,l, count : integer
#found : boolean
#MKata : Matrix of character
#First, kata, kata1 : List of character
#ALGORITMA
Tab = [['' for i in range (10)],[0 for i in range (10)]]
n = 0


#Baca File kemudian disimpan dalam MKata
f = open("file.txt", "r")
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
                    Tab[0][n] = kata[i]
                    n += 1
                else:
                    print("Terdapat lebih dari 10 huruf yang berbeda")
        MKata.append(kata1)
    kata = f.readline().strip("\n").strip("+")

#Mencatat waktu awal
start = time.time()
count = 0 #jumlah test yang dilakukan
found = False #jawaban sudah sesuai
#Melakukan permutasi kemudian mengetes apakah hasil permutasi merupakan jawaban yang sesuai
#Jika jawaban sudah sesuai loop berhenti
a = 0
while a < 10 and not found:
    b = 0
    while b < 10 and not found:
        if b != a:
            c = 0
            while c < 10 and not found:
                if c != a and c != b:
                    d = 0
                    while d < 10 and not found:
                        if d != a and d != b and d != c:
                            e = 0
                            while e < 10 and not found:
                                if e != a and e != b and e != c and e != d:
                                    f = 0
                                    while f < 10 and not found:
                                        if f != a and f != b and f != c and f != d and f != e:
                                            g = 0
                                            while g < 10 and not found:
                                                if g != a and g != b and g != c and g != d and g != e and g != f:
                                                    h = 0
                                                    while h < 10 and not found:
                                                        if h != a and h != b and h != c and h != d and h != e and h != f and h != g:
                                                            i = 0
                                                            while i < 10 and not found:
                                                                if i != a and i != b and i != c and i != d and i != e and i != f and i != g and i != h:
                                                                    j = 0
                                                                    while j < 10 and not found:
                                                                        if j!= a and j != b and j != c and j != d and j != e and j != f and j != g and j != h and j != i:
                                                                            count += 1
                                                                            A = [a,b,c,d,e,f,g,h,i,j] 
                                                                            if Test(MKata, Tab, First, A):
                                                                                found = True
                                                                                for k in range (10):
                                                                                    Tab[1][k] = A[k]
                                                                        if not found:
                                                                            j += 1
                                                                if not found:
                                                                    i += 1
                                                        if not found:
                                                            h += 1
                                                if not found:
                                                    g += 1
                                        if not found:
                                            f += 1
                                if not found:
                                    e += 1
                        if not found:
                            d += 1
                if not found:
                    c += 1
        if not found:
            b += 1
    if not found:
        a += 1
                                                                        
                                                                                
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
        if MKata[k+1][l] == "":
            print(" ", end="")
        else:
            print(MKata[k+1][l], end="")
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
        if MKata[k+1][l] == "" or MKata[k+1][l] == " ":
            print(" ", end="")
        else:
            print(CtoInt(MKata[k+1][l], Tab, Tab[1]), end="")
    print()
    print()
    print("Ditemukan pada tes ke", count)
    print("Waktu yang dibutuhkan:", (time.time()-start), "detik")











