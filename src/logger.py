# import logging
# import os
# from datetime import datetime

# # Define logs directory
# LOG_DIR = os.path.join(os.getcwd(), 'logs')
# os.makedirs(LOG_DIR, exist_ok=True)  # Ensure logs directory exists

# # Create log file with timestamp
# LOG_FILE = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
# LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# # Configure logging
# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )
# logger = logging.getLogger(__name__)

# if __name__ == '__main__':
#     logging.info('Logging has started')


# src/logger.py

import logging
import os
from datetime import datetime

# Create logs directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Log file name with timestamp
LOG_FILE = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)
