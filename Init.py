from program.logic.os_path_operation import get_project_path, whether_setting_file_exist

# Sprawdzenie istnienia pliku Automatic File Player setting
path = get_project_path()
whether_exist = whether_setting_file_exist(path)
decision_if_file_setting_exist_or_not()

file_path = take_patch_from_user()
check_whether_path_is_correct(file_path)
