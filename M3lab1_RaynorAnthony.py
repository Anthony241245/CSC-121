# Anthony Raynor
# M3lab1
# 3/13/25
# Reading csv data into class onjects
import csv

# Make a class
class Customer:
    # Create __init__ function
    def __init__(self, first, last, phone, email, state, address):
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email
        self.state = state
        self.address = address

    def display_info(self):
        return f"\n{self.first} {self.last}\n{self.phone}\n{self.email}\n{self.address}, {self.state}\n\n"
    
# Test
# customer1 = Customer("Anthony", "J", "704-555-4521", "JJOE@gmail.com", "NC","2313 fasthill drive")

# print(customer1.display_info())

# Create Empty List to hold csv info
customer_input = []

with open('customer.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        customer_input.append(row)

print(customer_input)

# TO-DO
'''
iterate through the nested list. Ignore the first inner list.
For each remaining list, create a Customer object from the list order data


'''