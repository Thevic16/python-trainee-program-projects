from packages.administration.admin_logic import AdminLogic
from packages.auxiliary.utility_functions import custom_input
import cmd

from packages.entities.entities import Task, Todo
from packages.exceptions.exceptions import IdDontExistException
from packages.exceptions.exceptions import TitleExistException


class AdminPrint(cmd.Cmd):
    """
    Admin Print is in charge to manage the input of data and
    display the information of the program.
    """

    def __init__(self):
        super(AdminPrint, self).__init__()

    @staticmethod
    def do_create_todo_list(*arg):
        """
        Receive data and call the necessary logic to create a todo list

        Args:
            *arg: Without this parameter the module cmd throw an error

        Raises:
            TitleExistException: Title already exist
        """
        title = custom_input("string", "Enter the title of the todo list:")
        try:
            AdminLogic.create_todo_list(title)
        except TitleExistException:
            print(f'The title "{title}" already exist.')

    @classmethod
    def do_add_task(cls, *arg):
        """
        Receive data and call the necessary logic to add an task

        Args:
            *arg: Without this parameter the module cmd throw a error

        Raises:
            IdDontExistException: Todo list id do not exist
        """
        dict_inputs = cls.get_custom_inputs_add_task()
        try:
            AdminLogic.add_task(dict_inputs.get("id_todolist"),
                                dict_inputs.get("title"),
                                dict_inputs.get("content"),
                                dict_inputs.get("tag"),
                                dict_inputs.get("status"))
        except IdDontExistException:
            print(f'The id "{dict_inputs.get("id_todolist")}" do not exist.')

    @staticmethod
    def do_list_all_current_tasks(*arg):
        """
        Display the information of all tasks

        Args:
            *arg: Without this parameter the module cmd throw an error
        """
        print('\n\n---------------------------',
              'List all the current tasks.',
              '---------------------------',
              f'{"Id_task":<25} '
              f'{"Id_todo":<25} '
              f'{"Title":<25} '
              f'{"Content":<25} '
              f'{"Tag":<25} '
              f'{"Status":<25} ', sep='\n'
              )

        for task in AdminLogic.tasks.values():
            print(f'{task.id_task:<25} '
                  f'{task.id_todolist:<25} '
                  f'{task.title:<25} '
                  f'{task.content:<25} '
                  f'{task.tag:<25} '
                  f'{task.status:<25} \n')

        print('---------------------------',
              'End.',
              '---------------------------', '', sep='\n')

    @classmethod
    def do_list_tasks_by_id_todo(cls, *arg):
        """
        Display the information of tasks by Todo list id

        Args:
            *arg: Without this parameter the module cmd throw an error
        """
        id_todo = custom_input("int", "Enter the id of todo List:")
        cls.list_tasks_by_id_todo(id_todo)

    @classmethod
    def do_list_all_todo_list(cls, *arg):
        """
        Display the information of all todo lists

        Args:
            *arg: Without this parameter the module cmd throw an error
        """
        print('\n\n---------------------------',
              'List all todo lists.',
              '---------------------------', '', sep='\n')

        for todo_list in AdminLogic.todo_lists.values():
            print('\n\n---------------------------',
                  'Todo list.',
                  '---------------------------', '',
                  f'{"Id_todo":<25} {"Title":<25}',
                  f'{todo_list.id_todo:<25} '
                  f'{todo_list.title:<25}', sep='\n')

            cls.list_tasks_by_id_todo(todo_list.id_todo)

        print('---------------------------',
              'End.',
              '---------------------------', '', sep='\n')

    @classmethod
    def do_obtain_task_by_id(cls, *arg):
        """
        Display the information of a task by id

        Args:
            *arg: Without this parameter the module cmd throw an error
        """
        id_task = custom_input("int", "Enter the id of the task:")
        try:
            cls.list_one_task(AdminLogic.obtain_task_by_id(id_task))
        except AttributeError as err:
            print('The Input type is incorrect. '
                  'Please try again.\n'
                  f'Error: {err} \n')

    @classmethod
    def do_obtain_todo_by_id(cls, arg):
        """
        Display the information of a todo list by id

        Args:
            *arg: Without this parameter the module cmd throw an error
        """
        id_todo = custom_input("int", "Enter the id of todo List:")
        try:
            cls.list_one_todo_list(AdminLogic.obtain_todo_by_id(id_todo))
        except AttributeError as err:
            print('The Input type is incorrect.'
                  ' Please try again.\n'
                  f'Error: {err} \n')

    @classmethod
    def do_modify_task(cls, *arg):
        """
        Receive data and call the necessary logic to modify a task

        Args:
            *arg: Without this parameter the module cmd throw an error

        Raises:
            AttributeError: The Input type is incorrect
            IdDontExistException: One o more provided id do not exist
        """
        dict_inputs = cls.get_custom_inputs_modify_task()
        try:
            AdminLogic.modify_task(dict_inputs.get("id_task"),
                                   dict_inputs.get("id_todolist"),
                                   dict_inputs.get("title"),
                                   dict_inputs.get("content"),
                                   dict_inputs.get("tag"),
                                   dict_inputs.get("status"))
        except AttributeError as err:
            print('The Input type is incorrect. '
                  'Please try again.\n'
                  f'Error: {err} \n')
        except IdDontExistException:
            print(f'The "id_task:{dict_inputs.get("id_task")} '
                  f'or id_todolist:{dict_inputs.get("id_todolist")}" '
                  f'do not exist.')

    @staticmethod
    def do_delete_task(*arg):
        """
        Receive data and call the necessary logic to delete a task

        Args:
            *arg: Without this parameter the module cmd throw an error

        Raises:
            AttributeError: The Input type is incorrect
        """
        id_task = custom_input("int", "Enter the id of the task:")
        try:
            AdminLogic.delete_task(id_task)
        except AttributeError as err:
            print('The Input type is incorrect.'
                  ' Please try again.\n'
                  f'Error: {err} \n')

    @classmethod
    def do_search_tasks_by_title(cls, *arg):
        """
        Display tasks based on a match in title

        Args:
            *arg: Without this parameter the module cmd throw an error
        """
        title = custom_input("string", "Enter the title of the task:")

        for task in AdminLogic.search_tasks_by_title(title):
            cls.list_one_task(task)

    @classmethod
    def do_search_tasks_by_content(cls, *arg):
        """
        Display tasks based on a match in content

        Args:
            *arg: Without this parameter the module cmd throw an error
        """
        content = custom_input("string", "Enter the title of the task:")

        for task in AdminLogic.search_tasks_by_content(content):
            cls.list_one_task(task)

    @staticmethod
    def do_EOF(*arg):
        """
        Allow to exit the program

        Args:
            *arg: Without this parameter the module cmd throw an error
        """
        return True

    # Auxiliar methods
    @staticmethod
    def list_one_task(task: Task):
        """
        Display the information of a task

        Args:
            task (Task): Task to display
        """
        print('\n\n---------------------------',
              'Task.',
              '---------------------------', '',
              f'{"Id_task":<25} {"Id_todo":<25} {"Title":<25} '
              f'{"Content":<25} {"Tag":<25} {"Status":<25}',
              f'{task.id_task:<25} {task.id_todolist:<25} '
              f'{task.title:<25} {task.content:<25} '
              f'{task.tag:<25} {task.status:<25}',
              '---------------------------',
              'End.',
              '---------------------------', '', sep='\n')

    @classmethod
    def list_one_todo_list(cls, todo: Todo):
        """
        Display the information of a todo list

        Args:
            todo (Todo): Todo list to display
        """
        print('\n\n---------------------------',
              'Todo list.',
              '---------------------------', '',
              f'{"Id_todo":<25} {"Title":<25}',
              f'{todo.id_todo:<25} {todo.title:<25}', sep='\n')
        cls.list_tasks_by_id_todo(todo.id_todo)
        print('---------------------------',
              'End.',
              '---------------------------', '', sep='\n')

    @staticmethod
    def list_tasks_by_id_todo(id_todo: int):
        """
        Display the information of a tasks by todo list id

        Args:
            id_todo (int): Todo list to display
        """
        print('\n\n---------------------------',
              'Sub-List task.',
              '----------------------------',
              f'{"Id_task":<25} {"Id_todo":<25} '
              f'{"Title":<25} {"Content":<25}'
              f'{"Tag":<25} {"Status":<25}', sep='\n'
              )

        for task in AdminLogic.obtain_tasks_by_id_todo(id_todo):
            print(f'{task.id_task:<25} {task.id_todolist:<25}'
                  f' {task.title:<25} {task.content:<25} '
                  f'{task.tag:<25} {task.status:<25} \n')

    @staticmethod
    def get_custom_inputs_modify_task() -> dict:
        """
        Return the data provided by the user
        Returns:
            dict_inputs (dict): Dictionary with task data
        """
        id_task = custom_input("int", "Enter the id of the task:")
        id_todolist = custom_input("int", "Enter the id of todo List:")
        title = custom_input("string", "Enter the title of the task:")
        content = custom_input("string", "Enter the content of task:")
        tag = custom_input("string", "Enter the tag of task:")
        status = custom_input("status", "Enter the status of task.\n"
                                        "Options.\n"
                                        "unassigned = 1 \n"
                                        "pending = 2 \n"
                                        "accepted = 3 \n"
                                        "started = 4 \n"
                                        "completed = 5 \n"
                                        "Enter selection (one number):")

        return {"id_task": id_task, "id_todolist": id_todolist,
                "title": title, "content": content, "tag": tag,
                "status": status}

    @staticmethod
    def get_custom_inputs_add_task() -> dict:
        """
        Return the data provided by the user
        Returns:
            dict_inputs (dict): Dictionary with task data
        """
        id_todolist = custom_input("int", "Enter the id of todo List:")
        title = custom_input("string", "Enter the title of the task:")
        content = custom_input("string", "Enter the content of task:")
        tag = custom_input("string", "Enter the tag of task:")
        status = custom_input("status", "Enter the status of task.\n"
                                        "Options.\n"
                                        "unassigned = 1 \n"
                                        "pending = 2 \n"
                                        "accepted = 3 \n"
                                        "started = 4 \n"
                                        "completed = 5 \n"
                                        "Enter selection (one number):")

        return {"id_todolist": id_todolist, "title": title,
                "content": content, "tag": tag, "status": status}
