def acceptable_datatype_for_title_main_label():
    return type(str.__name__)


def max_title_size():
    return 60


def max_window_size():
    pass


def main_window_size():
    min_width = 800
    min_height = 200
    return min_width, min_height
