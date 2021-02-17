from faxreader.core.handle_fax_data import split_input_to_list
import unittest


class MyTestCase(unittest.TestCase):

    def test_split_input_to_list_list(self):
        input_acc_number = ['1','2','3']
        self.assertEqual(split_input_to_list(input_acc_number),['1','2','3'])

    def test_split_input_to_list_string(self):
        input_acc_number= ['1', '2', '3']
        self.assertNotEqual(split_input_to_list(input_acc_number),'123')


