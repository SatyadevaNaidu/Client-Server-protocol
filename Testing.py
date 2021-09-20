import os
import unittest
from server_services import ServerServices

class TestSum(unittest.TestCase):
    """
    this module is for unit testing and does testing for folder_creation and read_file
    """
    def test_folder_creation(self):
        """
        tests for folder_creation
        """
        client = ServerServices(os.getcwd(), os.getcwd(), 'satya')
        input_data = [
            'fo','fo'
        ]
        expected_value = [
            'failed to create folder',
            'failed to create folder'
        ]
        result = []
        for inputval in input_data:
            result.append(client.create_folder(inputval))
        self.assertListEqual(result, expected_value)


    def test_read_file(self):
        """
        test to read_file
        """
        way = os.path.join(os.getcwd(), 'satya')
        client = ServerServices(os.getcwd(), way, 'satya')
        input_data = [
            ['ok.txt'],
            ['asdf.txt'],
            ['set.txt']
        ]
        expected_value = [
            'file doesnot exist',
            'file doesnot exist',
            'file doesnot exist'
        ]
        result = []
        for inputval in input_data:
            result.append(client.file_read(inputval[0]))
        self.assertListEqual(result, expected_value)

if __name__ == '__main__':
    unittest.main()
