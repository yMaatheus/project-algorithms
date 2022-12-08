def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    mid = len(word) // 2
    count = 0
    while count <= mid:
        start = word[count]
        end = word[(len(word) - 1) - count]
        if (start != end):
            return False
        count += 1
    return True
