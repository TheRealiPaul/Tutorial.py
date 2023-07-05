def function(lst):
    counter = 0
    for text in lst:
        if len(text) >= 2:  # Check if the length of the text is at least 2
            if (
                text[0] == text[len(text) - 1]
            ):  # Check if the first and last characters are the same
                counter += 1  # Increment the counter by 1
    return counter


print(function(["abc", "xyz", "aba", "1221"]))
