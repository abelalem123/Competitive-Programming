# class Solution:
#     def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
#         for j in range(len(names)):
#             for i in range(1,len(names)-j):   
#                 if heights[i-1]<heights[i]:
#                     temp=names[i-1]
#                     names[i-1]=names[i]
#                     names[i]=temp
#                     tempn=heights[i-1]
#                     heights[i-1]=heights[i]
#                     heights[i]=tempn
#         return names

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_dict = dict(zip(heights,names)) # // height_dict = {180: 'Mary', 165: 'John', 170: 'Emma'}
        names.clear()
        for key in sorted(height_dict.keys(),reverse=True):
            names.append(height_dict[key])
        return names