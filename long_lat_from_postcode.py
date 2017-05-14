
# coding: utf-8

import urllib.request, json 

class long_lat(object):
    '''
    from a user entered postcode I need to return a longditude and lattitude. I use the api api.postcodes
    '''
    def __init__(self, postcode, long_lat_result = []):
        self.postcode = postcode
        self.long_lat_result = long_lat_result
        
    def find_long_lat(self):
        ''' using postcode I retrieve the long and lat as a list of strings '''
        with urllib.request.urlopen("http://api.postcodes.io/postcodes/" + self.postcode) as url:
            data = json.loads(url.read().decode())
            
        longd = data['result']['longitude']
        lat = data['result']['latitude']
        self.long_lat_result.append(longd)
        self.long_lat_result.append(lat)
 
        return self.long_lat_result




# In[ ]:



