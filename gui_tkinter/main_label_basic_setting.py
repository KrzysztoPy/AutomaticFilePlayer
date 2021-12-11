def acceptable_datatype_for_title_main_label():
    return type(str.__name__)


def max_title_size():
    return 60


def exception_not_allowed_data_type_for_title(invalid_type):
    return f": Invalid type use {invalid_type}. You can use only {acceptable_datatype_for_title_main_label().__name__}"


def exception_title_cannot_be_empty():
    return 'Title cannot be empty.'


def title_above_max_title_size():
    return f'Title can\'t be greater than {max_title_size()}.'
