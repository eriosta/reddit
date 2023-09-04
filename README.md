# Reddit Post and Comment Search Tool

This project is a simple search tool for Reddit posts and their corresponding comments. It uses a JSON file as a data source, which contains a dictionary of two lists. The first list contains dictionaries, where each record is a post on Reddit. The main text for that post is in the field "freetext". Each post has responses/comments, and there's another field in that record called "comments_id" that has a list of all the ids for the corresponding comments. 

The second list is a dictionary of comments, where each comment's id matches the "comments_id" in the post record. The comment text is stored in the field "comment_text".

The search tool is a Streamlit app that allows you to choose a subreddit and view each post and its corresponding comments.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The project requires the following python libraries:

- streamlit==0.79.0
- pandas==1.2.3
- numpy==1.20.1
- requests==2.25.1
- json5==0.9.5

You can install these using pip:

```
pip install -r requirements.txt
```

### Running the App

To run the app, navigate to the project directory and run the following command:

```
streamlit run app.py
```

This will start the Streamlit server and open the app in your default web browser.

## Project Structure

The project has the following file structure:

- `requirements.txt`: Contains the python libraries required to run the app.
- `reddit_data.json`: The JSON data source for the app.
- `app.py`: The main Streamlit app.
- `utils.py`: Contains utility functions used by the app.
- `README.md`: This file, containing information about the project and instructions on how to run it.

## Authors

- Your Name

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
