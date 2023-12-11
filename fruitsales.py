import pandas as pd 

# Creating a dictionary with the sales data
data = {
    'Apples': [35, 41],
    'Bananas': [21, 34]
}

# Creating a DataFrame from the dictionary
file = pd.DataFrame(data, index=['2017 Sales', '2018 Sales'])

file.to_csv('fruit.csv')
