nums = [10, 20, 30, 40, 50]
names =["Viivi","Ahmed","Pekka","olga","Mary","Radin"]
print(nums[0])
print(nums[4])
print(nums[-1])
print(names[2])
print(names[-3])

print(len(nums))
print(len(names))
print("Ahmed" in names)
print("Sara" in names)



print(nums[1:3])#without 3rd position
print(nums[:2])#without 2nd position
print(nums[2:])#with 2nd position
print(names[0:4])#without 4th position
print(names[::4])
print(names[4::])

nums[2] = 300; print(nums)
names.append("Teppo"); print(names)
names.remove("Pekka"); print(names)
names.insert(1, "Matti"); print(names)
nums.sort(); print(nums)