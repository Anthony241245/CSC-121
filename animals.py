
############### NESTED DICTIONARY

animals = {
    "Big Cats": {
        "Lion": ["Asiatic Lion", "West African Lion", "South African Lion"],
        "Tiger": ["Bengal Tiger", "Siberian Tiger", "Indochinese Tiger"],
        "Cheetah": ["African Cheetah", "Asiatic Cheetah", "Saharan Cheetah"]
    },
    "Wild Dogs": {
        "Wolf": ["Arctic Wolf", "Gray Wolf", "Timber Wolf"],
        "Fox": ["Red Fox", "Silver Fox", "Cross Fox"],
        "Wild Dog": ["African Wild Dog", "Painted Wolf", "Cape Hunting Dog"]
    },
    "Bears": {
        "Brown Bear": ["Grizzly Bear", "Kodiak Bear", "Eurasian Brown Bear"],
        "Polar Bear": ["Greenland Polar Bear", "Hudson Bay Polar Bear"],
        "Andean Bear": ["Northern Andean Bear", "Southern Andean Bear"]
    }
}

#animals is a dictinary and each items are 

# Describe the structure of the variable animals

# Pull specified data from the dictionary where the key is "Big Cats" and  the value is another dictinary now the keys are lion, tiger , cheetah
# print the list
print(animals["Wild Dogs"]["Fox"])
# Retrieve silver Fox 
print(animals["Wild Dogs"]["Fox"][1])
# Retrieve the string greenland polar bear
print(animals["Bears"]["Polar Bear"][0])
print(F"One Type of Polar bear is the {animals['Bears']['Polar Bear'][0]}")

# Write a loop to display every piece of data in animals
# Loop through the nested dictionary
for a in animals: # animals is the outer dictionary
    print(a)
   # print(animals[a])
    #print("\n")
    for n in animals[a]:  # animals[a] is the inner dictionary
        print("\t",n)
        print("\t\t",animals[a][n]) # animals[a][n] is a list
    for i in animals[a][n]:
        print("\t\t", i)



################## THREE LEVEL NESTED LIST

'''
How the nesting works:
First level: Broad fish categories (Freshwater Fish, Saltwater Fish, Coral Reef Fish).
Second level: Types of fish within each category (e.g., Bass, Trout, Catfish).
Third level: Specific species of each type.
'''

fish_types = [
    ["Freshwater Fish", 
        ["Bass", 
            ["Largemouth Bass", "Smallmouth Bass", "Spotted Bass"]
        ],
        ["Trout", 
            ["Rainbow Trout", "Brown Trout", "Brook Trout"]
        ],
        ["Catfish", 
            ["Channel Catfish", "Blue Catfish", "Flathead Catfish"]
        ]
    ],
    ["Saltwater Fish", 
        ["Sharks", 
            ["Great White Shark", "Hammerhead Shark", "Tiger Shark"]
        ],
        ["Tuna", 
            ["Bluefin Tuna", "Yellowfin Tuna", "Albacore Tuna"]
        ],
        ["Marlin", 
            ["Blue Marlin", "White Marlin", "Black Marlin"]
        ]
    ],
    ["Coral Reef Fish", 
        ["Clownfish", 
            ["Common Clownfish", "Saddleback Clownfish", "Clark's Clownfish"]
        ],
        ["Angelfish", 
            ["Emperor Angelfish", "French Angelfish", "Queen Angelfish"]
        ],
        ["Parrotfish", 
            ["Stoplight Parrotfish", "Rainbow Parrotfish", "Bicolor Parrotfish"]
        ]
    ]
]

print(fish_types[2][2][1][2])

# Use some looping for each data structure
# Show each Broad fish categories (Freshwater Fish, Saltwater Fish, Coral Reef Fish).
# Then show each type of fish within that category
# Then show each species of fish within the category (most inner nested list)


######## NESTED DICTIONARY SIMILAR TO HOMEWORK

dog_breeds = {
    "Labrador Retriever": {
        "desc": "Friendly and outgoing, great family dog",
        "weight": 65,
        "cost": 800
    },
    "German Shepherd": {
        "desc": "Intelligent and versatile, often used in police work",
        "weight": 75,
        "cost": 1000
    },
    "Golden Retriever": {
        "desc": "Loyal and loving, excellent for therapy and assistance",
        "weight": 70,
        "cost": 900
    },
    "Bulldog": {
        "desc": "Gentle and affectionate, known for their wrinkled face",
        "weight": 50,
        "cost": 1200
    },
    "Poodle": {
        "desc": "Highly intelligent and hypoallergenic coat",
        "weight": 45,
        "cost": 1500
    }
}



# Let's pull some info from the dictinary and loop through it :)
# Retrieve cost of a bulldog
print(dog_breeds["Bulldog"]["cost"])
print("\n\n\n\n")

for key in dog_breeds:
    print(key)
for each in dog_breeds[key]: # dof_breed[keys] is a dictionary
    print("\t", each, ":" ,dog_breeds[key][each])

