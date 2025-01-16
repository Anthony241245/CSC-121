# Anthony Raynor
# 1/16/2025
# M2Lab
# Use functions to simulate shopping
# Create a function that returns a string if the string is in a list of available items
# Create a function that asks the user how many of that item would they like to purchase
# Create a function that gets the cost of item
# Calculate and display the total items purchased and the total cost for all items

# Creat function to determine if item exists
def if_item_exist(item):
    '''
    Functions takes in one string. If that string exists in a list
    return true, if the string not in list, return false,
    '''
    store_Items = ["Cat food", "ball", "cat shirts", "brush"]

    if item in store_Items:
     return True

    else:
        return False
    
def getCost(item, quantity):
   '''
   Function takes in an item as a string and a quantity as integer
   Function calcualte the cost using a dictinary and return the total cost
   '''
   item_prices ={"Cat food":99.99, "ball":7.50, "cat shirts":4.50, "brush":50.32 }

    # Get the cost of the item from the dictionary
   item_cost = item_prices[item]

   total_cost = item_cost * quantity

   return total_cost
   






# Define the main function
def main():
    
        # Call all our other functions
    print("Welcome to Cat-Co!")

    run_again = "yes"

    final_cost = 0

    while run_again == "yes":
       
        # Get an item from the user
        user_item = input("What do you want to purchase?: ")

        if (if_item_exist(user_item)) == True:
            quantity = int(input(f"How many {user_item} will you buy?: "))
            final_cost = final_cost + getCost(user_item,quantity)
        else:
            print("Item doesn't exist")

    
       
        run_again = input("Will you add more items?: ")
        
    print(f"${final_cost:.2f}")
    
# Call the main function
if __name__ == "__main__":
    main()