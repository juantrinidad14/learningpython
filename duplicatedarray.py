def duplicate(list1):
   list_copy = []
   list_copy = list1.copy()
   return list_copy

list1 = [ 1, 2, 3, 4, 5]
list2 = duplicate(list1)

print(list2)

