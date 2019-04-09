import logging
import logging.config
import os
import yaml

LOG_LEVEL_VERBOSE = 5

class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        """
        Format an exception so that it prints on a single line.
        """
        result = super(OneLineExceptionFormatter, self).formatException(exc_info)
        # return 'did this work' # repr(result)  # or format into one line however you want to
        return ''

    def format(self, record):
        s = super(OneLineExceptionFormatter, self).format(record)
        if record.exc_text:
            s = s.replace('\n', '') + '|'
        return s
        
def configureLogging(filename):
	logging.addLevelName(LOG_LEVEL_VERBOSE, "VERBOSE")
	
	if (os.path.isfile(filename)):
		try:
			extension = os.path.splitext(filename)[1]
			if (extension == '.ini'):
				logging.config.fileConfig(filename)
			elif (extension == '.json'):
				with open(filename) as file:
					config = json.load(file)
				logging.config.dictConfig(config)
			elif (extension == '.yaml'):
				with open(filename) as file:
					config = yaml.safe_load(file.read())
				logging.config.dictConfig(config)
			else:
				raise Exception('Unknown logging config file type: %s' % (extension))
		except Exception as ex:
			raise Exception('Failed processing logging config file: %s' % (filename)) from ex
	else:
		raise Exception('Logging config file does not exist: %s' % (filename))