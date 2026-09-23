class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #index,height
        maxArea = 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h:
                si,h2 = stack.pop()
                maxArea = max((i-si)*h2,maxArea)
                start = si
            stack.append((start,h))
        #process the remaining eleemnts of the stack
        
        while stack:
            newi,newH = stack.pop()
            maxArea = max(maxArea,(len(heights)-newi)*newH)
        return maxArea