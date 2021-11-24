from Program.displaying_and_text_manipulation import view_text, combining_multiple_texts_into_one, \
    removing_white_spaces_at_the_end_text, removing_white_spaces_at_the_end_text


def test_view_text():
    view_text(patch_to_the_folder_with_file_to_play_text)
    print(patch_to_the_folder_with_file_to_play_text)


def test_combining_multiple_texts_into_one():
    samples_1, samples_2, samples_3 = 'Yes, yes, thought Amerigo Bonasera.', 'Animals. Animals.', 'The judge went on.'
    expected_result = 'Yes, yes, thought Amerigo Bonasera. Animals. Animals. The judge went on.'

    result = combining_multiple_texts_into_one(samples_1, samples_2, samples_3)
    assert result == expected_result


def test_removing_white_spaces_at_the_end_text():
    samples = ['Yes, yes, thought Amerigo Bonasera. ', 'Animals. Animals.', 'The judge went on.       ', '', ' ', 'a ']
    expected_result = ['Yes, yes, thought Amerigo Bonasera.', 'Animals. Animals.', 'The judge went on.', '', '', 'a']

    for num_test in range(len(samples)):
        result = removing_white_spaces_at_the_end_text(samples[num_test])
        assert result == expected_result[num_test]
