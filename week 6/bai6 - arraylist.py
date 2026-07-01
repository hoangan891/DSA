class AutoResizingArray:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity
    def add(self, val):
        if self.size == self.capacity:
            self.capacity *= 2
            new_arr = [0] * self.capacity
            for i in range(self.size): new_arr[i] = self.arr[i]
            self.arr = new_arr
        self.arr[self.size] = val
        self.size += 1
ara = AutoResizingArray()
print(ara.capacity)