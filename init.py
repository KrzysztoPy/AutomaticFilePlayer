from gui_tkinter.main_label import NewMainLabel
from setting_init import title_for_main_label, multiple_reduction_width_main_label, multiple_reduction_high_main_label


def gui_init():
    main_label = NewMainLabel(title_for_main_label(),
                              multiple_reduction_width_main_label(),
                              multiple_reduction_high_main_label())
    main_label.set_title_main_label()
    main_label.set_size_and_position_main_label()
    main_label.mian_loop_for_main_label()


gui_init()
