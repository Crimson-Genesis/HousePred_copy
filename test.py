#!/usr/bin/env python

import pandas as pd

data = pd.read_csv("./USA_Housing.csv");
y = data["Price"] * 84;

print(y[1]);
print(data["Price"][1]);
