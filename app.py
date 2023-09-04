import streamlit as st
import pandas as pd
import json

from utils import get_comments

# Load JSON data
uploaded_file = st.sidebar.file_uploader("Choose a JSON file or use the default", type="json")
if uploaded_file is not None:
    data = json.load(uploaded_file)
else:
    with open('reddit_dummy_data.json') as f:
        data = json.load(f)

# Create a list of subreddit names
subreddits = list(data.keys())

# Create a sidebar for subreddit selection
subreddit = st.sidebar.selectbox('Choose a subreddit', subreddits)

# Display the selected subreddit
st.title(f'Selected subreddit: {subreddit}')

# Get the posts from the selected subreddit
posts = data[subreddit]

# Create a list of post ids
post_ids = [post['id'] for post in posts]

# Create a sidebar for post selection
post_id = st.sidebar.selectbox('Choose a post', post_ids)

# Get the selected post
post = next(post for post in posts if post['id'] == post_id)

# Display the selected post
st.subheader('Selected post:')
st.write(post['selftext'])

# Get the comments from the selected post
comments_id = post['_comments_by_id']
comments = get_comments(post['comments'], comments_id)

# Display the comments
st.subheader('Comments:')
for comment in comments:
    st.write(comment['body'])
