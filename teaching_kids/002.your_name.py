import os
import sys

def say(message):
  if sys.platform.startswith('darwin'):
    message = 'say "%s"' % message
    os.system(message)

# this will ask for your name and then print it out for you.
say("What is your name?")
name = input("What is your name: ")
say("Hi," + name)
say("What do you want me to say: ")
message = input("message: ")
say(message)
say("Good Bye! Have a great time learning!")
