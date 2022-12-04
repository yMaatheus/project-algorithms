def is_anagram(first_string, second_string):
    is_anagram = True
    first_string_sorted = ''.join(sorted(first_string))
    second_string_sorted = ''.join(sorted(second_string))
    for char in first_string:
        if char.lower() not in map(str.lower, second_string):
            is_anagram = False
    print((first_string_sorted, second_string_sorted, is_anagram))
    return (first_string_sorted, second_string_sorted, is_anagram)
