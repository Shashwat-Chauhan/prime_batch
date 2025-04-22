arr = [1, 2 , 3]
temp = []
def generate(temp: list[int] , idx, nums: list[int]):
    if idx == len(nums) - 1:
        print(temp)
        return

    generate(temp, idx + 1, nums) #Not take the element --> 0 Times

    temp.append(nums[idx])   #Take element once --> 1 Times
    generate(temp, idx+1 , nums)
    temp.pop()

    temp.append(nums[idx])  #Take element 2 Times --> 2 Times
    temp.append(nums[idx])

    generate(temp , idx + 1, nums)
    temp.pop()
    temp.pop()

generate(temp , 0 , arr)

    

