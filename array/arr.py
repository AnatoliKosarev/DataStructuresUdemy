import array as arr


arr1 = arr.array('i', [1, 2, 3, 4, 5, 6, 4])
print(arr1)

arr1.remove(4)
print(arr1)

arr1.insert(0, 4)
print(arr1)

print(arr1.index(4))

arr1.fromlist([123, 55])
print(arr1)

print(arr1.count(4))

arr_to_list = arr1.tolist()
print(arr_to_list)

array_part = arr1[:3]
print(array_part)
print(arr1)
