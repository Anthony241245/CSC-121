
# dollar store discount - cost and display using functions

# calculate pre-tax cost with conditional discount
def calcCost(count):
    """
    Parameters
    ----------
    count : number of items bought

    Returns
    -------
    cost : cost with or without discount

    """
    cost = 1
    discount_rate = 0.5
    tax_rate = 0.62
    if count >= 10:
       discount = discount_rate * cost
    tax = tax_rate * cost
    cost = count - discount
    return cost, tax

    # function to display lines with a consistent format
def displayLine(label, amount):
    print(f"{label:<15} {amount:.2f}")

# display results
def display(cost, tax):
    """
    Parameters
    ----------
    cost : calculated cost - discount
    tax : tax amount

    Returns
    -------
    None.

    """
    
    print("\nResults:")
    displayLine("Net Cost:",cost)
    displayLine("Tax:", tax)
    displayLine("After tax:", cost+tax)







