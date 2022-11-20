a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
  if a > b and a > c:
    a, c = c, a
  elif b > a and b > c:
    c, b = b, c
  elif a == b and a > c:
    a, c = c, a

  if (a**2 + b**2) == c**2:
    print("right")
  elif (a**2 + b**2) > c**2:
    print("acute")
  else:
    print("obtuse")
else:
  print("impossible")
  


