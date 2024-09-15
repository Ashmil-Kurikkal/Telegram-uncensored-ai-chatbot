
<br/>
<div align="center">

<h3 align="center">Telegram AI uncensored Chatbot</h3>
<p align="center">
A Telegram bot scripted in python using Ollama API and MySQL for chat history.


  


</p>
</div>

## About The Project

![Logo](https://i.postimg.cc/K88h3t5V/logo1.jpg)

This Telegram bot uses the [Ollama API](https://ollama.com/) to interact with users as a chatbot. It uses censored and uncensored Llama models, a coding-specific model (Deepseek-coder), and uses MySQL to maintain chat history.
### Built With

- [Python](https://python.org)
- [Ollama](https://ollama.com)
- [MySQL](https://mysql.com)
- [Telegram Bots & The BotFather](https://telegram.org/blog/bot-revolution)
## Getting Started

To get a local copy up and running follow these simple example steps.
### Prerequisites

Do not miss a thing!
### Requirements
#### Software
- Python 3
- MySQL server
- Ollama API
- Telegram Bot API token

#### Hardware
- 8 GB RAM (might not work, get 16 if you can)
- GPU support is available on windows too after latest ollama update, fine with linux.
### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

0. Rename the .env_sample file to .env
1. Create your bot from the BotFather on telegram and obtain the API token. Now either place the API token in line 134 of the python script or replace it in the env sample file.
2. Clone the repo
   ```sh
   git clone https://github.com/Ashmil-Kurikkal/Telegram-AI-Chat-Bot.git
   ```
3. Install PIP packages
```bash
pip install pyTelegramBotAPI requests mysql-connector-python python-dotenv
```
4. Install and Setup Ollama API.

Visit the Ollama website and follow the installation instructions for your system.

Once installed, Ollama runs on localhost:11434 by default, to make sure, run 
```sh
ollama serve
```
on the terminal.

Enter the port in the .env file.
5. Install MySQL and setup a database and a table named 'users'.



## License

Distributed under the MIT License. See [MIT License](https://opensource.org/licenses/MIT) for more information.
