import random
from datetime import datetime, time, timedelta



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



async def bias_of_the_day(channel):
    WHEN = await rand_when()    # await get_when będzie i będzie odczytywać z pliku to WHEN
    NOW = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(WHEN)
    print(NOW)
    if NOW == WHEN: # if now (in string format "hh:mm") is WHEN time
        await channel.send('hejka tu <@!916014586786897921>') # send message
        # with open file:
        #     save rand_when()
        # i wsm chyba tyle
        # jest pętla i ona sprawdza czy jest teraz ta data i godzina
        # i jeśli jest to wysyła wiadomość i generuje nową datę i godzinę (jutro)
        # teraz TODO: jak zrobić by oznaczało te błędy poznawcze, które już były
        # np. log 15 ostatnich i update pliku o jedną linijkę i spradzanie czy w tym logu jest wylosowany błąd


async def rand_when():
    hh = random.randint(10, 18) # random hour
    mm = random.randint(0, 59)  # random minute
    WHEN = datetime.combine(datetime.now().date() + timedelta(days=1), time(hour=hh, minute=mm)).strftime("%Y-%m-%d %H:%M")
    return WHEN




        # if dt.now().strftime("%H:%M") == "16:28":
        #     print('stopping the loop')
        #     cognitive_bias_of_the_day.stop()

# WHEN = time(13, 00, 00)
# channel_id = 781633200522002452

# async def called_once_a_day(chan):  # Fired every day
#     # await bot.wait_until_ready()  # Make sure your guild cache is ready so the channel can be found via get_channel
#     channel = chan
#     await channel.send("your message here")

# async def background_task(chan):
#     now = datetime.utcnow()
#     if now.time() > WHEN:  # Make sure loop doesn't start after {WHEN} as then it will send immediately the first time as negative seconds will make the sleep yield instantly
#         tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
#         seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
#         await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start
#     while True:
#         now = datetime.utcnow() # You can do now() or a specific timezone if that matters, but I'll leave it with utcnow
#         target_time = datetime.combine(now.date(), WHEN)  # 6:00 PM today (In UTC)
#         seconds_until_target = (target_time - now).total_seconds()
#         await asyncio.sleep(seconds_until_target)  # Sleep until we hit the target time
#         await called_once_a_day(chan)  # Call the helper function that sends the message
#         tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
#         seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
#         await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start a new iteration
