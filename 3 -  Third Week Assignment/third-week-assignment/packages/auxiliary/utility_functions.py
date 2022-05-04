from packages.entities.entities import Status
from packages.auxiliary.logger import Logger


def custom_input(input_type, text):
    """
    Allow to receive custom input from the user

    Args:
        input_type (str): Specify the selected mode
        text (str): Text to display to the user

    Returns:
        data: The information received from the user
    """
    while True:
        try:
            data = input(text)
            if input_type == 'int':
                return int(data)
            if input_type == 'string':
                return data
            if input_type == 'status':
                if 1 <= (selection := int(data)) <= 5:
                    return Status(selection).name
                else:
                    print("Input should be one of the options.")
        except ValueError as err:
            Logger.error('The Input type is incorrect. '
                         'Please try again.\n'
                         f'Error: {err} \n')
