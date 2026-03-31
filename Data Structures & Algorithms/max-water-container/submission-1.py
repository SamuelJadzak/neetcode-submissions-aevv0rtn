class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # o(n^2) solution 
        # biggest_area = 0
        # for i, height1 in enumerate(heights):
        #     for j, height2 in enumerate(heights):
        #         height = min(height1, height2)
        #         biggest_area = max( biggest_area, height * (j - i))
        # return biggest_area
        biggest_area = 0
        i = 0
        j = len(heights)-1
        while i < j:
            biggest_area = max(biggest_area, min(heights[i], heights[j])*(j-i))
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return biggest_area

        
    