# QA-chatbot-using-llm
Chat--bot-using-LLM
This project is a Question-Answering (QA) chatbot that utilizes Weaviate, a vector search engine, to interact with users, answer their questions, and provide relevant information. The chatbot uses Natural Language Processing (NLP) to understand user queries and provide accurate responses.

Features User registration and login Question-answering capabilities Integration with Weaviate for data storage and retrieval User profile management Files and Directories addingData.py This script handles the addition of data to the system. It manages the input and storage of knowledge base entries and user details in Weaviate.

askingques.py This script is responsible for processing user queries and generating responses. It uses NLP techniques to understand the questions and provide relevant answers.

vecDBManager.py This script manages the vector database operations in Weaviate, ensuring efficient data storage, retrieval, and query processing

Overview This document outlines the steps to extract text from a PDF file and upload it to a Weaviate database using a Python script.

Prerequisites Python installed on your machine. pip (Python Package Installer). PDF file ready for uploading. Access to a Weaviate instance and relevant authentication credentials. Step-by-Step Guide

Install Required Packages Open your terminal or command prompt and run the following command to install the necessary Python packages:
sh Copy code pip install pypdf2 weaviate-client 2. Set Up Project Directory Create a project directory and navigate into it:

sh Copy code mkdir pdf-to-weaviate cd pdf-to-weaviate 3. Add Your PDF File Place your PDF file (e.g., stephen_hawking_a_brief_history_of_time.pdf) into the project directory.

Create Python Script Create a Python script file (e.g., upload_pdf_to_weaviate.py) in your project directory. This script will handle the extraction of text from the PDF and upload it to Weaviate.

Prepare Weaviate Instance Ensure you have access to a Weaviate instance. You will need:

Cluster URL Authentication credentials (e.g., API key) 6. Run the Python Script Open the terminal or command prompt and navigate to your project directory. Execute the Python script to extract text from the PDF and upload it to Weaviate: sh Copy code python upload_pdf_to_weaviate.py 7. Verify Upload Check your Weaviate dashboard or use the Weaviate client to query the uploaded data and ensure it has been successfully stored.

Troubleshooting Missing Packages: Ensure all required packages are installed using pip install pypdf2 weaviate-client. Authentication Errors: Verify your Weaviate instance URL and authentication credentials. PDF Extraction Issues: Check the integrity of your PDF file and make sure it is not corrupted.
