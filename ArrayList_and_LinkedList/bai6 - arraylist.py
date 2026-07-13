class AutoResizingArray:
    def __init__(self): self.capacity, self.size, self.arr = 4, 0, [0]*4
    def add(self, val):
        if self.size == self.capacity:
            self.capacity *= 2; new_arr = [0]*self.capacity
            for i in range(self.size): new_arr[i] = self.arr[i]
            self.arr = new_arr
        self.arr[self.size] = val; self.size += 1
ara = AutoResizingArray(); ara.add(1); print(ara.capacity)