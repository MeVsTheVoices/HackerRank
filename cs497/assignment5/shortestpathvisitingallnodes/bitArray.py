class BitArray:
    def __init__(self, n):
        self.n = n
        self.bits = [False] * n
        self.count = 0

    def set(self, i):
        if not self.bits[i]:
            self.bits[i] = True
            self.count += 1

    def unset(self, i):
        if self.bits[i]:
            self.bits[i] = False
            self.count -= 1

    def numberOfSetBits(self):
        return self.count
    
    def numberOfUnsetBits(self):
        return self.n - self.count

    def __getitem__(self, i):
        return self.bits[i]
    
    def __len__(self):
        return self.n
    
    def __str__(self):
        return str(self.bits)
    
    def __iter__(self):
        return iter(self.bits)
    
    def __contains__(self, i):
        return self.bits[i]
    
    def __eq__(self, other):
        return self.bits == other.bits