import commandparser

class VersionCommandParser(commandparser.CommandParser):
    def fill_command(self, args):
        return VersionCommand()

class VersionCommand(commandparser.Command):
    @property
    def expects_input(self):
        return False
    def begin(self):
        pass
    def process(self, input):
        message = '{} does not expect input'.format(self.__class__.__name__)
        raise Exception(message)
    def end(self):
        return 'Version 0.1'
