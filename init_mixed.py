from tkinter import Tk, ttk
from init_setting import title_for_main_label


def init_main_label():
    mian_label_root = Tk()
    mian_label_root.title(title_for_main_label)

    mian_label_root.mainloop()


init_main_label()
