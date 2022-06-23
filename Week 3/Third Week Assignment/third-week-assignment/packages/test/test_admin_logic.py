import unittest
from packages.administration.admin_logic import AdminLogic
from packages.exceptions.exceptions import IdDontExistException
from packages.exceptions.exceptions import TitleExistException


class TestAdminLogic(unittest.TestCase):
    # Test Attributes
    test_todo_list1 = None
    test_todo_list2 = None
    test_task1 = None
    test_task2 = None
    unassigned_positive_id = 100
    unassigned_negative_id = -1

    def setUp(self):
        # Initializing Admin Logic
        TestAdminLogic.reset_admin_logic()

        # Create a test todo list
        self.test_todo_list1 = AdminLogic.create_todo_list("test todo 1 list")

        self.test_todo_list2 = AdminLogic.create_todo_list("test todo 2 list")

        # Create test tasks attach to todo list 1
        self.test_task1 = AdminLogic.add_task(self.test_todo_list1.id_todo,
                                              "test task1 title",
                                              "test task1 content",
                                              "test task1 tag",
                                              "completed")
        self.test_task2 = AdminLogic.add_task(self.test_todo_list1.id_todo,
                                              "test task2 title",
                                              "test task2 content",
                                              "test task2 tag",
                                              "completed")

    def test_create_todo_list(self):
        self.assertEqual(self.test_todo_list1,
                         AdminLogic.todo_lists.get
                         (self.test_todo_list1.id_todo))

    def test_create_todo_list_TitleExistException(self):
        # the title = "test todo list" already exist.
        with self.assertRaises(TitleExistException):
            AdminLogic.create_todo_list("test todo 1 list")

    def test_add_task(self):
        self.assertEqual(self.test_task1,
                         AdminLogic.tasks.get(self.test_task1.id_task))

    def test_add_task_IdDontExistException(self):
        # test 1
        with self.assertRaises(IdDontExistException):
            # id_todo_list = 100 do not exist
            AdminLogic.add_task(self.unassigned_positive_id, "test title",
                                "test content", "test tag", "completed")
        # test 2
        with self.assertRaises(IdDontExistException):
            # id_todo_list = -1 do not exist
            AdminLogic.add_task(self.unassigned_negative_id, "test title",
                                "test content", "test tag", "completed")

    def test_obtain_task_by_id(self):
        # test 1
        self.assertEqual(self.test_task1,
                         AdminLogic.obtain_task_by_id
                         (self.test_task1.id_task))

        # test 2
        # id_task=100 do not exist
        self.assertIsNone(AdminLogic.obtain_task_by_id
                          (self.unassigned_positive_id))

        # test 3
        # id_task=-1 do not exist
        self.assertIsNone(AdminLogic.obtain_task_by_id
                          (self.unassigned_negative_id))

    def test_obtain_todo_by_id(self):
        # test 1
        self.assertEqual(self.test_todo_list1,
                         AdminLogic.obtain_todo_by_id
                         (self.test_todo_list1.id_todo))

        # test 2
        # id_todo_list=100 do not exist
        self.assertIsNone(AdminLogic.obtain_todo_by_id
                          (self.unassigned_positive_id))

        # test 3
        # id_todo_list=-1 do not exist
        self.assertIsNone(AdminLogic.obtain_todo_by_id
                          (self.unassigned_negative_id))

    def test_modify_task(self):
        # Defining attribute to modify the task
        id_task_modify = self.test_task1.id_task
        # Change to todo list 2
        id_todo_modify = self.test_todo_list2.id_todo
        title_modify = "title modify"
        content_modify = "content modify"
        tag_modify = "tag modify"
        status_modify = "status modify"

        AdminLogic.modify_task(id_task_modify, id_todo_modify,
                               title_modify, content_modify,
                               tag_modify, status_modify)

        self.assertEqual(self.test_task1.id_task, id_task_modify)
        self.assertEqual(self.test_task1.id_todolist, id_todo_modify)
        self.assertEqual(self.test_task1.title, title_modify)
        self.assertEqual(self.test_task1.content, content_modify)
        self.assertEqual(self.test_task1.tag, tag_modify)
        self.assertEqual(self.test_task1.status, status_modify)

    def test_modify_task_IdDontExistException(self):
        # Defining attribute to modify the task
        id_task_modify = self.test_task1.id_task
        # Change to todo list 2
        id_todo_modify = self.test_todo_list2.id_todo
        title_modify = "title modify"
        content_modify = "content modify"
        tag_modify = "tag modify"
        status_modify = "status modify"

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
        self.assertIsNone(AdminLogic.obtain_task_by_id(id_task_delete))

    def test_search_tasks_by_title(self):
        self.assertEqual([self.test_task1, self.test_task2],
                         AdminLogic.search_tasks_by_title("test"))

    def test_search_tasks_by_content(self):
        self.assertEqual([self.test_task1, self.test_task2],
                         AdminLogic.search_tasks_by_content("test"))

    def test_obtain_tasks_by_id_todo(self):
        self.assertEqual([self.test_task1, self.test_task2],
                         AdminLogic.obtain_tasks_by_id_todo
                         (self.test_todo_list1.id_todo))

    def test_create_todo_list_load_data(self):
        todo_list = AdminLogic. \
            create_todo_list_load_data(0,
                                       "test_create_todo_list_load_data")
        self.assertEqual(todo_list,
                         AdminLogic.todo_lists[todo_list.id_todo])

    def test_add_task_load_data(self):
        todo_list = AdminLogic.create_todo_list("test_add_task_load_data")
        task = AdminLogic.add_task_load_data(0,
                                             todo_list.id_todo,
                                             "test title",
                                             "test content",
                                             "HTML", "completed")

        self.assertEqual(task, AdminLogic.tasks[task.id_task])

    def test_get_admin_logic_as_list(self):
        # Comparing admin logic representation with the method.
        self.assertEqual(
            [2, 2, [{"id_task": 0,
                     "id_todolist": 0,
                     "title": "test task1 title",
                     "content": "test task1 content",
                     "tag": "test task1 tag",
                     "status": "completed"},
                    {"id_task": 1,
                     "id_todolist": 0,
                     "title": "test task2 title",
                     "content": "test task2 content",
                     "tag": "test task2 tag",
                     "status": "completed"}
                    ],
             [{"id_todo": 0,
               "title": "test todo 1 list"}, {"id_todo": 1,
                                              "title": "test todo 2 list"}]],
            AdminLogic.get_admin_logic_as_list())

    def test_load_data_from_list(self):
        # Reset AdminLogic
        TestAdminLogic.reset_admin_logic()

        # Test admin load logic as list
        admin_logic_list = [1, 1, [
            {"id_task": 0,
             "id_todolist": 0,
             "title": "test title",
             "content": "test content",
             "tag": "HTML",
             "status": "completed"}], [{"id_todo": 0,
                                        "title": "test_load_data_from_list"}]]

        AdminLogic.load_data_from_list(admin_logic_list)

        self.assertEqual(admin_logic_list,
                         AdminLogic.get_admin_logic_as_list())

    def test_title_todo_exist(self):
        # The title should not exist.
        self.assertFalse(
            AdminLogic.title_todo_exist("This title do not exist"))

        # This title already exist.
        self.assertTrue(
            AdminLogic.title_todo_exist(self.test_todo_list1.title))

    # Auxiliary method
    @staticmethod
    def reset_admin_logic():
        AdminLogic.count_id_task = 0
        AdminLogic.count_id_todo = 0
        AdminLogic.tasks = {}
        AdminLogic.todo_lists = {}


if __name__ == '__main__':
    unittest.main()
