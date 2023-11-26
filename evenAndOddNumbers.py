count_odd =0
count_even = 0

  
for numbers in range(1,101):
     if numbers % 2  == 0:
       count_even +=1
 
     elif numbers % 2 != 0:
        count_odd += 1
       


     print("Number of even numbers:",count_even)
        
     print("Number of odd numbers:",count_odd)