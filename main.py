# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from collections import defaultdict

def read_file_content(filename):
    f = open(filename, 'r')
    content = f.read()
    
    return content


def count_words():
    texti = read_file_content("story.txt")

    # remove leading and trailing spaces in texti
    texti = texti.strip().lower()

    # remove punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    text = ""
    for char in texti:
        if char not in punctuations:
            text = text + char

    text = " ".join(text.split()) #remove nextline
    text += " "

    keeper = ""
    words_counted = defaultdict(int)

    # loop through the string text
    for a in text:
    # wen the string is an empty string
        if (a == " "):
            # check if the keeper is in d dict "wordCounted"
            if keeper in words_counted:
                # if yes, increament d value by 1
                words_counted[keeper] += 1
            else:
                # else, add it to d dict with value 1
                words_counted[keeper] = 1

            keeper = ""
        else:
            # append each string to a variable "keeper"
            keeper += a


    return str(dict(words_counted))

# print(read_file_content('story.txt'))
print(count_words())

