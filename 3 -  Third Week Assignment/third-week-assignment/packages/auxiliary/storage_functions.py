import json
from json import JSONDecodeError
from packages.administration.admin_logic import AdminLogic
from packages.auxiliary.logger import Logger
from decouple import config


def load_data_from_json_file():
    """
    Try to load the data from JSON file

    Raises:
        JSONDecodeError: Error trying to load JSON data
        FileNotFoundError: File not found Error
    """
    try:
        with open(config('JSON_FILE_PATCH'), mode="r") as read_file:
            admin_logic_list = json.load(read_file)

        # Initializing dictionaries
        AdminLogic.tasks = {}
        AdminLogic.todo_lists = {}

        # Load data to class AdminLogic
        AdminLogic.load_data_from_list(admin_logic_list)

    except JSONDecodeError as err:
        Logger.error('Error trying to load JSON data.'
                     f'Error: {err} \n')
        # Initializing dictionaries
        AdminLogic.tasks = {}
        AdminLogic.todo_lists = {}

    except FileNotFoundError as err:
        Logger.warning('File not found Error.'
                       f'Error: {err} \n')
        # Initializing dictionaries
        AdminLogic.tasks = {}
        AdminLogic.todo_lists = {}


def save_data_as_json_file(admin_logic_list):
    """
    Try to save the data to JSON file

    Args:
        admin_logic_list: List representation of Admin logic class

    Raises:
        JSONDecodeError: Error trying to load JSON data
        FileNotFoundError: File not found Error
    """
    try:
        with open(config('JSON_FILE_PATCH'), mode="w+") as write_file:
            json.dump(admin_logic_list, write_file)
        Logger.info("The program has been saved successfully!")
    except JSONDecodeError as err:
        Logger.error('Error trying to save JSON data.'
                     f'Error: {err} \n')
    except FileNotFoundError as err:
        Logger.warning('File not found Error.'
                       f'Error: {err} \n')
