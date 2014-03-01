import logging
import sys

log_file = "./semiSH.log"
log_level = logging.DEBUG

logger = logging.getLogger("logging.NormalLogger")
# add log to file
handler = logging.FileHandler(log_file)
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
# add log to stdout
sout = logging.StreamHandler(sys.stdout)
sfmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
sout.setFormatter(sfmt)
logger.addHandler(sout)

logger.setLevel(log_level)


def get():
    return logger


def shutdown():
    logging.shutdown()
