from decorators.decorator import validation_of_name_setting_conditions_for_main_label


@validation_of_name_setting_conditions_for_main_label
def title_for_main_label():
    return 'Automatic File Player'


def multiple_reduction_width_main_label():
    return 2


def multiple_reduction_high_main_label():
    return 5


print(title_for_main_label)
