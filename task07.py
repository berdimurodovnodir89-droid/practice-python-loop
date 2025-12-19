num = int(input(f'ball 1: '))

max_ball = num

for i in range(2,5+1):
    num = int(input(f'son  {i}:'))
  
    if num > max_ball:
        max_ball = num

print(max_ball)