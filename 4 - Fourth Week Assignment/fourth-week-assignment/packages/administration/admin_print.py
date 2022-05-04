import cmd
from packages.administration.admin_logic import AdminLogic
from packages.auxiliary.utility_functions import custom_input
from packages.entities.entities import Task, Todo
from packages.exceptions.exceptions import IdDontExistException
from packages.exceptions.exceptions import TitleExistException
from packages.auxiliary.logger import Logger


class AdminPrint(cmd.Cmd):
    """
    Admin Print is in charge to manage the input of data
    and display the information of the program.
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
        except AttributeError as err:
            Logger.error('The Input type is incorrect. '
                         'Please try again.\n'
                         f'Error: {err} \n')
        except TitleExistException:
            Logger.error(f'The title "{title}" already exist.')

    @classmethod
    def do_add_task(cls, *arg):
        """
        Receive data and call the necessary logic to add a task

        Args:
            *arg: Without this parameter the module cmd throw an error

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
        except AttributeError as err:
            Logger.error('The Input type is incorrect. '
                         'Please try again.\n'
                         f'Error: {err} \n')
        except IdDontExistException:
            Logger.error(f'The id "'
                         f'{dict_inputs.get("id_todolist")}"'
                         f' do not exist.')

    @classmethod
    def do_list_all_current_tasks(cls, *arg):
        """
        Display the information of all tasks

        Args:
            *arg: Without this parameter the module cmd throw an error
        """
        cls.list_multiples_tasks(AdminLogic.get_tasks())

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

        for todo_list in AdminLogic.get_todos():
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
            Logger.error('The Input type is incorrect. '
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
            Logger.error('The Input type is incorrect. '
                         'Please try again.\n'
                         f'Error: {err} \n')
        except IdDontExistException:
            Logger.error(f'The "id_todolist:{id_todo}" do not exist.')

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
            Logger.error('The Input type is incorrect. '
                         'Please try again.\n'
                         f'Error: {err} \n')
        except IdDontExistException:
            Logger.error(f'The "id_task:{dict_inputs.get("id_task")} '
                         f'or id_todolist:{dict_inputs.get("id_todolist")}"'
                         f' do not exist.')

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
            Logger.error('The Input type is incorrect.'
                         ' Please try again.\n'
                         f'Error: {err} \n')
        except IdDontExistException:
            Logger.error(f'The "id_task:{id_task}" do not exist.')

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

    @classmethod
    def do_sort_tasks(cls, *arg):
        """
        Display the information of tasks order by parameter

        Args:
            *arg: Without this parameter the module cmd throw an error
        """
        sort_task = custom_input("sorttask", "Enter the parameter to use "
                                             "to sort the tasks.\n"
                                             "Options.\n"
                                             "Id_task = 1 \n"
                                             "Id_todo = 2 \n"
                                             "Title = 3 \n"
                                             "Content = 4 \n"
                                             "Tag = 5 \n"
                                             "Status = 6 \n"
                                             "Enter selection (one number):")

        sort_keyword = custom_input("sortkeyword", "Enter the order to use "
                                                   "to sort the tasks.\n"
                                                   "Options.\n"
                                                   "Ascending = 1 \n"
                                                   "Descending = 2 \n"
                                                   "Enter selection (one "
                                                   "number):")

        cls.list_multiples_tasks(AdminLogic.sort_tasks(sort_task,
                                                       sort_keyword))

    @classmethod
    def do_group_tasks_by_tag(cls, *arg):
        """
        Display the information of tasks in the database relater to the tag

        Args:
            *arg: Without this parameter the module cmd throw an error
        """
        tag = custom_input("string", "Enter the tag to search the group:")

        cls.list_multiples_tasks(AdminLogic.group_tasks_by_tag(tag))

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

    @staticmethod
    def list_multiples_tasks(tasks: list[Task]):
        """
        Display the information of multiple tasks

        Args:
            tasks (list[Task]): tasks to list
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

        for task in tasks:
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
