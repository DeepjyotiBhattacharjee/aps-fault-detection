import logging
import os
from datetime import datetime
import sys

LOGFILE_NAME = f"{datetime.now().strftime('%d%m%Y_%H%M%S')}.log"
LOGFILE_DIR = os.path.join(os.getcwd(),"logs")

# create logs folder if not available
os.makedirs(LOGFILE_DIR,exist_ok=True)

# create logfile path
LOGFILE_PATH = os.path.join(LOGFILE_DIR,LOGFILE_NAME)

logging.basicConfig(
    filename=LOGFILE_PATH,
    format=" [ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s ",
    level=logging.INFO
)