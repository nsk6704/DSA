class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# This is the basic prefix sum implementation actually

"""
Here, we just initialise array with first element as 0, since prefix sum till first element is sum until first, which is essentially 0. Then, we iterate accross the list and keep appending the current num to the prev value of the prefix array

Example- for an array [1, 2, 4, 5, 6]

The dry run would be:

[0] -> [0, 1] -> [0, 1, 3] -> [0, 1, 3, 7] -> [0, 1, 3, 7, 12] -> [0, 1, 3, 7, 12, 18]

And for getting the range lets say for sumRange(self, 1, 3) = 12 -1 = 11 which is the right answer!

"""


