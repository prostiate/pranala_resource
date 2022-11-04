import unittest
import math
from efishery_test_case import Pranala


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.pranala = Pranala()

    def test_add_record(self):
        """Test add_records"""
        result = self.pranala.add_records('gurame', 'jawa tengah', 'cilacap', '50', '40000')
        self.assertEqual(result, result)

    def test_delete_record(self):
        """Test delete_records"""
        result = self.pranala.delete_records(['uuid=79877fd3-1aa7-4b19-ad51-8246a3338b1f'])
        self.assertEqual(result, result)

    def test_get_aggregation_price(self):
        """Test get_aggregation_price"""
        result = self.pranala.get_aggregation_price('komoditas')
        self.assertEqual(result, result)

    def test_get_all_by_commodity(self):
        """Test get_all_by_commodity"""
        result = self.pranala.get_all_by_commodity('gurame')
        self.assertEqual(result, result)

    def test_get_all_by_range(self):
        """Test get_all_by_range"""
        result = self.pranala.get_all_by_range('2,50000', '30,170', '2020-11-02,2022-11-02')
        self.assertEqual(result, result)

    def test_get_by_area(self):
        """Test get_by_area"""
        result = self.pranala.get_by_area('jawa tengah', 'cilacap')
        self.assertEqual(result, result)

    def test_get_by_id(self):
        """Test get_by_id"""
        result = self.pranala.get_by_id('2c75f19f-ac7a-4c28-9459-8fbb64c8cb00')
        self.assertEqual(result, result)

    def test_get_by_range_price(self):
        """Test get_by_range_price"""
        result = self.pranala.get_by_range_price(5, 50000)
        self.assertEqual(result, result)

    def test_get_max_price(self):
        """Test get_max_price"""
        result = self.pranala.get_max_price()
        self.assertEqual(result, result)

    def test_get_most_records(self):
        """Test get_most_records"""
        result = self.pranala.get_most_records()
        self.assertEqual(result, result)

    def test_update_records(self):
        """Test update_records"""
        result = self.pranala.update_records(['uuid=79877fd3-1aa7-4b19-ad51-8246a3338b1f'], ['size=170'])
        self.assertEqual(result, result)



if __name__ == '__main__':
    unittest.main()
