print("====NOMOR 3====\n")

class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.items)

    def pop(self):
        assert not self.isEmpty(), "Tidak bisa dipop dari Stack kosong"
        return self.items.pop()

    def push(self, data):
        self.items.append(data)
        
def cetakBiner(d):
    print ("Nilai desimal: {}".format(d))
    f = Stack()
    if d == 0: f.push(0);
    while d != 0:
        sisa = d%2
        d = d//2
        f.push(sisa)
    st = ""
    for i in range (len(f)):
        st = st + str(f.pop())
    return st

print (cetakBiner(10))
