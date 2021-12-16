# TODO: maybe try to change the code to create commands with this extension: https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html

import discord, random
from discord.ext import commands
from asyncio import TimeoutError
from os import getenv
from pathlib import Path
from dotenv import load_dotenv
import Gw2

# load enviroment to use it to load BOT_TOKEN later
load_dotenv()  # loads enviroment
env_path = Path('.') / '.env'  # sets enviroment path as .env file path
load_dotenv(dotenv_path=env_path)  # loads enviroment with new path (a DISCORD_BOT_TOKEN variable from .env file


# create a class KogniClient that inherits from discord.Client class and add functions inside this KogniClient class
# args and kwargs just pass all agruments into the __init__ method of discord.Client class
# (super().__init__ meand discord.Client.__init__ here)
class KogniClient(discord.Client):
    def __init__(self, *args, **kwargs):  # define __init__ method with all possible arguments
        super().__init__(*args, **kwargs)  # run discord.Client __init__ method with all arguments
        self.command_list = {  # list of all available commands with descriptions (used in $command-list)
            '$command-list': 'lists all commands of KogniBot',
            '$hemlo': 'says Hemlo World!',
            '$guess': 'lets u play a simple guessing game',
            '$credits': 'displays credits for KogniBot creators',
            '$wejsciowka': 'invites u to wejsciowka'
        }

    bot = commands.Bot(command_prefix='$')

    @bot.command()
    async def testy(self, ctx):
        print(ctx)

    # connect with server
    async def on_ready(self):
        print(f'Logged on as {self.user}!')  # and confirm that connected successfully

    # run every time someone sends a message
    async def on_message(self, message):  # if someone sends a message
        print(f'Message from {message.author}: {message.content}')  # first print the message in the console
        # TODO: DELETE ABOVE LINE IN THE END OF DEVELOPMENT

        if message.author.id == self.user.id:  # we do not want the bot to reply to itself
            pass  # if message.author == @KogniBot

        if message.content.startswith('$command-list'):  # command $command-list
            for x, y in self.command_list.items():
                await message.channel.send(f'{x} - {y}')

        if message.content.startswith('$hemlo'):  # command $hemlo
            await message.channel.send('Hemlo World!')

        if message.content.startswith('') and message.channel.name == '👽︱kosmiczne-jaja':  # reaction to meme
            await message.add_reaction('😂')  # add a baloon face reaction

        if message.content.startswith('$wejsciowka'):  # command $wejsciowka
            await message.channel.send('SZANOWNI PAŃSTWO')
            try:
                await self.wait_for('message', timeout=4)  # wait 2 seconds
            except TimeoutError:  # asyncio.TimeoutError
                pass
            finally:
                await message.channel.send('ZAPRASZAM NA WEJŚCIÓWKĘ!')
                await message.channel.send(
                    'https://b.socrative.com/login/student/\nW polu room name proszę wpisać ANDRZEJ5101')
                await message.channel.send('POWODZENIA!!!')

        if message.content.startswith('$credits'):  # command $credits
            await message.channel.send(
                'KogniBot developed by:\nBartosz Bizański @bizon#8563\nMichał Kaczmarek @MurzyN#9695\nJakub Karp @quni#8918\n Kamil Małecki @Ærooo#5807\nJulia Mika @Julcia#3267')

        if message.content.lower().startswith('pytasz dzika'):  # a little easter egg
            await message.channel.send('CZY SRA W LESIE!?')
            await message.add_reaction('🐗')  # add a boar reaction

        if message.content.startswith('$guess'):  # command $guess
            await message.channel.send('Guess the number between 1 and 9')

            def is_correct(m):  # define how to check if the answer message is correct
                return m.author == message.author and m.content.isdigit()  # check if the author is the same and if the message is a digit

            answer = random.randint(1, 10)  # generate random number

            try:
                guess = await self.wait_for('message', check=is_correct,
                                            timeout=5.0)  # if message is correct and sent in five seconds, guess = message
            except TimeoutError:  # asyncio.TimeoutError
                return await message.channel.send(
                    'Sorry, you took too long it was {}'.format(answer))  # if not or time passed

            if int(guess.content) == answer:  # if the answer is correct
                await message.channel.send('You are right!')  # congrats
            else:  # if not:
                await message.channel.send('Oop- it is actually {}'.format(answer))

            if message.content.startswith('$build'):
                parts = message.content.split(' ')
                build_link = Gw2.get_build(parts[1], parts[2])
                await client.send_message(message.channel, build_link)


if __name__ == '__main__':
    BOT_TOKEN = getenv('DISCORD_BOT_TOKEN')  # import token from .env file using os.getenv()
    client = KogniClient()
    client.run(BOT_TOKEN)




    # TODO: dokończyć
