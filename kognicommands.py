from asyncio import sleep
# now import our own modules:
from Gw2 import Gw2
from Gw2 import arcdps
from utils import COMMAND_DICT, CREDITS, deletemessage, bias_of_the_day



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

# a function that runs a bias_of_the_day() function from utils
async def bias_of_the_day_pass_channel(channel):
    await bias_of_the_day(channel)



# ---------------------------------------------------
# GW2 commands:

async def build(ctx, spec):
    await deletemessage(ctx)  # delete the command message
    build_link = Gw2.get_build(spec)  # set build_link as the return of get_build() function from Gw2 module
    await ctx.send(build_link)  # send message wih build_link


async def login_logs(ctx, bot):
    await deletemessage(ctx)  # delete the command message
    await arcdps.login_logs(ctx, bot)
