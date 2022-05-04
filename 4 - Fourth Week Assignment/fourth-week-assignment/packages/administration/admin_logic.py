from packages.entities.entities import Todo, Task, SortTask, SortKeyword
from packages.exceptions.exceptions import IdDontExistException
from packages.exceptions.exceptions import TitleExistException
from packages.auxiliary.logger import Logger
from packages.database.database import Database


class AdminLogic:
    """
    Admin Logic is in charge to manage the logic/operations of the program.
    """

    # Setup Database
    @staticmethod
    def setup_database(url: str):
        Database.setup_database(url)

    # Main methods
    @classmethod
    def create_todo_list(cls, title: str):
        """
        Allow to create a todo list

        Args:
            title (str): The title of the todo list

        Raises:
            TitleExistException: Title already exist
        """
        if cls.title_todo_exist(title):
            raise TitleExistException(title)
        else:
            Database.make_query(
                f"INSERT INTO todo (title) VALUES ('{title}');")

    @classmethod
    def add_task(cls, id_todolist: int, title: str, content: str,
                 tag: str, status: int):
        """
         Allow to add a task to a todo list

        Args:
            id_todolist (int): Todo list id
            title (str): Task title
            tag (str): Task tag
            content (str): Task content
            status (int): Task status

        Raises:
            IdDontExistException: Todo list id do not exist
        """
        if not cls.exist_todo(id_todolist):
            raise IdDontExistException(f'id_todolist:{id_todolist}')
        else:
            id_tag = cls.add_tag(tag)
            Database.make_query(
                f"INSERT INTO task (id_todolist, title, content, id_tag, "
                f"id_status) VALUES ({id_todolist}, "
                f"\'{title}\', \'{content}\', {id_tag}, {status});")

    @classmethod
    def obtain_task_by_id(cls, id_task: int) -> Task:
        """
        Try to return a task by id

        Args:
            id_task (int): Task id

        Returns:
            task (Task): if task id exist
        """
        if not cls.exist_task(id_task):
            raise IdDontExistException(f'id_task:{id_task}')

        task_query = \
            Database.make_query_with_return("SELECT task.id_task, "
                                            "task.id_todolist, "
                                            "task.title, "
                                            "task.content, "
                                            "tag.tag_name, "
                                            "status.status_name "
                                            "from task JOIN tag ON "
                                            "task.id_tag = "
                                            "tag.id_tag JOIN status "
                                            "ON task.id_status = "
                                            "status.id_status WHERE "
                                            f"task.id_task = "
                                            f"{id_task} ;")[0]

        return cls.create_task_as_object(task_query.get("id_task"),
                                         task_query.get("id_todolist"),
                                         task_query.get("title"),
                                         task_query.get("content"),
                                         task_query.get("tag_name"),
                                         task_query.get("status_name"))

    @classmethod
    def obtain_todo_by_id(cls, id_todo: int) -> Todo:
        """
        Try to return a todo list by id

        Args:
            id_todo (int): Todo list id

        Raises:
            IdDontExistException: Id todo do not exist

        Returns:
            todo (Todo): if todo id exist
        """
        if not cls.exist_todo(id_todo):
            raise IdDontExistException(f'id_todolist:{id_todo}')

        todo_query = \
            Database.make_query_with_return(f"SELECT * FROM todo WHERE"
                                            f" id_todo = {id_todo};")[0]

        return cls.create_todo_as_object(todo_query.get("id_todo"),
                                         todo_query.get("title"))

    @classmethod
    def modify_task(cls, id_task: int, id_todolist: int,
                    title: str, content: str, tag: str, status: int):
        """
        Try to modify an existing task

        Args:
            id_task (int): Task id
            id_todolist (int): Todo id
            title (str): Task title
            content (str): Task content
            tag (str): Task tag
            status (int): Task status

        Raises:
            IdDontExistException: Task id do not exist
        """
        if not cls.exist_todo(id_todolist):
            raise IdDontExistException(f'id_todolist:{id_todolist}')

        if not cls.exist_task(id_task):
            raise IdDontExistException(f'id_task:{id_task}')

        Database.make_query(f"UPDATE task SET id_todolist = {id_todolist}, "
                            f"title = \'{title}\', content = \'{content}\',"
                            f" id_tag = {cls.add_tag(tag)},id_status ={status}"
                            f" WHERE id_task = {id_task}")

    @classmethod
    def delete_task(cls, id_task: int):
        """
        Try to delete an existing task

        Raises:
            IdDontExistException: Task id do not exist

        Args:
            id_task (int): Task id
        """
        if not cls.exist_task(id_task):
            raise IdDontExistException(f'id_task:{id_task}')

        Database.make_query(f"DELETE FROM task WHERE id_task = {id_task}")
        print("The task have been deleted successfully.")
        # If I put this line with logger create an infinite loop
        # Logger.info("The task have been deleted successfully.")

    @classmethod
    def search_tasks_by_title(cls, title: str) -> list[Task]:
        """
        Search for a match at tasks titles

        Args:
            title (str): String to search for match

        Returns:
            title_tasks (list[Tasks]): List of tasks
        """

        return cls.create_tasks_as_object(
            Database.make_query_with_return(
                "SELECT task.id_task, task.id_todolist,"
                " task.title, task.content, tag.tag_name,"
                " status.status_name from "
                "task JOIN tag ON task.id_tag = tag.id_tag"
                " JOIN status ON task.id_status = status.id_status"
                f" WHERE task.title LIKE \'%%{title}%%\';")
        )

    @classmethod
    def search_tasks_by_content(cls, content: str) -> list[Task]:
        """
        Search for a match at tasks content

        Args:
            content (str): String to search for match

        Returns:
            content_tasks (list[Tasks]): List of tasks
        """

        return cls.create_tasks_as_object(
            Database.make_query_with_return(
                "SELECT task.id_task, task.id_todolist,"
                " task.title, task.content, tag.tag_name,"
                " status.status_name from "
                "task JOIN tag ON task.id_tag = tag.id_tag"
                " JOIN status ON task.id_status = status.id_status"
                f" WHERE task.content LIKE \'%%{content}%%\';")
        )

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

        return cls.create_tasks_as_object(
            Database.make_query_with_return("SELECT task.id_task,"
                                            " task.id_todolist,"
                                            " task.title,"
                                            " task.content,"
                                            " tag.tag_name,"
                                            " status.status_name "
                                            "from task JOIN tag "
                                            "ON task.id_tag = tag.id_tag"
                                            " JOIN status ON "
                                            "task.id_status = status.id_status"
                                            f" WHERE task.id_todolist "
                                            f"= {id_todo};")
        )

    # Method to transform data into objects.
    @staticmethod
    def create_todo_as_object(id_todo: int, title: str) -> Todo:
        """
        Allow to create a todo list object by parameters

        Args:
            id_todo (int): Todo list id
            title (str): Todo list title

        Returns:
            todo_list (Todo): Todo list
        """

        return Todo(id_todo, title)

    @classmethod
    def create_todos_as_object(cls, todos_as_list: list[dict]):
        """
        Allow to create a todo list object by list

        Args:
            todos_as_list (list[dict]): todos as list

        Returns:
            todos_list (List[Todo]): Todos list
        """

        return [cls.create_todo_as_object(todo_as_dict.get('id_todo'),
                                          todo_as_dict.get('title'))
                for todo_as_dict
                in todos_as_list]

    @staticmethod
    def create_task_as_object(id_task: int, id_todolist: int, title: str,
                              content: str, tag: str, status: int):
        """
        Allow to create a task object by parameters

        Args:
            id_task (int): Task id
            id_todolist (int): Todo id
            title (str): Task title
            content (str): Task content
            tag (str): Task tag
            status (int): Task status

        Returns:
            task (Task): Task list
        """

        return Task(id_task, id_todolist, title, content, tag, status)

    @classmethod
    def create_tasks_as_object(cls, tasks_as_list: list[dict]) -> list[Task]:

        return [cls.create_task_as_object(task_as_dict.get('id_task'),
                                          task_as_dict.get('id_todolist'),
                                          task_as_dict.get('title'),
                                          task_as_dict.get('content'),
                                          task_as_dict.get('tag_name'),
                                          task_as_dict.get('status_name'))
                for task_as_dict
                in tasks_as_list]

    # Exist methods
    @staticmethod
    def title_todo_exist(title: str) -> bool:
        """
        Verify if the todo list title already exist

        Args:
            title (str): Title to verify

        Raise:
            IndexError: Title is valid

        Returns:
            boolean: depends on the existence of the title
        """
        try:
            if title == Database.make_query_with_return(
                    f"SELECT title"
                    f" from todo "
                    f"WHERE title = '{title}';")[0].get("title"):
                return True
        except IndexError:
            Logger.info('Title is valid. \n')

        return False

    @classmethod
    def add_tag(cls, tag: str) -> int:
        """
        Allow to add a new tag if necessary

        Args:
            tag (str): Tag to add

        Returns:
            id_tag (int): The id of the tag
        """
        if not cls.exist_tag(tag):
            Database.make_query(f"INSERT INTO tag (tag_name) VALUES ('{tag}')")

        return Database.make_query_with_return(
            f"SELECT id_tag FROM tag WHERE tag_name = '{tag}';")[0].get(
            "id_tag")

    @staticmethod
    def exist_tag(tag: str) -> bool:
        """
        Verify if the tag already exist

        Args:
            tag (str): Tag to verify

        Raise:
            IndexError: Tag is new

        Returns:
            boolean: depends on the existence of the tag
        """
        try:
            if tag == Database.make_query_with_return(
                    f"SELECT tag_name FROM tag "
                    f"WHERE tag_name = '{tag}';")[0].get("tag_name"):
                return True
        except IndexError:
            Logger.info('Tag is new. \n')

        return False

    @staticmethod
    def exist_task(id_task: int) -> bool:
        """
        Verify if the Task already exist

        Args:
            id_task (int): Task to verify

        Raise:
            IndexError: Task is no valid

        Returns:
            boolean: depends on the existence of the task
        """
        try:
            if id_task == Database.make_query_with_return(
                    f"SELECT id_task FROM task "
                    f"WHERE id_task = {id_task};;")[0].get("id_task"):
                return True
        except IndexError:
            Logger.info('Task is not valid. \n')

        return False

    @staticmethod
    def exist_todo(id_todo: int) -> bool:
        """
        Verify if the Todo list already exist

        Args:
            id_todo (int): Todo list to verify

        Raise:
            IndexError: Todo is no valid

        Returns:
            boolean: depends on the existence of the todo
        """
        try:
            if id_todo == Database.make_query_with_return(
                    f"SELECT id_todo FROM todo "
                    f"WHERE id_todo = {id_todo};;")[0].get("id_todo"):
                return True
        except IndexError:
            Logger.info('Todo is not valid. \n')

        return False

    # Get entities from database methods
    @classmethod
    def get_tasks(cls) -> list[Task]:
        """
        Return all the task in the database
        Returns:
            tasks (list[Task]): Tasks from db
        """
        return cls.create_tasks_as_object(
            Database.make_query_with_return("SELECT task.id_task,"
                                            " task.id_todolist,"
                                            " task.title,"
                                            " task.content,"
                                            " tag.tag_name,"
                                            " status.status_name"
                                            " from task JOIN tag ON"
                                            " task.id_tag = tag.id_tag"
                                            " JOIN status ON "
                                            "task.id_status = status.id_status"
                                            ";")
        )

    @classmethod
    def get_todos(cls) -> list[Todo]:
        """
        Return all the todos in the database
        Returns:
            tasks (list[Task]): Tasks from db
        """
        return cls.create_todos_as_object(
            Database.make_query_with_return("SELECT * FROM todo;")
        )

    # Sort task Method
    @classmethod
    def sort_tasks(cls, sort_task: int, sort_keyword: int) -> list[Task]:
        """
        Return all the task in the database sort by a specify parameter
        Attributes
            sort_task (int): Enum that represent parameter to sort
            sort_keyword (int): Enum that represent keyword order (ASC or DESC)
        Returns:
            tasks (list[Task]): Tasks from db
        """
        return cls.create_tasks_as_object(
            Database.make_query_with_return("SELECT task.id_task,"
                                            " task.id_todolist,"
                                            " task.title,"
                                            " task.content,"
                                            " tag.tag_name,"
                                            " status.status_name, "
                                            " status.id_status "
                                            "from task JOIN tag"
                                            " ON task.id_tag = tag.id_tag "
                                            "JOIN status ON task.id_status"
                                            " = status.id_status ORDER BY "
                                            f"{SortTask(sort_task).name} "
                                            f"{SortKeyword(sort_keyword).name}"
                                            f";")
        )

    # Group tasks by tag method
    @classmethod
    def group_tasks_by_tag(cls, tag: str) -> list[Task]:
        """
        Return all the tasks in the database relater to the tag
        Attributes
            tag (str): Tag to search
        Returns:
            tasks (list[Task]): Tasks from db
        """
        return cls.create_tasks_as_object(
            Database.make_query_with_return("SELECT task.id_task,"
                                            " task.id_todolist,"
                                            " task.title,"
                                            " task.content,"
                                            " tag.tag_name,"
                                            " status.status_name"
                                            " from task JOIN tag"
                                            " ON task.id_tag = tag.id_tag"
                                            " JOIN status ON task.id_status"
                                            " = status.id_status"
                                            f" WHERE tag.tag_name = \'{tag}\'"
                                            ";")
        )
