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
    for comment_id in comments_id:
        if comment_id in comments_dict:
            comments.append(comments_dict[comment_id]['body'])
    return comments

