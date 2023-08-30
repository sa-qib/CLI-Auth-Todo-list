from .exceptions import *
from utilities.display import Display

def get_input(text):
        """
        Get user input with a given prompt.

        Args:
            prompt (str): The prompt message.

        Returns:
            str: The user's input.
        """
        
        try:
            user_input = input(text).lower() 
            return user_input
        except EmptyValueError:
            Display.flash_msg("Value cannot be empty")
        except IncorrectIntError:
            Display.flash_msg("Priority must be between 1 and 10.")

