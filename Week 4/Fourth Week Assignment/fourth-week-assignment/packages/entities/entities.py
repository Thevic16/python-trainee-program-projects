import enum
from dataclasses import dataclass


@dataclass
class Task:
    """
    Represents a task

    Attributes:
        id_task (int): Task id
        id_todolist (int): Todo list id
        title (str): Task title
        content (str): Task content
        tag (str): Task tag
        status (int): Task status
        ('unassigned', 'pending', 'accepted', 'started', 'completed')
    """
    __slots__ = ['id_task', 'id_todolist', 'title', 'content', 'tag', 'status']
    id_task: int
    id_todolist: int
    title: str
    content: str
    tag: str
    status: int


@dataclass
class Todo:
    """
    Represents a Todo list

    Attributes:
        id_todo (int): Todo list id
        title (str): Todo list title
    """
    __slots__ = ['id_todo', 'title']
    id_todo: int
    title: str


@dataclass
class Status(enum.Enum):
    """
    Represents the states that a task can take

    Attributes:
        unassigned
        pending
        accepted
        started
        completed
    """
    __slots__ = ['unassigned', 'pending', 'accepted', 'started', 'completed']
    unassigned: int = 1
    pending: int = 2
    accepted: int = 3
    started: int = 4
    completed: int = 5


@dataclass
class SortTask(enum.Enum):
    """
    Represents the different parameter that the tasks can be sort

    Attributes:
        id_task
        id_todolist
        title
        content
        tag_name
        status_name
    """
    __slots__ = ['id_task', 'id_todolist', 'title', 'content', 'tag_name',
                 'status_name']
    id_task: int = 1
    id_todolist: int = 2
    title: int = 3
    content: int = 4
    tag_name: int = 5
    id_status: int = 6


@dataclass
class SortKeyword(enum.Enum):
    """
    Represents the different orders that the tasks can be sort

    Attributes:
        ASC
        DESC
    """
    __slots__ = ['ASC', 'DESC']
    ASC: int = 1
    DESC: int = 2
