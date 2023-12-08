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
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris_df = sns.load_dataset('iris')

# Streamlit app title
st.title("Iris Data Exploration App")

# Sidebar with user inputs
st.sidebar.header("Select Species")
selected_species = st.sidebar.selectbox("Choose a species:", iris_df['species'].unique())

# Filter the data based on the selected species
selected_data = iris_df[iris_df['species'] == selected_species]

# Display descriptive statistics
st.write(f"### Descriptive Statistics for {selected_species} Species:")
st.write(selected_data.describe())

# Display a pair plot of features
st.write(f"### Pair Plot for {selected_species} Species:")
sns.pairplot(selected_data, hue='species')
st.pyplot()

# Display a correlation heatmap
st.write("### Correlation Heatmap:")
correlation_matrix = selected_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
st.pyplot()

# Additional content (optional)
st.markdown("---")
st.write("Explore the Iris dataset by selecting different species.")

# Show the app
if __name__ == "__main__":
    st.sidebar.markdown("[![View on GitHub](https://img.shields.io/badge/View%20on%20GitHub--blue?logo=github)](https://github.com/yourusername/your-repo)")
