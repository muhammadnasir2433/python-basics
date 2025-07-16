# from typing import Tuple, Dict

# def my_function(a:int,b:int,*abc:int,**xyz:int)->None:
#     print(a,b,abc,xyz)

# my_function(1,2, 2,3,4,5,6,  d = 4,e = 8, c = 80)



import math

def circle_stats(radius):
    return math.pi * radius ** 2
print(circle_stats(20))