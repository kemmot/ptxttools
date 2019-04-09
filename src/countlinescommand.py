class CountLinesCommand:
    def begin(self):
        self.__count = 0
        return None
    def process(self, input):
        self.__count += 1
        return input
    def end(self):
        return self.__count
