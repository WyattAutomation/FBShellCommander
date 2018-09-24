# FBShellCommander


Run a remote shell through Facebook Messenger: Linux or Windows.  Allows you to send commands, and recieve output from the CLI (terminal or CMD) on the deivce it's installed on.

##Installation

Requires carpedm20's FBChat (source for his work here:  https://github.com/carpedm20/fbchat )
```
pip3 install fbchat
```

Then, edit FBcmd.py, and enter a Facebook username and password where indicated (in the following line):

```
client = EchoBot("YourFBLoginEmail@example.com", "YourFBPasswordHere")
```

run it:
```
python3 FBcmd.py
```

Enjoy!
