N = int(input())
l = []
for x in range(N): l.append(input().split(" "))


for x in l: 
  for z in range(N): 
    x[z] = int(x[z])
    
def minu(x, y):
  minus = []
  for z in range(y):
    minus.append(min(x))
    x.remove(min(x))
  return minus
  
sum = []
for w in l:
  c = 1
  while c <= N:
    sum.append(minu(w, N - 1))
  c += 1

    
    
