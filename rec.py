def closestNumbers(numbers):
    if numbers:
    # Write your code here
       numbers.sort()
       sorted_num = numbers
        
       seen = []
       min_diff = abs(sorted_num[0] - sorted_num[1])
       for i in range(len(numbers)-1):
          if abs(sorted_num[i] - sorted_num[i+1]) == min_diff :
            small = sorted_num[i]
            large =  sorted_num[i+1]
            seen.append([small,large])
            
       for i in seen:
         print(i[0],i[1])


closestNumbers([1,2,3,4,5,7,10,9])