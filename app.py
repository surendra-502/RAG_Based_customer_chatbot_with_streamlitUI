import streamlit as st
import warnings

warnings.filterwarnings("ignore")

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
#from langchain_ollama import ChatOllama
from langchain_ollama import OllamaLLM



# -------------------------------------------------------
# Streamlit UI
# -------------------------------------------------------

st.set_page_config(
    page_title="Customer Support Chatbot",
    page_icon="💬"
)

st.title("💬 Customer Support Chatbot")
st.write("Ask questions about your order, account, refunds, shipping, and more.")


# -------------------------------------------------------
# Step 1: Load PDF
# -------------------------------------------------------

loader = PyPDFLoader("customer_support.pdf")
docs = loader.load()


# -------------------------------------------------------
# Step 2: Split into chunks
# -------------------------------------------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)


# -------------------------------------------------------
# Step 3: Create Embeddings
# -------------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# -------------------------------------------------------
# Step 4: Create FAISS Vector Store
# -------------------------------------------------------

vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)


# -------------------------------------------------------
# Step 5: Load Ollama Model
# -------------------------------------------------------

llm = OllamaLLM(
    model="qwen2.5:0.5b",
    temperature=0,
    num_ctx=1024
)


# -------------------------------------------------------
# Step 6: User Question
# -------------------------------------------------------

query = st.text_input("Ask your question")


# -------------------------------------------------------
# Step 7: Answer Question
# -------------------------------------------------------

if query:

    try:

        # Retrieve similar chunks
        result_docs = vectorstore.similarity_search(
            query,
            k=3
        )

        # Combine chunks into context
        context = "\n\n".join(
            [doc.page_content for doc in result_docs]
        )

        # Prompt
        prompt = f"""
You are a helpful customer support assistant.

Answer the user's question ONLY using the context below.

If the answer is not available in the context, reply exactly:

I could not find that in our support documentation. Please contact our support team for further help.

Context:
{context}

Question:
{query}

Answer:
"""

        # Generate answer
        response = llm.invoke(prompt)

        # Display answer
        st.subheader("Answer")
        st.write(response)

    except Exception as e:
        st.error(f"Error: {e}")