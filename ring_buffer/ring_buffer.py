
class RingBuffer:
    def __init__(self, size_max):
        self.max = size_max
        self.data = []

    # class __Full:
    #     def append(self, x):

    def append(self, x):
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            self.data[self.cur] = x
            self.cur = (self.cur+1) % self.max
            # Permanently change self's class from non-full to full
            # self.__class__ = self.__Full

    def get(self):
        return self.data


new_ring = RingBuffer(5)
# for i in range(50):
#     new_ring.append(i)
new_ring.append(1)
new_ring.append(2)
new_ring.append(3)
new_ring.append(4)
new_ring.append(5)
new_ring.get()
