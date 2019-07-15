# Give range of offers to purchase a house

# State market price
print('A one bedroom in the Bay Area is listed at $599,000')

# Prompt user to make an offer on a house 
print('Enter your first offer on the house.')

# Set offer equal to input()
offer = abs(int(input()))

# Prompt user to enter best offer on house 
print('Enter your best offer on the house.')

# Set best equal to input()
best = abs(int(input()))

# Prompt user to choose increments 
print('How much more do you want offer each time?')

# Set increment equal to input()
increment = abs(int(input()))

# Set offer_accepted equal to False
offer_accepted = False

# Initialize for loop from offer to best
while offer <= best:
    
    # If offer is greater than 650,000, they get the house 
    if offer >= 650000:
        offer_accepted = True
        print('Your offer of', offer, 'has been accepted!')
        break
    
    # If offer does not exceed 650,000 they don't get the house
    print('We\'re sorry, you\'re offer of', offer, 'has not been accept-ed.' )
    
    # Add increment to offer
    offer += increment