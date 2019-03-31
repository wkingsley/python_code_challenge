# 2. Merge Names 
def unique_names(names1, names2):
  names = names1 + names2
  return list(set(names))

# OR

# def unique_names(names1, names2):
#   new_names = []
#   names = names1 + names2
#   for x in names:
#     if x not in new_names:
#       new_names.append(x)
#   return new_names

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2))
# should print Ava, Emma, Olivia, Sophia
