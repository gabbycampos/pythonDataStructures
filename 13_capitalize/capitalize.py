def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    return phrase[0].title() + phrase[1::]
    # there's a built-in method for this!
    #return phrase.capitalize()

print(capitalize('only first word'))
