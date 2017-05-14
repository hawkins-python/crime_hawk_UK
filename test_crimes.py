
# coding: utf-8

# In[1]:

import unittest


from long_lat_from_postcode import long_lat

class LongLatTestCase(unittest.TestCase):
    ''' test for long_lat_from_postcode.py'''
    
    def test_get_correct_Long_Lat(self):
        ''' do I get [-0.125668386000805, 51.506582950758] for this postcode?'''
        correct_postcode = [-0.125668386000805, 51.506582950758]
        
        postcode = 'SW1A2HJ'
        result = long_lat(postcode)
        post_result = result.find_long_lat()
        assert(post_result == correct_postcode)

        
if __name__ == '__main__':
    unittest.main()


# In[ ]:



