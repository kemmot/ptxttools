# standard modules
import logging
import os
import sys
import yaml

# custom modules
import logginghelper

# commands
import countlinescommand

EXIT_CODE_SUCCESS = 0
EXIT_CODE_EXECUTION_ERROR = 1
EXIT_CODE_ARGUMENT_ERROR = 2

logger = logging.getLogger(__name__)

class CommandLineArgumentException(Exception):
    pass

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

def process_command():
    command = countlinescommand.CountLinesCommand()
    command.begin()
    for line in sys.stdin:
        print(str(command.process(line.rstrip())))
    print(str(command.end()))

try:
    configure_logging()
    process_command()
    exit_code = EXIT_CODE_SUCCESS
except CommandLineArgumentException as e:
    exit_code = EXIT_CODE_ARGUMENT_ERROR
    logger.error('Problem with command line arguments', e)
except Exception as e:
    exit_code = EXIT_CODE_EXECUTION_ERROR
    logger.error('Problem with command execution', e)

logger.debug('Exit code: {}'.format(exit_code))
sys.exit(exit_code)
