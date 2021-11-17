# Create a Python class to describe a citizen of the City of Python. The class should be named Citizen and have the following data and functionality.

# A docstring that describes the class
# An init method that takes first_name and last_name arguments (strings) and assigns them as instance variables
# An instance method called full_name that returns a string that combines the first and last name instance variables, with a single space between them
# A class variable called greeting which is a string set to For the glory of Python!

class Citizen:
    """A class to represent a citizen of the City of Python"""

    greeting = "For the glory of Python!"

    def __init__(self, first_name, last_name):
        """Initialize the Citizen object"""
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        """Return the full name of the citizen"""
        return f"{self.first_name} {self.last_name}"
