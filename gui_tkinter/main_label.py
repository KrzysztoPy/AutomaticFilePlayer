import tkinter
from gui_tkinter.condition_variable_setting import validation_of_name_setting_conditions_for_main_label


class NewMainLabel:
    '''
    @:param: title - It is a object string type. Not longer than 60 letter.
    @:param: multiple_reduction_width_main_label - It is a multiple of the reduction of the window width size in
             relation to the later downloaded screen width resolution
    @:param: multiple_reduction_height_mian_label - It is a multiple of the reduction of the window height size in
             relation to the later downloaded screen height resolution
    '''

    def __init__(self, title, multiple_reduction_width_main_label, multiple_reduction_height_mian_label):
        self.__root = tkinter.Tk()
        self.title = validation_of_name_setting_conditions_for_main_label(title)
        self.multiple_reduction_width_main_label = multiple_reduction_width_main_label
        self.multiple_reduction_height_mian_label = multiple_reduction_height_mian_label
        self.screen_width, self.screen_height = self.return_screen_resolution()
        self.main_label_window_width, self.main_label_window_height = self.set_size_main_label()
        self.main_width_position, self.main_height_position = self.return_the_center_position_of_the_main_window()

    def return_screen_resolution(self):
        return self.__root.winfo_screenwidth(), self.__root.winfo_screenheight()

    def set_title_main_label(self):
        self.__root.title = self.title

    def set_size_main_label(self):
        return self.screen_width // self.multiple_reduction_width_main_label, \
               self.screen_height // self.multiple_reduction_height_mian_label

    def return_the_center_position_of_the_main_window(self):
        '''
        Returns the central position of the main window, taking into account the screen size and the declared size of the
        window.
        :return: main_width_position - Calculation
        '''
        main_width_position = self.screen_width // 2 - self.main_label_window_width // 2
        main_height_position = self.screen_height // 2 - self.main_label_window_height // 2

        return main_width_position, main_height_position

    def set_size_and_position_main_label(self):
        self.__root.geometry(
            f'{self.main_label_window_width}x{self.main_label_window_height}'
            f'+{self.main_width_position}+{self.main_height_position}')

    def mian_loop_for_main_label(self):
        self.__root.mainloop()
