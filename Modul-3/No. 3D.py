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
def tambah(head, posisi):
    a = tgsLink4(5)
    b = tgsLink4(6)
    c = tgsLink4(7)
    d = tgsLink4(8)
    L = tgsLink4(head)
    if posisi == "awal":
        L.next = a
        a.next = b
        b.next = c
        c.next = d
        print (L.data)
        print (L.next.data)
        print (L.next.next.data)
        print (L.next.next.next.data)
        print (L.next.next.next.next.data)
