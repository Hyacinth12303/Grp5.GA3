# -*- coding: utf-8 -*-
"""Grp5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mi81r81MbTI1uehzA53NHGIwmhNy9XLA"""

#loading the necessities




# imports
import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

# Set seaborn styles
sns.set_theme(style="whitegrid", palette="pastel")
sns.set_palette("Set2")

# Clear annoying package and version warnings
import warnings
warnings.filterwarnings('ignore')

#get the file
#from google.colab import drive
#drive.mount('/content/drive')

st.title("Group 5 - BM7")

st.write("Bagoyos, Ira Louise B.")

st.write("Ramos, Louella Amor C.")

st.write("Reyes, Joanna Hyacinth M.")

df = pd.read_csv("Electronic_sales_Sep2023-Sep2024.csv")

df #access the csv file

st.header("Describing the Dataset")

df.info()

st.write("This dataset contains 20000 customer's ID, purchase information, their purchases and their ratings")

df.isna().sum()

st.write("This table shows how many either didn't disclose their gender or if they purchased any add-ons. So far, there's only 1 who didn't disclose their gender and 4868 people didn't purchase add-ons.")

df.describe()

st.write("The categorical values are Gender, Loyalty Member, Product Type, SKU, Order Status, Payment Method, Shipping Type, Purchase Date, Add-ons Purchased.")

st.write("The numerical values are Age, Rating, Total Price, Unit Price, Quantity, Add-on Total.")

df['Gender'].value_counts()

df['Loyalty Member'].value_counts()

df['Product Type'].value_counts()

df['SKU'].value_counts()

df['Order Status'].value_counts()

df['Payment Method'].value_counts()

df['Shipping Type'].value_counts()

df['Purchase Date'].value_counts()

df['Add-ons Purchased'].value_counts()

st.markdown("**[Reyes]** - Product Type Popularity by Gender")

def ProdGender():
  product_index = df.groupby(['Product Type', 'Gender'])['Gender'].count().reset_index(name='index')
  fig, ax = plt.subplots()
  sns.barplot(x='Product Type', y='index', hue='Gender', data=product_index, palette={"Male": "lightblue", "Female": "pink"}, ax=ax)
  ax.set_title('Product Type Popularity by Gender')
  ax.set_xlabel('Product Type')
  ax.set_ylabel('Number of Purchases')
  st.pyplot(fig)
ProdGender()

"""This shows that there are more people who prefers purchasing Smartphones the most while Headphones the least. It also shows that more men buy the products than women with a slight difference.
"""
st.markdown("**[Reyes]** - Ratings by Product Type")

def ProdRatings():
  ProdRate = df.groupby(['Product Type', 'Rating'])['Rating'].count().reset_index(name='count')
  fig, ax = plt.subplots()
  sns.barplot(x='Product Type', y='count', hue='Rating', data=ProdRate, ax=ax)
  ax.set_title('Ratings by Product Type')
  ax.set_xlabel('Product Type')
  ax.set_ylabel('Number of Ratings')
  st.pyplot(fig)

ProdRatings()

"""In this graph, it shows that Laptop, Smartwatch and Tablet had a rating of 3 stars the most, while the Smartphone has a mix of 2 and 5 star ratings. There are also more people who rated 2 stars more than 5 stars from purchasing the Smartphone."""

st.markdown("**[Ramos]** - Percentages of Male and Female Loyalty Members")

def pie_chart(gender, colors, title):
  loyalty_member = gender['Loyalty Member'].value_counts()
  plt.pie(loyalty_member, labels=loyalty_member.index, colors=colors, autopct='%1.2f%%')
  plt.title(title)
  #plt.show()
  st.pyplot(plt)
  plt.clf()

gender_male = df[df['Gender']=='Male']
color_male = ['steelblue', 'skyblue']
title_male = 'Percentage of Male Loyalty Members'

gender_female = df[df['Gender']=='Female']
color_female = ['pink', 'salmon']
title_female = 'Percentage of Female Loyalty Members'

pie_chart(gender_male, color_male, title_male)
pie_chart(gender_female, color_female, title_female)

st.write("As can be seen in these pie charts, the percentages of male and female loyalty members are almost exactly similar, with there being 21.67% and 21.75% loyalty members in male and female demographics respectively.")

st.markdown("**[Ramos]** - Total Price by Age")

def scatter_plot():
    plt.scatter(x=df['Age'], y=df['Total Price'], alpha=0.2)
    plt.title('Total Price by Age')
    plt.xlabel('Age')
    plt.ylabel('Total Price')
    #plt.show()
    st.pyplot(plt)
    plt.clf()

scatter_plot()

st.write("As can be seen in the scatter plot, age seems to not have much effect on the total price spent by a customer as the distribution of total price spent seems quite even among all ages.")

"""**[Bayogos]** - Piechart of Shipping Distribution
"""

def pie():
  shipping_counts = df['Shipping Type'].value_counts()
  plt.pie(shipping_counts, labels=shipping_counts.index, autopct='%1.1f%%', startangle=90)
  plt.title('Shipping Type Distribution')
  plt.show()
pie()

"""The pie chart shows majority of the Shipping Type used in the dataset was the Standard form of delivery with a percentage of 33.6%, while the other methods for shipping are nearly equally distributed to 16%.

**[Bayogos]** - Price of Product Type
"""

def violin():
  sns.violinplot(x='Product Type', y='Total Price', data=df)
  plt.title('Distribution of Total Price by Product Type')
  plt.xlabel('Product Type')
  plt.ylabel('Total Price')
  plt.show()

violin()

"""This violin graph shows the distribution of the total price for each product. The wider sections indicate a high concentration of that product, shown to be more common within the lower price range. When counting in the narrower peaks, it is revealed that smartphones and smartwatch have a variety with their models, while tablets and headphones are more concentrated."""

st.header("Conclusion")

st.markdown("""

1. Observations by Gender
  *   Slightly more men buy products than women.
  *   By percentage, slightly more women are loyalty members than men.

2. Observations by Product Type
  * People prefer purchasing smartphones the most while headphones the least.
  * In connection to that, smartphone purchases have the most variety in total price spent, and headphones the least.
  * Laptops, smartwatch and tablet are rated 3 stars most frequently, while the smartphone was most frequently rated 2 stars or to a slightly lesser degree, 5 stars.

3. Observation by Age

    Age seems to not have much effect on the total price spent by a customer; every age seem likely to spend at a very wide price range.

4. Observation by Shipping Type

    Majority of the Shipping Type used by customers was the Standard form of delivery, while the other methods for shipping are nearly equally distributed.

""")
