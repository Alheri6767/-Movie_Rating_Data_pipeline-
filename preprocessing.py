#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd

# Step 1: Load raw dataset
df = pd.read_csv("netflix_titles.csv")
print(df.head())


# In[43]:


# check for missing data on the dataset 
print(df.isnull().sum())


# In[44]:


# Handling missing data in  netflix dataset
# Fill missing 'director' and 'cast' with 'Unknown'
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")

# Fill missing 'country' with 'Unknown'
df['country'] = df['country'].fillna("Unknown")

# Convert 'date_added' to datetime, fill missing with default date
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['date_added'] = df['date_added'].fillna(pd.Timestamp("2000-01-01"))

# Fill missing 'rating' with the most frequent rating (mode)
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])

# Fill missing 'duration' with 'Unknown'
df['duration'] = df['duration'].fillna("Unknown")
df = df.where(pd.notnull(df), None)


# In[19]:


# ✅ Data Cleaning Before Insert

# 1. Remove spaces from titles
df['title'] = df['title'].str.strip()

# 2. Convert 'type' column to lowercase
df['type'] = df['type'].str.lower()

# 3. Remove duplicate rows
df = df.drop_duplicates()

# 5. Replace ALL NaT / NaN across the entire DataFrame with None
df = df.where(pd.notnull(df), None)

# 6. Build records safely
records = [tuple(row) for _, row in df.iterrows()]

print(df.head())



# In[45]:


print(df.info())
print(df.head())


# In[46]:


#rename column name from cast to casts 
df.rename(columns={"casts": "cast"}, inplace=True)




# In[47]:


print(df.columns.tolist())


# In[7]:


print(df.head(10))


# In[52]:


# Ensure 'date_added' is datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Replace NaT with None for Postgres
df['date_added'] = df['date_added'].apply(lambda x: None if pd.isna(x) else x)


# In[48]:


import pandas as pd
import psycopg2
from psycopg2.extras import execute_batch

# Load CSV
df = pd.read_csv("netflix_titles.csv")


# 4. Reorder columns to match your table definition
df = df[["show_id", "type", "title", "director", "cast", "country",
         "release_year", "rating", "duration", "listed_in", "description"]]

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="ETL",
    user="postgres",
    password="5925",
    host="localhost",
    port="5432"
)
cur = conn.cursor()
execute_batch(cur, """
    INSERT INTO netflix_titles 
    (show_id, "type", title, director, "cast", country, release_year, rating, duration, listed_in, description)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )
    ON CONFLICT (show_id) DO NOTHING;
""", records, page_size=1000)

conn.commit()
cur.close()
conn.close()

print("✅ Data inserted successfully!")


# In[49]:


expected_cols = ["show_id", "type", "title", "director", "casts", "country", 
                 "date_added", "release_year", "rating", "duration", "listed_in", "description"]

print("Match:", list(df.columns) == expected_cols)


# In[ ]:




