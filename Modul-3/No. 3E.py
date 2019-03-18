class tgsLink4(object):
    def __init__(self, nama, next = None):
        self.data = nama
        self.next = next
a = tgsLink4(5)
b = tgsLink4(6)
c = tgsLink4(7)
d = tgsLink4(8)
a.next = b
b.next = c
c.next = d
print ("Simpul Awal")
print (a.data)
print (a.next.data)
print (a.next.next.data)
print (a.next.next.next.data)
def hapus(posisi):
    q = str(posisi)
    a = tgsLink4(5)
    b = tgsLink4(6)
    c = tgsLink4(7)
    d = tgsLink4(8)
    if q == "awal":
        b.next = c
        c.next = d
        print (b.data)
        print (b.next.data)
        print (b.next.next.data)
    elif q == "tengah":
        a.next = c
        c.next = d
        print (a.data)
        print (a.next.data)
        print (a.next.next.data)
    elif q == "akhir":
        a.next = b
        b.next = c
        print (a.data)
        print (a.next.data)
        print (a.next.next.data)
