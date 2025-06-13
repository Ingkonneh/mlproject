# src/exception.py

import logging
import sys
from src.logger import logger  # Import the custom logger from you src into the exception.py


def error_message_detail(error, error_detail: sys):
    '''
    This function generates a detailed error message including the script name,
    line number, and the actual error message.
    '''
    _, _, exc_tb = sys.exc_info()  # Corrected to use sys, not error_detail
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'Error occurred in python script name [{0}] line number [{1}] error message [{2}]'.format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Corrected super call
        self.error_message = error_message_detail(error_message, error_detail)
    
    def __str__(self):
        return self.error_message
    
# Test logger with custom exception
if __name__ == '__main__':
    try:
        1 / 0
    except Exception as e:
        logger.info('Divide by zero occurred')  # This will now write to the log file
        raise CustomException(e, sys)
