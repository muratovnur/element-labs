#Not completed
a = float(input())
b = float(input())
c = float(input())

discriminant = b**2 - 4*a*c
if discriminant > 0:
  x1 = (-b + discriminant**0.5)/(2*a)
  x2 = (-b - discriminant**0.5)/(2*a)
  print((x1))
  print((x2))
elif discriminant == 0:
  print(-b/2*a)
else:
  print();