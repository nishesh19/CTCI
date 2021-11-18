class Solution:
    def findDuplicate(self, nums) -> int:
        slower = nums[0]
        faster = nums[nums[0]]

        while slower != faster:
            slower = nums[slower]
            faster = nums[nums[faster]]

        slower = nums[0]

        while slower != faster:
            slower = nums[slower]
            faster = nums[faster]

        return slower

    def findDuplicate2(self, nums):
        # Find the intersection point of the two runners.
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1


if __name__ == '__main__':
    sol = Solution()

    # print(sol.findDuplicate2([1, 3, 4, 2, 2]))
    print(sol.findDuplicate([1, 3, 4, 2, 2]))
    
