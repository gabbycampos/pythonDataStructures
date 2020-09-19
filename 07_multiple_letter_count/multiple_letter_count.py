def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    counter = {}
    for letter in phrase:
        if letter in counter:
            counter[letter]+=1
        else:
            counter[letter]=1
    return counter
print(multiple_letter_count('yay'))