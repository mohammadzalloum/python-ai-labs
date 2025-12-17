class LargeDatasetIterator :
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < (len(self.data)):
            value = self.data[self.index]
            self.index +=1
            return value
        else:
            #raise StopIteration
            return None


#R2
l = LargeDatasetIterator([1, 2, 3, 4, 5])
for i in range(6):
    print(l.__next__())


print(len([1, 2, 3, 4, 5]))