import discord
from discord.ext import commands
from os import getenv
from pathlib import Path
from dotenv import load_dotenv
import json
# now import our own modules:
import kognicommands as kc



# create a class KogniClient that inherits from commands.Bot class and add functions inside this KogniClient class
# args and kwargs just pass all agruments into the __init__ method of discord.Client class
# (super().__init__     means     discord.Client.__init__ here)
class KogniClient(commands.Bot):
    def __init__(self, *args, **kwargs):  # define __init__ method with all possible arguments
        super().__init__(*args, **kwargs)  # run discord.Client __init__ method with all arguments

        # some properties used in GW2 arcdps:
        # TODO: CREATE GW2 CLASS AND PUT ALL GW2 RELATED STUFF IN OTHER MODULE
        self.status_format = 'Current User: {}'
        self.emoji_list = []
        # self.clear_list = []
        with open('Gw2/Logs/user.json', 'r') as user_prop:  # open the file user.json
            user = json.load(user_prop) # and import its content to user variable
        self.owner_name = user['name']
        self.owner_id = user['id']
        self.owner_key = user['key']
        self.owner_filepath = user['filepath']

    # connect with server
    async def on_ready(self):
        print(f'Logged on as {self.user}!')  # and confirm that connected successfully

    # used in GW2 arcdps, idk how it works XD
    # TODO: CREATE GW2 CLASS AND PUT ALL GW2 RELATED STUFF IN OTHER MODULE
    async def update_status(self, name):
        self.owner_name = name
        status = discord.Game(name=self.status_format.format(name))
        await self.change_presence(activity=status)

    # run every time someone sends a message
    async def on_message(self, message):  # if someone sends a message
        print(f'Message from {message.author}: {message.content}')  # first print the message in the console
        # a developer running the bot can see every one message sent on server in every channel - #jkm-chat is not private anymore!
        # TODO: DELETE ABOVE LINE IN THE END OF DEVELOPMENT

        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:  # if message author is me
            pass  # don't do anything
        else:  # if message author is someone else
            # check if message meets any of the following conditions:

            # we want the commands defined in the end of this file to work
            await self.process_commands(message)  # check if a message is a command and if it is, process it using ext.commands

            # =====================================================
            # NOW OUR FEATURES
            # =====================================================

            # TODO: MOVE TO UTILS.PY
            # a little easter egg
            if 'pytasz dzika' in message.content.lower():
                await message.channel.send('CZY SRA W LESIE!?')  # send message
                await message.add_reaction('🐗')  # add a boar reaction

            # reaction to memes on '👽︱kosmiczne-jaja' channel
            if message.attachments != [] and message.channel.name == '👽︱kosmiczne-jaja':  # if message contains any attachments (e.g. pic, video, etc.) and is sent on that channel
                await message.add_reaction('😂')  # add a baloon face reaction


            #TODO smacznej kawusi jebać kapusi

            #TODO księżyc i słonko na dobranoc i dzien dobry/hemlo

            # =====================================================
            # END OF on_message() method and class KogniClient
            # =====================================================


# =================================================================


# load enviroment to use it to load BOT_TOKEN in the end of code
load_dotenv()  # loads enviroment
env_path = Path('.') / '.env'  # sets enviroment path as .env file path
load_dotenv(dotenv_path=env_path)  # loads enviroment with new path (a DISCORD_BOT_TOKEN variable from .env file


# MAIN PROGRAM
if __name__ == '__main__':  # if app.py is run directly (not imported to other module) do the following block of code
    BOT_TOKEN = getenv('DISCORD_BOT_TOKEN')  # import token from .env file using os.getenv()
    bot = KogniClient(command_prefix='$')  # create new client object of class KogniClient (command_prefix - what sing to use in commands)


    # -----------------------------------------------
    # NOW WE DEFINE OUR COMMANDS
    # -----------------------------------------------


    # a test command and how commands work
    @bot.command()   # change the function defined below to a bot command and add it to bot
    async def elu(ctx, arg):    # a test command $elu "something"
        await ctx.send(f'{arg}wina')    # send "something"wina


    # command $command-list
    @bot.command(name='command-list')   # name= lets us use $command-list command instead of $command_list (the name of defined function)
    async def command_list(ctx):
        await kc.command_list(ctx)


    # command $hemlo
    @bot.command()
    async def hemlo(ctx):
        await kc.hemlo(ctx)


    # command $credits
    @bot.command()
    async def credits(ctx):
        await kc.credits(ctx)


    # command $wejsciowka
    @bot.command()
    async def wejsciowka(ctx):
        await kc.wejsciowka(ctx)


    # command build "specialization"
    @bot.command()
    async def build(ctx, scpec):
        await kc.build(ctx, scpec)

    # import arcdps logs
    @bot.command()
    async def login_logs(ctx):
        await kc.login_logs(ctx, bot)

    # clearing messages
    @bot.command(aliases=['purge', 'delete', 'c'])
    @commands.has_permissions(manage_messages=True)
    async def clear(ctx, amount = 100000):
        await kc.clear(ctx, amount)

    @bot.command()
    async def kick(ctx):
        await kc.kick(ctx)



    @clear.error
    async def clear_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permissions!")


    # -----------------------------------------------
    # END OF COMMANDS
    # -----------------------------------------------

    bot.run(BOT_TOKEN)  # run using bot token imported above
