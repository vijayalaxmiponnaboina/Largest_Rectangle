class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack=[]
        max_area=0
        for i in range(n):
            while stack and heights[i]<heights[stack[-1]]:
                prev=stack.pop()
                height=heights[prev]
                if len(stack)==0:
                    width=i
                else:
                    width=i-stack[-1]-1
                area=height*width
                max_area=max(area,max_area)
            stack.append(i)
        while stack:
            prev=stack.pop()
            height=heights[prev]
            i=len(heights)
            if len(stack)==0:
                width=i
            else:
                width=i-stack[-1]-1
            area=height*width
            max_area=max(area,max_area)
        return max_area