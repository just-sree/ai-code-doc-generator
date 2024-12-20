import streamlit as st
from doc_generator import generate_documentation
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

# Load FAISS retriever
retriever = FAISS.load_local("faiss_index", OpenAIEmbeddings())

# Streamlit app
st.title("AI-Powered Code Documentation Generator")
st.subheader("Generate documentation for your Python code.")

# File uploader
uploaded_file = st.file_uploader("Upload your Python file", type=["py"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    temp_file_path = f"temp/{uploaded_file.name}"
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write("Processing your file...")
    try:
        # Generate documentation
        documentation = generate_documentation(temp_file_path, retriever)
        st.markdown("### Generated Documentation")
        st.text_area("Output", documentation, height=400)
    except Exception as e:
        st.error(f"An error occurred: {e}")
