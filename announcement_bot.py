import time, os, platform
from time import sleep as wait 
from datetime import date
from datetime import datetime
try:
    import discord
except ModuleNotFoundError:
    print("Required module not found, running 'pip install discord' now")
    os.system("pip install discord")
    print("DOWNLOADED")
    import discord
#GAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHH
#load token
file=open("token.txt", "r")
token=file.read()
file.close()
system_os=platform.system()
client = discord.Client()
print("Do not open the log file while bot is running or else logs will not be created and commands will fail")
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    await client.change_presence(activity=discord.Game('*help'))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for *help"))
print('Bot active')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Hey, **AbyssWalker240** just posted a video!'):
        today = date.today()
        messageCon = message.content
        log_content= open('commands.log','a+')
        log_content.write(messageCon + '  -  -  -  -  -  ' + str(today) + '\n' + '\n')
        log_content.close()
        await message.channel.send('<@466814162098454529>')

    if message.content.startswith('Who likes cbt?'):
        today = date.today()
        messageCon = message.content
        log_content= open('commands.log','a+')
        log_content.write(messageCon + '  -  -  -  -  -  ' + str(today) + '\n' + '\n')
        log_content.close()
        await message.channel.send('<@466814162098454529> does!')

    if message.content.startswith("Who's the short dick man?"):
        today = date.today()
        messageCon = message.content
        log_content= open('commands.log','a+')
        log_content.write(messageCon + '  -  -  -  -  -  ' + str(today) + '\n' + '\n')
        log_content.close()
        await message.channel.send('<@671526219891605516> is!')

    if message.content.startswith('*info'):
        today = date.today()
        messageCon = message.content
        log_content= open('commands.log','a+')
        log_content.write(messageCon + '  -  -  -  -  -  ' + str(today) + '\n' + '\n')
        log_content.close()
        await message.channel.send('Bot made by <@671526219891605516> & <@466814162098454529> for The Hobbyist Heaven')

    if message.content.startswith('*help'):
        today = date.today()
        messageCon = message.content
        log_content= open('commands.log','a+')
        log_content.write(messageCon + '  -  -  -  -  -  ' + str(today) + '\n' + '\n')
        log_content.close()
        await message.channel.send('*info:\n    Info about the bot/creator\n*staff-list:\n    Lists all staff members (and will almost certainly summon staff members to the current channel)\n*help:\n    This message\n*test:\n    Run to test whether the bot is properly online or not\n*send.message:\n   Sends message to the log file\n*submit:\n    Submits recommended new channel to log file\n*ban:\n    Dont even bother')
        # await message.channel.send('Used for the auto announcements role that is still in development')
        # await message.channel.send('*info:')
        # await message.channel.send('Info about the bot/creator')
        # await message.channel.send('*help:')
        # await message.channel.send('This message')
    if message.content.startswith('*staff-list'):
        today = date.today()
        messageCon = message.content
        log_content= open('commands.log','a+')
        log_content.write(messageCon + '  -  -  -  -  -  ' + str(today) + '\n' + '\n')
        log_content.close()
        await message.channel.send('Staff List:\n-<@466814162098454529> - Owner\n-<@671526219891605516> - Moderator')

    if message.content.startswith('*ban'):
        today = date.today()
        messageCon = message.content
        log_content= open('commands.log','a+')
        log_content.write(messageCon + '  -  -  -  -  -  ' + str(today) + '\n' + '\n')
        log_content.close()
        await message.channel.send('If you do not straighten up *right now*, you will be exterminated via &ban.')

    if message.content.startswith('*submit'):
        today = date.today()
        messageCon = message.content
        print(messageCon)
        log_content= open('commands.log','a+')
        log_content.write(messageCon + '  -  -  -  -  -  ' + str(today) + '\n' + '\n')
        log_content.close()
        try:
            today = date.today()
            sFOB = open('submissions.txt','a+')
            sFOB.write(messageCon + '  -  -  -  -  -  ' + str(today) + '\n' + '\n')
            sFOB.close()
            await message.channel.send('Submission recorded successfully!')
        except:
            sFOB.close()
            print("error")

    if message.content.startswith('*clear-submits'):
        today = date.today()
        messageCon = message.content
        log_content= open('commands.log','a+')
        log_content.write(messageCon + '  -  -  -  -  -  ' + str(today) + '\n' + '\n')
        log_content.close()
        try:
            sFOB = open('submissions.log','w+')
            sFOB.write(' ')
            sFOB.close()
            await message.channel.send('Submissions cleared')
        except:
            sFOB.close()
            print("error")

    if message.content.startswith('*computer'):
        today = date.today()
        messageCon = message.content
        log_content= open('commands.log','a+')
        log_content.write(messageCon + '  -  -  -  -  -  ' + str(today) + '\n' + '\n')
        log_content.close()
        await message.channel.send("Platform:  "+system_os)
        # os.system('neofetch > computer.tmp')
        # time.sleep(2)
        # with open ('computer.tmp', 'r') as neofetch_out:
        #     data=neofetch_out.readlines()
        # await message.channel.send(data)
        # os.remove('computer.tmp')
        await message.channel.send('A laptop is widely know as a potato, and a desktop computer is widely known as a PC, which stands for Potato Chip')

    if message.content.startswith('*test'):
        today = date.today()
        messageCon = message.content
        log_content= open('commands.log','a+')
        log_content.write(messageCon + '  -  -  -  -  -  ' + str(today) + '\n' + '\n')
        log_content.close()
        await message.channel.send('Bot running')
        print('Bot tested')

    if message.content.startswith("*send.message"):
        today = date.today()
        messageCon = message.content
        log_content= open('messages.log','a+')
        log_content.write(messageCon + '  -  -  -  -  -  ' + str(today) + '\n' + '\n')
        log_content.close()
        await message.channel.send('Message sent')
        print("Message recieved:", messageCon)


client.run(token)
