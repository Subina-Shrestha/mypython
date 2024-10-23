# * 
# * *
# * * *
# * * * *
# * * * * *
for i in range(0,6):
      for j in range(0,i):
            print("*", end=" ")
      print("")

# * * * * *
# * * * *
# * * *
# * *
# * 
print()
for i in range(6,0,-1):
      for j in range(0,i):
            print("*", end=" ")
      print("")


# full pyramid
n=5
for i in range(n+1):
      for j in range(n-i):
            print(" ",end="")
      for k in range(1, 2*i):
            print("*",end="")
      print()

n=5
for i in range(n+1):
      for j in range(n-i):
            print(" ",end="")
      for k in range(1, 2*i):
            print("* ",end="")
      print()

