import telebot
import requests
import time
# from keep_alive import keep_alive
# keep_alive()

def fetch_phone_numbers():
    try:
        response = requests.get("https://pastebin.com/raw/g78N2gyg")
        phone_numbers = response.text.replace('\r', '').strip()  # Remove \r characters
        return phone_numbers
    except Exception as e:
        print(f"Error fetching phone numbers: {e}")
        return ""

phone_numbers_string = fetch_phone_numbers()
phone_numbers_list = phone_numbers_string.strip().split('\n')


# Initialize your Telegram bot with the token you obtained from BotFather
bot = telebot.TeleBot("6891639487:AAHXiGM2tumJSwuYe0ydtSYQkypPE4ZnEeY")
running = True
def make_call(phone_number,message):
    url = "https://sms-call.vercel.app/api/call"
    payload = {
        "phone": phone_number
    }
    try:
        response = requests.post(url, json=payload)
        if response.json()['message'] == 'Sent':
            print(f"Call made to {phone_number} successfully!")
            bot.send_message(-1002041695132, f"Calls sent successfully to {phone_number}")
        else:
            print(f"Failed to make call to {phone_number}. Status code: {response.status_code}")
            bot.send_message(-1002041695132, f"Failed to make call to {phone_number}. error is: {response.json()['message']}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while making call to {phone_number}: {e}")
        bot.send_message(-1002041695132, f"Error occurred while making call to {phone_number}: {e}")

def make_calls(phone_numbers,message):
    global running
    for number in phone_numbers:
        if not running:
            break  
        make_call(number,message)
        time.sleep(2)
        

# Handle "/send" command from Telegram
@bot.message_handler(commands=['send'])
def send_messages(message):
    phone_numbers_string = fetch_phone_numbers()
    phone_numbers_list = phone_numbers_string.strip().split('\n')
    # Example list of phone numbers
    bot.reply_to(message, "Sending......")
    global running
    running = True
    make_calls(phone_numbers_list,message)
    bot.reply_to(message, "Done sent calls successfully!")

@bot.message_handler(commands=['whatsapp'])
def spam_call(message):
    phone_numbers_string = fetch_phone_numbers()
    phone_numbers_list = phone_numbers_string.strip().split('\n')
    chat_id =-1002041695132
    for phone_number in phone_numbers_list:
        try:
            response2 = requests.get(
                f'https://spamwhats.vercel.app/send_spam?number={phone_number}')
            if response2.status_code == 200:
                message = f"Whats Message made to{phone_number} successfully!"
                bot.send_message(chat_id, message, parse_mode="HTML")

            else:
                message = f"Failed to make Whats Message to {phone_number}. Status code: {response2.status_code}"
                bot.send_message(chat_id, message, parse_mode="HTML")

        except requests.exceptions.RequestException as e:
            print(f"Error occurred while making Whats Message to {phone_number}: {e}")
        time.sleep(5)
@bot.message_handler(commands=['start'])
def send_messages(message):

    bot.send_message(-1002041695132, "/send دوس هنا عشان تبعت المكالمات ")

@bot.message_handler(commands=['stop'])
def stop_messages(message):
    global running
    running = False
    bot.reply_to(message, "Send Call stopped!")

# Start the bot
bot.infinity_polling()
