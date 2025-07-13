from typing import Callable

add : Callable[[int,int],int] = lambda x,y : x + y
result = add(19,50)
print(result) 
