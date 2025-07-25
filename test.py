#!/usr/bin/env python

# import pandas as pd
# data = pd.read_csv("./USA_Housing.csv");
# y = data["Price"] * 84;
#
# print(y[1]);
# print(data["Price"][1]);


import os

sec_key = os.getenv("DJANGO_SECRET_KEY");

print(sec_key);
