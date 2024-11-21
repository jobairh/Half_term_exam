nums = [3, 6, 2, 7, 5, 6, 8, 5, 8, 3, 7]

# Step-1---
new_nums = []
for i in nums:
    if i not in new_nums:
        new_nums.append(i)

print('Remove duplicates from the list:\n', new_nums)

# Step-2---
l1 = new_nums
print("Original List:", l1)
 
for i in range(0, len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j],l1[i]
 
print("Sorted List", l1)

# Step-3---
mid_nums = int(len(new_nums) / 2)
new_list = new_nums[mid_nums - 1:mid_nums + 2]

print('Middle Three Elements:\n', new_list)


