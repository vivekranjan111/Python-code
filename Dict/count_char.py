# str1 = "bAnana"
# str2 = str1.lower()
# dict1 = {}

# for ch in str2:
#     dict1[ch] = dict1.get(ch,0) + 1

# print(dict1)

# s = "banana"
# dict1 = {}
# for ch in s:
#     if ch in dict1:
#         dict1[ch] += 1
#     else:
#         dict1[ch] = 1
# print(dict1)


# text = "python is easy and python is powerful"
# text1 = text.replace(" ","")
# dict1 = {}

# for char in text1:
#     dict1[char] = dict1.get(char,0) + 1
# print(dict1)


# text = "python is easy and python is powerful"
# dict1 = {}
# for char in text.split():
#     dict1[char] = dict1.get(char,0) + 1
# print(dict1)


# # Find first non-repeating character
# str1 = "aabbccdef"
# dict1 = {}
# for ch in str1:
#     dict1[ch] = dict1.get(ch,0) + 1
# for ch in str1:
#     if dict1[ch] == 1:
#         print(ch)
#         break


# Find non-repeating character
str1 = "aabbccdef"
dict1 = {}
for ch in str1:
    dict1[ch] = dict1.get(ch,0) + 1
for ch in str1:
    if dict1[ch] == 1:
        print(ch)