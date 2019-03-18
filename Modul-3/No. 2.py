#a
def buatNol(baris):
    'Masukkan ukuran'
    matriks = [[0 for j in range(baris)] for i in range(baris)]
    for i in matriks:
        print (i)
    print ("Matriks nol ber ordo",baris,'x',baris)

def BuatNol(baris, kolom):
    'm nilai kolom dan n nilai baris'
    matriks = [[0 for j in range(baris)] for i in range(kolom)]
    for i in matriks:
        print (i)
    print ("Matriks nol ber ordo",baris,'x',kolom)

##b
def buatIdentitas(baris):
    'Masukkan Ukuran'
    matriks = [[1 if j == i else 0 for j in range(baris)] for i in range(baris)]
    for i in matriks:
        print (i)
    print ("Matriks identitas ber ordo",baris,'x',baris)
