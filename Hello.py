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
from datetime import datetime

def get_greeting_style(greeting_style):
    if greeting_style == "Friendly":
        return "Hello"
    elif greeting_style == "Formal":
        return "Greetings"
    else:
        return "Hey"

# Streamlit app title
st.title("Advanced Greeting App")

# Sidebar with user inputs
st.sidebar.header("User Inputs")
user_name = st.sidebar.text_input("Enter your name:")
birth_date = st.sidebar.date_input("Your birthdate:")
age = st.sidebar.slider("Your age:", min_value=0, max_value=100, value=25)
greeting_style = st.sidebar.radio("Greeting Style:", ["Friendly", "Formal", "Casual"])

# Calculate age
if birth_date:
    today = datetime.now().date()
    age = (today - birth_date).days // 365

# Button to trigger the greeting
if st.sidebar.button("Generate Greeting"):
    # Get the selected greeting style
    style = get_greeting_style(greeting_style)

    # Display a personalized greeting message
    st.write(f"{style}, {user_name}! 🎉")
    st.write(f"I see you're {age} years old.")

    # Additional content based on age
    if age < 18:
        st.write("You're still young! 🌟")
    elif age > 60:
        st.write("Enjoy your golden years! 🌅")
    else:
        st.write("Hope you're having a great day!")

# Additional content (optional)
st.markdown("---")
st.write("This is an advanced Streamlit application with more features.")


