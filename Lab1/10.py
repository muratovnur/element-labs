a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
  a, c = c, a
elif b > a and b > c:
  c, b = b, c
elif a == b and a > c:
  a, c = c, a

  
if a > b:
  b, a = a, b
print(a, b, c, sep=" ")