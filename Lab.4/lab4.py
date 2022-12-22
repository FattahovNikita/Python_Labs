import requests
from bs4 import BeautifulSoup
from sklearn import datasets
from functools import reduce


num_list = [1, 2, 3, 4, 5]
print(num_list)
print(list(map(lambda x: x * 2, num_list)))
print(reduce(lambda x, y: x + y, num_list))