
# 1. Write a Python program to calculate the length of a string.
string = input("enter string: ")
length = len(string)
print("do dai cua chuoi la:", length)
# 2. Write a Python program to count the number of characters (character frequency) in a string.
string = input("enter string")
char_freq = {}
for char in string:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
# Sample String : google.com'
string = "google.com"
char_freq = {}
for char in string:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
print("tần suất ký tự trong chuỗi là:")
for key, value in char_freq.items():
    print(f"'{key}': {value}")
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
string = "google.com"
char_freq = {}
for char in string:
    if char not in char_freq:
        char_freq[char] = 1
    else:
        char_freq[char] += 1
print(char_freq)
# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given
# string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
def first_last_2chars(s):
    if len(s) < 2:
        return ""
    return s[:2] + s[-2:]
print (first_last_2chars("w3resource"))
print (first_last_2chars("w3"))
print (first_last_2chars("w"))
# 4. Write a Python program to get a string from a given string where all occurrences of its first
# char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'
def change_first_char(s):
    first_char = s[0]
    return first_char + s[1:].replace(first_char, "$")
print(change_first_char("restart"))
# 5. Write a Python program to get a single string from two given strings, separated by a space and
# swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'
def swap_first2_char(a, b):
    # Đảm bảo 2 chuỗi đều có ít nhất 2 ký tự
    if len(a) < 2 or len(b) < 2:
        return "Strings must have at least 2 characters"

    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]

    return new_a + " " + new_b
# Test
print(swap_first2_char("abc", "xyz"))
# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If
# the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is
# less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'
def add_ing(s):
    if len(s)<3:
        return s
    if s.endswith("ing"):
        return s + ("ly")
    else:
        return s + "ing"
print(add_ing("abc"))
print(add_ing("string"))
print(add_ing("hi"))
# 7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given
# string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the
# resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
def not_poor(s):
    not_pos = s.find("not")
    poor_pos = s.find("poor")
    if not_pos != -1 and poor_pos != -1 and not_pos < poor_pos:
        return s[:not_pos] + "good" + s[poor_pos + 4:]
    return s

print(not_poor("The lyrics is not that poor!"))
print(not_poor("The lyrics is poor!"))
# 8. Write a Python function that takes a list of words and return the longest word and the length
# of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9
def longest_word(words):
    longest = max(words, key=len)
    return longest, len(longest)
words_list = ["PHP", "Exercices", "Backed"]
word, length = longest_word(words_list)
print("longest word:", word)
print("length of the longest word", length)
# 9. Write a Python program to remove the nth index character from a nonempty string.
def remove_char(s, n):
    return s[:n] + s[n+1:]

print(remove_char("python", 0))
print(remove_char("python", 3))
# 10. Write a Python program to change a given string to a newly string where the first and last
# chars have been exchanged.
def exchange_first_last(s):
    if len(s) <= 1:
        return s
    return s[-1] + s[1:-1] + s[0]

print(exchange_first_last("python"))
print(exchange_first_last("a"))
# 11. Write a Python program to remove characters that have odd index values in a given string.
def remove_odd_index(s):
    return s[::2]
print(remove_odd_index("python"))
print(remove_odd_index("abcdef"))
# 12. Write a Python program to count the occurrences of each word in a given sentence.
def word_count(sentence):
    words = sentence.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts
print(word_count("the quick brown fox jumps over the lazy dog the"))
# 13. Write a Python script that takes input from the user and displays that input back in upper
# and lower cases.
def upper_lower():
    s = input("enter string: ")
    print("Upper case:", s.upper())
    print("Lower case:", s.lower())
# 14. Write a Python program that accepts a comma-separated sequence of words as input and
# prints the distinct words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red
def distinct_sorted_words():
    items = input("Enter comma separated words: ")
    # Tách từ, bỏ khoảng trắng dư thừa
    words = [word.strip() for word in items.split(",")]
    # Loại bỏ trùng lặp bằng set, rồi sắp xếp
    result = sorted(set(words))
    print(",".join(result))

# Test
# Input: red, white, black, red, green, black
# Output: black,green,red,white
distinct_sorted_words()
# 15. Write a Python function to create an HTML string with tags around the word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
def add_tags(tag, word):
    return f"<{tag}>{word}</{tag}>"
# test
print(add_tags('i', 'python'))
print(add_tags('b', 'python tutorial'))
# <i>Python</i>
# <b>Python Tutorial</b>
# 16. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', ' Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
def insert_string_middle(container, word):
    mid = len(container)//2
    return container[:mid] + word + container[mid:]
# test
print(insert_string_middle("[[]]", "python"))
print(insert_string_middle("{{}}", "PHP"))
# 17. Write a Python function to get a string made of 4 copies of the last two characters of a
# specified string (length must be at least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('exercises') -> eseseses
def insert_end(s):
    return s[-2:] * 4
# test
print(insert_end("python"))
print(insert_end("exercices"))
# 18. Write a Python function to get a string made of the first three characters of a specified string.
# If the length of the string is less than 3, return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three(' python') -> pyt
def first_three(s):
    return s if len(s) < 3 else s[:3]
# test
print(first_three("ipy"))
print(first_three("python"))
print(first_three("hi"))
# 19. Write a Python program to get the last part of a string before a specified character.
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python
def last_part_before_char(s, char):
    return s.rsplit(char, 1)[0]

# Test
print(last_part_before_char("https://www.w3resource.com/python-exercises", "/"))
# https://www.w3resource.com/python
print(last_part_before_char("https://www.w3resource.com/python", "/"))
# https://www.w3resource.com

# 20. Write a Python function to reverse a string if its length is a multiple of 4.
def reverse_if_multiple_of_4(s):
    return s[::-1] if len(s) % 4 == 0 else s
print(reverse_if_multiple_of_4("abcd"))     # dcba
print(reverse_if_multiple_of_4("python"))   # python (length 6, not multiple of 4)

# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2
# uppercase characters in the first 4 characters.
def uppercase_if_two_in_first4(s):
    count = sum(1 for c in s[:4] if c.isupper())
    if count >= 2:
        return s.upper()
    return s

# test
print(uppercase_if_two_in_first4("PyThon"))   # PYTHON
print(uppercase_if_two_in_first4("Python"))  # Python

# 22.Write a Python program to sort a string lexicographically.
def sort_string(s):
    return "".join(sorted(s))

# test
print(sort_string("python"))  # hnopty
print(sort_string("zyxabc"))  # abcxyz
# 23. Write a Python program to remove a newline in Python.
def remove_newline(s):
    return s.replace("\n", "")

# test
text = "Hello\nWorld\nPython"
print(remove_newline(text))   # HelloWorldPython

# 24. Write a Python program to check whether a string starts with specified characters.
def starts_with(s, prefix):
    return s.startswith(prefix)

# test
print(starts_with("Python programming", "Py"))   # True
print(starts_with("Python programming", "Java")) # False
# 25. Write a Python program to create a Caesar encryption.
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's
# code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a
# type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed
# number of positions down the alphabet. For example, with a left shift of 3, D would be replaced
# by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his
# private correspondence.
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():           # chỉ mã hóa chữ cái
            base = ord('A') if char.isupper() else ord('a')
            result += chr(base + (ord(char) - base + shift) % 26)
        else:
            result += char
    return result

# test
print(caesar_encrypt("ABC", 3))          # DEF
print(caesar_encrypt("xyz", 3))          # abc
print(caesar_encrypt("Hello world", 5))  # Mjqqt btwqi

# 26. Write a Python program to display formatted text (width=50) as output.
import textwrap

text = "Python is an interpreted high-level general-purpose programming language."
print(textwrap.fill(text, width=50))

# 27. Write a Python program to remove existing indentation from all of the lines in a given text.
import textwrap

text = """    
        Python is powerful
        and easy to learn.
"""
print(textwrap.dedent(text))

# 28. Write a Python program to add prefix text to all of the lines in a string.
text = """Python
is powerful
and easy to learn"""
prefix = ">> "
print('\n'.join(prefix + line for line in text.splitlines()))

# 29. Write a Python program to set the indentation of the first line.
text = "Python is powerful and easy to learn."
print('    ' + text)  # Thêm 4 khoảng trắng đầu dòng

# 30. Write a Python program to print the following numbers up to 2 decimal places.
num = 12.34567
print("{:.2f}".format(num))

# 31. Write a Python program to print the following numbers up to 2 decimal places with a sign.
num1 = 12.34567
num2 = -12.34567
print("{:+.2f}".format(num1))
print("{:+.2f}".format(num2))

# 32. Write a Python program to print the following positive and negative numbers with no
# decimal places.
num1 = 12.789
num2 = -12.789
print("{:.0f}".format(num1))
print("{:.0f}".format(num2))

# 33. Write a Python program to print the following integers with zeros to the left of the specified
# width.
num = 42
print("{:05d}".format(num))  # width=5

# 34. Write a Python program to print the following integers with '*' to the right of the specified
# width.
num = 42
print("{:*<5d}".format(num))  # width=5, lấp đầy bằng *

# 35. Write a Python program to display a number with a comma separator.
num = 1234567890
print("{:,}".format(num))

# 36. Write a Python program to format a number with a percentage.
num = 0.756
print("{:.2%}".format(num))

# 37. Write a Python program to display a number in left, right, and center aligned with a width of
# 10.
text = "Python"
print("{:<10}".format(text))   # Left
print("{:>10}".format(text))   # Right
print("{:^10}".format(text))   # Center

# 38. Write a Python program to count occurrences of a substring in a string.
text = "Python is easy. Python is powerful."
print(text.count("Python"))

# 39. Write a Python program to reverse a string.
s = "Python"
print(s[::-1])

# 40. Write a Python program to reverse words in a string.
s = "Python is easy"
print(' '.join(reversed(s.split())))

# 41. Write a Python program to strip a set of characters from a string.
s = "///Python///"
print(s.strip("/"))
# 42. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2
from collections import Counter

s = 'thequickbrownfoxjumpsoverthelazydog'
counter = Counter(s)

# Sắp xếp theo số lần xuất hiện giảm dần
for char, count in sorted(counter.items(), key=lambda x: -x[1]):
    if count > 1:
        print(char, count)

# 49. Write a Python program to count and display vowels in text.
text = "Python is an interpreted high-level programming language."
vowels = "aeiouAEIOU"

count = {}
for ch in text:
    if ch in vowels:
        count[ch.lower()] = count.get(ch.lower(), 0) + 1

print("Vowel counts:")
for v in "aeiou":
    if v in count:
        print(v, count[v])

# 50. Write a Python program to split a string on the last occurrence of the delimiter.
text = "w3resource.python.practice"
parts = text.rsplit('.', 1)
print(parts)

# 51. Write a Python program to find the first non-repeating character in a given string.
from collections import Counter

s = "abcabdeff"
counter = Counter(s)

for ch in s:
    if counter[ch] == 1:
        print("First non-repeating character:", ch)
        break

# 52. Write a Python program to print all permutations with a given repetition number of characters
# of a given string.
import itertools

s = "abc"
r = 2  # repetition number

perms = itertools.product(s, repeat=r)
for p in perms:
    print(''.join(p))

# 53. Write a Python program to find the first repeated character in a given string.
s = "abcabdeff"

seen = set()
for ch in s:
    if ch in seen:
        print("First repeated character:", ch)
        break
    seen.add(ch)

# 54. Write a Python program to find the first repeated character in a given string where the index
# of the first occurrence is smallest.
s = "geeksforgeeks"

# Dictionary lưu {ký tự: index}
index_map = {}

first_repeat = None
min_index = len(s)

for i, ch in enumerate(s):
    if ch in index_map:
        if index_map[ch] < min_index:
            first_repeat = ch
            min_index = index_map[ch]
    else:
        index_map[ch] = i

print("First repeated character (with smallest index):", first_repeat)

# 55.Write a Python program to find the first repeated word in a given string.
def first_repeated_word(text):
    words = text.split()
    seen = set()
    for w in words:
        if w in seen:
            return w
        seen.add(w)
    return None

# Sample test
s = "he had had he"
print("First repeated word:", first_repeated_word(s))

# 56. Write a Python program to find the second most repeated word in a given string.
from collections import Counter

def second_most_repeated(text):
    words = text.split()
    freq = Counter(words)
    # Sắp xếp theo số lần xuất hiện (giảm dần)
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    if len(sorted_words) >= 2:
        return sorted_words[1][0]
    return None

# Sample test
s = "cat dog cat mouse dog cat mouse dog mouse"
print("Second most repeated word:", second_most_repeated(s))


