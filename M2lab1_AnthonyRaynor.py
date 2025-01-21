# Anthony Raynor
# 1/18/2025
# M1Lab2
# Make a program that finds out the average speed on each route and deteermine which route the shuttle driver should take

More_routes = 'y'
route_num = 1
fastest_time = []
# While loop starts
while More_routes  == 'y':
    route_distance = int(input(f"Enter route {route_num} distance (miles): "))
    route_speed = int(input(f"Enter route {route_num} speed (miles/hours): "))
    # Calc
    time_hr = route_distance / route_speed
    fastest_time = time_hr * 60
    fastest_route_number = route_num
        
    route_num += 1    
    More_routes = input("More routes (y/n)?: ")

    fastest_time.index = min()
        
    # Display
print(f"Route {fastest_route_number} is the fastest; {fastest_time:.0f} mintues")

    
    
     

   
