# count = 1
# while count <= 5:
#     print("hello",count)
#     count += 1

# print 1 to 100-
# i = 1
# while i <= 100:
#     print(i)
#     i += 1
# print("loop end here")

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1
# print("loop end")

# # multiple of table n -
# i = int(input("enter a number : "))
# n = 1
# while n <= 10:
#     x = i * n 
#     print(x)
#     n += 1

# i = 1
# n = 1
# x = []
# while i <= 10:
#     x =(i * n)
#     i += 1
#     n += 1
#     print(x)

# x = []
# i = 1
# n = 1
# while i <= 10:
#     x.append(i * n)
#     i += 1
#     n += 1
# print(x)

# tut = (2,4,6,7,1,9,4,7,22,9)
# num = 9
# i = 0

# while i < len(tut):
#     if tut[i] == 9:
#         print("found", i)
#     else:
#         print("finding...")
#     i += 1


# tut = (2,4,6,7,1,9,4,7,22)
# i = 0
# n = 9
# print(len(tut))
# while len(tut) > i:
#     if tut[i] == 9:
#         print("found")
#         break;
#     else:
#         print("finding...")
#     i += 1

# tut = (2,4,6,7,1,9,4,7,22,9)
# i = 0
# n = 9
# print(len(tut))
# while len(tut) > i:
#     if tut[i] == 9:
#         print("found")
#     else:
#         print("finding...")
#     i += 1


# i = 1
# while i <= 10:
#     if (i %2 != 0):
#         i += 1
#         continue
#     print(i)
#     i += 1

# str1 = "abcdefghi"
# for char in str1:
#     if char == "f":
#         print("found",char)
#         continue;
#     print(char)
# print("end")

# list1 = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while len(list1) > i:
#     print(list1[i])
#     i += 1

# tup = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# x = int(input("enter any number mention in above : "))
# while len(tup) > i:
#     if tup[i] == x:
#         print("found at index of", i)
#         break;
#     i += 1

tup = [1,4,9,16,25,36,49,64,81,100]
x = int(input("enter any number mention in above : "))
i = 0
for char in tup:
    if char == x:
        print("found",char)
    i += 0
    
    
























