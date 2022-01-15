import discord
import os
import random

from discord.ext import commands
from keep_alive import keep_alive

# Global:
CLIENT = discord.Client()
PREFIX = "!"


# Commands:
def random_generator(first, last):
  return (random.randint(first, last))


def losuj(message):
  MSG = message.content
  try:
    last = int(MSG.split(PREFIX + "losuj", 1)[1])
    return ("<:THO_BlobCatRobot:541708128794705996> **| Losowy numer od 1 do " + str(last) + " to: " + str(random_generator(1, last)) + "**")
  except Exception:
    return ("<:THO_BlobCatMage:736568215051829289> **| Poprawne uzycie to: `" + PREFIX + "losuj [przedzial]`**")


# Working:
@CLIENT.event
async def on_ready():
  print('Dzialam jako {0.user}.'.format(CLIENT))


# Waiting for the commands:
@CLIENT.event
async def on_message(message):
  USERNAME = str(message.author).split('#'[0])
  CHANNEL = str(message.channel.name)
  USER_MESSAGE = str(message.content)
  MSG = message.content
  RESEND = message.channel.send

  if message.author == CLIENT.user:
    return

  if message.channel.name != "komendy" and message.channel.name != "boty":
    return

  print(f"{USERNAME}: {USER_MESSAGE} ({CHANNEL})")

  if MSG.startswith(PREFIX + "hej"):
    await RESEND("Hejka !")
    return

  elif MSG.startswith(PREFIX + "losuj"):
    await RESEND(losuj(message))
    return

# Main:
if __name__ == '__main__':
  keep_alive()
  CLIENT.run(os.environ['TOKEN'])
