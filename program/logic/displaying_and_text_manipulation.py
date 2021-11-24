def view_text(text):
    print(text)


def combining_multiple_texts_into_one(*texts):
    combining_text = ''
    for count in range(len(texts)):
        combining_text += texts[count] + ' '

    combining_text = removing_white_spaces_at_the_end_text(combining_text)
    return combining_text


def removing_white_spaces_at_the_end_text(text):
    if text == '' or text == ' ':
        return ''

    for count in range(len(text) - 1, 0, -1):
        if text[count] == ' ':
            text = text[:-1]
        else:
            return text

    return text
