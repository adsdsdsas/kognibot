import discord, random
from asyncio import TimeoutError
from os import getenv
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

'''maybe try to change the code to create commands with this extension: https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html'''

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.command_list = {                                    # list of all available commands with descriptions
            'k$list': 'lists all commands of KogniBot',
            'k$hell': 'says Hello World!',
            'k$guess': 'lets u play a simple guessing game',
            'k$credits': 'displays credits for KogniBot creators'
        }


    # connect with server
    async def on_ready(self):
        print(f'Logged on as {self.user}!')                 # and confirm that connected successfully


    # run every time someone send a message
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')      # print the message in the console

        if message.author.id == self.user.id:               # we do not want the bot to reply to itself
            return

        if message.content.startswith('k$list'):             # command k$list
            for x, y in self.command_list.items():
                await message.channel.send(f'{x} - {y}')

        if message.content.startswith('k$hell'):             # command k$hell
            await message.channel.send('Hello World!')

        if message.content.startswith('k$credits'):             # command k$credits
            await message.channel.send('KogniBot developed by:\nBartosz Bizański @bizon#8563\nMichał Kaczmarek @MurzyN#9695\nJakub Karp @quni#8918\n Kamil Małecki @Ærooo#5807\nJulia Mika @Julcia#3267')

        if message.content.lower().startswith('pytasz dzika'):             # a little easter egg
            await message.channel.send('CZY SRA W LESIE!?')
            await message.add_reaction('🐗')                               # add a boar reaction

        if message.content.startswith('k$guess'):            # command k$guess
            await message.channel.send('Guess the number between 1 and 9')

            def is_correct(m):                              # define how to check if the answer message is correct
                return m.author == message.author and m.content.isdigit()       # check if the author is the same and if the message is a digit

            answer = random.randint(1, 10)                  # generate random number

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)                           # if message is correct and sent in five seconds, guess = message
            except TimeoutError:                # asyncio.TimeoutError
                return await message.channel.send('Sorry, you took too long it was {}'.format(answer))         # if not or time passed

            if int(guess.content) == answer:                                    # if the answer is correct
                await message.channel.send('You are right!')                    # congrats
            else:                                                               # if not:
                await message.channel.send('Oop- it is actually {}'.format(answer))











if __name__ == '__main__':
    BOT_TOKEN = getenv('DISCORD_BOT_TOKEN')              # import token from .env file using os.getenv()
    client = MyClient()
    client.run(BOT_TOKEN)