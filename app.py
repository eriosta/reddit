import streamlit as st
import pandas as pd
import json

from utils import get_comments

# Load JSON data
with open('reddit_data.json') as f:
    data = json.load(f)

# Create a list of subreddit names
subreddits = list(data.keys())

# Create a sidebar for subreddit selection
subreddit = st.sidebar.selectbox('Choose a subreddit', subreddits)

# Display the selected subreddit
st.title(f'Selected subreddit: {subreddit}')

# Get the posts from the selected subreddit
posts = data[subreddit]['posts']

# Create a list of post ids
post_ids = [post['id'] for post in posts]

# Create a sidebar for post selection
post_id = st.sidebar.selectbox('Choose a post', post_ids)

# Get the selected post
post = next(post for post in posts if post['id'] == post_id)

# Display the selected post
st.subheader('Selected post:')
st.write(post['freetext'])

# Get the comments from the selected post
comments_id = post['comments_id']
comments = get_comments(data[subreddit]['comments'], comments_id)

# Display the comments
st.subheader('Comments:')
for comment in comments:
    st.write(comment)
