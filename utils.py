def get_comments(data, subreddit, post_id):
    """
    This function takes a dictionary of data, a subreddit, and a post id,
    and returns a list of comments that match the given post id in the given subreddit.

    Parameters:
    data (dict): A dictionary of data.
    subreddit (str): A subreddit.
    post_id (str): A post id.

    Returns:
    list: A list of comments that match the given post id in the given subreddit.
    """
    comments = []
    posts = data[subreddit]
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is not None:
        comments_id = post['_comments_by_id']
        for comment in post['comments']:
            if isinstance(comment, dict) and comment['id'] in comments_id:
                comments.append(comment['body'])
    return comments
