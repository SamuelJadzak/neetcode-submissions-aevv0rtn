class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggest_area = 0
        for i, height1 in enumerate(heights):
            for j, height2 in enumerate(heights):
                height = min(height1, height2)
                biggest_area = max( biggest_area, height * (j - i))
        return biggest_area