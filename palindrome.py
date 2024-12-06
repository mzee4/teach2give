# 2.Write a Python function that checks whether a word or phrase is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"

def reverse(phrase):
    rev_phrase = phrase[::-1]

    return rev_phrase


phrase = "table"

flipped_phrase = reverse(phrase)

if phrase == flipped_phrase:
    print(f"The {phrase} is a palindrome.")

else:
    print(f"The {phrase} is not a palindrome.")