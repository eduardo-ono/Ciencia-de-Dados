
import glob
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from tkinter import *
from random import choice

arquivos_treino = [f for f in glob.glob("dados_treino/*.yml")]
# print(arquivos_treino)

bot_unisal = ChatBot(
    'ChatBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

# treino = ChatterBotCorpusTrainer(bot_unisal)
# for arq in arquivos_treino:
#     treino.train(arq)

# Interface gráfica
root = Tk()
root.minsize(width=360, height=360)
root.geometry('400x400+0+0')
user = StringVar()
bot = StringVar()
Label(root, text='Chatbot').pack()
Label(root, text='').pack()
Label(root, text='').pack()
root.title('ChatBot')
Label(root, text='Digite a sua mensagem').pack()
Entry(root, textvariable=user, width='50').pack()
Label(root, text='Bot:').pack()
Entry(root, textvariable=bot, width='50').pack()

def main():
    pergunta = user.get()
    resposta = bot_unisal.get_response(pergunta)
    if float(resposta.confidence) > 0.1:
        resp = []
        resp.append(resposta)
        bot.set(choice(resp))
    else:
        resposta = ['Não entendi!']
        bot.set(choice(resposta))

Label(root, text='').pack()
Button(root, text='Enviar', command=main).pack()

mainloop()
