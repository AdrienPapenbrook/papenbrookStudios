import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '>')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Say >commands | www.papenbrookstudios.gq'))
    print('Ready, Freddy')
@client.event
async def on_message(message):
    if message.content.startswith('>version'):
        msg = '{0.author.mention} :white_check_mark:the Current Version of me is [V0.001.043] LastUpdate[10/31/2018]:white_check_mark:'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('>commands'):
        msg = '{0.author.mention} All Commands start with (>) heres a small list of commands >rick,>list,>papenbrook,>help,>website.For more please visit my sweet crib https://www.papenbrookstudios.gq'.format(message)
        await client.send_message(message.channel, msg)
    if message.content == '>rick':
        await client.send_message(message.channel,'Rick and Morty?')
    if message.content == '>Sp.invite':
        await client.send_message(message.channel,'Here you go. Make sure to give me the creds for letting you join https://discord.gg/EvRx2pR  | https://www.roblox.com/My/Groups.aspx?gid=3029783?')
    if message.content == '>list':
        await client.send_message(message.channel,'Sorry my Power is below 6000 Check back later')
    if message.content == '>Sp.OOF':
        await client.send_message(message.channel,'Check Out OOF , its one of the best games on Roblox.com https://www.roblox.com/games/1552670060/Project-Oof-Pre-Alpha')
    if message.content == '>papenbrook':
        await client.send_message(message.channel,'Thats me:wave:.')
    if message.content == '>help':
        await client.send_message(message.channel,':wave:You must be new here , Check https://www.papenbrookstudios.gq')
    if message.content == '>music':
        await client.send_message(message.channel,':x:Ops, Sorry my permission is limited by my creator:x:')
    if message.content == '>produed':
        await client.send_message(message.channel,'Hey i know that guy... i think.')
    if message.content == '>roblox':
        await client.send_message(message.channel,'https://www.roblox.com')
    if message.content == '>youtube':
        await client.send_message(message.channel,'https://www.youtube.com')
    if message.content == '>facebook':
        await client.send_message(message.channel,'https://www.facebook.com')
    if message.content == '>tic':
        await client.send_message(message.channel,'tac toe.')
    if message.content == '>adminlogin':
        await client.send_message(message.channel,':warning:(0.author.mention)Yicks, your doing somthing you cant do:warning:')
    if message.content == '>website':
        await client.send_message(message.channel,'https://www.papenbrookstudios.gq is where you can find me.')
    if message.content == '>invite':
        await client.send_message(message.channel,'You are not permitted to invite me to any sever. am giving you a warning.')
    if message.content == '>911':
        await client.send_message(message.channel,'A nation reborn.')
    if message.content == '>banlist':
        await client.send_message(message.channel,':no_entry_sign:ERROR 1,you dont not have permission:no_entry_sign:')
    if message.content == '>rick invite':
        await client.send_message(message.channel,'https://discord.gg/2MFmk3d .. https://discord.gg/VHnYeUd')
    if message.content == '$danny bongo cat':
        em = discord.Embed(description='Tada the meme lives.')
        em.set_image(url='(0.author.mention)https://i.kym-cdn.com/photos/images/newsfeed/001/411/204/30c.png')
        await client.send_message(message.channel, embed=em)
    elif message.content.startswith('>flip'):
        flip = random.choice(["Heads","Tails"])
        await client.send_message(message.channel, (flip))
    if message.author == client.user:
        return
    elif message.content.startswith('>emoji'):
        emoji = random.choice([":smile:",":open_mouth:",":angry:",":frowning:",":smiley:",":wink:",":kissing:",":grinning:",":cry:",":rage:",":money_mouth:"])
        await client.send_message(message.channel, (emoji))
    if message.author == client.user:
        return
    elif message.content.startswith('>dice'):
        dice = random.choice([":game_die:=:one:",":game_die:=:two:",":game_die:=:three:",":game_die:=:four:",":game_die:=:five:",":game_die:=:six:"])
        await client.send_message(message.channel, (dice))
    if message.author == client.user:
        return
    if message.content.startswith('>hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('>guess'):
        await client.send_message(message.channel, 'Guess a number between 1 to 10')

        def guess_check(m):
            return m.content.isdigit()

        guess = await client.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
        answer = random.randint(1, 10)
        if guess is None:
            fmt = 'Sorry, you took too long. It was {}.'
            await client.send_message(message.channel, fmt.format(answer))
            return
        if int(guess.content) == answer:
            await client.send_message(message.channel, 'You are right!')
        else:
            await client.send_message(message.channel, 'Sorry. It is actually {}.'.format(answer))



client.run('Mzg0MzkxMTQ3ODkzODE3MzU0.Drowrw.4s8851aSPZ6Wgkn8amtdKZz1CQ0')
