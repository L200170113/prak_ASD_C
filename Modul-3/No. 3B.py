class tgsLink2(object):
    def __init__(self, nama, next = None):
        self.data = nama
        self.next = next
def tambahDepan(x):
    print ("Simpul Awal")
    print (a.data)
    print (a.next.data)
    print (a.next.next.data)
    print (a.next.next.next.data)
    L = tgsLink2(x)
    L.next = a
    w = a
    print ("Simpul setelah ditambah")
    print (L.data)
    print (L.next.data)
    print (L.next.next.data)
    print (L.next.next.next.data)
    print (L.next.next.next.next.data)
a = tgsLink2(7)
b = tgsLink2(6)
c = tgsLink2(5)
d = tgsLink2(4)
a.next = b
b.next = c
c.next = d
