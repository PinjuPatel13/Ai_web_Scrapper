# 🕸️ AI Web Scraper

## 🚀 Overview
This project is an AI-powered web scraper built with **Streamlit**. It allows users to input a website URL, scrape its content, and parse specific information using AI models.

## ✨ Features
- 🌐 Scrape website content by entering a URL.
- 🧹 Clean and extract meaningful content from the scraped data.
- 🤖 Parse and analyze the extracted content using AI models.
- 🎛️ Interactive user interface with Streamlit.

## 📂 Project Structure
```
📦Ai_web_Scrapper
 ┣ 📂.streamlit
 ┃ ┗ 📜config.toml
 ┣ 📂__pycache__
 ┃ ┣ 📜parse.cpython-310.pyc
 ┃ ┗ 📜scrape.cpython-310.pyc
 ┣ 📜main.py
 ┣ 📜parse.py
 ┣ 📜requirements.txt
 ┗ 📜scrape.py
```

- `main.py`: The main application file that runs the Streamlit interface.
- `parse.py`: Contains functions to parse and analyze the extracted content using AI models.
- `scrape.py`: Contains functions to scrape and clean website content.
- `requirements.txt`: Lists the Python dependencies required for the project.
- `.streamlit/config.toml`: Configuration file for Streamlit settings.

## 📥 Installation
### Prerequisites
- Python 3.10 or higher
- [Streamlit](https://streamlit.io/)

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/PinjuPatel13/Ai_web_Scrapper.git
   cd Ai_web_Scrapper
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🛠️ Usage
1. **Run the Streamlit application:**
   ```bash
   streamlit run main.py
   ```

2. **Interact with the app:**
   - Enter the website URL you want to scrape.
   - Click on "Scrape Website" to fetch and display the content.
   - Provide a description of what you want to parse in the extracted content.
   - Click on "Parse Content" to analyze the content using the AI model.

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements or new features.

## 📜 License
This project is licensed under the MIT License.

## 👤 Author
[Pinju Patel](https://github.com/PinjuPatel13)
