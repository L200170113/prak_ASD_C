print("====NOMOR 1====\n")

class Perpus(object):
    def __init__(self, judul, nama, kategori, tahun):
        self.judul = judul
        self.nama = nama
        self.kategori = kategori
        self.tahun = tahun

p1 = Perpus("Bumi Manusia", "Pramoedya Ananta Toer", "Sastra", "2014")
p2 = Perpus("Aku", "Sjuman Djaya", "Sastra", "2017")
p3 = Perpus("Catatan Seorang Demonstran", "Soe Hok Gie", "Sejarah", "2013")
p4 = Perpus("Dunia Sophie", "Jostein Gaarder", "Filsafat", "2012")
p5 = Perpus("Demokrasi Kita", "Mohammad Hatta", "Politik", "2016")
p6 = Perpus("Max Havelar", "Multatuli", "Sejarah", "2011")
p7 = Perpus("Petir", "Dee Lestari", "Sastra", "2010")
p8 = Perpus("Madilog", "Tan Malaka", "Filsafat", "2015")

p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6
p6.next = p7
p7.next = p8

def mergeSort(A):
    #print("Membelah      ",A)
    if len(A) > 1:
        mid = len(A) // 2
        separuhkiri = A[:mid]
        separuhkanan = A[mid:]

        mergeSort(separuhkiri)
        mergeSort(separuhkanan)

        i = 0;j=0;k=0
        while i < len(separuhkiri) and j < len(separuhkanan):
            if separuhkiri[i] < separuhkanan[j]:
                A[k] = separuhkiri[i]
                i = i + 1
            else:
                A[k] = separuhkanan[j]
                j = j + 1
            k=k+1

        while i < len(separuhkiri):
            A[k] = separuhkiri[i]
            i = i + 1
            k=k+1

        while j < len(separuhkanan):
            A[k] = separuhkanan[j]
            j = j + 1
            k=k+1
    #print("Menggabungkan",A)

def convert(arr, obj):
    hasil=[]
    for x in range (len(arr)):
        for i in range (len(arr)):
            if arr[x] == obj[i].tahun:
                hasil.append(obj[i])
    return hasil

Daftar = (p1, p2, p3, p4, p5, p6, p7, p8)
A = []
for x in Daftar:
    A.append(x.tahun)

print("MERGE SORT")
mergeSort(A)
a = 1
for x in convert(A, Daftar):
    print("Buku {}".format(a))
    print("Judul: "+x.judul)
    print("Nama Pengarang: "+x.nama)
    print("Kategori: "+x.kategori)
    print("Tahun: "+x.tahun)
    print("\n")
    a = a+1
