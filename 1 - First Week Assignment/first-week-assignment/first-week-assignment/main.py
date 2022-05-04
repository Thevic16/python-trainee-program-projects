import cmd


def define_input(input_type, text):
    while True:
        try:
            data = input(text)
            if input_type == 'int':
                return int(data)
            if input_type == 'string':
                return data
            if input_type == 'boolean':
                if data == 'True':
                    return True
                elif data == 'False':
                    return False
                else:
                    print("Input should be a boolean type (True or False).")
        except BaseException as err:
            print('The Input type is incorrect. Please try again.\n'
                  f'Error: {err} \n')


class Task:
    def __init__(self, id_task, id_todolist, title, content, status):
        self.id_task = id_task
        self.id_todolist = id_todolist
        self.title = title
        self.content = content
        self.status = status


class Todo:
    def __init__(self, id_todo, title):
        self.id_todo = id_todo
        self.title = title


class Admin(cmd.Cmd):
    count_id_task = 0
    count_id_todo = 0
    tasks = {}
    todo_lists = {}

    # Main methods
    def do_create_todo_list(self, *arg):
        try:
            title = define_input("string", "Enter the title of the todo list:")
            new_todo = Todo(self.count_id_todo, title)
            self.todo_lists[new_todo.id_todo] = new_todo
            self.count_id_todo = self.count_id_todo + 1
        except BaseException as err:
            print('The Input type is incorrect. Please try again.\n'
                  f'Error: {err} \n')

    def do_add_task(self, *arg):
        try:
            id_todolist = define_input("int", "Enter the id of todo List:")
            title = define_input("string", "Enter the title of the task:")
            content = define_input("string", "Enter the content of task:")
            status = define_input("boolean", "Enter the status of task "
                                             "(True or False):")

            if self.count_id_todo > id_todolist >= 0:
                new_task = Task(self.count_id_task, id_todolist, title,
                                content, status)
                self.tasks[self.count_id_task] = new_task
                self.count_id_task = self.count_id_task + 1
            else:
                print("The id of todo List do not exist:")
        except BaseException as err:
            print('The Input type is incorrect. Please try again.\n'
                  f'Error: {err} \n')

    def do_list_all_current_tasks(self, *arg):
        try:
            print(('\n\n---------------------------\n'
                   'List all the current tasks. \n'
                   '--------------------------- \n'
                   f'{"Id_task":<30} '
                   f'{"Id_todo":<35} '
                   f'{"Title":<30} '
                   f'{"Content":<30} '
                   f'{"Status":<30} \n'
                   ))

            for ind in range(self.count_id_task):
                if ind in self.tasks.keys():
                    print(f'{self.tasks[ind].id_task:<30} '
                          f'{self.tasks[ind].id_todolist:<35} '
                          f'{self.tasks[ind].title:<30} '
                          f'{self.tasks[ind].content:<30} '
                          f'{str(self.tasks[ind].status):<30} \n')

            print(('--------------------------- \n'
                   'End. \n'
                   '--------------------------- \n\n'))
        except BaseException as err:
            print(f'The Input type is incorrect. Please try again.\n'
                  f'Error: {err} \n')

    def do_list_tasks_by_id_todo(self, *arg):
        try:
            id_todo = define_input("int", "Enter the id of todo List:")

            print(('\n\n--------------------------- \n'
                   'Sub-List task. \n'
                   '--------------------------- \n'
                   f'{"Id_task":<30} {"Id_todo":<35} {"Title":<30} '
                   f'{"Content":<30} {"Status":<30} \n'
                   ))

            tasks = self.obtain_tasks_by_id_todo(id_todo)

            for ind in range(len(tasks)):
                print(f'{tasks[ind].id_task:<30} {tasks[ind].id_todolist:<35}'
                      f' {tasks[ind].title:<30} {tasks[ind].content:<30}'
                      f'{str(tasks[ind].status):<30} \n')

            print(('--------------------------- \n'
                   'End. \n'
                   '--------------------------- \n \n'))
        except BaseException as err:
            print('The Input type is incorrect. Please try again.\n'
                  f'Error: {err} \n')

    def do_list_all_todo_list(self, *arg):
        try:
            print(('\n\n--------------------------- \n'
                   'List all todo lists. \n'
                   '--------------------------- \n\n'))

            for ind in range(self.count_id_todo):
                print(('\n\n--------------------------- \n'
                       'Todo list. \n'
                       '--------------------------- \n\n'
                       f'{"Id_todo":<30} {"Title":<35}'
                       f'{self.todo_lists[ind].id_todo:<30} '
                       f'{self.todo_lists[ind].title:<35}'))
                self.list_tasks_by_id_todo(ind)

            print(('--------------------------- \n'
                   'End. \n'
                   '--------------------------- \n \n'))
        except BaseException as err:
            print('The Input type is incorrect. Please try again.\n'
                  f'Error: {err} \n')

    def do_obtain_task_by_id(self, *arg):
        try:
            id_task = define_input("int", "Enter the id of the task:")
            self.list_one_task(self.tasks[id_task])
        except BaseException as err:
            print('The Input type is incorrect. Please try again.\n'
                  f'Error: {err} \n')

    def do_obtain_todo_by_id(self, arg):
        try:
            id_todo = define_input("int", "Enter the id of todo List:")
            # todo_tasks = self.obtain_tasks_by_id_todo(id_todo)
            self.list_one_todo_list(self.todo_lists[id_todo])
        except BaseException as err:
            print('The Input type is incorrect. Please try again.\n'
                  f'Error: {err} \n')

    def do_modify_task(self, *arg):
        try:
            id_task = define_input("int", "Enter the id of the task:")
            id_todolist = define_input("int", "Enter the id of todo List:")
            title = define_input("string", "Enter the title of the task:")
            content = define_input("string", "Enter the content of task:")
            status = define_input("boolean", "Enter the status of task "
                                             "(True or False):")

            if self.count_id_todo > id_todolist >= 0 \
                    and self.exist_id_task(id_task):
                task_to_modify = self.tasks[id_task]
                task_to_modify.id_todolist = id_todolist
                task_to_modify.title = title
                task_to_modify.content = content
                task_to_modify.status = status
            else:
                print("The id of todo List or task do not exist:")

        except BaseException as err:
            print('The Input type is incorrect. Please try again.\n'
                  f'Error: {err} \n')

    def do_delete_task(self, *arg):
        try:
            id_task = define_input("int", "Enter the id of the task:")
            self.tasks.pop(id_task)
            print("The task have been deleted successfully.")
        except BaseException as err:
            print('The Input type is incorrect. Please try again.\n'
                  f'Error: {err} \n')

    def do_search_tasks_by_title(self, *arg):
        try:
            title = define_input("string", "Enter the title of the task:")
            title_tasks = []

            for ind in range(self.count_id_task):
                if self.tasks[ind].title == title:
                    title_tasks.append(self.tasks[ind])

            for task in title_tasks:
                self.list_one_task(task)
        except BaseException as err:
            print('The Input type is incorrect. Please try again.\n'
                  f'Error: {err} \n')

    def do_search_tasks_by_content(self, *arg):
        try:
            content = define_input("string", "Enter the content of task:")
            content_tasks = []

            for ind in range(self.count_id_task):
                if self.tasks[ind].content == content:
                    content_tasks.append(self.tasks[ind])

            for task in content_tasks:
                self.list_one_task(task)
        except BaseException as err:
            print('The Input type is incorrect. Please try again.\n'
                  f'Error: {err} \n')

    # Auxiliary Methods
    def obtain_tasks_by_id_todo(self, id_todo):
        todo_tasks = []

        for ind in range(self.count_id_task):
            if ind in self.tasks.keys():
                if self.tasks[ind].id_todolist == id_todo:
                    todo_tasks.append(self.tasks[ind])

        return todo_tasks

    def list_one_task(self, task):
        print(('\n\n --------------------------- \n'
               'Task. \n'
               '--------------------------- \n\n'
               f'{"Id_task":<30} {"Id_todo":<35} {"Title":<30} '
               f'{"Content":<30} {"Status":<30}\n'
               f'{task.id_task:<30} {task.id_todolist:<35} '
               f'{task.title:<30} {task.content:<30} '
               f'{str(task.status):<30}\n'
               '--------------------------- \n'
               'End. \n'
               '--------------------------- \n \n'))

    def list_one_todo_list(self, todo):
        print(('\n\n --------------------------- \n'
               'Todo list. \n'
               '--------------------------- \n\n'
               f'{"Id_todo":<30} {"Title":<30}\n'
               f'{todo.id_todo:<30} {todo.title:<30}\n'))
        self.list_tasks_by_id_todo(todo.id_todo)
        print(('--------------------------- \n'
               'End. \n'
               '--------------------------- \n\n'))

    def list_tasks_by_id_todo(self, id_todo):
        print(('\n\n --------------------------- \n'
               'Sub-List task. \n'
               '--------------------------- \n'
               f'{"Id_task":<30} {"Id_todo":<35} '
               f'{"Title":<30} {"Content":<30} {"Status":<30} \n'
               ))
        tasks = self.obtain_tasks_by_id_todo(id_todo)

        for ind in range(len(tasks)):
            print(f'{tasks[ind].id_task:<30} {tasks[ind].id_todolist:<35}'
                  f' {tasks[ind].title:<30} {tasks[ind].content:<30} '
                  f'{str(tasks[ind].status):<30} \n')

    def exist_id_task(self, id_task):
        if self.tasks[id_task]:
            return True
        else:
            return False


if __name__ == '__main__':
    print("Write 'help' to see all the commands:")
    Admin().cmdloop()


