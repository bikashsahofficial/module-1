def custom_encoder(text):
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    for char in text:
        lower_char = char.lower()
        if lower_char in reference_string:
            result.append(reference_string.index(lower_char))
        else:
            result.append(-1)
    return result