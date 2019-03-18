class tugasLink(object):
    def __init__(self, nama, next = None):
        self.data = nama
        self.next = next
#a
def cari(x, y):
    if y == 1:
        print (x.data)
    elif y == 2:
        print (x.next.data)
    elif y == 3:
        print (x.next.next.data)
    elif y == 4:
        print (x.next.next.next.data)
    else:
        print ("data tidak tersedia" )

a = tugasLink(10)
b = tugasLink(20)
c = tugasLink(30)
d = tugasLink(40)
a.next = b
b.next = c
c.next = d
print ("Headnya a, cari(a, (urutan data yg dicari))")
