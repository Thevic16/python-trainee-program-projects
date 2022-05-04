import unittest
from packages.administration.admin_logic import AdminLogic
from packages.database.database import Database
from packages.entities.entities import Status
from packages.exceptions.exceptions import IdDontExistException
from packages.exceptions.exceptions import TitleExistException


class TestAdminLogic(unittest.TestCase):
    # Need to work on that
    # Test Attributes
    test_todo_list1 = None
    test_todo_list2 = None
    test_task1 = None
    test_task2 = None
    test_task3 = None
    test_task4 = None
    test_task5 = None
    unassigned_positive_id = 100
    unassigned_negative_id = -1

    def setUp(self):
        # Setup Database
        AdminLogic.setup_database('URL_TEST_DATABASE')

        # Create a test todo list
        AdminLogic.create_todo_list("test todo 1 list")
        self.test_todo_list1 = AdminLogic.obtain_todo_by_id(1)

        AdminLogic.create_todo_list("test todo 2 list")
        self.test_todo_list2 = AdminLogic.obtain_todo_by_id(2)

        # Create test tasks attach to todo list 1
        AdminLogic.add_task(self.test_todo_list1.id_todo,
                            "test task1 title",
                            "test task1 content",
                            "test task1 tag",
                            1)
        self.test_task1 = AdminLogic.obtain_task_by_id(1)

        AdminLogic.add_task(self.test_todo_list1.id_todo,
                            "test task2 title",
                            "test task2 content",
                            "test task2 tag",
                            2)
        self.test_task2 = AdminLogic.obtain_task_by_id(2)

        AdminLogic.add_task(self.test_todo_list2.id_todo,
                            "test task3 title",
                            "test task3 content",
                            "test task3 tag",
                            3)
        self.test_task3 = AdminLogic.obtain_task_by_id(3)

        AdminLogic.add_task(self.test_todo_list2.id_todo,
                            "test task4 title",
                            "test task4 content",
                            "test task4 tag",
                            4)
        self.test_task4 = AdminLogic.obtain_task_by_id(4)

        AdminLogic.add_task(self.test_todo_list2.id_todo,
                            "test task5 title",
                            "test task5 content",
                            "test task5 tag",
                            5)
        self.test_task5 = AdminLogic.obtain_task_by_id(5)

    def test_create_todo_list(self):
        self.assertEqual(self.test_todo_list1,
                         AdminLogic.obtain_todo_by_id(
                             self.test_todo_list1.id_todo))

    def test_create_todo_list_TitleExistException(self):
        # the title = "test todo list" already exist.
        with self.assertRaises(TitleExistException):
            AdminLogic.create_todo_list("test todo 1 list")

    def test_add_task(self):
        self.assertEqual(self.test_task1,
                         AdminLogic.obtain_task_by_id(self.test_task1.id_task))

    def test_add_task_IdDontExistException(self):
        # test 1
        with self.assertRaises(IdDontExistException):
            # id_todo_list = 100 do not exist
            AdminLogic.add_task(self.unassigned_positive_id, "test title",
                                "test content", "test tag", 5)
        # test 2
        with self.assertRaises(IdDontExistException):
            # id_todo_list = -1 do not exist
            AdminLogic.add_task(self.unassigned_negative_id, "test title",
                                "test content", "test tag", 5)

    def test_obtain_task_by_id(self):
        # test 1
        self.assertEqual(self.test_task1,
                         AdminLogic.obtain_task_by_id
                         (self.test_task1.id_task))
        # test 2
        # id_task=100 do not exist
        with self.assertRaises(IdDontExistException):
            AdminLogic.obtain_task_by_id(self.unassigned_positive_id)

        # test 3
        # id_task=-1 do not exist
        with self.assertRaises(IdDontExistException):
            AdminLogic.obtain_task_by_id(self.unassigned_negative_id)

    def test_obtain_todo_by_id(self):
        # test 1
        self.assertEqual(self.test_todo_list1,
                         AdminLogic.obtain_todo_by_id
                         (self.test_todo_list1.id_todo))

        # test 2
        # id_todo_list=100 do not exist
        with self.assertRaises(IdDontExistException):
            AdminLogic.obtain_todo_by_id(self.unassigned_positive_id)

        # test 3
        # id_todo_list=-1 do not exist
        with self.assertRaises(IdDontExistException):
            AdminLogic.obtain_todo_by_id(self.unassigned_negative_id)

    def test_modify_task(self):
        # Defining attribute to modify the task
        id_task_modify = self.test_task1.id_task
        # Change to todo list 2
        id_todo_modify = self.test_todo_list2.id_todo
        title_modify = "title modify"
        content_modify = "content modify"
        tag_modify = "tag modify"
        status_modify = 1

        AdminLogic.modify_task(id_task_modify, id_todo_modify,
                               title_modify, content_modify,
                               tag_modify, status_modify)

        self.test_task1 = AdminLogic.obtain_task_by_id(id_task_modify)

        self.assertEqual(self.test_task1.id_task, id_task_modify)
        self.assertEqual(self.test_task1.id_todolist, id_todo_modify)
        self.assertEqual(self.test_task1.title, title_modify)
        self.assertEqual(self.test_task1.content, content_modify)
        self.assertEqual(self.test_task1.tag, tag_modify)
        self.assertEqual(self.test_task1.status, Status(status_modify).name)

    def test_modify_task_IdDontExistException(self):
        # Defining attribute to modify the task
        id_task_modify = self.test_task1.id_task
        # Change to todo list 2
        id_todo_modify = self.test_todo_list2.id_todo
        title_modify = "title modify"
        content_modify = "content modify"
        tag_modify = "tag modify"
        status_modify = 1

        # id_task = 100 do not exist
        with self.assertRaises(IdDontExistException):
            AdminLogic.modify_task(self.unassigned_positive_id, id_todo_modify,
                                   title_modify, content_modify,
                                   tag_modify, status_modify)

        # id_task = -1 do not exist
        with self.assertRaises(IdDontExistException):
            AdminLogic.modify_task(self.unassigned_negative_id, id_todo_modify,
                                   title_modify, content_modify,
                                   tag_modify, status_modify)

        # id_todo = 100 do not exist
        with self.assertRaises(IdDontExistException):
            AdminLogic.modify_task(id_task_modify, self.unassigned_positive_id,
                                   title_modify, content_modify,
                                   tag_modify, status_modify)

        # id_todo = -1 do not exist
        with self.assertRaises(IdDontExistException):
            AdminLogic.modify_task(id_task_modify, self.unassigned_negative_id,
                                   title_modify, content_modify,
                                   tag_modify, status_modify)

    def test_delete_task(self):
        id_task_delete = self.test_task1.id_task
        AdminLogic.delete_task(id_task_delete)
        with self.assertRaises(IdDontExistException):
            AdminLogic.obtain_task_by_id(id_task_delete)

    def test_delete_task_IdDontExistException(self):
        id_task_delete = self.unassigned_positive_id
        with self.assertRaises(IdDontExistException):
            AdminLogic.delete_task(id_task_delete)

        id_task_delete = self.unassigned_negative_id
        with self.assertRaises(IdDontExistException):
            AdminLogic.delete_task(id_task_delete)

    def test_search_tasks_by_title(self):
        self.assertEqual([self.test_task1, self.test_task2, self.test_task3,
                          self.test_task4, self.test_task5],
                         AdminLogic.search_tasks_by_title("test"))

    def test_search_tasks_by_content(self):
        self.assertEqual([self.test_task1, self.test_task2, self.test_task3,
                          self.test_task4, self.test_task5],
                         AdminLogic.search_tasks_by_content("test"))

    def test_obtain_tasks_by_id_todo(self):
        self.assertEqual([self.test_task1, self.test_task2],
                         AdminLogic.obtain_tasks_by_id_todo
                         (self.test_todo_list1.id_todo))

    def test_sort_task(self):
        # Sort tasks by id_task ASC
        self.assertEqual([self.test_task1, self.test_task2, self.test_task3,
                          self.test_task4, self.test_task5],
                         AdminLogic.sort_tasks(1, 1))

        # Sort tasks by id_task DESC
        self.assertEqual([self.test_task5, self.test_task4, self.test_task3,
                          self.test_task2, self.test_task1],
                         AdminLogic.sort_tasks(1, 2))

        # Sort tasks by id_todolist ASC
        self.assertEqual([self.test_task1, self.test_task2, self.test_task3,
                          self.test_task4, self.test_task5],
                         AdminLogic.sort_tasks(2, 1))

        # Sort tasks by id_todolist DESC
        self.assertEqual([self.test_task3, self.test_task4, self.test_task5,
                          self.test_task1, self.test_task2],
                         AdminLogic.sort_tasks(2, 2))

        # Sort tasks by title ASC
        self.assertEqual([self.test_task1, self.test_task2, self.test_task3,
                          self.test_task4, self.test_task5],
                         AdminLogic.sort_tasks(3, 1))

        # Sort tasks by title DESC
        self.assertEqual([self.test_task5, self.test_task4, self.test_task3,
                          self.test_task2, self.test_task1],
                         AdminLogic.sort_tasks(3, 2))

        # Sort tasks by content ASC
        self.assertEqual([self.test_task1, self.test_task2, self.test_task3,
                          self.test_task4, self.test_task5],
                         AdminLogic.sort_tasks(4, 1))

        # Sort tasks by content DESC
        self.assertEqual([self.test_task5, self.test_task4, self.test_task3,
                          self.test_task2, self.test_task1],
                         AdminLogic.sort_tasks(4, 2))

        # Sort tasks by tag_name ASC
        self.assertEqual([self.test_task1, self.test_task2, self.test_task3,
                          self.test_task4, self.test_task5],
                         AdminLogic.sort_tasks(5, 1))

        # Sort tasks by tag_name DESC
        self.assertEqual([self.test_task5, self.test_task4, self.test_task3,
                          self.test_task2, self.test_task1],
                         AdminLogic.sort_tasks(5, 2))

        # Sort tasks by id_status ASC
        self.assertEqual([self.test_task1, self.test_task2, self.test_task3,
                          self.test_task4, self.test_task5],
                         AdminLogic.sort_tasks(6, 1))

        # Sort tasks by id_status DESC
        self.assertEqual([self.test_task5, self.test_task4, self.test_task3,
                          self.test_task2, self.test_task1],
                         AdminLogic.sort_tasks(6, 2))

    def test_group_tasks_by_tag(self):
        self.assertEqual(self.test_task1,
                         AdminLogic.group_tasks_by_tag(self.test_task1.tag)[0])

        self.assertEqual(self.test_task2,
                         AdminLogic.group_tasks_by_tag(self.test_task2.tag)[0])

        self.assertEqual(self.test_task3,
                         AdminLogic.group_tasks_by_tag(self.test_task3.tag)[0])

        self.assertEqual(self.test_task4,
                         AdminLogic.group_tasks_by_tag(self.test_task4.tag)[0])

        self.assertEqual(self.test_task5,
                         AdminLogic.group_tasks_by_tag(self.test_task5.tag)[0])

    def tearDown(self):
        # Roll back the transaction
        Database.make_query('DELETE FROM task;')
        Database.make_query('DELETE FROM todo;')
        Database.make_query('DELETE FROM tag;')
        Database.make_query('ALTER SEQUENCE task_id_task_seq RESTART;')
        Database.make_query('ALTER SEQUENCE todo_id_todo_seq RESTART;')
        Database.make_query('ALTER SEQUENCE tag_id_tag_seq RESTART;')


if __name__ == '__main__':
    unittest.main()
