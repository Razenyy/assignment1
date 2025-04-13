''' Create two sets:
set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}
(a) Write code to perform a union of these sets. Print the length of the resulting set.
(b) Write code to perform an intersection of set1 and set2.
(c) Write code to compute the symmetric difference between set1 and set2
(d) Write code to add the value 40 to set1, did the set change?
(e) Write code to remove value 20 from set2.
'''
set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}

# (a) Union
union_set = set1 | set2
print("Union length:", len(union_set))

# (b) Intersection
intersection_set = set1 & set2
print("Intersection:", intersection_set)

# (c) Symmetric Difference
symmetric_difference_set = set1 ^ set2
print("Symmetric Difference:", symmetric_difference_set)

# (d) Add 40 to set1
set1.add(40)  # No change since 40 is already present

# (e) Remove 20 from set2
set2.discard(20)
print("Updated set2:", set2)
