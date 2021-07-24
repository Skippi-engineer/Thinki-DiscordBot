import discord
import os
import random

from keep_alive import keep_alive

CLIENT = discord.Client()
PREFIX = "!"


# Commands:
def random_generator(first, last):
  rand = random.randint(first, last)
  return rand


# Working:
@CLIENT.event
async def on_ready():
  print('Dzialam jako {0.user}.'.format(CLIENT))


# Waiting for the commands:
@CLIENT.event
async def on_message(message):
  MSG = message.content
  RESEND = message.channel.send

  if message.author == CLIENT.user:
    return

  elif MSG.startswith(PREFIX + "hej"):
    await RESEND("Hejka !")

  elif MSG.startswith(PREFIX + "losuj"):
    try:
      last = int(MSG.split(PREFIX + "losuj", 1)[1])
      await RESEND("<:THO_BlobCatRobot:541708128794705996> **| Losowy numer od 1 do " + str(last) + " to: __" + str(random_generator(1, last)) + "__**")
    except Exception:
      await RESEND("<:THO_BlobCatMage:736568215051829289> **| Poprawne uzycie to: `" + PREFIX + "losuj [przedzial]`**" )

# Main:
keep_alive()
CLIENT.run(os.environ['TOKEN'])
