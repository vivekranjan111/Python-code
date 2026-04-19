# dict1 = {
#     "name" : "vivek",
#     "age" : 26 ,
#     "city" : "Bangalore"
# }
# print(dict1)

# print(dict1["name"])
# print(dict1.keys())
# print(dict1.values())

# dict1["salary"] = 5000 
# print(dict1)

# dict1["age"] = 30
# print(dict1)

# del dict1["city"] 
# print(dict1)

# Input from keyboard
# dict2 = {}
# x = int(input("enter your phy marks : "))
# dict2.update({"phy": x})
# y = int(input("enter your chem marks : "))
# dict2.update({"chem":y})
# z = int(input("enter your math marks : "))
# dict2.update({"math98":z})
# print(dict2)

# Create dict inside dict--
# dict1 = {
#     "name": "vivek",
#     "class": 7,
#     "subject": {
#         "phy": 56,
#         "chem": 88,
#     },
#     "gender" : "male"
# }
# print(dict1.values())


# text = "python is easy and python is powerful"
# text1 = text.replace(" ","")
# dict1 = {}

# for char in text1:
#     dict1[char] = dict1.get(char,0) + 1
# print(dict1)


response = {"status": "success", "code": 200}

expected = {"status": "success", "code": 200}

for k in expected:
    if response.get(k) != expected[k]:
        print("Mismatch found")
    else:
        print("pass")