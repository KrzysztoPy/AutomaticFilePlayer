from tkinter import ttk


class NewButton:
    # upper_root, name , command, width_size, height_size,
    def __init__(self, upper_root_label, button_name, job_to_do, width_button, height_button):
        self.upper_root_label = upper_root_label
        self.button_name = button_name
        self.job_to_do = job_to_do
        self.width_button = width_button
        self.height_button = height_button
        self.new_button = ttk.Button(self.upper_root_label)

    def set_button_upper_root_label(self):
        # self.new_button.master = self.upper_root_label
        # self.new_button.config(text=self.button_name)
        pass

    def set_button_name(self):
        self.new_button.config(text=self.button_name)
        self.new_button.config(text='bla')

