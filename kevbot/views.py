from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


bot = ChatBot('chatbot', read_only=False,
    logic_adapters=[{'import_path':'chatterbot.logic.BestMatch',
                    #'default_response':'Sorry I cannot understand',
                    #'maximum_similarity_threshold':.80
                    }
                    ])

list_to_train =[
    
    'Hi',
    'Hi Whats Up. How can I help you',
    'What is your name',
    'My Name is kev the Bot',
    'Who is your master',
    'kevin is my creator',
    'What is your college',
    'SRM is my College',
    'Your Country',
    'I am from India'
]

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)

#List & Corpus Trainer
list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train) 
chatterbotCorpusTrainer.train('chatterbot.corpus.english')


def index(request):
    return render (request, 'kevbot/index.html'  )

def specific(request):
    return HttpResponse('This is a specific URL') 


def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)
