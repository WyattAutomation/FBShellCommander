from fbchat import log, Client
import sys
import subprocess
import os, signal
from subprocess import check_output

# An FBChat "Echobot", set up to pass string values in/out of a local shell using Python's subprocess module
class EchoBot(Client):
    def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)
        
        log.info("Message from {} in {} ({}): {}".format(author_id, thread_id, thread_type.name, message))

        if author_id != self.uid:
            process = subprocess.Popen(message, shell=True, stdout=subprocess.PIPE)
            process.wait()
            cmd_output = process.stdout.read()
            self.sendMessage(cmd_output, thread_id=thread_id, thread_type=thread_type)
            
#replace "YourFBLoginEmail@example.com", "YourFBPasswordHere" with a real Facebook login
client = EchoBot("YourFBLoginEmail@example.com", "YourFBPasswordHere")
client.listen()

#if it crashes, just start over
os.system("FBcmd.py")
