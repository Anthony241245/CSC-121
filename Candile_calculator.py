# Anthony Raynor
# 1/14/25
# Calculate cost of item based on quantity

'''
Get number of candles to purchase from user 
if num_candles between 1-19, cost per item is $4.75
if num_candles between 20-49, cost per item is $4.50
if num_candles between 50-99, cost per item is $4.25
if num_candles greater than ir equal to 100, cost per item is $4.00
Calculate total by multiplying num_candles cost per item
'''
# Get number of candles from user
run_again = "yes"

#While loop begins here
while run_again == "yes":
    
    num_candles = int(input("How many candles will you buy?: "))
    if num_candles > 0 and num_candles < 20:
        cost_per_item = 4.75

    elif num_candles > 19 and num_candles < 50:
        cost_per_item = 4.50

    elif num_candles > 49 and num_candles < 100:
        cost_per_item = 4.25

    elif num_candles >= 100:
        cost_per_item = 4.00

    else:
        cost_per_item = 0
        print("Error, invalid number of candles entered!!")
        # Display info to user
    print("\n\n\n")
    print("*" * 30)
    print(f"Number of candles purchased: {num_candles}")
    print(f"Cost per item: ${cost_per_item:.2f}")
    print(f"Total cost of all candles purchased: ${(num_candles * cost_per_item):.2f}")
    
    # Ask user to run again
    run_again = input("Would you like to run the program again?: ")

print("Program has ended!")