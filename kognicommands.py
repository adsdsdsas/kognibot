import random
from asyncio import TimeoutError
# now import our own modules:
from kognibot.Gw2 import Gw2
from kognibot.Gw2 import arcdps

COMMAND_DICT = {  # list of all available commands with descriptions (used in $command-list)
    '$command-list': 'lists all commands of KogniBot',
    '$hemlo': 'says Hemlo World!',
    '$credits': 'displays credits for KogniBot creators',
    '$wejsciowka': 'invites u to wejsciowka',
    '$build "name of specialization"': 'Shows SC link to specialization builds site',
    '$guess': 'lets u play a simple guessing game'
}

CREDITS = '''<@!916014586786897921> developed by:
Bartosz Bizański <@!693551445139521587>
Michał Kaczmarek <@!278522018805186563>
Jakub Karp <@!263730543827484672>
Kamil Małecki <@!534446289396695053>
Julia Mika <@!782601330229248030>'''

async def deletemessage(ctx):
    guild = ctx.guild
    if guild is None:
        has_perms = False
    else:
        has_perms = ctx.channel.permissions_for(guild.me).manage_messages
    if has_perms:
        await ctx.message.delete()
    else:
        await ctx.send('I do not have permissions to delete messages.')


async def command_list(m):
    for x, y in COMMAND_DICT.items():  # for every pair of key and value in dictionary do the following
        await m.channel.send(f'{x} - {y}')  # send message with pattern: $command - description


async def hemlo(m):
    await m.channel.send('Hemlo World!')  # send message


async def credits(m):
    await m.channel.send(CREDITS)  # send message


async def wejsciowka(self, m):
    await m.channel.send('SZANOWNI PAŃSTWO')  # send message
    try:  # try to do the following
        await self.wait_for('m',
                            timeout=4)  # wait 2 seconds, if someone wrote something, break; if time passed, raise asyncio.TimeoutError
    except TimeoutError:  # if asyncio.TimeoutError raised
        pass  # do nothing
    finally:  # execute no matter if asyncio.TimeoutError raised or not
        await m.channel.send('ZAPRASZAM NA WEJŚCIÓWKĘ!')  # send message
        await m.channel.send(
            'https://b.socrative.com/login/student/\nW polu room name proszę wpisać ANDRZEJ5101')  # send message (\n - new line)
        await m.channel.send('POWODZENIA!!!')  # send message


async def build(m):
    parts = m.content.split(
        ' ')  # make a list containing every word (each string separated by spaces) in message as a separate value
    build_link = Gw2.get_build(parts[1])  # set build_link as the return of get_build() function from Gw2 module
    await m.channel.send(build_link)  # send message wih build_link

async def login_logs(ctx, bot):
    await arcdps.login_logs(ctx, bot)



# ==============================

async def guess(self, message):
    await message.channel.send('Guess the number between 1 and 9')  # send message

    def is_correct(m):  # define how to check if the answer message is correct
        return m.author == message.author and m.content.isdigit()  # check if the author is the same and if the message is a digit

    answer = random.randint(1, 9)  # generate random number
    # print(answer) # used to check the answer while developing this feature

    try:  # try to do the following
        guess = await self.wait_for('message', check=is_correct,
                                    timeout=5.0)  # if message is correct and sent in five seconds, guess = message
    except TimeoutError:  # if time passed, asyncio.TimeoutError is raised and the following is done
        return await message.channel.send(f'Sorry, you took too long it was {answer}')  # send message

    if int(guess.content) == answer:  # if the answer is correct
        await message.channel.send('You are right!')  # send congrats
    else:  # if not:
        await message.channel.send('Oop- it is actually {answer}')  # send message
