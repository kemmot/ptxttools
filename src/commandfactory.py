import logging

import commandlineargumentexception

class CommandFactory:
    def __init__(self):
        self.__command_parsers = []
        self.__logger = logging.getLogger(self.__class__.__name__)

    def register(self, command_parser):
        self.__command_parsers.append(command_parser)

    def get_command(self, args):
        input_path, args = self.__get_input(args)
        if input_path is None:
            input_path = '-'

        output_path, args = self.__get_output(args)
        if output_path is None:
            output_path = '-'

        self.__logger.debug(f'Looking for command for args: [{args}]')
        for command_parser in self.__command_parsers:
            command = command_parser.get_command(args)
            if command != None:
                command.input_path = input_path
                command.output_path = output_path
                return command
        message = 'Unknown command: {}'.format(args[1])
        raise commandlineargumentexception.CommandLineArgumentException(message)

    def __get_input(self, args):
        arg_index = 0
        for arg in args:
            if arg == '-i' or arg == '--input':
                input = args[args.index(arg) + 1]
                args = args[:arg_index] + args[arg_index + 2:]
                return input, args
            arg_index += 1
        return None, args

    def __get_output(self, args):
        arg_index = 0
        for arg in args:
            if arg == '-o' or arg == '--output':
                input = args[args.index(arg) + 1]
                args = args[:arg_index] + args[arg_index + 2:]
                return input, args
            arg_index += 1
        return None, args
