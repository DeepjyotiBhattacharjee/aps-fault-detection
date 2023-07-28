import sys
import os

def error_message_details(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in python script : {file_name} on line number : {exc_tb.tb_lineno}. Error message : {str(error)}"
    return error_message

class SensorException(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message_details(error_message,error_details=error_details)

    def __str__(self):
        return self.error_message
