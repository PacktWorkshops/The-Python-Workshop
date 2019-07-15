>>> # Find the perfect square of a number

>>> # Prompt user to enter a number to see if its a perfect square 
>>> print('Enter a number to see if it\'s a perfect square.')

>>> # Set a variable equal to input()
>>> number = input()

>>> # Ensure input is a positive whole number
>>> number = abs(int(number))

>>> # Choose iterator variable
>>> i = -1

>>> # Initialize Boolean to check for perfect square
>>> square = False

>>> # Initialize while loop from -1 to square root of the number
>>> while i <= number**(0.5):
    
>>>    # Increment i by 1
>>>    i += 1
    
>>>    # Check if is the square root of the number
>>>    if i*i == number:
        
>>>        # Indicate that we have a perfect square
>>>        square = True
        
>>>        # break out of loop
>>>        break

>>> # If the number is square, print out the result
>>> if square:
>>>    print('The square root of', number, 'is', i, '.')

>>> # If the number is not a square print out the result    
>>> else:
>>>    print('', number, 'has no perfect square.')

Enter a number to see if it's a perfect square.
49
The square root of 49 is 7.