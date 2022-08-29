for i in range(100,201):
   if all(i%x != 0 for x in range(2,i)):
     print(i)