
# coding: utf-8

# In[1]:

import unittest


from long_lat_from_postcode import find_long_lat, create_long_lat_grid

class LongLatTestCase(unittest.TestCase):
    ''' test for long_lat_from_postcode.py'''
    
    def test_get_correct_Long_Lat(self):
        ''' do I get [-0.125668386000805, 51.506582950758] for this postcode?'''
        long_and_lat = [51.506582950758, -0.125668386000805]
     				
        postcode = 'SW1A2HJ'
        result = find_long_lat(postcode)
    
        assert(result == long_and_lat)

    def test_create_long_lat_grid(self):
    	''' test create_long_lat_grid I'm going check that the length is the same and do a view spot checks '''
    	long_and_lat = [51.506582950758, -0.125668386000805]
    	result = create_long_lat_grid(long_and_lat)
    	correct_lat_value = [51.511582950757976, -0.130668386000805]
    	assert(result[-1] == correct_lat_value)




if __name__ == '__main__':
    unittest.main()


# In[ ]:



