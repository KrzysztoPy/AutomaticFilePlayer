import unittest
import pytest
from decorators.decorator import validation_of_name_setting_conditions_for_main_label
from gui_tkinter.main_label_basic_setting import acceptable_datatype_for_title_main_label
from gui_tkinter.mixed.setting_for_raised_exceptions import *


class TestMainLabel(unittest.TestCase):
    def setUp(self) -> None:
        self.test_validation_of_name_setting_conditions_for_main_label_first_condition()

        # self.test_validation_of_name_setting_conditions_for_main_label_first_second(string_is_not_string, result)
        # self.test_validation_of_name_setting_conditions_for_main_label_first_third(string_is_not_string, result)

    def test_validation_of_name_setting_conditions_for_main_label_first_condition(self):
        samples = (1, 22.0, [], (), {}, {1: 'a'}, None)
        for sample in samples:
            with self.assertRaisesRegex(TypeError, exception_not_allowed_data_type_for_title(sample,
                                                                                             acceptable_datatype_for_title_main_label())):
                validation_of_name_setting_conditions_for_main_label(lambda: sample)

                # @pytest.mark.parametrize('sample_title', (1, 22.0, [], (), {}, {1: 'a'}, None, ''))
                # def test_validation_of_name_setting_conditions_for_main_label_first_condition_with_parametrize(self,
                #                                                                                                sample_title):
                #     with self.assertRaisesRegex(TypeError,
                #                                 exception_not_allowed_data_type_for_title(sample_title,
                #                                                                           acceptable_datatype_for_title_main_label())):
                #         validation_of_name_setting_conditions_for_main_label(sample_title)

    def tearDown(self) -> None:
        pass

    if __name__ == '__main__':
        unittest.main()
