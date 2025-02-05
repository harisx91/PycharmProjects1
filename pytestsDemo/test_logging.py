import logging

def test_loggingDemo():
##Object to log everything
## __name__ catches the file name and prints out the name
    logger = logging.getLogger(__name__)

##it is an object where logfile will be executed
    fileHandler = logging.FileHandler("logfile.log")
    formater = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formater)

#It will accept
    logger.addHandler(fileHandler) #filehandler object (Nothing but file location)

#Setting level where to log everything

    logger.setLevel(logging.CRITICAL)

    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Warning statement is executed")
    logger.error("Error statement is executed") ##A major error occured
    logger.critical("Critical statement is executed") #Critical issue