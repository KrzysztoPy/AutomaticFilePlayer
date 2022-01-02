from gui_tkinter.main_label_func.main_label import NewMainLabel
from gui_tkinter.wrap_in_classes.main_label_func.condition_variable_setting import validation_of_name_setting_conditions_for_main_label
from gui_tkinter.main_label_func.main_label_basic_setting import acceptable_datatype_for_title_main_label, \
    exception_title_cannot_be_empty, title_above_max_title_size

import unittest
import random
import pyautogui
import inspect


def randomly_generated_of_the_declared_length(length):
    if isinstance(length, int):
        if length > 0:
            return [chr(random.randint(32, 126)) for i in range(length)]
        else:
            raise ValueError('Length is equal 0 or less.')
    else:
        raise ValueError(f'Parameter length is not int.')


class TestMethodsNeededForTesting(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_randomly_generated_of_the_declared_length_equal(self, samples, expected_result):
        method_parameter_name = list(
            inspect.signature(self.test_randomly_generated_of_the_declared_length_equal).parameters)

        if len(samples) == len(expected_result):
            for index in range(0, len(samples)):
                with self.subTest(index=index):
                    result = randomly_generated_of_the_declared_length(samples[index])
                    self.assertEqual(len(result), expected_result[index][0])
                    self.assertEqual(type(result).__name__, expected_result[index][1])
        else:
            raise IndexError(
                f'Parameter {method_parameter_name[0]} and {method_parameter_name[1]} are of different length.')

    def test_randomly_generated_of_the_declared_length_assert_raises_regex(self, samples, raises_expected,
                                                                           result_expected):

        method_parameter_name = list(
            inspect.signature(self.test_randomly_generated_of_the_declared_length_equal).parameters)

        if len(samples) == len(raises_expected) == len(result_expected):
            for index in range(0, len(samples)):
                with self.subTest(index=index):
                    with self.assertRaisesRegex(raises_expected[index], 'Length is equal 0 or less.'):
                        randomly_generated_of_the_declared_length(result_expected[index])
        else:
            raise IndexError(
                f'Parameter {method_parameter_name[0]} and {method_parameter_name[1]} are of different length.')

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

    def tearDown(self) -> None:
        pass

    if __name__ == '__main__':
        unittest.main()


class TestMainLabel(unittest.TestCase):

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

    def test_validation_of_name_setting_conditions_for_main_label_1(self, sample, result, expected_result):
        pass
        # for index in sample:
        #     with self.assertRaisesRegex()

    def test_return_screen_resolution(self):
        width, height = pyautogui.size()
        result = self.__tested_main_label_object.return_screen_resolution()
        self.assertEqual(result, (width, height))

    def test_set_title_main_label(self):
        samples = (randomly_generated_of_the_declared_length(10), randomly_generated_of_the_declared_length(40),
                   randomly_generated_of_the_declared_length(59))

        for sample in samples:
            new_main_label_obj = NewMainLabel(sample, 2, 2)
            new_main_label_obj.set_title_main_label()
            self.assertEqual(new_main_label_obj.root.title(), sample)

    def test_set_size_main_label(self):
        width, height = pyautogui.size()
        samples = ((1, 1), (2, 5))

        for sample in samples:
            new_main_label_obj = NewMainLabel('Correctness name', sample[0], sample[1])
            self.assertEqual((width // sample[0], height // sample[1]), new_main_label_obj.set_size_main_label())

        del new_main_label_obj

    # Dodanie wartości stałej i warunków krańcowych
    def test_return_the_center_position_of_the_main_window(self):
        width, height = pyautogui.size()
        samples = ((1, 1), (2, 5))

        expected_result = ((width // 2 - (width // samples[0][0]) // 2, height // 2 - (height // samples[0][1]) // 2),
                           (width // 2 - (width // samples[1][0]) // 2, height // 2 - (height // samples[1][1]) // 2))

        for index in range(0, len(samples)):
            new_main_label_obj = NewMainLabel('Correctness name', samples[index][0], samples[index][1])
            self.assertEqual(new_main_label_obj.return_the_center_position_of_the_main_window(),
                             expected_result[index])

    if __name__ == '__main__':
        unittest.main()
