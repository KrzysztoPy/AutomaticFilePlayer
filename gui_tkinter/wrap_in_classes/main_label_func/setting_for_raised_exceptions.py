def exception_not_allowed_data_type_for_title(invalid_type, acceptable_datatype_for_title_main_label):
    return f": Invalid type use {invalid_type}. You can use only {acceptable_datatype_for_title_main_label().__name__}"


def exception_title_cannot_be_empty():
    return 'Title cannot be empty.'


def title_above_max_title_size(max_title_size):
    return f'Title can\'t be greater than {max_title_size()}.'
