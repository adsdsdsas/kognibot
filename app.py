import discord
from discord.ext import commands
from os import getenv
from pathlib import Path
from dotenv import load_dotenv
# now import our own modules:
import kognicommands as kc


# create a class KogniClient that inherits from discord.Client class and add functions inside this KogniClient class
# args and kwargs just pass all agruments into the __init__ method of discord.Client class
# (super().__init__ meand discord.Client.__init__ here)
class KogniClient(commands.Bot):
    def __init__(self, *args, **kwargs):  # define __init__ method with all possible arguments
        super().__init__(*args, **kwargs)  # run discord.Client __init__ method with all arguments

    # connect with server
    async def on_ready(self):
        print(f'Logged on as {self.user}!')  # and confirm that connected successfully

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

            await self.process_commands(message)  # check if a message is a command and if it is, process it

            # command $command-list
            if message.content.startswith('$command-list'):
                await kc.command_list(message)

            # command $hemlo
            if message.content.startswith('$hemlo'):
                await kc.hemlo(message)

            # command $credits
            if message.content.startswith('$credits'):
                await kc.credits(message)

            # command $wejsciowka
            if message.content.startswith('$wejsciowka'):
                await kc.wejsciowka(self, message)

            # command build "specialization"
            if message.content.startswith('$build'):
                await kc.build(message)

            # command $guess
            if message.content.startswith('$guess'):
                await kc.guess(self, message)

            # =====================================================
            # NOW OTHER FEATURES
            # =====================================================

            # a little easter egg
            if 'pytasz dzika' in message.content.lower():
                await message.channel.send('CZY SRA W LESIE!?')  # send message
                await message.add_reaction('🐗')  # add a boar reaction

            # reaction to memes on '👽︱kosmiczne-jaja' channel
            if message.attachments != [] and message.channel.name == '👽︱kosmiczne-jaja':  # if message contains any attachments (e.g. pic, video, etc.) and is sent on that channel
                await message.add_reaction('😂')  # add a baloon face reaction

            # =====================================================
            # END OF IF STATEMENT
            # END OF on_message() method
            # END OF CLASS KogniClient
            # =====================================================


# =================================================================


# load enviroment to use it to load BOT_TOKEN later
load_dotenv()  # loads enviroment
env_path = Path('.') / '.env'  # sets enviroment path as .env file path
load_dotenv(dotenv_path=env_path)  # loads enviroment with new path (a DISCORD_BOT_TOKEN variable from .env file

# main program
if __name__ == '__main__':  # if app.py is run directly (not imported to other module) do the following block of code
    BOT_TOKEN = getenv('DISCORD_BOT_TOKEN')  # import token from .env file using os.getenv()
    bot = KogniClient(command_prefix='$')  # create new client object of class KogniClient


    # @client.event
    # async def on_ready():
    #     print(f'Logged on as {client.user}!')  # and confirm that connected successfully
    #
    # @client.event
    # async def on_message(message):
    #     if message.content.startswith('$hemlo'):
    #         await kc.hemlo(message)


    @bot.command()
    async def elu(ctx, arg):
        await ctx.send(f'{arg}wina')

    @bot.command()
    async def login_logs(ctx):
        await kc.login_logs(ctx, bot)





    bot.run(BOT_TOKEN)  # run using bot token imported above
