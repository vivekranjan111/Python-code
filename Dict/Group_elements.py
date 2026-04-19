words = ["cat", "car", "dog", "door"]

d = {}
for word in words:
    key = word[0]
    d.setdefault(key, []).append(word)

print(d) 