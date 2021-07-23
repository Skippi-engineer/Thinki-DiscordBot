import discord
import os
import random

CLIENT = discord.Client()
PREFIX = "!"


def random_generator(first, last):
  rand = random.randint(first, last)
  return rand

@CLIENT.event
async def on_ready():
  print('Dzialam jako {0.user}.'.format(CLIENT))


@CLIENT.event
async def on_message(message):
  MSG = message.content
  RESEND = message.channel.send

  if message.author == CLIENT.user:
    return
  elif MSG.startswith(PREFIX + "hej"):
    await RESEND("Hejka !")
  elif MSG.startswith(PREFIX + "los"):
    last = int(MSG.split(PREFIX + "los", 1)[1])
    await RESEND("Losowy numer od 1 do " + str(last) + " to: " + str(random_generator(1, last)))

# Main:
CLIENT.run(os.environ['TOKEN'])
