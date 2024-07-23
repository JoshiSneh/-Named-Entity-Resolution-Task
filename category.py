import re

# Function to normalize product_category_tree
def normalize_category_tree(category_tree):
    if pd.isna(category_tree):
        return ''
    # Remove special characters and whitespace
    category_tree = re.sub(r'[\[\]\']', '', category_tree)
    # Split categories by separator
    categories = category_tree.split('>>')
    # Strip whitespace and lowercase
    categories = [category.strip().lower() for category in categories]
    return ' >> '.join(categories)

# Apply the normalization function to both datasets
amazon_data['normalized_category'] = amazon_data['product_category_tree'].apply(normalize_category_tree)
flipkart_data['normalized_category'] = flipkart_data['product_category_tree'].apply(normalize_category_tree)

# Display the normalized categories
print(amazon_data[['uniq_id', 'normalized_category']].head())
print(flipkart_data[['uniq_id', 'normalized_category']].head())



# Function to extract the top-level category
def extract_top_level_category(normalized_category):
    if not normalized_category:
        return ''
    top_level_category = normalized_category.split(' >> ')[0]
    return top_level_category

# Extract top-level category for both datasets
amazon_data['top_level_category'] = amazon_data['normalized_category'].apply(extract_top_level_category)
flipkart_data['top_level_category'] = flipkart_data['normalized_category'].apply(extract_top_level_category)

# Display the top-level categories
print(amazon_data[['uniq_id', 'top_level_category']].head())
print(flipkart_data[['uniq_id', 'top_level_category']].head())
