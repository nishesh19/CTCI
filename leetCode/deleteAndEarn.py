import random


class Solution:

    def __init__(self, nums):
        self.orig = nums
        self.current = nums

    def reset(self) :
        """
        Resets the array to its original configuration and return it.
        """
        self.current = self.orig[:]
        return self.current

    def shuffle(self) :
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.current)
        return self.current


if __name__ == '__main__':
    nums = [1, 2, 3]
    obj = Solution(nums)
    param_1 = obj.reset()
    param_2 = obj.shuffle()
# Your Solution object will be instantiated and called as such:
