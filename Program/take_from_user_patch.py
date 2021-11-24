from Program.displaying_and_text_manipulation import view_text,combining_multiple_texts_into_one
from Program.take_patch_from_user_text import *


def take_patch_from_user():
    received_patch = input(
        view_text(patch_to_the_folder_with_file_to_play_text()) + view_text(patch_to_folder_tip_text()))
