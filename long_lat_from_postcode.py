
# coding: utf-8

import urllib.request, json 

def find_long_lat(postcode):
    '''
    This finds the long lat from a postcode using an api called postcodes. I want to output the result as a list 
    '''
    # Download the json data from api.postcodes
    with urllib.request.urlopen("http://api.postcodes.io/postcodes/" + postcode) as url:
        data = json.loads(url.read().decode())

    # create the output list and append latt
    long_and_lat = []
    long_and_lat.append(data['result']['latitude'])
    long_and_lat.append(data['result']['longitude'])
    
    return long_and_lat


def create_long_lat_grid(long_and_lat):
    '''
    Take a single long/lat coordinate and make a grid around that coordinate.  
    '''
    # create a coordinate at the bottom right of the square I want.
    long_and_lat[0] = long_and_lat[0] - float(0.005)
    long_and_lat[1] = long_and_lat[1] + float(0.005)
               
    # all the values in the square are going to be saved here. 
    long_lat_grid = []

    # Move up one 0.001 10 times. Add that value to my list. 
    for _ in range(10):
        long_and_lat[0] =   long_and_lat[0] + float(0.001)
        long_lat_grid.append(long_and_lat.copy())
 
        # move left 0.001 10 times. again add this value to my list. 
        for _ in range(10):
            long_and_lat[1] =   long_and_lat[1] - float(0.001)
            long_lat_grid.append(long_and_lat.copy())
        
        # once I've done the whole bottom row start again at the right.     
        long_and_lat[1] = long_and_lat[1] + float(0.01)

    return long_lat_grid
       
    
def():
    ''' I'm going to look through every long lat in my grid from create_long_lat_grid and run it for every month in the last x months'''
    





postcode = 'SW1A2HJ'
long_lat_result = find_long_lat(postcode)  
print (long_lat_result)

grid_result = create_long_lat_grid(long_lat_result)

