
from m5labfunctions import readcsv, calc_product_totals,writing_to_csv

def main():
   data = readcsv()
   products = calc_product_totals(data)
   writing_to_csv(products)
  
    
    
    

if __name__ == "__main__":
    main()