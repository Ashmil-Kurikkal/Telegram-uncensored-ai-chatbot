# Telegram AI Chatbot with Local LLMs

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white) ![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

A well-documented starter template for developers looking to build a Telegram chatbot powered by a locally-hosted Large Language Model using Ollama.

This approach ensures 100% user privacy and has zero API costs, making it ideal for experiments, personal assistants, or applications where data confidentiality is critical.

![Logo](https://i.postimg.cc/K88h3t5V/logo1.jpg)

## Key Features

* **Local AI:** Leverages the Ollama API to interact with locally-run LLMs, ensuring privacy and control.
* **Multi-Model Support:** Easily configurable to use various models, including general-purpose (Llama) and code-specific (Deepseek-coder) models.
* **Chat History:** Uses a MySQL database to maintain a persistent chat history for each user, allowing for conversational context.

## Tech Stack

* **Backend:** Python
* **AI Integration:** Ollama
* **Database:** MySQL
* **Messaging Platform:** Telegram Bot API
* **Libraries:** `pyTelegramBotAPI`, `requests`, `mysql-connector-python`

## Getting Started

Follow these steps to get a local copy up and running.

### Prerequisites

* Python 3.8+
* A running MySQL server
* Ollama installed and running
* A Telegram Bot API token from BotFather

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/Ashmil-Kurikkal/Telegram-AI-Chat-Bot.git](https://github.com/Ashmil-Kurikkal/Telegram-AI-Chat-Bot.git)
    cd Telegram-AI-Chat-Bot
    ```

2.  **Create a `requirements.txt` file** containing the following lines:
    ```
    pyTelegramBotAPI
    requests
    mysql-connector-python
    pyfiglet
    python-dotenv
    ```
    Then, install the packages:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables:**
    Rename the `.env.sample` file to `.env` and add your credentials. **Do not edit the Python script directly.**
    ```env
    TELEGRAM_BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
    OLLAMA_API_PORT="11434"
    DB_HOST="localhost"
    DB_USER="your_db_user"
    DB_PASSWORD="your_db_password"
    DB_NAME="your_db_name"
    ```

4.  **Set up the Database:**
    Ensure your MySQL server is running. Create a database and a table named `users` using the schema from the `schema.sql` file.

5.  **Ensure Ollama is Running:**
    You can check the status by running `ollama serve` in a separate terminal. The bot will connect to it via the port specified in your `.env` file.

## Usage

Once everything is configured, run the main script:
```bash
python main.py
