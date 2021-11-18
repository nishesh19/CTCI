from collections import Counter


class Solution:
    def isPossible(self, nums) -> bool:
        if (not nums) or (len(nums) < 6):
            return False

        numbers = Counter(nums)
        total_seq = 0
        while numbers:
            prev = None
            prev_seq = total_seq
            curr_len = 0

            for num in sorted(numbers.keys()):
                if curr_len == 3:
                    break

                if not prev:
                    prev = num
                    curr_len = 1
                elif prev + 1 == num:
                    curr_len += 1
                    prev = num
                else:
                    if prev in numbers:
                        del numbers[prev]
                    prev = num
                    curr_len = 1

                if (numbers[num] - 1) == 0:
                    del numbers[num]
                else:
                    numbers[num] -= 1

            if curr_len == 3:
                if total_seq + 1 == 2:
                    return True
                total_seq += 1

            if prev_seq == total_seq:
                break

        return False


if __name__ == '__main__':
    sol = Solution()

    print(sol.isPossible([1, 1, 2, 3, 3, 4, 5]))
    # print(sol.isPossible([1, 2, 3, 3, 4, 4, 5, 5]))
    # print(sol.isPossible([1, 2, 3, 4, 4, 5]))
