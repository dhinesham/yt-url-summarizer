
# 📝 YT/URL Summarizer

A **Streamlit app** that generates concise summaries from **YouTube videos** and **websites** using the **Groq LLaMA-3.1-8B-Instant** model via the Groq API.

## 🚀 Features

* 🔗 Accepts **YouTube links** or **website URLs**
* ⚡ Fetches content using `yt-dlp` (for YouTube) or `UnstructuredURLLoader` (for websites)
* 🤖 Summarizes text with **LLaMA-3.1-8B-Instant** powered by **Groq API**
* 🎚 Adjustable summary length (100–600 words)
* 📊 Displays extra metadata for YouTube videos (title, channel, URL)

## 🛠️ Tech Stack

* [Streamlit](https://streamlit.io/) – UI framework
* [LangChain](https://www.langchain.com/) – Prompt & summarization chain
* [Groq API](https://groq.com/) – LLM inference
* [yt-dlp](https://github.com/yt-dlp/yt-dlp) – Extract YouTube data
* [Unstructured](https://www.unstructured.io/) – Web content loading

## 📦 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/dhinesham/yt-url-summarizer.git
cd yt-url-summarizer
pip install -r requirements.txt
```

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Enter your **Groq API key** in the sidebar, paste a **YouTube/Website URL**, and click **Summarize Content**.

## 🔑 Environment Setup

You’ll need a **Groq API Key**.
Set it in the sidebar when running the app.

Alternatively, you can set it as an environment variable:

```bash
export GROQ_API_KEY="your_api_key_here"
```

## 📷 Demo

<img width="1915" height="706" alt="Screenshot 2025-09-04 210047" src="https://github.com/user-attachments/assets/08a20c54-f62f-4b02-8a66-9469854acd8d" />


## 🗂 Project Structure

```
.
├── app.py              # Main Streamlit application
├── requirements.txt    # Dependencies
├── .env                # API keys
└── README.md           # Documentation
```

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to improve.

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.


