# standard modules
import logging
import os
import sys
import yaml

# custom modules
import commandlineargumentexception
import commandfactory
import logginghelper

# commands
import aligncommand
import countlinescommand
import formattimesheetcommand
import prefixlinescommand
import tabulatecommand
import versioncommand

EXIT_CODE_SUCCESS = 0
EXIT_CODE_EXECUTION_ERROR = 1
EXIT_CODE_ARGUMENT_ERROR = 2

logger = logging.getLogger(__name__)

def configure_logging():
    script_path = os.path.realpath(__file__)
    script_folder = os.path.dirname(script_path)
    loggingConfigFilename = 'log_config.yaml'
    logging_config_path = os.path.join(script_folder, loggingConfigFilename)
    try:
        logginghelper.configureLogging(logging_config_path)
    except Exception as e:
        logging.basicConfig(filename='ptxttools.log',level=logging.DEBUG)
        logger.error('Failed to initialize logging', e)

def log_command_line_arguments(args):
    logger.debug('%d command line argument(s)', len(args))
    for index in range(0, len(args)):
        arg = args[index]
        logger.debug('Argument %s: %s', index, arg)

def create_command(args):
    try:
        log_command_line_arguments(args)
        command_factory = commandfactory.CommandFactory()
        command_factory.register(aligncommand.AlignCommandParser())
        command_factory.register(countlinescommand.CountLinesCommandParser())
        command_factory.register(formattimesheetcommand.FormatTimesheetCommandParser())
        command_factory.register(prefixlinescommand.PrefixLinesCommandParser())
        command_factory.register(tabulatecommand.TabulateCommandParser())
        command_factory.register(versioncommand.VersionCommandParser())
        command = command_factory.get_command(args)
        return command
    except Exception as e:
        raise commandlineargumentexception.CommandLineArgumentException() from e

def process_command(command):    
    if command.output_path == '-':
        output_stream = sys.stdout
    else:    
        output_stream = open(command.output_path, 'w')

    command.begin()
    if command.expects_input:
        if command.input_path == '-':
            input_stream = sys.stdin
        else:    
            input_stream = open(command.input_path, 'r')

        for line in input_stream:
            output = command.process(line.rstrip())
            if output != None:
                print(str(output), file=output_stream)

        if input_stream != sys.stdin:
            input_stream.close()

    print(str(command.end()), file=output_stream)
    
    if output_stream != sys.stdin:
        output_stream.close()
    

try:
    configure_logging()
    command = create_command(sys.argv)
    process_command(command)
    exit_code = EXIT_CODE_SUCCESS
except commandlineargumentexception.CommandLineArgumentException as e:
    exit_code = EXIT_CODE_ARGUMENT_ERROR
    logger.error('Problem with command line arguments', exc_info=True)
except Exception as e:
    exit_code = EXIT_CODE_EXECUTION_ERROR
    logger.error('Problem with command execution', exc_info=True)

logger.debug('Exit code: {}'.format(exit_code))
sys.exit(exit_code)
