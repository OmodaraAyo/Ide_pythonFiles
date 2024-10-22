class MyStack:

    def __init__(self):
        self.__elementCount = 0
        self.__elementData = []

    def is_empty(self):
        return self.__elementCount == 0

    def append(self, item):
        self.__elementData.insert(self.__elementCount, item)
        self.__elementCount += 1
        return self.peek()

    def peek(self):
        if self.is_empty():
            self.empty_stack_exception()
        return self.__elementData[self.__elementCount - 1]

    def pop(self):
        if self.is_empty():
            self.empty_stack_exception()
        removed_item = self.peek()
        self.__elementData.pop(self.__elementCount - 1)
        self.__elementCount -= 1
        return removed_item

    def search(self, item):
        if self.is_empty():
            return -1
        for i in range(len(self.__elementData)):
            if self.__elementData[i] == item:
                return i

    def none_(self):
            return None

    def empty_stack_exception(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty")

