import streamlit as st
import validators
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader

# ---------------------- Streamlit Config ----------------------
st.set_page_config(
    page_title="YT/URL Summarizer",
    page_icon="📝",
    layout="wide"
)

st.title("Summarize YouTube or Website Content")
st.caption("Paste a YouTube link or website URL, and get a concise summary powered by **llama-3.1-8b-instant** with Groq API.")

# ---------------------- Sidebar ----------------------
with st.sidebar:
    st.header(" API & Settings")
    groq_api_key = st.text_input("Groq API Key", value="", type="password")
    summary_length = st.slider("Summary length (words)", min_value=100, max_value=600, value=300, step=50)

    st.markdown("---")
    
# ---------------------- Input Section ----------------------
url = st.text_input("Enter a YouTube or Website URL:")

# ---------------------- Helper Functions ----------------------
from langchain_community.document_loaders import YoutubeLoader
import yt_dlp
from langchain.schema import Document

def load_youtube_with_ytdlp(url: str):
    """Load YouTube transcript/description using yt-dlp (more stable than pytube)."""
    ydl_opts = {"quiet": True, "skip_download": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        description = info.get("description", "")
        title = info.get("title", "Unknown Title")
        channel = info.get("uploader", "Unknown Channel")

        return [Document(
            page_content=description,
            metadata={"title": title, "channel": channel, "url": url}
        )]

def load_content(url: str):
    if "youtube.com" in url or "youtu.be" in url:
        return load_youtube_with_ytdlp(url)
    else:
        loader = UnstructuredURLLoader(urls=[url], ssl_verify=False)
        return loader.load()

def summarize_content(docs, llm, length):
    """Summarize the extracted content with LLM."""
    prompt_template = f"""
    Provide a clear, concise summary of the following content in about {length} words.
    Content: {{text}}
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
    chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
    return chain.run(docs)

# ---------------------- Main App Logic ----------------------
if st.button(" Summarize Content"):
    if not groq_api_key.strip() or not url.strip():
        st.error("Please enter both the **Groq API key** and a valid **URL** to continue.")
    elif not validators.url(url):
        st.error("❌ Invalid URL. Please provide a valid YouTube or Website link.")
    else:
        try:
            with st.spinner("⏳ Fetching content..."):
                docs = load_content(url)

            llm = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=groq_api_key)

            with st.spinner("⚡ Summarizing..."):
                summary = summarize_content(docs, llm, summary_length)

            st.success(" Summary generated successfully!")
            st.write(summary)

            # Show extra metadata for YouTube
            if "youtube.com" in url or "youtu.be" in url:
                st.markdown("---")
                st.subheader(" Video Info")
                video_info = docs[0].metadata
                st.json(video_info)

        except Exception as e:
            st.error("An error occurred while processing your request.")
            st.exception(e)
