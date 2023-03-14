#1st trial with time limit exceeded
# class Solution(object):
#     def replaceElements(self, arr):
#         """
#         :type arr: List[int]
#         :rtype: List[int]
#         """
#         for i in range(len(arr)-1):
#             arr[i] = max(arr[i+1:])
#         arr[-1] = -1
#         return arr

#accepted one
#instead of looping from i+1 to len-1 every iteration 
# we can loop from the end and getting max between 
# current item and last item
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        max_val = -1
        for i in range(len(arr)-1, -1, -1):
            arr[i], max_val = max_val, max(max_val, arr[i])
        return arr