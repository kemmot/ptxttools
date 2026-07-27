import commandparser

class SortCommandParser(commandparser.CommandParser):
    def fill_command(self, args):
        return SortCommand()

class SortCommand(commandparser.Command):
    @property
    def expects_input(self):
        return True
    def begin(self):
        self.__lines = []
        return None
    def process(self, input):
        self.__lines.append(input)
        return input
    def end(self):
        output = ''
        for line in sorted(self.__lines, key=len):
            if len(output) > 0:
                #output += os.linesep
                output += '\n'
            output += line
        return output
