from typing import Union
per : Union[int, float] = int(input("Enter your numbers"))

grade : Union[str ,None] = None
if per >= 80:
    grade = "A+"
elif per >= 70:
    grade = "A"
elif per >= 60:
    grade = "B"
elif per >= 50:
    grade = "C"
elif per >= 40:
    grade = "D"
elif per >= 33:
    grade = "E"
else:
    grade = "Fail"
print(f"Dear student your calculated percentage is {per} Now your calculated grad is {grade}")


