import pandas as pd
import timeit
from BTrees.OOBTree import OOBTree  # type: ignore


# Load and shuffle data from CSV file
items_df = pd.read_csv("src/chapter_03/generated_items_data.csv")

# Initialize OOBTree and dictionary
product_tree = OOBTree()
product_dict = {}

# Function to add items to OOBTree and dict
def add_item_to_tree(tree, item_id, item_data):
    tree[item_id] = item_data

def add_item_to_dict(dct, item_id, item_data):
    dct[item_id] = item_data

# Populate the structures with items from the dataframe
for _, row in items_df.iterrows():
    item_id = int(row["ID"])
    item_data = {"Name": row["Name"], "Category": row["Category"], "Price": row["Price"]}
    add_item_to_tree(product_tree, item_id, item_data)
    add_item_to_dict(product_dict, item_id, item_data)

# Optimized range query for OOBTree
def range_query_tree(tree, min_price, max_price):
    return [value for _, value in tree.items(min=min_price, max=max_price)]

# Range query for dict (linear scan)
def range_query_dict(dct, min_price, max_price):
    results = []
    for key, value in dct.items():
        if min_price <= value["Price"] <= max_price:
            results.append(value)
    return results

# Define a sample price range
min_price = 100
max_price = 300

# Measure range query performance for OOBTree and dict
results = {
    "OOBTree": timeit.timeit(
        'range_query_tree(product_tree, min_price, max_price)',
        globals=globals(), number=100
    ),
    "Dict": timeit.timeit(
        'range_query_dict(product_dict, min_price, max_price)',
        globals=globals(), number=100
    )
}

# Display results
for structure, time_taken in results.items():
    print(f"Total range_query time for {structure}: {time_taken:.6f} seconds")
