import commandparser

class CountLinesCommandParser(commandparser.CommandParser):
    def fill_command(self, args):
        return CountLinesCommand()

class CountLinesCommand:
    @property
    def expects_input(self):
        return True
    def begin(self):
        self.__count = 0
        return None
    def process(self, input):
        self.__count += 1
        return input
    def end(self):
        return self.__count
