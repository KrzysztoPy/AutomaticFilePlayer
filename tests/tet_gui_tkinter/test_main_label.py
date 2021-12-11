import random

from gui_tkinter.main_label import NewMainLabel
from gui_tkinter.condition_variable_setting import validation_of_name_setting_conditions_for_main_label
from gui_tkinter.main_label_basic_setting import acceptable_datatype_for_title_main_label, \
    exception_title_cannot_be_empty, title_above_max_title_size

import unittest
import random
import pyautogui


def randomly_generated_of_the_declared_length(length):
    if length > 0:
        tmp_string = ''
        for index in range(length):
            tmp_string += chr(random.randint(32, 126))
        return tmp_string
    else:
        raise ValueError('Length is equal 0 or less.')


class TestMethodsNeededForTesting(unittest.TestCase):

    def test_randomly_generated_of_the_declared_length(self):
        samples_correct = 34, 652, 1
        ex_re_samples_correct = ((34, 'str'), (652, 'str'), (1, 'str'))
        sample_raise_exception = 0, -12

        # samples_correct with expexted result
        for index in range(0, len(samples_correct)):
            with self.subTest(index=index):
                result = randomly_generated_of_the_declared_length(samples_correct[index])
                self.assertEqual(len(result), ex_re_samples_correct[index][0])
                self.assertEqual(type(result).__name__, ex_re_samples_correct[index][1])

        # sample raise expected: expected raise
        for index in range(0, len(sample_raise_exception)):
            with self.subTest(index=index):
                with self.assertRaisesRegex(ValueError, 'Length is equal 0 or less.'):
                    randomly_generated_of_the_declared_length(sample_raise_exception[index])


class TestMainLabel(unittest.TestCase):
    def setUp(self) -> None:
        initiation_test_data = ('Example title', 2, 5)
        self.__tested_main_label_object = NewMainLabel(initiation_test_data[0],
                                                       initiation_test_data[1],
                                                       initiation_test_data[2])

    def test_validation_of_name_setting_conditions_for_main_label(self):
        string_is_not_string = (1, 21.37)
        string_is_empty = ''
        string_above_60_sign = randomly_generated_of_the_declared_length(61)
        string_equal_60_sign = randomly_generated_of_the_declared_length(60)
        string_is_correct = 'Video player'

        for sample in string_is_not_string:
            with self.assertRaisesRegex(TypeError,
                                        f': Invalid type use {type(sample).__name__}. You can use only {acceptable_datatype_for_title_main_label().__name__}'):
                validation_of_name_setting_conditions_for_main_label(sample)

        with self.assertRaisesRegex(AttributeError,
                                    exception_title_cannot_be_empty()):
            validation_of_name_setting_conditions_for_main_label(string_is_empty)

        with self.assertRaisesRegex(TypeError,
                                    title_above_max_title_size()):
            validation_of_name_setting_conditions_for_main_label(string_above_60_sign)

        with self.assertRaisesRegex(TypeError,
                                    title_above_max_title_size()):
            validation_of_name_setting_conditions_for_main_label(string_equal_60_sign)

        self.assertEqual(string_is_correct, validation_of_name_setting_conditions_for_main_label(string_is_correct))

    '''
    Verification of correctness of downloading the computer screen resolution by tkinter, checked with pyautogui.size() 
    method from pyautogui.  
    '''

    def test_return_screen_resolution(self):
        width, height = pyautogui.size()
        result = self.__tested_main_label_object.return_screen_resolution()
        self.assertEqual(result, (width, height))

    def test_set_size_main_label(self):
        width, height = pyautogui.size()
        samples = ((1, 1), (2, 5))

        for sample in samples:
            new_main_label_obj = NewMainLabel('Correctness name', sample[0], sample[1])
            self.assertEqual((width // sample[0], height // sample[1]), new_main_label_obj.set_size_main_label())

    def tearDown(self) -> None:
        del self.__tested_main_label_object

    if __name__ == '__main__':
        unittest.main()
