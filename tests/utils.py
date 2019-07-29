import re


def stripped(text):
    """
    Removes all whitespace from a string
    """
    return re.sub(r'\s+', '', text)
