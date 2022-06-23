import enum
from dataclasses import dataclass


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
class Task:
    """
    Represents a task

    Attributes:
        id_task (int): Task id
        id_todolist (int): Todo list id
        title (str): Task title
        tag (str): Task tag
        content (str): Task content
        status (str): Task status
        ('unassigned', 'pending', 'accepted', 'started', 'completed')
    """
    __slots__ = ['id_task', 'id_todolist', 'title', 'content', 'tag', 'status']
    id_task: int
    id_todolist: int
    title: str
    content: str
    tag: str
    status: str


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
