import faxreader.core.handle_fax_data as handle_data
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.valid_acc_number_one = "123"
        self.valid_acc_number_two = ['1', '2', '3']
        self.invalid_acc_number = ['1', 'n', '3']

    def test_split_input_to_list_list(self):
        self.assertEqual(handle_data.split_input_to_list(self.valid_acc_number_one), ['1', '2', '3'])

    def test_split_input_to_list_string(self):
        self.assertNotEqual(handle_data.split_input_to_list(self.valid_acc_number_one), '123')

    def test_check_input_and_type_conversion_false(self):
        self.assertNotEqual(handle_data.split_input_to_list(self.valid_acc_number_one), '123')

    def test_check_input_and_type_conversion_true(self):
        self.assertEqual(handle_data.check_input_and_type_conversion(self.valid_acc_number_two), [1, 2, 3])

    def test_check_input_and_type_conversion_raise_error(self):
        with self.assertRaises(TypeError):
            handle_data.check_input_and_type_conversion(self.invalid_acc_number)


if __name__ == "__main__":
    unittest.main()
