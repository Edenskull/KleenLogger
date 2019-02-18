import logging
from time import strftime

filename = "log/{}-{}.log".format("myapp", strftime("%Y_%m_%d_%H_%M_%S"))

logging.basicConfig(
    level=logging.INFO,
    filename=filename,
    format="[%(asctime)s][%(levelname)s] : [%(filename)s][%(funcName)s] : %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

pylogger = logging.getLogger()
