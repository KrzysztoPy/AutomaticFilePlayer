from program.logic.displaying_and_text_manipulation import view_text, combining_multiple_texts_into_one, \
    removing_white_spaces_at_the_end_text


def test_view_text():
    view_text(patch_to_the_folder_with_file_to_play_text)
    print(patch_to_the_folder_with_file_to_play_text)


# Samples from book Mario Puzo - The Godfather: page 2
def test_combining_multiple_texts_into_one():
    def sample_1():
        return 'The judge went on.'

    def sample_2():
        return 'Only forty years of professional mourning kept the overwhelming frustration and hatred ' \
               'from showing on Amerigo Bonasera’s face.'

    expected_result_1 = 'The judge went on. Only forty years of professional mourning kept the overwhelming ' \
                        'frustration and hatred from showing on Amerigo Bonasera’s face.'
    sample_3, sample_4, sample_5 = 'Yes, yes, thought Amerigo Bonasera.', 'Animals. Animals.', 'The judge went on.'
    expected_result_2 = 'Yes, yes, thought Amerigo Bonasera. Animals. Animals. The judge went on.'

    result = combining_multiple_texts_into_one(sample_1(), sample_2())
    assert result == expected_result_1

    result = combining_multiple_texts_into_one(sample_3, sample_4, sample_5)
    assert result == expected_result_2


# Samples from book Mario Puzo - The Godfather: page 2
def test_removing_white_spaces_at_the_end_text():
    samples = ['Yes, yes, thought Amerigo Bonasera. ', 'Animals. Animals.', 'The judge went on.       ', '', ' ', 'a ']
    expected_result = ['Yes, yes, thought Amerigo Bonasera.', 'Animals. Animals.', 'The judge went on.', '', '', 'a']

    for num_test in range(len(samples)):
        result = removing_white_spaces_at_the_end_text(samples[num_test])
        assert result == expected_result[num_test]
