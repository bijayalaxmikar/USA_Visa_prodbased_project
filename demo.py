from usa_visa.logger import logging
from usa_visa.exception import USvisaException
import sys

logging.info("examining")

try:
    a = 1 / 0
except Exception as e:
    logging.error("An error occurred: %s", e)
    raise USVisaException(e, sys) from e
finally:
    logging.info("Execution completed")
