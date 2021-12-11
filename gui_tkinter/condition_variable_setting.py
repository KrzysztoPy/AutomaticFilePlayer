from gui_tkinter.main_label.main_label_basic_setting import acceptable_datatype_for_title_main_label, max_title_size, \
    title_above_max_title_size, exception_title_cannot_be_empty, exception_not_allowed_data_type_for_title

'''
  All data is taken from main_label_basic_setting

  Checks for the given name:
  1) Is string type.
  2) Whether the program length is greater than the allowable length.

  :param: title_name - It is a program name from basic setting
  :return: string title_name
  '''


def validation_of_name_setting_conditions_for_main_label(title_name):
    if isinstance(title_name, acceptable_datatype_for_title_main_label()):
        if title_name != '':
            if len(title_name) < max_title_size():
                return title_name
            else:
                raise TypeError(title_above_max_title_size())
        else:
            raise AttributeError(exception_title_cannot_be_empty())
    else:
        raise TypeError(
            exception_not_allowed_data_type_for_title(type(title_name).__name__))
