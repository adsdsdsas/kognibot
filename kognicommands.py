from asyncio import sleep
# now import our own modules:
from Gw2 import Gw2
from Gw2 import arcdps
from utils import deletemessage


COMMAND_DICT = {  # list of all available commands with descriptions (used in $command-list)
    '$command-list': 'lists all commands of KogniBot',
    '$hemlo': 'says Hemlo World!',
    '$credits': 'displays credits for KogniBot creators',
    '$wejsciowka': 'invites u to wejsciowka',
    '$build "name of specialization"': 'Shows SC link to specialization builds site',
    '$login_logs': '?????'  # TODO: update the description of $login_logs command
}

CREDITS = '''<@!916014586786897921> developed by:
Bartosz Bizański <@!693551445139521587>
Michał Kaczmarek <@!278522018805186563>
Jakub Karp <@!263730543827484672>
Kamil Małecki <@!534446289396695053>
Julia Mika <@!782601330229248030>'''



async def command_list(ctx):
    await deletemessage(ctx)  # delete the command message
    for x, y in COMMAND_DICT.items():  # for every pair of key and value in dictionary do the following
        await ctx.send(f'{x} - {y}')  # send message with pattern: $command - description


async def hemlo(ctx):
    await deletemessage(ctx)  # delete the command message
    await ctx.send('Hemlo World!')  # send message


async def credits(ctx):
    await deletemessage(ctx)  # delete the command message
    await ctx.send(CREDITS)  # send message


async def wejsciowka(ctx):
    await deletemessage(ctx)  # delete the command message
    await ctx.send('SZANOWNI PAŃSTWO')  # send message
    await sleep(4)  # asyncio.sleep() - wait for 4 seconds
    await ctx.send('ZAPRASZAM NA WEJŚCIÓWKĘ!')  # send message
    await ctx.send(
        'https://b.socrative.com/login/student/\nW polu room name proszę wpisać ANDRZEJ5101')  # send message (\n - new line)
    await ctx.send('POWODZENIA!!!')  # send message


# ---------------------------------------------------
# GW2 commands:

async def build(ctx, spec):
    await deletemessage(ctx)  # delete the command message
    build_link = Gw2.get_build(spec)  # set build_link as the return of get_build() function from Gw2 module
    await ctx.send(build_link)  # send message wih build_link


async def login_logs(ctx, bot):
    await deletemessage(ctx)  # delete the command message
    await arcdps.login_logs(ctx, bot)
