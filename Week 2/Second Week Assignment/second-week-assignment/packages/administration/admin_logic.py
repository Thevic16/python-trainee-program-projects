from packages.entities.entities import Todo
from packages.entities.entities import Task
from packages.exceptions.exceptions import IdDontExistException
from packages.exceptions.exceptions import TitleExistException
from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict


@dataclass
class AdminLogic:
    """
    Admin Logic is in charge to manage the logic/operations of the program.

    Attributes:
        count_id_task (int): Amount of tasks.
        count_id_todo (int): Amount of Todo List.
        tasks (dict[int, Task]): Dict that contains the tasks.
        todo_lists (dict[int, Todo]): Dict that contains the Todo Lists.
    """
    # If I put this line raise the following.
    # ValueError: 'count_id_task' in __slots__ conflicts with class variable
    # __slots__ = ['count_id_task', 'count_id_todo', 'tasks', 'todo_lists']
    count_id_task: int = 0
    count_id_todo: int = 0
    tasks: dict[int, Task] = field(default_factory=dict)
    todo_lists: dict[int, Todo] = field(default_factory=dict)

    # Main methods
    @classmethod
    def create_todo_list(cls, title: str) -> Todo:
        """
        Allow to create a todo list

        Args:
            title (str): The title of the todo list

        Raises:
            TitleExistException: Title already exist

        Returns:
            new_todo (Todo): The created todo list
        """
        if cls.title_todo_exist(title):
            raise TitleExistException(title)
        else:
            new_todo = Todo(cls.count_id_todo, title)
            cls.todo_lists[new_todo.id_todo] = new_todo
            cls.count_id_todo = cls.count_id_todo + 1
            return new_todo

    @classmethod
    def add_task(cls, id_todolist: int, title: str, content: str,
                 tag: str, status: str) -> Task:
        """
         Allow to add a task to a todo list

        Args:
            id_todolist (int): Todo list id
            title (str): Task title
            tag (str): Task tag
            content (str): Task content
            status (str): Task status
            ('unassigned', 'pending', 'accepted', 'started', 'completed')

        Raises:
            IdDontExistException: Todo list id do not exist

        Returns:
            new_task (Task): The added task
        """
        if cls.count_id_todo > id_todolist >= 0:
            new_task = Task(cls.count_id_task, id_todolist, title,
                            content, tag, status)
            cls.tasks[cls.count_id_task] = new_task
            cls.count_id_task = cls.count_id_task + 1
            return new_task
        else:
            raise IdDontExistException(id_todolist)

    @classmethod
    def obtain_task_by_id(cls, id_task: int) -> Task:
        """
        Try to return a task by id

        Args:
            id_task (int): Task id

        Returns:
            task (Task): if task id exist
            None: if don't exist
        """
        return cls.tasks.get(id_task, None)

    @classmethod
    def obtain_todo_by_id(cls, id_todo: int) -> Todo:
        """
        Try to return a todo list by id

        Args:
            id_todo (int): Todo list id

        Returns:
            todo (Todo): if todo id exist
            None: if don't exist
        """
        return cls.todo_lists.get(id_todo, None)

    @classmethod
    def modify_task(cls, id_task: int, id_todolist: int,
                    title: str, content: str, tag: str, status: str) -> Task:
        """
        Try to modify an existing task

        Args:
            id_task (int): Task id
            id_todolist: Todo id
            title: Task title
            content: Task content
            tag: Task tag
            status: Task status
            ('unassigned', 'pending', 'accepted', 'started', 'completed')

        Raises:
            IdDontExistException: Task id do not exist

        Returns:
            task (Task): if task id exist
        """
        if id_todolist >= cls.count_id_todo or id_todolist < 0:
            raise IdDontExistException(f'id_todolist:{id_todolist}')

        task_to_modify = cls.tasks.get(id_task, None)

        if task_to_modify is None:
            raise IdDontExistException(f'id_task:{id_task}')

        task_to_modify.id_todolist = id_todolist
        task_to_modify.title = title
        task_to_modify.content = content
        task_to_modify.tag = tag
        task_to_modify.status = status
        return task_to_modify

    @classmethod
    def delete_task(cls, id_task: int):
        """
        Try to delete an existing task

        Raises:
            KeyError: Task id do not exist

        Args:
            id_task (int): Task id

        """
        try:
            cls.tasks.pop(id_task)
        except KeyError:
            print(f'Key {id_task} not found in the dictionary.\n')
        else:
            print("The task have been deleted successfully.")

    @classmethod
    def search_tasks_by_title(cls, title: str) -> list[Task]:
        """
        Search for a match at tasks titles

        Args:
            title (str): String to search for match

        Returns:
            title_tasks (list[Tasks]): List of tasks
        """
        title_tasks = [task for task in cls.tasks.values()
                       if title.lower() in task.title.lower()]
        return title_tasks

    @classmethod
    def search_tasks_by_content(cls, content: str) -> list[Task]:
        """
        Search for a match at tasks content

        Args:
            content (str): String to search for match

        Returns:
            content_tasks (list[Tasks]): List of tasks
        """
        content_tasks = [task for task in cls.tasks.values()
                         if content.lower() in task.content.lower()]
        return content_tasks

    # Auxiliary Methods
    @classmethod
    def obtain_tasks_by_id_todo(cls, id_todo: int) -> list[Task]:
        """
        Return a tasks' list by todo list id

        Args:
            id_todo: Todo list id

        Returns:
            todo_tasks (list[Tasks]): List of tasks
        """

        return [task for task in cls.tasks.values()
                if id_todo == task.id_todolist]

    @classmethod
    def title_todo_exist(cls, title: str):
        """
        Verify if the todo list title already exist

        Args:
            title (str): Title to verify

        Returns:
            boolean: depends on the existence of the title
        """
        for todo_list in cls.todo_lists.values():
            if title == todo_list.title:
                return True

        return False

    @classmethod
    def create_todo_list_load_data(cls, id_todo: int, title: str):
        """
        Allow to create a todo list by parameters

        Args:
            id_todo (int): Todo list id
            title (str): Todo list title
        """
        new_todo = Todo(id_todo, title)
        cls.todo_lists[id_todo] = new_todo

    @classmethod
    def add_task_load_data(cls, id_task: int, id_todolist: int, title: str,
                           content: str, tag: str, status: str):
        """
        Allow to create a task by parameters

        Args:
            id_task (int): Task id
            id_todolist: Todo id
            title: Task title
            content: Task content
            tag: Task tag
            status: Task status
            ('unassigned', 'pending', 'accepted', 'started', 'completed')
        """
        new_task = Task(id_task, id_todolist, title,
                        content, tag, status)
        cls.tasks[id_task] = new_task

    @classmethod
    def load_data_from_list(cls, admin_logic_list:
                            list[int, int, list[dict], list[dict]]):
        """
        Allow to load the data from a list representation of the class
        Args:
            admin_logic_list (list):  List representation of the class

        Raises:
            IndexError: Index Error when load list data
        """
        try:
            cls.load_counters(admin_logic_list[0], admin_logic_list[1])
            cls.load_todo_lists(admin_logic_list[3])
            cls.load_tasks(admin_logic_list[2])

        except IndexError as err:
            print('Index Error when load list data.\n'
                  f'Error: {err} \n')

    @classmethod
    def load_counters(cls, count_id_task: int, count_id_todo: int):
        """
        Help to load the counters from the list representation of the class
        Args:
            count_id_todo (int): Counter id todo
            count_id_task (int): Counter id task
        """
        cls.count_id_task = count_id_task
        cls.count_id_todo = count_id_todo

    @classmethod
    def load_todo_lists(cls, todo_lists_dic: list[dict]):
        """
        Help to load the todo list from the list representation
        of the class
        Args:
            todo_lists_dic (list[dict]): List of dictionaries
            with todo list data
        Raises:
            KeyError: Id do not exist in the list
        """
        try:
            for todo_list_dic in todo_lists_dic:
                cls.create_todo_list_load_data(todo_list_dic['id_todo'],
                                               todo_list_dic['title'])
        except KeyError as err:
            print(f'Key not found in the dictionary. '
                  f'Error: {err}\n')

    @classmethod
    def load_tasks(cls, tasks_dic):
        """
        Help to load the task from the list representation of the class
        Args:
            tasks_dic (list[dict]): List of dictionaries with task data

        Raises:
            KeyError: Id do not exist in the list
        """
        try:
            for task_dic in tasks_dic:
                cls.add_task_load_data(task_dic['id_task'],
                                       task_dic['id_todolist'],
                                       task_dic['title'],
                                       task_dic['content'],
                                       task_dic['tag'],
                                       task_dic['status'])
        except KeyError as err:
            print(f'Key not found in the dictionary. '
                  f'Error: {err}\n')

    @classmethod
    def get_admin_logic_as_list(cls):
        """
        Return a class representation as a list

        Returns:
            admin_logic (list): class representation as a list
        """
        tasks_json = [asdict(task_dic)
                      for task_dic in cls.tasks.values()]
        todo_lists_json = [asdict(todo_list_dic)
                           for todo_list_dic in cls.todo_lists.values()]

        return [cls.count_id_task, cls.count_id_todo,
                tasks_json, todo_lists_json]
