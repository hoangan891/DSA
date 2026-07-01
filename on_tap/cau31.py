class ResizingList:
    def __init__(self):
        self.capacity, self.size, self.arr = 2, 0, [0]*2
    def append(self, val):
        if self.size == self.capacity:
            self.capacity *= 2; new_arr = [0]*self.capacity
            for i in range(self.size): new_arr[i] = self.arr[i]
            self.arr = new_arr
        self.arr[self.size] = val; self.size += 1
rl = ResizingList(); rl.append(10); print(rl.arr)