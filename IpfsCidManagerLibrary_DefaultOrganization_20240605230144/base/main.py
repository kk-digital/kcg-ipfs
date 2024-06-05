'''
Unit tests for CidManager class in CID Manager Library
'''
import unittest
from unittest.mock import MagicMock, patch
from cid_manager import CidManager
class TestCidManager(unittest.TestCase):
    def setUp(self):
        self.cid_manager = CidManager()
    def test_add_cid_data(self):
        self.cid_manager.add_cid_data("Cid1", "Hash1")
        self.cid_manager.add_cid_data("Cid2", "Hash2")
        self.cid_manager.add_cid_data("Cid3", "Hash3")
        self.assertEqual(len(self.cid_manager.cid_data_list), 3)
    def test_serialize_cid_data(self):
        self.cid_manager.add_cid_data("Cid1", "Hash1")
        self.cid_manager.add_cid_data("Cid2", "Hash2")
        self.cid_manager.add_cid_data("Cid3", "Hash3")
        # Mock the os.path.getsize function
        os_path_getsize_mock = MagicMock(return_value=100)
        with patch('os.path.getsize', os_path_getsize_mock):
            self.cid_manager.serialize_cid_data()
        self.assertEqual(os_path_getsize_mock.call_count, 3)
    def test_deserialize_cid_data(self):
        # Create mock json files
        json_data1 = '{"cid": "Cid1", "hash": "Hash1"}'
        json_data2 = '{"cid": "Cid2", "hash": "Hash2"}'
        json_data3 = '{"cid": "Cid3", "hash": "Hash3"}'
        # Mock the os.walk function
        os_walk_mock = MagicMock(return_value=[(".", [], ["file1.json", "file2.json", "file3.json"])])
        with patch('os.walk', os_walk_mock):
            # Mock the open function
            open_mock = MagicMock(side_effect=[MagicMock(read=MagicMock(return_value=json_data1)),
                                               MagicMock(read=MagicMock(return_value=json_data2)),
                                               MagicMock(read=MagicMock(return_value=json_data3))])
            with patch('builtins.open', open_mock):
                cid_data_list = self.cid_manager.deserialize_cid_data()
        self.assertEqual(len(cid_data_list), 3)
        self.assertEqual(cid_data_list[0].cid, "Cid1")
        self.assertEqual(cid_data_list[0].hash, "Hash1")
        self.assertEqual(cid_data_list[1].cid, "Cid2")
        self.assertEqual(cid_data_list[1].hash, "Hash2")
        self.assertEqual(cid_data_list[2].cid, "Cid3")
        self.assertEqual(cid_data_list[2].hash, "Hash3")
if __name__ == "__main__":
    unittest.main()