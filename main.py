import telebot
import openai #  pip unstall openai=0.28
# from config import OpenAiKey
# from config import TgKey

openai.api_key = ''
bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def welkome(message):
    bot.send_message(message.chat.id, 'Привет, я ChatGPT в telegram.')


@bot.message_handler(content_types=['text'])
def talk(message):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        presence_penalty=0.5
    )
    gpt_text = response['choices'][0]['text']
    bot.send_message(message.chat.id, gpt_text)


bot.polling(none_stop=True)