import unittest
import json
import os

from todo import save_data, load_data, add_task, delete_all_data

class TestToDoListFunctions(unittest.TestCase):

    def setUp(self):
        self.filename = "test_data_file.json"
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_load_data(self):
        self.assertEqual(load_data(self.filename), {})

        with open(self.filename, "w") as write_file:
            json.dump({1: "Task1", 2: "Task2"}, write_file)
        self.assertEqual(load_data(self.filename), {'1': "Task1", '2': "Task2"})

    def test_save_data(self):
        data = {'1': "Task1", '2': "Task2"}
        save_data(self.filename, data)
        self.assertEqual(load_data(self.filename), data)

    def test_add_task(self):
        data = {1: "Task1", 2: "Task2"}
        new_data = add_task(data, "Task3")
        self.assertEqual(new_data, {1: "Task1", 2: "Task2", 3: "Task3"})

    def test_delete_all_data(self):
        data = {1: "Task1", 2: "Task2"}
        self.assertEqual(delete_all_data(data), {})

if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)