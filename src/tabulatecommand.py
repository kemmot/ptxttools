import commandlineargumentexception
import commandparser

class TabulateCommandParser(commandparser.CommandParser):
    def fill_command(self, args):
        if len(args) < 3:
            message = 'Delimiter argument not specified'
            raise commandlineargumentexception.CommandLineArgumentException(message)
        command = TabulateCommand()
        command.delimiter = args[2]
        return command

class TabulateCommand:
    def __init__(self):
        self.__delimiter = ''
        self.__rows = []
        self.__column_widths = []
    @property
    def expects_input(self):
        return True
    @property
    def delimiter(self):
        return self.__delimiter
    @delimiter.setter
    def delimiter(self, value):
        self.__delimiter = value
    def begin(self):
        return None
    def process(self, input):
        cells = input.split(self.__delimiter)
        self.__rows.append(cells)
        column_index = 0
        for cell in cells:
            if column_index >= len(self.__column_widths):
                self.__column_widths.append(len(cell))
            elif len(cell) > self.__column_widths[column_index]:
                self.__column_widths[column_index] = len(cell)
            column_index += 1
        return None
    def end(self):
        output = ''
        for row in self.__rows:
            if output:
                output += '\n'
            column_index = 0
            for cell in row:
                if column_index > 0:
                    output += self.__delimiter
                output += cell.ljust(self.__column_widths[column_index])
                column_index += 1
        return output
