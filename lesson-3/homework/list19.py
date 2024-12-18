list = [1,2,3,4,5,6,7,8,9,10]
element = input("Enter the element: ")
list.remove(list[0])
list.insert(0, int(element))
print(list)