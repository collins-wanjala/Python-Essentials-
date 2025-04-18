#Basic scientifc calculator
first_number = eval(input("Enter the first number :")) 
#choose the operator
operator = input(" '+' , '-' , '/' , '%', '*' : " )

#Enter the second number
second_number = eval(input("Enter the second number :" ))

#Computation processing
if operator == ' ':
    print("No operator was entered ,enteran operator from  above")
    #Addition
elif operator == '+':
    sum = first_number + second_number 
    print(f"The sum of {first_number} and {second_number} is " ,sum)
    #subtraction
elif operator == '-':
    #inside loop
    if first_number > second_number :
        subtraction =   first_number -  second_number
        print(f"The Difference  of {first_number} and {second_number} is " ,subtraction)
    if second_number > first_number :
        subtraction = second_number - first_number
        print(f"The Difference  of {second_number} and {first_number} is " ,subtraction)
  #product      
elif operator =='*' :
    product = first_number * second_number
    print(f"The Product of {first_number} and {second_number} is " ,product)
    
#modulus
elif operator =='%' :
    modulus = first_number % second_number
    print(f"The Modulus  of {first_number} and {second_number} is " ,modulus)
    
#Division
elif operator =='/' :
    while True :
        second_number = eval(input("Enter the second number :" ))
        if second_number == 0 :
            
            print("⚠️ Division by zero is not allowed. Please enter a non-zero number.")
           # Check a zero
        else:
            division = first_number / second_number
            print(f"The Division  of {first_number} by {second_number} is " ,division) 
            print("✅ Reminder: Avoid dividing by zero in future calculations.") 
            break
    
             
#Close the program
else:
    print("Unknown Operator ")
