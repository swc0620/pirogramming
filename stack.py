class test_public():
    def __init__(self):
        self.arr = [1, 2, 3]

test1= test_public()
test1.arr[1]

class test_private():
    def __init__(self):
        self.__arr = [1, 2, 3]
    def get(self, index):
        return self.__arr[index]

test2 = test_private()
test2.arr[1]

class stack():
    def __init__(self):
        self.__arr = []
        self.__top = 0

    def push(self, item):
        self.__arr.append(item)
        self.__top += 1

    def isEmpty(self):
        if self.__arr == []:
            True
        else:
            False
    def pop(self):
        if self.isEmpty():
            return False
        else:
            self.__top -= 1
            item = self.__arr[self.__top]
            del(self.__arr[self.__top])

            return item
    def peek (self):
        if self.isEmpty():
            return False
        else item = self__arr[self.top - 1]:
                return item