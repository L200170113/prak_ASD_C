print("====NOMOR 4====\n")

class PriorityQueue(object):
    def __init__(self):
        self.qlist = []

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.qlist)

    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)

    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        a = []
        for i in self.qlist:
            a.append(i.priority)
        print (self.qlist.pop(a.index(min(a))).item)

class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority


S = PriorityQueue()
S.enqueue("Buku Tulis", 4)
S.enqueue("Bolpoin", 1)
S.enqueue("Pensil", 5)
S.enqueue("Penggaris", 3)
S.enqueue("Spidol", 2)
