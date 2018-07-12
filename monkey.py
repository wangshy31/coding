def pick_peach(nums):

    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return 1
    else:
        pre_pre_num = pre_num = min(nums[0], nums[1])
        if nums[0] == nums[1]:
            result = 2
        else:
            result = 1
            for i in range(2, len(nums)):
                if nums[i] >= pre_num:
                    result = result + 1
                    pre_pre_num = pre_num
                    pre_num = nums[i]
                else:
                    if nums[i] >= pre_pre_num:
                        pre_num = nums[i]
                print nums[i], pre_num, pre_pre_num
    return result

if __name__ == "__main__":
    nums = [2,1,5,3,6,4,8,9,7]
    result = pick_peach(nums)
    print result

