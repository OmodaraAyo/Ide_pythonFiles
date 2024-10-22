import queue


class MyQueue:

    def __init__(self):
        self.__element_count = 0
        self.__element_data = [None]

    def add(self, item):
      self.__element_data.insert(self.__element_count, item)
      self.__element_count += 1
      return True

    def element(self):
        if self.__element_count == 0:
            return None
        return self.__element_data[0]

    def offer(self, item):
        return self.add(item)

    def peek(self):
        if self.__element_count == 0:
            return None
        return self.element()

    def poll(self):
        if self.__element_count == 0:
            return None
        return self.__remove()

    def remove(self):
        return self.__remove()

    def __remove(self):
        removed_item = self.__element_data[0]
        self.__element_data.pop(0)
        return removed_item

    # raise queue.Empty("Queue is empty")
