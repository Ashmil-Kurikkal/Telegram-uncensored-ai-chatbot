import telebot
import requests
import json
import mysql.connector
import os
import pyfiglet


sql_username = input("Enter MySQL username. \n")
sql_pass = input("\nEnter your MySQL password.\n")
db_name = input("\nEnter your MySQL database name you'd like to use for storing user data.\n")
ollama_api = input("\nEnter your Ollama port that shows up when you type Ollama Serve in your terminal.\nUsually something like = 'http://127.0.0.1:11434/api/chat\n")
telegram_bot_token = input("\nEnter your Telegram bot token you would like to use the bot with, obtained from the BotFather bot.\n")
owner_description = input("\nDescribe yourself briefly so if the user asks about the creator the model can use this info to give a proper description.\n")
owner_name = input("\nEnter your name that you want to let the user know you by.\n")
print("\n\nWaiting for users to text the bot.")

asciish = pyfiglet.figlet_format("k3yb0ard")
print(asciish)

def connect_to_database():
    global database
    try:
        database = mysql.connector.connect(
            host='localhost',
            database=db_name,
            user=sql_username,
            password=sql_pass
        )
        if database.is_connected():
            print('Connected to MySQL database')
            return database
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def insert_data(username, user_id, messages):
    try:
        cursor = database.cursor()
        # Ensure messages is a list before dumping to JSON
        if not isinstance(messages, list):
            print("```FORMAT INVALID```")
        json_messages = json.dumps(messages)
        sql = "INSERT INTO users (username, user_id, history) VALUES (%s, %s, %s)"
        cursor.execute(sql, (username, user_id, json_messages))
        database.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def fetch_data(user_id):
    cursor = database.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    row = cursor.fetchone()
    if row:
        print("\nDisplaying Data:")
        print("\nusername :", row[0])
        print("\nuser_id :", row[1])
        print("\nhistory :", row[2])
        messages = json.loads(row[2])
        return row[0], row[1], messages
def update_data(user_id, history):
    try:
        cursor = database.cursor()
        sql = "UPDATE users SET history = %s WHERE user_id = %s"
        cursor.execute(sql, (history, user_id))
        database.commit()
        print("History updated successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def chat(messages):
    port = ollama_api
    try:
        response = requests.post(port, json={"model": selected_model, "messages": messages, "stream": True}, stream=True)
        response.raise_for_status()

        output = ""
        for line in response.iter_lines():
            if line:
                body = json.loads(line.decode('utf-8'))

                if "error" in body:
                    raise Exception(body["error"])

                if body.get("done", False):
                    output += body.get("message", {}).get("content", "")
                    break
                content = body.get("message", {}).get("content", "")
                output += content
                print(content, end="", flush=True)
        return output
    except requests.exceptions.RequestException as e:
        print(f"Request error: {str(e)}")
        return "Error processing request."
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {str(e)}")
        return "Error decoding JSON response."

def history_check(username, user_id):
    global messages
    connect_to_database()
    try:
        username_from_db, user_id_from_db, message_history = fetch_data(user_id)
        print(message_history)
        if user_id_from_db != user_id:
            messages = []
            insert_data(username, user_id, messages)
        else:
            messages = json.loads(message_history)
            print (messages)
    except:
        messages = []
        insert_data(username, user_id, messages)

def main(text):
    if text:
        if owner_name == text.lower():
            connect_to_database()
            text = owner_description
            messages.append({"role": "user", "content": text})
            response = chat(messages)
            messages.append({"role": "assistant", "content": response})
            json_messages = json.dumps(messages)
            update_data(user_id, json_messages)
            print(response, "\n\n\n")
            return response
        else:
            connect_to_database()
            messages.append({"role": "user", "content": text})
            response = chat(messages)
            messages.append({"role": "assistant", "content": response})
            json_messages = json.dumps(messages)
            update_data(user_id, json_messages)
            print(response, "\n\n\n")
            return response


# API token
bot = telebot.TeleBot(telegram_bot_token)
user_id = 0
@bot.message_handler(commands=['start'])
def start(message):
    global username
    global user_id
    if message.chat.type == "private":
        username = message.from_user.username
    elif message.chat.type == "group":
        username = "telegram_group"
    user_id = message.chat.id
    pic = open("logo1.jpg", "rb")
    bot.send_photo(user_id, pic)
    print("Image sent successfully")
    bot.reply_to(message, "Hi, AI-lice here. You will be on que, please be patient for a few moments and ```!DON'T SPAM!```. 👾 \n\n~~~Ashmil-Kurikkal~~~\nThanks.")
    convo_type = message.chat.type
    print("\n\n", username, "\n\n", user_id, "\n\n", convo_type)
    bot.reply_to(message, "Hi there again, seems like you were patient enough, Click on --> /ailice to proceed.")

user_states = {}
START, SELECT_LLM, CONTINUE_CONVERSATION = range(3)

def set_state(user_id, state):
    user_states[user_id] = state

def get_state(user_id):
    return user_states.get(user_id, START)

@bot.message_handler(commands=['ailice'])
def ailice_response(message):
    global ailice_user_id

    ailice_user_id = message.chat.id
    if user_id!=0 :
        if ailice_user_id == user_id :
            bot.reply_to(message, "Send 'clear' to remove previous chat context/history.\n\n\n !!!Clear history before switching to a new Model if you had a previous conversation!!!\n\n\n---------\n Send '1' for Alice-uncensored AI assistant. \n\n\nSend '2' for Alice-censored AI assistant. \n\n\nSend '3' for Deepseek-coder with better coding skills but low capability of engaging in conversations.")
            set_state(message.from_user.id, SELECT_LLM)
        else :
            bot.reply_to(message,"Limitter to avoid heavy duty on the server \n\n\nANOTHER USER IN QUE. Click on /start first\nThen click on /ailice")
    else:
        bot.reply_to(message,"PLEASE INITIALISE BY /start COMMAND.")
@bot.message_handler(func=lambda message: get_state(message.from_user.id) == SELECT_LLM)
def select_llm(message):
    global selected_model,select_llm_user_id

    user_input = message.text
    selected_model = user_input
    select_llm_user_id = message.chat.id
    if select_llm_user_id == ailice_user_id:
        username = message.from_user.username
        user_id = message.chat.id
        if "1" in selected_model:
            bot.reply_to(message, "You're in que, searching for previous history with this model.")
            history_check(username, str(user_id))
            selected_model = "llama2-uncensored"
            text = "Say that I have selected Ashlice-uncensored AI assistant created by ashmil based on the large language model llama2 and explain your capabilities very briefly."
            reply_text = main(text)
            bot.reply_to(message, reply_text)
            set_state(message.from_user.id, CONTINUE_CONVERSATION)
        
        elif "2" in selected_model:
            bot.reply_to(message, "You're in que, searching for previous history with this model.")
            history_check(username, str(user_id))
            selected_model = "llama3"
            text = "Say that I have selected Ashlice-3 AI assistant created by k3yb0ard based on the large language model Llama3 and explain your capabilities very briefly."
            reply_text = main(text)
            bot.reply_to(message, reply_text)
            set_state(message.from_user.id, CONTINUE_CONVERSATION)
        
        elif "3" in selected_model:
            bot.reply_to(message, "You're in que, searching for previous history with this model.")
            history_check(username, user_id)
            selected_model = "Deepseek-Coder"
            text = "Say that the I have selected deepseek-coder, and explain your capabilities very briefly. Don't forget to specify that you are weak in immersive conversation but better at Computer science and relatives."
            reply_text = main(text)
            bot.reply_to(message, reply_text)
            set_state(message.from_user.id, CONTINUE_CONVERSATION)
        elif selected_model.lower() == 'clear':
            bot.reply_to(message, "Clearing history.....")
            history = "[]"
            history_json = json.dumps(history)
            database = connect_to_database()
            if database:
                update_data(user_id, history_json)
                print("history cleared")
                bot.reply_to(message, "HISTORY CLEARED")
        else:
            bot.reply_to(message, "INVALID SELECTION, Send me a choice 1,2 or 3 after reading the model description, or 'clear' to clear previous chat context/history")
    else:
        bot.reply_to(message,"This bot runs solely on a laptop, including the storage server, thus to avoid heavy duty, a limitter is in place.\n\n\nANOTHER USER IN QUE\n\n\nClick on /start first\nThen click on /ailice")            
@bot.message_handler(func=lambda message: get_state(message.from_user.id) == CONTINUE_CONVERSATION)
def continue_conversation(message):
    if message.chat.id==user_id:
        bot.reply_to(message, "Queueing you....")
        user_input = message.text
        text = user_input
        print("RECIEVED INPUT \n\n")
        bot.reply_to(message, main(text))
    else:
        if message.chat.type == "private":
            bot.reply_to(message,"ANOTHER USER IN QUE\n\nClick on /start first\nThen click on /ailice")
            print("Multiple input lag.")
        elif message.chat.type == "group":
            bot.reply_to(message,"REPLYING TO ANOTHER USER IN THE GROUP, PLEASE WAIT.")
            print("Multiple input lag.")
# Start the bot
bot.polling()