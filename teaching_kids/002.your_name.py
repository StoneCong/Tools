import os
import sys
import time

def say(message):
  if sys.platform.startswith('darwin'):
    message = 'say "%s"' % message
    os.system(message)

# this will ask for your name and a message and speak them out
say("What is your name?")
name = input("What is your name: ")
say("Hi," + name)

say("What do you want me to say:")
message = input("message: ")
say(message)

time.sleep(1)  # Wait for a second
say("Talk to you later! Have a great time learning!")
