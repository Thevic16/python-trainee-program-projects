import unittest
from unittest.mock import patch

from packages.administration.admin_logic import AdminLogic
from packages.auxiliary.storage_functions import load_data_from_json_file


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # Initializing dictionaries
        AdminLogic.tasks = {}
        AdminLogic.todo_lists = {}
        AdminLogic.load_data_from_list([0, 0, [], []])

    @patch('packages.auxiliary.storage_functions.json')
    @patch("packages.auxiliary.storage_functions.open", create=True)
    def test_load_data_from_json_file(self, mock_file, mock_json):
        admin_logic_list = [1, 1, [
            {"id_task": 0,
             "id_todolist": 0,
             "title": "test title",
             "content": "test content",
             "tag": "HTML",
             "status": "completed"}],
                            [{"id_todo": 0,
                              "title": "test_load_data_from_json_file"}]]

        mock_json.load.return_value = admin_logic_list
        load_data_from_json_file()
        self.assertEqual(AdminLogic.get_admin_logic_as_list(),
                         admin_logic_list)


if __name__ == '__main__':
    unittest.main()
