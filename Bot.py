from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')

conversa = ['oi', 'olá', 'Tudo bem?', 'Estou bem']

bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
    quest = input ("Voce:")
    respota = bot.get_response(quest)
    print ('Bot:', respota)
