import sleekxmpp
import logging
import cleverbot
#import dnspython

def session_start(event):
    chatbot.send_presence()
    print 'Session started'
    chatbot.get_roster()

def message(msg):
    if msg['type'] in ('chat','normal'):
        msg1 = msg['body']
        reply = cb.Ask(msg1)
        msg.reply(reply).send()

jid = 'YOUR-FB:ID@chat.facebook.com'
password = 'YOUR FB PASSWORD'
addr = ('chat.facebook.com', 5222)
ipaddr = ('209.85.175.125',5222)

chatbot = sleekxmpp.ClientXMPP(jid,password)
chatbot.add_event_handler("session_start", session_start)
chatbot.add_event_handler("message", message)

chatbot.auto_reconnect = True

#logging.basicConfig(level=logging.DEBUG,
#                       format='%(levelname)-8s %(message)s')

cb = cleverbot.Session()

chatbot.connect(addr)
chatbot.process(block=True)
