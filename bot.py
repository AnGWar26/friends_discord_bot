import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

# this function randomly capitalizes letters in a sentence
def random_caps(sentence):
    new_sentence = ""
    number = 0 #Dummy number for tracking

    for letter in sentence.lower():
        if len(new_sentence)<2: #Creates the first two letter
            random_number = random.randint(0,1) #This randomly decides if the letter should be upper or lowercase
            if random_number==0:
                new_sentence += letter.upper()
            else:
                new_sentence += letter
        else:
            if (new_sentence[number-2].isupper() and new_sentence[number-1].isupper() or new_sentence[number-2].islower() and new_sentence[number-1].islower())==True:
                #Checks if the two letters before are both upper or lowercase
                if new_sentence[number-1].isupper(): #Makes the next letter the opposite of the letter before
                    new_sentence += letter.lower()
                else:
                    new_sentence += letter.upper()
            else:
                random_number = random.randint(0,1)
                if random_number==0:
                    new_sentence += letter.upper()
                else:
                    new_sentence += letter
                
        number += 1 #Add one more to the tracking
     
    return(new_sentence)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='mock')
async def mock_func(ctx):
    channel = bot.get_channel(783045227321098301)
    msg_history = await channel.history(limit=10).flatten() # create list of message objects
    previous_message = msg_history[1].content # get the message beofore $mock command
    await ctx.send(random_caps(previous_message))

bot.run(TOKEN)