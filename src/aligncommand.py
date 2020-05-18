import os

class AlignCommand:
    def __init__(self):
        self.__separator = ': '
    @property
    def expects_input(self):
        return True
    def init(self, args):
        if len(args) >= 3:
            self.__separator = args[2]
    def begin(self):
        self.__position = -1
        self.__lines = []
        return None
    def process(self, input):
        self.__lines.append(input)
        position = input.find(self.__separator)
        if position > self.__position:
            self.__position = position
        return None
    def end(self):
        output = ''
        for line in self.__lines:
            if len(output) > 0:
                #output += os.linesep
                output += '\n'
            left, right = line.split(self.__separator)
            output += left.ljust(self.__position) + self.__separator + right
        return output
