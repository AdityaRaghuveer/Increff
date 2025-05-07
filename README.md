# Increff
The Increff web application provides users with an interactive FAQ chatbot to answer common questions related to product returns, order tracking, payment methods, and smartphone warranties. It is built using Flask, a lightweight Python web framework, and integrates a chatbot for real-time responses. The main goal of the project is to provide quick and automated responses to users' questions.

## Features

### 1. **Chatbot Integration**
- The chatbot listens for user input (i.e., questions) and generates responses based on predefined FAQ data.
- The chatbot provides answers related to topics such as return policy, order tracking, payment methods, and warranties.

### 2. **Flask Backend**
- The app is built using Flask, which handles HTTP requests and renders templates for the front-end.
- When a user submits a question via the form, a `POST` request is sent to the Flask backend.
- The backend processes the input using the chatbot's logic to generate the appropriate answer.

### 3. **.env Configuration**
- Sensitive environment variables, like API keys, are stored in the `.env` file, keeping them secure.
- The `.env` file includes the `OPENAI_API_KEY`, which is used to connect to an API (such as OpenAI) for advanced chatbot functionalities.

### 4. **Dynamic Query Handling**
- Users can type their questions in the text box on the frontend. When the form is submitted, the backend processes the query.
- The response from the chatbot is dynamically displayed on the page.

### there is some issue going ,the API key isnt properly invoked and the application doesnt seem to work properly . 

## within .env file i wrote API key and within .gitignore i have included that file as it is secret key .


## Dependencies

To run this project, you'll need the following dependencies:

1. **Flask**: A lightweight Python web framework used to build the backend.
2. **Flask-Cors**: Provides Cross-Origin Resource Sharing (CORS) support for handling requests from different origins.
3. **python-dotenv**: Loads environment variables from a `.env` file for secure handling of sensitive data.
4. **openai**: The official Python client for interacting with the OpenAI API.

You can install these dependencies by running the following command in your terminal:

```bash
pip install -r requirements.txt

and to run , clone the repo , set up environment 
python -m venv venv
venv\Scripts\activate

and go to project folder(increff) and python app.py 

 
