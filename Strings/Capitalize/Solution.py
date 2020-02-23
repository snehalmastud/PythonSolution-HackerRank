
# Complete the solve function below.
def solve(s):
    str= [i.strip().capitalize() for i in s.split() ]
    for i in str:
         s =s.replace(i.lower(),i)
    return s

