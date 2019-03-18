class tgsLink3(object):
    def __init__(self, nama, next = None):
        self.data = nama
        self.next = next
def tambahAkhir(x):
    a = tgsLink3(12)
    b = tgsLink3(13)
    c = tgsLink3(14)
    d = tgsLink3(15)
    a.next = b
    b.next = c
    c.next = d
    print ("Simpul Awal")
    print (a.data)
    print (a.next.data)
    print (a.next.next.data)
    print (a.next.next.next.data)
    
    a = tgsLink3(11)
    b = tgsLink3(12)
    c = tgsLink3(13)
    d = tgsLink3(14)
    L = tgsLink3(x)
    a.next = b
    b.next = c
    c.next = d
    d.next = L
    print ("Nilai setelah di tambah")
    print (a.data)
    print (a.next.data)
    print (a.next.next.data)
    print (a.next.next.next.data)
    print (a.next.next.next.next.data)
