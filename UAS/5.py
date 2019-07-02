print("====NOMOR 5====\n")
class Simpul(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

a = Simpul("B")
b = Simpul("C")
c = Simpul("D")
d = Simpul("A")
e = Simpul("F")
f = Simpul("E")

a.left = b; a.right = c
b.left = d
c.left = e; c.right = f

def postorder(akar):
    if akar is not None:
        postorder(akar.left)
        postorder(akar.right)
        print(akar.data)
