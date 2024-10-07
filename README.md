# Electronic sales Analysis Project
## Team Members
- Bayogos, Ira Louise B. - 2021105633 - IraBrazil
- Ramos, Louella Amor C. - StudNo - lacramos
- Reyes, Joanna Hyacinth M. - 2020116410 - Hyacinth12303
## Overview
This  project provides a comprehensive analysis of customer purchases from an electronics sales dataset spanning from September 2023 to September 2024. The analysis includes insights into product preferences, customer demographics, purchase behaviors, and ratings. The dataset contains 20,000 entries, capturing customer ID, demographic information, purchase details, ratings, and other factors relevant to the transactions.

## Dataset Description
The dataset contains the following features:
- **Categorical Variables**: Gender, Loyal Member, Product Type, SKU, Order Staus,Payment Method, Shipping Type, Purchase Date, Add-ons Purchased
- **Numerical Variables**: Age, Rating, Total Price, Unit Price, Quantity, Add-on Total

### Missing Data
- 1 customer did not disclose their gender
- 4,868 customers did not purchse any add-ons

### Libraries Used
The following Python libraries were used to clean, process, and visualize the dataset:
- **Streamlit**: For interactive web-based apps
- **Pandas**: For data manipulation and analysis
- **NumPy**: For numerical operations
- **Mathplotlib**: For data visualization and plotting

## Exploratory Data Analysis (EDA)
### Gender-Based Product Preferences
A bar plot visualizes product type popularity by gender. The analysis shows that:
- **Smartphones** are the most popular product overall.
- **Headphones** are the least popular.
### Ratings by Product Type
A bar plot visualizes customer ratings for each product type.
- **Laptops, Smartwatches, and Tablets**  are most often rated 3 stars.
- **Snartphones** receive mixed reviews, with many ratings of 2 and 5 stars.
### Loyalty Membership Distribution by Gender
Pie charts display the percentages of loyalty program participation for men and women. Both genders have almost identical percentages of loyalty membership.
- **Male**: 21.67%
- **Female**: 21.75%
### Total Price Spent by Age
A scatter plot shows that the total price spent by customers is evenly distributed across age groups, indicating that age does not significantly impact spending patterns.
### Shipping Type Distribution
- Standard Shipping is used by the majority (33.6%) of customers.
- Other shipping types are nearly equally distributed, each representing about 16% of the data.
### Total Price by Product Type
A violin plot visualizes the price distribution by product type:
- **Smartphones** and **Smartwatches** exhibit the most varied price ranges.
- **Headphones** and **Tablets** are more concentrated within lower price ranges.

## Key Insights
1. **Gender Differences**:
- Slightly more men purchase electronics than women.
- A marginally higher percentage of women are loyalty members compared to men.
2. **Product Preferences**:
- Smartphones are the most purchased product, followed by laptops.
- Laptops, smartwatches, and tablets are most commonly rated 3 stars.
- Smartphones have the widest price range, while headphones are the least expensive and least varied.
3. **Age and Price**:
- Customer age does not significantly affect spending; people of all ages tend to spend across a wide range of prices
4. **Shipping Preferences**:
- The majority of customers use standard shipping, with other methods equally divided.

## Running the Project
1. Install the required libraries:
```
pip install streamlit pandas mathplotlib seaborn
```
2. Load the dataset and run the analysis:
```
streamlit run app.py
```

## Visualizations
The program includes several visualizations such as bar plots, pie charts, scatter plots, and violin plots to showcase insights into customer behaviors and preferences.

## Conclusion
This program provides a deep dive into customer behaviors and trends in the electronics retail space. The insights can be valuable for the retailer to make data-driven decisions regarding product inventory, marketing strategies, and customer engagement initiatives, particularly focusing on product variety, customer satisfaction, and shipping optimization.
