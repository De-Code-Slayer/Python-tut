def elems(e):
  for i,j in enumerate(e):
        while i > 0:
            if e[i] < e[i-1]:
                e[i], e[i-1] = e[i-1], e[i]
                i-=1
                continue
            break
  return e
 
print(elems([8,9,77,5,6,1]))
