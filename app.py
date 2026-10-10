import html
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from htmlTemplates import css, bot_template, user_template


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    llm = ChatOllama(model="qwen2.5:latest", temperature=0.3)
    retriever = vectorstore.as_retriever()

    # Step 1: rewrite follow-up questions into standalone ones
    contextualize_prompt = ChatPromptTemplate.from_messages([
        ("system",
         "Given the chat history and the latest user question, rewrite the "
         "question so it makes sense without the history. Do NOT answer it. "
         "Return the original question if no rewrite is needed."),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ])
    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_prompt)

    # Step 2: answer from the retrieved chunks
    qa_prompt = ChatPromptTemplate.from_messages([
        ("system",
         "Answer the question using only the context below. "
         "If the answer is not in the context, say you don't know.\n\n{context}"),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ])
    qa_chain = create_stuff_documents_chain(llm, qa_prompt)

    return create_retrieval_chain(history_aware_retriever, qa_chain)


def handle_userinput(user_question):
    if st.session_state.conversation is None:
        st.warning("⚠️ Please upload and process your PDFs in the sidebar first.")
        return

    with st.spinner("Analyzing documents & generating response..."):
        history = st.session_state.chat_history
        response = st.session_state.conversation.invoke(
            {"input": user_question, "chat_history": history})

        history.append(HumanMessage(content=user_question))
        history.append(AIMessage(content=response["answer"]))


def render_chat():
    for message in st.session_state.chat_history:
        template = user_template if isinstance(message, HumanMessage) else bot_template
        safe_text = html.escape(message.content).replace("\n", "<br>")
        st.write(template.replace("{{MSG}}", safe_text), unsafe_allow_html=True)


def main():
    load_dotenv()
    st.set_page_config(
        page_title="MultiPDF AI Assistant",
        page_icon="📚",
        layout="wide"
    )
    
    # Inject Custom CSS Theme
    st.markdown(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "processed_files" not in st.session_state:
        st.session_state.processed_files = 0

    # Header Section
    is_ready = st.session_state.conversation is not None
    status_html = (
        '<span class="status-badge ready">🟢 Ready to Chat</span>'
        if is_ready else
        '<span class="status-badge waiting">🟡 Awaiting PDFs</span>'
    )
    
    st.markdown(
        f'''
        <div class="main-header">
            <h1 class="main-title">📚 MultiPDF AI Assistant</h1>
            {status_html}
        </div>
        ''',
        unsafe_allow_html=True
    )

    # Sidebar Dashboard
    with st.sidebar:
        st.markdown("### 📄 Document Manager")
        
        pdf_docs = st.file_uploader(
            "Upload your PDF files below:",
            type=["pdf"],
            accept_multiple_files=True
        )

        if st.button("🚀 Process Documents"):
            if pdf_docs:
                with st.spinner("Parsing PDFs & building vector index..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    vectorstore = get_vectorstore(text_chunks)
                    st.session_state.conversation = get_conversation_chain(vectorstore)
                    st.session_state.processed_files = len(pdf_docs)
                    st.success(f"Successfully processed {len(pdf_docs)} file(s)!")
                    st.rerun()
            else:
                st.warning("Please attach at least one PDF document.")

        st.markdown("---")
        
        if st.session_state.processed_files > 0:
            st.info(f"📊 Active Index: **{st.session_state.processed_files} document(s)** loaded")
            
        if st.button("🗑️ Clear Chat History"):
            st.session_state.chat_history = []
            st.rerun()

        st.markdown("---")
        st.markdown(
            """
            <small style="opacity:0.7;">
                💡 <b>How it works:</b><br>
                1. Upload PDF files<br>
                2. Click Process Documents<br>
                3. Ask natural language questions!
            </small>
            """,
            unsafe_allow_html=True
        )

    # Main Chat Area
    if not st.session_state.chat_history and not is_ready:
        st.markdown(
            """
            <div style="text-align: center; padding: 4rem 2rem; background: rgba(20, 20, 23, 0.6); border-radius: 16px; border: 1px dashed rgba(249, 115, 22, 0.35);">
                <h3 style="color: #fb923c; font-weight: 600;">👋 Welcome to MultiPDF AI Assistant!</h3>
                <p style="color: #a1a1aa;">Upload your PDF documents using the sidebar on the left and click <b style="color: #ff8c00;">Process Documents</b> to start querying your data.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        render_chat()

    # Fixed Chat Input Box
    user_question = st.chat_input("Ask a question about your uploaded documents...")
    if user_question:
        handle_userinput(user_question)
        st.rerun()


if __name__ == '__main__':
    main()
