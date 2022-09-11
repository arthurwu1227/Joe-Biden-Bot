import discord
import os
from keep_alive import keep_alive
import random
import time

trigger = ['bill', 'build', 'back', 'better', 'conservative', 'liberal', 'democrat', 'republican', 'trump', 'black', 'american', 'afghanistan', 'abortion']
quotes = ["you ain't black", "We hold these truths to be self-evident: all men and women are created, by the, you know the, you know the thing.", "I probably have a much higher IQ than you do, I suspect,",  'You’re a lying dog-faced pony soldier.', 'poor kids are just as bright and talented as white kids']

bidenmoment = discord.Embed()
bidenmoment.set_image(url = 'https://media.discordapp.net/attachments/901935815561740371/927256426152337428/2Fmethode2Ftimes2Fprod2Fweb2Fbin2F792de58e-5563-11e9-b872-7488e2315159.png?width=893&height=1116')
bidenmoment2 = discord.Embed()
bidenmoment2.set_image(url = 'https://media.discordapp.net/attachments/901935815561740371/927324786156245093/4661.png?width=1115&height=1115')
bidenmoment3 = discord.Embed()
bidenmoment3.set_image(url = 'https://media.discordapp.net/attachments/901935815561740371/927324813805121576/93d6e6ae817a8a3e1e271217aa07670fc1-2-joe-biden-b.png?width=1115&height=1114')
bidenmoment4 = discord.Embed()
bidenmoment4.set_image(url = 'https://media.discordapp.net/attachments/901935815561740371/927324907442929704/11788442-9631457-Vice_President_Joe_Biden_kisses_a_niece_of_incoming_Senate_Major-a-29_1622251618180.png')
bidenmoments = [bidenmoment, bidenmoment2, bidenmoment3, bidenmoment4]

client = discord.Client()
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('.help'):
    await message.channel.send("Cmds: .sniff to start sniffing")

  if message.content.startswith('.sniff'):
    while(True):
      await message.channel.send(embed=random.choice(bidenmoments))
      time.sleep(4)
      if(random.randint(1, 10) > 9):
        break
      
      
  if any(word.lower() in message.content for word in trigger):
    await message.channel.send(random.choice(quotes))

keep_alive()
client.run(os.getenv('TOKEN'))
