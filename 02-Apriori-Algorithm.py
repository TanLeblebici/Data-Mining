#!/usr/bin/env python
# coding: utf-8

# # 1. Setting up installing and importing libraries

# In[1]:


get_ipython().system('pip install apyori')


# In[2]:


import pandas as pd


# # 2. Load and preprocess data

# In[3]:


raw_data = pd.read_csv('example1.csv', header = None)
#df = raw_data.copy()
#df.head(10)


# In[4]:


#df.info()


# In[5]:


transactions = [] # to hold non NaN values


# In[6]:


for index, row in raw_data.iterrows(): # Iterating over each row in the raw data
    transaction = []
    for item in row: # Iterating over each item in the row
        if pd.notnull(item): # Checking if the item is not NaN
            transaction.append(item) # Appending non-NaN item to the transaction list
    transactions.append(transaction) # Appending the transaction to the list of transactions


# In[7]:


transactions[1]


# # 3. Import apyori and apply apriori algorithm

# In[8]:


from apyori import apriori


# In[9]:


# Applying the Apriori algorithm to find association rules
rules = apriori(transactions, 
                min_support = 0.003, # Minimum support threshold
                min_confidence = 0.2, # Minimum confidence threshold
                min_lift = 3, # Minimum lift threshold
                min_length = 2, # Minimum number of items in a rule
                max_length =2) # Maximum number of items in a rule


# In[10]:


type(rules)


# In[11]:


results = list(rules) # Converting the rules into a list


# In[12]:


results


# In[13]:


results[0][1]


# In[14]:


tuple(results[0][2][0])[0]


# # 4. Convert the rules in a meaningful format

# In[15]:


# Extracting the antecedents (left hand side), consequents (right hand side),
# support, confidence, and lift for each rule
def convert_dataFrame(results):
    lhs = [tuple(result[2][0][0])[0] for result in results]
    rhs = [tuple(result[2][0][1])[0] for result in results]
    supports = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts = [result[2][0][3] for result in results]
    # Returning a list of tuples containing the extracted information for each rule
    return list(zip(lhs,rhs,supports,confidences,lifts)) 


# In[16]:


resultFrame = pd.DataFrame(convert_dataFrame(results),columns = ["Left Hand Side","Right Hand Side","Support","Confidence","Lift"])


# In[17]:


resultFrame.nlargest(n = 10, columns = "Lift")

