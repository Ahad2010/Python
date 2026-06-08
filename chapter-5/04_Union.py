# ==========================
# SET OPERATIONS
# ==========================

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# union() -> Dono sets ke unique elements
print(a.union(b))

# intersection() -> Common elements
print(a.intersection(b))

# difference() -> A mein hain lekin B mein nahi
print(a.difference(b))

# symmetric_difference() -> Common ko hata kar baqi
print(a.symmetric_difference(b))

# issubset() -> Kya A, B ka subset hai?
print({1, 2}.issubset(a))

# issuperset() -> Kya A superset hai?
print(a.issuperset({1, 2}))

# isdisjoint() -> Kya dono sets mein koi common element nahi?
print(a.isdisjoint({7, 8}))

# update() -> Union karke original set update
a.update(b)

# intersection_update() -> Common elements hi rehne deta hai
a.intersection_update(b)

# difference_update() -> Difference ke mutabiq update
a.difference_update(b)

# symmetric_difference_update() -> Symmetric difference ke mutabiq update
a.symmetric_difference_update(b)  