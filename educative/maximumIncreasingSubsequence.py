
def find_MSIS(nums):
    dp = [[None for _ in range(len(nums))] for _ in range(len(nums))]
    return find_MSIS_recursive(nums, dp, 0, -1, 0)


def find_MSIS_recursive(nums,  dp, currentIndex,  previousIndex,  sum):
    if currentIndex == len(nums):
        return sum

    # include nums[currentIndex] if it is larger than the last included number
    if dp[currentIndex][previousIndex] is None:
        s1 = sum
        if previousIndex == -1 or nums[currentIndex] > nums[previousIndex]:
            s1 = find_MSIS_recursive(nums, dp, currentIndex+1,
                                     currentIndex, sum + nums[currentIndex])

        # excluding the number at currentIndex
        s2 = find_MSIS_recursive(nums, dp, currentIndex+1, previousIndex, sum)

        dp[currentIndex][previousIndex] = max(s1, s2)
    
    return dp[currentIndex][previousIndex]


def main():
    # print(find_MSIS([4, 1, 2, 6, 10, 1, 12]))
    print(find_MSIS([-4, 10, 3, 7, 15]))


main()
