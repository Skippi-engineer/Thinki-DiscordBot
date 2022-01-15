import discord
import os
import random

from discord.ext import commands
from keep_alive import keep_alive

# Global:
BOT = commands.Bot(command_prefix='!')

####################################################
## Commands:
def random_generator(first, last):
  return (random.randint(first, last))

# Losuj:
@BOT.command()
async def losuj(ctx, *args):
  try:
    if len(args)==1:
      first = 1
      last = int(args[0])
    elif len(args)==2:
      first = int(args[0])
      last = int(args[1])
    else:
      raise Exception

    await ctx.send("<:THO_BlobCatRobot:541708128794705996> **| Losowy numer od "+ str(first) + " do " + str(last) + " to: " + str(random_generator(first, last)) + "**")

  except Exception:
    await ctx.send("<:THO_BlobCatMage:736568215051829289> **| Poprawne uzycie to: `" + BOT.command_prefix + "losuj [przedzial]`**")


# Test:
@BOT.command()
async def test(ctx, *args):
  await ctx.send(" ".join(args))


# Ping
@BOT.command()
async def ping(ctx):
  #await ctx.send("Pong! " + str(round(BOT.latency*1000)) + " ms!")
  await ctx.send(f"Pong! {round(BOT.latency*1000)} ms!")


####################################################
## Working:
@BOT.event
async def on_ready():
  print('Dzialam jako {0.user}.'.format(BOT))


#@BOT.event
#async def on_message(message):
#  USERNAME = str(message.author).split('#'[0])
#  CHANNEL = str(message.channel.name)
#  USER_MESSAGE = str(message.content)
#  MSG = message.content
#  RESEND = message.channel.send
#
#  if message.author == BOT.user:
#    return
#
#  if message.channel.name != "komendy" and message.channel.name != "boty":
#    return
#
#  print(f"{USERNAME}: {USER_MESSAGE} ({CHANNEL})")


# Main:
if __name__ == '__main__':
  keep_alive()
  BOT.run(os.environ['TOKEN'])
