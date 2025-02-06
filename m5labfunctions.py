import csv

def readcsv():
    with open("sales.csv", "r") as file:
        # Create csv reader object
        reader = csv.reader(file)
        #for row in reader:
            #print(row)
    return reader

def calc_product_totals(reader):
    products = {}
    with open("sales.csv", "r") as file:
        # Create csv reader object
        reader = csv.reader(file)
        # Skip the heading row
        next(reader)
        for row in reader:
            if row[2] not in products:
                products[row[2]] = int(row[4]) * float(row[5])
            else:
                products[row[2]] += int(row[4]) * float(row[5])
        for key, value in products.items():
            print(f"Product ID: {key}   ${value}")
    return products
    


def writing_to_csv(products):
    with open("sales.csv", "w", ) as file:
        column_names = ["Product ID", "Total Sales"]
        # Create CSV writer
        writer = csv.DictWriter(file, fieldnames=column_names)
        result = [{"Product ID":key, "Total Sales": value} for key, value in products.items()]
        writer.writeheader()
        writer.writerows(result)


    
                




    
