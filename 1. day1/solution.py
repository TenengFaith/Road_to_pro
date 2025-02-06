def target_sums(numbers,target):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j]==target:
                print(f"number indices are {i} and {j} ")
nums=[1,14,8,10,6,4,13,11]
target_sums(nums,target=14)