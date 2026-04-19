dict1 = {
    "name" : "vivek",
    "age" : 26,
    "city" : "pune"
}

dict2 = {
    "gender" : "male",
    "hight" : 5.2,
    "family" : {
        "brother" : 2,
        "sister" : 3
    }
}

dict1.update(dict2)
print(dict1)