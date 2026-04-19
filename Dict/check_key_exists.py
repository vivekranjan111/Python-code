# Check key exists
# dict1 = {
#     "name" : "vivek",
#     "city" : "pune",
#     "age" : 54
# }
# if "name" in dict1:
#     print("key exixt")


# # Get all keys and values. Print all keys and all values separately.
# dict1 = {
#     "name" : "vivek",
#     "city" : "pune",
#     "age" : 54
# }
# print(dict1.keys())
# print(dict1.values())


# # Find the key with the highest value.
# dict1 = {
#     "a" : 5,
#     "b" : 22.0,
#     "c" : 22.01
# }
# max_dict1 = max(dict1,key=dict1.get)
# print(max_dict1)


# # Swap keys and values
# dict1 = {
#     "a" : 2,
#     "b" : 5
# }
# print(dict1)
# new_dict1 = {v : k for k,v in dict1.items()}
# print(new_dict1)


# # Sum of values
# dict1 = {
#     "a" : 2,
#     "b" : 4,
#     "c" : 6
# }
# print(dict1.items())
# print(dict1.keys())
# print(dict1.values())
# print(sum(dict1.values()))

# # Remove duplicates using dictionary
# lst = [1,1,4,6,8,2,4,1]
# res = list(dict.fromkeys(lst))
# print(res)


# Sort dictionary by value
# d = {"a": 3, "b": 1, "c": 2}
# sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
# print(sorted_d)

# # Create dictionary from two lists
# keys = ["a", "b", "c"]
# values = [4,6,8]

# dict1= dict(zip(keys, values))
# print(dict1)



s = "banana"
dict1 = {}
for ch in s:
    if ch in dict1:
        dict1[ch] += 1
    else:
        dict1[ch] = 1
print(dict1)