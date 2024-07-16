import telepot
from telepot.loop import MessageLoop
from TOKEN import TOKEN

def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if content_type == 'text':
        command = msg['text']
        
        if command == '/start':
            bot.sendMessage(chat_id, '😀Bem-vindo ao Bot de comandos de Astronomia!\nComandos disponíveis:\n/sol - Descrição sobre o Sol\n/mercurio - Descrição sobre Mercúrio\n/venus - Descrição sobre Vênus\n/terra - Descrição sobre a Terra\n/marte - Descrição sobre Marte\n/jupiter - Descrição sobre Júpiter\n/saturno - Descrição sobre Saturno\n/urano - Descrição sobre Urano\n/netuno - Descrição sobre Netuno')
        elif command == '/sol':
            bot.sendMessage(chat_id, 'O Sol é uma estrela localizada no centro do Sistema Solar. É uma esfera de plasma composta principalmente de hidrogênio e hélio.')
        elif command == '/mercurio':
            bot.sendMessage(chat_id, 'Mercúrio é o menor planeta do Sistema Solar e o mais próximo do Sol. É conhecido por suas grandes variações de temperatura.')
        elif command == '/venus':
            bot.sendMessage(chat_id, 'Vênus é conhecido como o planeta irmão da Terra devido ao seu tamanho e composição semelhantes. Possui uma atmosfera densa e extremamente quente.')
        elif command == '/terra':
            bot.sendMessage(chat_id, 'A Terra é o nosso planeta, conhecido por sua biosfera única que suporta uma variedade de vida. É o terceiro planeta mais próximo do Sol.')
        elif command == '/marte':
            bot.sendMessage(chat_id, 'Marte é conhecido como o planeta vermelho devido à sua superfície coberta de óxido de ferro. Tem estações semelhantes às da Terra.')
        elif command == '/jupiter':
            bot.sendMessage(chat_id, 'Júpiter é o maior planeta do Sistema Solar e é conhecido por sua grande mancha vermelha, uma tempestade gigante visível na atmosfera.')
        elif command == '/saturno':
            bot.sendMessage(chat_id, 'Saturno é conhecido por seus anéis impressionantes, compostos principalmente de gelo e poeira. É o segundo maior planeta do Sistema Solar.')
        elif command == '/urano':
            bot.sendMessage(chat_id, 'Urano é um planeta gasoso que possui um eixo de rotação inclinado, fazendo com que ele gire de lado. Tem uma cor azul-esverdeada distintiva.')
        elif command == '/netuno':
            bot.sendMessage(chat_id, 'Netuno é o último planeta do Sistema Solar e é conhecido por seus ventos extremamente velozes. Tem uma cor azul profunda devido à presença de metano em sua atmosfera.')
        else:
            bot.sendMessage(chat_id, 'Comando inválido. Envie /start para iniciar!')

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle_message).run_as_thread()

print('BOT EM EXECUÇÃO...')

while True:
    pass
