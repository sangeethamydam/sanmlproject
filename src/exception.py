import sys
import logging

# Function to get detailed error message
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Get the exception details
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the filename where the error occurred
    error_message = "Error occurred in Python script: [{0}] at line number: [{1}] with message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

# Custom exception class to raise detailed error
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

# Main execution
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        a = 1 / 0  # Intentional ZeroDivisionError
    except Exception as e:
        logging.info("Logging has started, Divide by zero error")
        raise CustomException("A custom exception occurred", sys) from e
