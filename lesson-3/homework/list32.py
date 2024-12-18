list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [1,2,3,503, 32, 4,5,6,7,8,9,10, 20, 30]
new_list = list(set(list1+list2))
new_sorted_list = sorted(new_list)
print(new_sorted_list)