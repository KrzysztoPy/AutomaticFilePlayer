from gui_tkinter.main_label import NewMainLabel
from setting_init import title_for_main_label, multiple_reduction_width_main_label, multiple_reduction_high_main_label


def gui_init():
    mian_label = NewMainLabel(title_for_main_label(),
                              multiple_reduction_width_main_label(),
                              multiple_reduction_high_main_label())
