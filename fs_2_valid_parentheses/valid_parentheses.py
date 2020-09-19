def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    counter = 0
    for i in parens:
        if i == "(":
            counter += 1
        elif i == ")":
            counter -= 1
        if counter < 0:
            return False
    return counter == 0


print(valid_parentheses("((())"))

    # count = 0

    # for p in parens:
    #     if p == '(':
    #         count += 1
    #     elif p == ')':
    #         count -= 1

    #     # fast fail: too many right parens
    #     if count < 0:
    #         return False

    # return count == 0
