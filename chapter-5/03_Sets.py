# ==========================
# PYTHON SET METHODS
# ==========================

s = {1, 2, 3, 4, 5}

# add() -> Ek element add karta hai
s.add(6)

# remove() -> Element remove karta hai (na ho to error)
s.remove(2)

# discard() -> Element remove karta hai (na ho to error nahi)
s.discard(10)

# pop() -> Random element remove karta hai aur return karta hai
removed = s.pop()

# copy() -> Set ki copy banata hai
new_set = s.copy()

# clear() -> Set ko empty kar deta hai
# s.clear()

# len() -> Set ki length
print(len(s))

# max() -> Sab se badi value
print(max(s))

# min() -> Sab se choti value
print(min(s))

# sum() -> Numeric values ka total
print(sum(s))

# in -> Check karta hai element mojood hai ya nahi
print(3 in s)

# not in -> Check karta hai element mojood nahi hai
print(10 not in s)