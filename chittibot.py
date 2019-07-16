#import libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

#defining name for chatbot and defining trainer
bot=ChatBot('MUNSHBOT')
bot.set_trainer(ListTrainer)

#accessing chatbot corpus
for files in os.listdir('C:/Users/HP/Downloads/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    data=open('C:/Users/HP/Downloads/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
    bot.train(data)

while True:
        message=input('you:')
        if message.strip!='Bye' or message.strip!='bye':
            reply=bot.get_response(message)
            print('chatbot:',reply)
        if message.strip=='Bye' or message.strip=='bye':
            print('chatbot:it was nice talking to you ,bye')
            break 




















