class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_length = 0
        buff_dict = {0: 0}
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in buff_dict:
                max_length = max(max_length, index-buff_dict[count])
            else:
                buff_dict[count] = index


        return max_length