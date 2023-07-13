liste = [1234, 122, 1984, 19372, 100]

# Check if first digit/character of each element is the same
first_character = str(liste[0])[0]  # Get the first character of the first element

for item in liste:
    if str(item)[0] != first_character:
        print("First character is not the same for all elements.")
        break
else:
    print("First character is the same for all elements.")
