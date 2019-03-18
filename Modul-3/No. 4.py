class Linked(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
a = Linked(15)
b = Linked(16)
c = Linked(17)
d = Linked(18)
print ("Simpul Awal")
print (a.data)
print (b.data)
print (c.data)
print (d.data)

#a
def cetakDepan():
    a.next = b
    b.next = c
    c.next = d
    print (a.data)
    print (a.next.data)
    print (a.next.next.data)
    print (a.next.next.next.data)
    
def cetakBelakang():
    d.prev = c
    c.prev = b
    b.prev = a
    print (d.data)
    print (d.prev.data)
    print (d.prev.prev.data)
    print (d.prev.prev.prev.data)

#b
def tambahDepan(x):
    a.next = b
    b.next = c
    c.next = d
    L = Linked(x)
    L.next = a
    print ("Setelah ditambah")
    print (L.data)
    print (L.next.data)
    print (L.next.next.data)
    print (L.next.next.next.data)
    print (L.next.next.next.next.data)

#c
def tambahAkhir(k):
    a = Linked(15)
    b = Linked(16)
    c = Linked(17)
    d = Linked(18)
    K = Linked(k)
    d.prev = c
    c.prev = b
    b.prev = a
    K.prev = d
    print ("Setelah ditambah")
    print (K.data)
    print (K.prev.data)
    print (K.prev.prev.data)
    print (K.prev.prev.prev.data)
    print (K.prev.prev.prev.prev.data)
