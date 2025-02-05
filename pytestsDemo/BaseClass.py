import inspect
import logging

class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        ##Object to log everything
        ## __name__ catches the file name and prints out the name
        logger = logging.getLogger(loggerName)

        ##it is an object where logfile will be executed
        fileHandler = logging.FileHandler("logfile.log")
        formater = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formater)

        # It will accept
        logger.addHandler(fileHandler)  # filehandler object (Nothing but file location)

        # Setting level where to log everything

        logger.setLevel(logging.DEBUG)

        return logger