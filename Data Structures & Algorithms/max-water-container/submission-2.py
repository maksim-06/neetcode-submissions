class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_square = 0
        while left < right:
            square = (right - left) * min(heights[left], heights[right])
            if square > max_square:
                max_square = square
            
            if heights[left] <= heights[right]:
                left += 1
            
            else:
                right -= 1

        return max_square
            

            