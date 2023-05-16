import os

def clear_console():
    """
    clears the console when called
    https://www.delftstack.com/howto/python/python-clear-console/
    """
    command = 'clear'

    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'

    os.system(command)