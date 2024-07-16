listings['price'] = listings['price'].replace('[/$,]','',regex = True).astype(float)
superhost_neighbourhood = listings[listings['host_is_superhost'] == 't']
non_superhost_neighbourhood = listings[listings['host_is_superhost'] == 'f']
superhost_neighbourhood_price_median = superhost_neighbourhood.groupby("neighbourhood_cleansed")['price'].median().reset_index()
superhost_non_neighbourhood_price_median = non_superhost_neighbourhood.groupby("neighbourhood_cleansed")['price'].median().reset_index()



merged = pd.merge(superhost_neighbourhood_price_median,superhost_non_neighbourhood_price_median, on = "neighbourhood_cleansed", suffixes=["_neigh","_non_neigh"])
merged['price_diff'] = (merged['price_neigh'] - merged['price_non_neigh']).abs()

merged.loc[merged['price_diff'].idxmax()]
merged.head()


import pandas as pd

# Assuming listings DataFrame is already loaded
# listings = pd.read_csv('listings.csv')

# Remove dollar sign and commas, then convert to float
listings['price'] = listings['price'].replace('[\$,]', '', regex=True).astype(float)

# List of review score columns
review_columns = [
    'review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness',
    'review_scores_checkin', 'review_scores_communication', 'review_scores_location', 'review_scores_value'
]

# Fill missing values with the mean of each column
listings[review_columns] = listings[review_columns].fillna(listings[review_columns].mean())

# Calculate the correlation matrix for price and review score columns
correlation_matrix = listings[['price'] + review_columns].corr()

# Extract the correlation values for the 'price' column with review score columns
price_correlations = correlation_matrix['price'][review_columns]

# Find the review score column with the highest correlation to price
highest_correlation = price_correlations.idxmax()
highest_correlation_value = price_correlations.max()

print(f"The review score with the highest correlation to price is: {highest_correlation}")
print(f"The correlation value is: {highest_correlation_value}")