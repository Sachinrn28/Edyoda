#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
data = {
    'ship_mode': ["Same Day", "First Class", "Standard Class", "Second Class", "Same Day"],
    'sales': [100, 200, 150, 120, 180],
    'profit': [10, 20, 15, 12, 18]
}

df = pd.DataFrame(data)
print(df)

def calculate_surcharge(ship_mode):
    if ship_mode == "Same Day":
        return 0.2
    elif ship_mode == "First Class":
        return 0.1
    elif ship_mode == "Standard Class":
        return 0.05
    else:
        return 0

df['surcharge'] = df['ship_mode'].apply(calculate_surcharge)

df['total_cost'] = (df['sales'] - df['profit']) * (1 + df['surcharge'])

print('-'*50)


print(df)

