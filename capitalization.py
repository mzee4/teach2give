# 5.Write a program that accepts a string as input, capitalizes the first letter of each word in the string, and then returns the result string.
# Examples:
# "hi"=> returns "Hi"
# "i love programming"=> returns "I Love Programming"
def capitalize_all_words(sentense):
    
    all_words = sentense.split()
    
    print(all_words)
    final_words = []
    
    for word in all_words:
       capitalize = word.capitalize()
       
       print(capitalize)
       
       final_words.append(capitalize)

    print(final_words)
    # Join the words back together with spaces
    result = ' '.join(final_words)
    
    return result
    

sentense = "nurse are on strike"

results = capitalize_all_words(sentense)

print(results)