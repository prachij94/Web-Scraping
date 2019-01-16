# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 09:50:26 2018

@author: Prachi Jain
"""

from amazon.api import AmazonAPI
import bottlenose.api
region_options = bottlenose.api.SERVICE_DOMAINS.keys()

#Associates earn commissions by using their own websites to refer sales to Amazon.com. To get a commission, an Associate must have an Associate ID, also known as an Associate tag. The Associate ID is an automatically generated unique identifier that you will need to make requests through the Product Advertising API.
amazon_india = AmazonAPI('AKIA5AWST4BD3KUHYHMZ', '4eP/suPV4pI8EZLhqelKoq2+DfsM485z2/WwWqaU', 'indiamartcate-21', region="IN")
product = amazon_india.lookup(ItemId='B01ETPUQ6E')
product.title
product.price_and_currency