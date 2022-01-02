def exception_not_allowed_data_type_for_title(invalid_type, acceptable_datatype_for_title_main_label):
    return f": Invalid type use {type(invalid_type).__name__}. " \
           f"You can use only {acceptable_datatype_for_title_main_label.__name__}"


def exception_title_cannot_be_empty():
    return 'Title cannot be empty.'


def title_above_max_title_size(max_title_size):
    return f'Title can\'t be greater than {max_title_size}.'


def can_not_create_a_main_label_window(width_screen, height_screen, minimal_screen_width, minimal_screen_height):
    return f'Your screen resolution {width_screen}x{height_screen} ' \
           f'does not meet the minimum screen resolution requirements. ' \
           f'Minimal requirements is {minimal_screen_width}x{minimal_screen_height} '
