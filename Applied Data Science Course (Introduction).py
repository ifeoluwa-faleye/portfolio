#!/usr/bin/env python
# coding: utf-8

# # **Tabular Data and Python Data Structures**

# ## Working With Lists
# Python comes with several data structures that we can use to organize tabular data. Let's start by putting a single observation in a **list**

# In[1]:


# Declare variable 'house_0_list'
house_0_list = [115910.26, 128, 4]

#Print object type of 'house_0_list'
print("Object type of house_0_list:", type(house_0_list))

#Print the lenght of 'house_0_list'
print("The lenght of house_0_list:", len(house_0_list))

#Get the output of 'house_0_list'
house_0_list


# **Task 1.1.1** One metric that people in the real estate industry look at is price per square meter because it allows them to compare houses of different sizes. Can you use the information in this list to calculate the price per square meter for `house_0`?
# 
# -[What is a list](https://www.w3schools.com/python/python_lists.asp#:~:text=Lists%20are%20used%20to%20store,with%20different%20qualities%20and%20usage.)

# In[2]:


#Declear variable 'house_0_list_m2'
house_0_list_m2 = house_0_list[0]/house_0_list[1]

#Print object type of 'house_0_list_m2'
print("Object type of house_0_list_m2:", type(house_0_list_m2))

#Get the output of 'house_0_list_m2'
house_0_list_m2


# **Task 1.1.2** Next, use the *append* method to add the price per square meter to the end of the end of *house_0_list*

# In[3]:


# Append price / sq. meter to `house_0_list`
house_0_list.append(house_0_list_m2)

# Print object type of `house_0_list`
print("house_0_list type:", type(house_0_list))

# Print length of `house_0_list`
print("house_0_list length:", len(house_0_list))

# Get output of `house_0_list`
house_0_list


# Now that you can work with data for a single house, let's think about how to organize the whole dataset. One option would be to create a list for each observation and then put those together in another list. This is called a *nested list.*

# In[4]:


#Declare variable 'houses_nested_list'
houses_nested_list = [
    [115910.26, 128.0, 4.0],
    [48718.17, 210.0, 3.0],
    [28977.56, 58.0, 2.0],
    [36932.27, 79.0, 3.0],
    [83903.51, 111.0, 3.0]
]

# Print `houses_nested_list` type
print("houses_nested_list type:", type(houses_nested_list))

# Print `houses_nested_list` length
print("houses_nested_list length:", len(houses_nested_list))

# Get output of `houses_nested_list`
houses_nested_list


# Now that we have more observations, it doesn't make sense to calculate the price per square meter for each house one-by-one. Instead, we can automate this repetitive task using a *for* loop.

# **Task 1.1.3:** Append the price per square meter to each observation in `houses_nested_list` using a `for` loop.
# 
# - [What's a for loop?](../%40textbook/01-python-getting-started.ipynb#Python-for-Loops)
# - [Write a for loop in Python.](../%40textbook/01-python-getting-started.ipynb#Working-with-for-Loops)

# In[5]:


for house in houses_nested_list:
    print(house)


# In[6]:


for house in houses_nested_list:
    price_m2 = house[0]/house[1]
    house.append(price_m2)
    
houses_nested_list


# # Working With Dictionaries

# Lists are a good way to organize data, but one drawback is that we can only represent values. Why is that a problem? For example, someone looking at `[115910.26, 128.0, 4]` wouldn't know which values corresponded to price, area, etc. A better option might be a [**dictionary**](http://127.0.0.1:8888/lab/tree/work/ds_curriculum/%40textbook/Python.ipynb#whats-a-dictionary), where each value is associated with a key. Here's what `house_0` looks like as a dictionary instead of a list.

# In[7]:


# Declare variable house_0_dict
house_0_dict = {
    "price_approx_usd": 115910.26,
    "surface_covered_in_m2": 128,
    "rooms": 4,
}
# Print `house_0_dict` type
print("house_0_dict type:", type(house_0_dict))

# Get output of `house_0_dict`
house_0_dict


# In[8]:


house_0_dict["price_approx_usd"]


# In[9]:


# Add "price_per_m2" key-value pair to `house_0_dict`
house_0_dict["price_per_m2"] = house_0_dict["price_approx_usd"]/house_0_dict["surface_covered_in_m2"]

# Get output of `house_0_dict`
house_0_dict


# In[10]:


# Declare variable `houses_rowwise`
houses_rowwise = [
    {
        "price_approx_usd": 115910.26,
        "surface_covered_in_m2": 128,
        "rooms": 4,
    },
    {
        "price_approx_usd": 48718.17,
        "surface_covered_in_m2": 210,
        "rooms": 3,
    },
    {
        "price_approx_usd": 28977.56,
        "surface_covered_in_m2": 58,
        "rooms": 2,
    },
    {
        "price_approx_usd": 36932.27,
        "surface_covered_in_m2": 79,
        "rooms": 3,
    },
    {
        "price_approx_usd": 83903.51,
        "surface_covered_in_m2": 111,
        "rooms": 3,
    },
]

# Print `houses_rowwise` object type
print("houses_rowwise type:", type(houses_rowwise))

# Print `houses_rowwise` length
print("houses_rowwise length:", len(houses_rowwise))

# Get output of `houses_rowwise`
houses_rowwise


# **Task 1.1.5:** Using a `for` loop, calculate the price per square meter and store the result under a `"price_per_m2"` key for each observation in `houses_rowwise`.
# 
# - [What's JSON?](../%40textbook/01-python-getting-started.ipynb#JSON)
# - [Write a for loop in Python.](../%40textbook/01-python-getting-started.ipynb#Working-with-for-Loops)

# In[11]:


# Create for loop to iterate through `houses_rowwise`
for house in houses_rowwise:
    house["price_per_m2"] = house["price_approx_usd"]/house["surface_covered_in_m2"]
    # For each observation, add "price_per_m2" key-value pair
    

# Print `houses_rowwise` object type
print("houses_rowwise type:", type(houses_rowwise))

# Print `houses_rowwise` length
print("houses_rowwise length:", len(houses_rowwise))

# Get output of `houses_rowwise`
houses_rowwise


# **Task 1.1.6:** To calculate the mean price for `houses_rowwise` by completing the code below.
# 
# - [Write a for loop in Python.](../%40textbook/01-python-getting-started.ipynb#Working-with-for-Loops)
# - [Append an item to a list in Python.](../%40textbook/01-python-getting-started.ipynb#Appending-Items)

# In[12]:


# Declare `house_prices` as empty list
house_prices = []
for house in houses_rowwise:# Iterate through `houses_rowwise`
    house_prices.append(house["price_approx_usd"])    # For each house, append "price_approx_usd" to `house_prices`

# Calculate `mean_house_price` using `house_prices`
mean_house_price = sum(house_prices) / len(house_prices)

# Print `mean_house_price` object type
print("mean_house_price type:", type(mean_house_price))

# Get output of `mean_house_price`
mean_house_price


# One way to make this sort of calculation easier is to organize our data by features instead of observations. We'll still use dictionaries and lists, but we'll implement them a slightly differently.

# In[13]:


# Declare variable `houses_columnwise`
houses_columnwise = {
    "price_approx_usd": [115910.26, 48718.17, 28977.56, 36932.27, 83903.51],
    "surface_covered_in_m2": [128.0, 210.0, 58.0, 79.0, 111.0],
    "rooms": [4.0, 3.0, 2.0, 3.0, 3.0],
}

# Print `houses_columnwise` object type
print("houses_columnwise type:", type(houses_columnwise))

# Get output of `houses_columnwise`
houses_columnwise


# **Task 1.1.7:** Calculate the mean house price in `houses_columnwise`
# 
# - [Perform common aggregation tasks on a list in Python.](../%40textbook/01-python-getting-started.ipynb#Aggregating-Items)

# In[14]:


# Calculate `mean_house_price` using `houses_columnwise`
mean_house_price = sum(houses_columnwise["price_approx_usd"])/len(houses_columnwise["price_approx_usd"])

# Print `mean_house_price` object type
print("mean_house_price type:", type(mean_house_price))

# Get output of `mean_house_price`
mean_house_price


# Of course, when we organize our data according to columns / features, row-wise operations become more difficult.

# In[15]:


# Add "price_per_m2" key-value pair for `houses_columnwise`
price = houses_columnwise["price_approx_usd"]
area = houses_columnwise["surface_covered_in_m2"]
price_per_m2 = []
for i,j in zip(price, area):
    price_m2 = i/j
    price_per_m2.append(price_m2)

houses_columnwise["price_per_m2"] = price_per_m2

# Print `houses_columnwise` object type
print("houses_columnwise type:", type(houses_columnwise))

# Get output of `houses_columnwise`
houses_columnwise


# # Tabular Data and pandas DataFrames

# While you've shown that you can wrangle data using lists and dictionaries, it's not as intuitive as working with, say, a spreadsheet. Fortunately, there are lots of libraries for Python that make it an even better tool for tabular data — way better than spreadsheet applications like Microsoft Excel or Google Sheets! One of the best known data science libraries is **pandas**, which allows you to organize data into **DataFrames**.
# 
# Let's import pandas and then create a DataFrame from `houses_columnwise`.

# In[ ]:




