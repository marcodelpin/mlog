from mlog import MLog
import logging
import os

# Create a logger
logger = MLog("app_logger")

# Add a file handler in addition to console output
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

file_handler = logging.FileHandler(os.path.join(log_dir, "application.log"))
file_formatter = logging.Formatter(
    "%(levelname)s | %(asctime)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# Now logs will go to both console (with colors) and file (plain text)
logger.info("Application started")
logger.debug("Debug information")
logger.warning("Warning message")

try:
    # Simulate an error
    result = 10 / 0
except Exception as e:
    logger.error(f"Error occurred: {e}", exc_info=True)

logger.info("Application finished")