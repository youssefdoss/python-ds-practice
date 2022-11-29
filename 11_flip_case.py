def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap_lower_case = to_swap.lower()

    swapped_phrase = ""

    for letter in phrase:
        if letter.islower() and letter == to_swap_lower_case:
            swapped_phrase += letter.upper()
        elif letter.isupper() and letter.lower() == to_swap_lower_case:
            swapped_phrase += letter.lower()
        else:
            swapped_phrase += letter
            
    return swapped_phrase


