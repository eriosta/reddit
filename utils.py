def get_comments(comments_dict, comments_id):
    """
    This function takes a dictionary of comments and a list of comment ids,
    and returns a list of comments that match the given ids.

    Parameters:
    comments_dict (dict): A dictionary of comments.
    comments_id (list): A list of comment ids.

    Returns:
    list: A list of comments that match the given ids.
    """
    comments = []
    for comment in comments_dict:
        if comment['id'] in comments_id:
            comments.append(comment['body'])
    return comments
