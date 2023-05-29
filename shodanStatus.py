import os
from utils.Exceptions import *
from utils.helper import *

config = read_config()
LOGGER = logger("SHODAN_LOGGER")
PROCNAME = config["default"]["PROCNAME"]
CMD1 = config["default"]["COMMAND1"]
CMD2 = config["default"]["COMMAND2"]
CMD3 = config["default"]["COMMAND3"]

try:
    LOGGER.info(f"Checking if process {PROCNAME} is running")
    procRun = os.popen(CMD1).read()
    procCount = procRun.count(PROCNAME)
    print(procCount)
    LOGGER.info(f"Process {PROCNAME} has been detected running {procCount} times")
    if procCount>0:
        procStatus = os.popen(CMD2+" "+PROCNAME).readlines()
        print(procStatus)
        os.popen(CMD3)
        LOGGER.info("Process was restarted successfully")
    if procCount<=0:
        os.popen(CMD3)
        LOGGER.info("Process was started successfully")    
except Exception as err:
    LOGGER.fatal(err)