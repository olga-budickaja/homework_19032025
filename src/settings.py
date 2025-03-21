import logging
import os
import sys

from dotenv import load_dotenv

load_dotenv()


DB_NAME=os.environ["DB_NAME"]
DB_USER=os.environ["DB_USER"]
DB_PASSWORD=os.environ["DB_PASSWORD"]
DB_HOST=os.environ["DB_HOST"]
DB_PORT=os.environ["DB_PORT"]

# Logger
logger = logging.getLogger("server")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

file_handler= logging.FileHandler("server.log")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s -  %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
