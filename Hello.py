# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Generate sample data for an e-commerce product catalog
num_products = 50

categories = ["Electronics", "Clothing", "Books", "Home & Kitchen", "Toys"]
products = [
    f"Product-{i}" for i in range(1, num_products + 1)
]
prices = np.random.uniform(10, 200, num_products).round(2)
stock_quantities = np.random.randint(5, 100, num_products)

# Create a DataFrame
ecommerce_df = pd.DataFrame({
    'Product': products,
    'Category': np.random.choice(categories, num_products),
    'Price': prices,
    'Stock Quantity': stock_quantities
})

# Streamlit app title
st.title("E-commerce Product Explorer")

# Sidebar with user inputs
st.sidebar.header("Filter Products")
selected_category = st.sidebar.selectbox("Select a category:", ["All"] + categories)

# Filter the data based on the selected category
filtered_data = ecommerce_df if selected_category == "All" else ecommerce_df[ecommerce_df['Category'] == selected_category]

# Display filtered products
st.write(f"### {selected_category} Products:")
st.write(filtered_data)

# Display summary statistics
st.write("### Summary Statistics:")
st.write(f"Total Products: {len(filtered_data)}")
st.write(f"Average Price: ${filtered_data['Price'].mean():.2f}")
st.write(f"Total Stock Quantity: {filtered_data['Stock Quantity'].sum()}")

# Additional content (optional)
st.markdown("---")
st.write("Explore and filter e-commerce products based on categories.")

# Show the app
if __name__ == "__main__":
    st.sidebar.markdown("[![View on GitHub](https://img.shields.io/badge/View%20on%20GitHub--blue?logo=github)](https://github.com/yourusername/your-repo)")
