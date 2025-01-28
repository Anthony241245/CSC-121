
import store_fun as fn
# from store_fun import (functions)


def main():
    
    print("\nIMPORTANT How cost is calculated:\n")
    
    print("Each item in the store costs $1 dollar")
    print("Customer buying 10 or more items recieves 5% discount")
    print("Customer LESS than 10 items, recieves 0 discount")
    print("6.2% sales tax is applied")

    # Initialize choice
    choice = 1

    
    
    
    while choice != 2:
        
        # call menu function        
        fn.menu()

        #enter choice
        choice = int(input("\nEnter Choice: "))
        
        #evaluate what user entered
        
        if choice == 1:

                # get input
            count = int(input("Enter number of items: "))
                
            # calculate cost, tax rate, and tax
            cost = fn.calcCost(count)
            taxrate= .062
            tax = cost * taxrate


        
            fn.display(cost,tax)
    
        elif choice == 2:

            print("\nProgram Terminationg....")

        else:

            print("Invalid Entry")
            
            
       
    
    
        



    

if __name__ == "__main__":
    
    main()