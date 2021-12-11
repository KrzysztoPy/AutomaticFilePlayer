from program.logic.displaying_and_text_manipulation import combining_multiple_texts_into_one, view_text, \
    combining_multiple_texts_into_one
from program.static_text.os_path_operation_text import *
import os

setting_file_name = 'Automatic File Player.txt'


def get_project_path():
    try:
        return os.getcwd()
    except OSError:
        view_text(combining_multiple_texts_into_one(os_critical_error_close_program_text(),
                                                    os_problem_get_project_path_text()))
        critical_error_stop_program()


def whether_setting_file_exist(setting_file_location_path):
    global setting_file_name
    try:
        return os.path.isfile(setting_file_location_path + '\\' + setting_file_name)
    except OSError:
        view_text(combining_multiple_texts_into_one(os_critical_error_close_program_text(),
                                                    os_problem_whether_setting_file_exist_text()))
        critical_error_stop_program()


def critical_error_stop_program():
    exit(0)

# def take_patch_from_user():
#     information_for_user = combining_multiple_texts_into_one(patch_to_the_folder_with_file_to_play_text(),
#                                                              patch_to_folder_tip_text())
#
#     received_patch = input(information_for_user)
#     return received_patch
#
#
# def check_whether_path_is_correct(file_path):
#     os.system('cd ' + file_path)
