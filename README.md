# 💬 Customer Support Chatbot Using Retrieval-Augmented Generation (RAG)

## 📌 Project Overview

The Customer Support Chatbot is an AI-powered application built using **Retrieval-Augmented Generation (RAG)** to provide accurate and context-aware responses to customer queries.

The main objective of this project is to develop an intelligent customer support assistant that can understand user questions and retrieve relevant information from a predefined knowledge base before generating responses using a Large Language Model (LLM).

Instead of relying entirely on the LLM's pre-trained knowledge, the chatbot retrieves relevant information from uploaded documents and uses that context to generate meaningful answers.

The application is developed using **Python, LangChain, Ollama, and Streamlit**, providing an interactive interface for users to ask questions related to orders, accounts, refunds, shipping policies, and other customer support topics.

## 🎯 Project Objectives

- Build an intelligent customer support assistant using Generative AI.
- Implement Retrieval-Augmented Generation (RAG).
- Retrieve relevant information from documents using semantic search.
- Generate context-aware responses using a locally running LLM.
- Reduce incorrect or irrelevant responses by grounding answers in retrieved information.
- Develop an interactive chatbot interface using Streamlit.

## ⚙️ Technologies Used

- **Python:** Core programming language.
- **LangChain:** Framework for building the RAG pipeline.
- **Ollama:** Runs Large Language Models locally.
- **Qwen 2.5 (0.5B):** Lightweight LLM used for response generation.
- **Embeddings:** Convert document text into numerical representations.
- **Vector Database:** Stores document embeddings for similarity search.
- **Streamlit:** Builds the interactive web application.

## 🔄 Project Workflow

1. **Document Loading:** Load customer support documents containing relevant information.
2. **Text Splitting:** Divide documents into smaller chunks for efficient retrieval.
3. **Embedding Generation:** Convert text chunks into vector representations.
4. **Vector Storage:** Store embeddings in a vector database.
5. **User Query:** Accept customer questions through the Streamlit interface.
6. **Information Retrieval:** Retrieve relevant document chunks using semantic similarity search.
7. **Context Preparation:** Combine retrieved information with the user's question.
8. **Response Generation:** Pass the prompt to the locally running LLM through Ollama.
9. **Answer Display:** Generate and display the response through the Streamlit application.

## ✨ Key Features

- Interactive customer support chatbot.
- Document-based question answering.
- Semantic search and information retrieval.
- Context-aware response generation.
- Local LLM execution using Ollama.
- Lightweight model configuration for systems with limited memory.
- User-friendly Streamlit interface.

## 🏗️ RAG Architecture

User Query → Retriever → Vector Database → Relevant Documents → Contextual Prompt → Ollama LLM → Generated Answer

## 💡 Example Use Cases

- How can I request a refund?
- What is the shipping policy?
- How can I track my order?
- What is the account registration process?
- What should I do if my order is delayed?

## 🚀 Project Outcome

This project demonstrates the practical implementation of Retrieval-Augmented Generation by combining document retrieval with Large Language Model capabilities.

It provides hands-on experience with document processing, embeddings, vector databases, semantic search, prompt engineering, LLM integration, and building Generative AI applications.

The project also demonstrates how locally hosted language models can be integrated into an AI-powered customer support system.
