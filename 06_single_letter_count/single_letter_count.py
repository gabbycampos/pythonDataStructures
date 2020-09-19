def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """
#     count = 0
#     for letter in word:
#         if letter[i] == letter:
#             count = count + 1

# print(single_letter_count('hello', 'h'))

    return word.lower().count(letter.lower())


print(single_letter_count('Hello World', 'h'))


# current_users = ['jason', 'jack', 'paul', 'cindy']
# new_users = ['Jimmy', 'John', 'Jason']

# current_users_lower = []
# for user in current_users:
#     current_users_lower.append(user.lower())

# for user in new_users:
#     if user.lower() in current_users_lower:
#         print('Sorry ' + user + ' username taken')
#     else:
#         print('Welcome ' + user)
