from datetime import datetime

from CBotD.cbotd_utils import rand_when, get_when



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



# delete a message that run a command
async def deletemessage(ctx):
    guild = ctx.guild   # get the server where the message was send
    if guild is None:   # check if server exist (if it's not a DM)
        has_perms = False
    else:   # check if bot has permissions for deleting messages
        has_perms = ctx.channel.permissions_for(guild.me).manage_messages
    if has_perms:   # if it bot has perms
        await ctx.message.delete()  # delete message
    else:   # if no server or perms
        await ctx.send('I do not have permissions to delete messages.') # send message


# -----------------------------------------------
# COGNITIVE BIAS OF THE DAY:
# -----------------------------------------------


# function that operates the cognitive bias of the day, run in cognitive_bias_of_the_day loop in app.py
async def bias_of_the_day(channel):
    when = get_when()    # get_when będzie i będzie odczytywać z pliku to when
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(when) # TODO: del later
    print(now) # TODO: del later
    if now == when: # if now (in string format "hh:mm") is when time
        await channel.send(f'Dear ladies & gentlemans!\nI\'m glad to inform u that right now is {now}!!!') # send message    # TODO: PASS RANDOMLY GENERATED BIAS HERE
        with open('CBotD/whenfile.csv', 'w') as whenfile:   # write to the file
            whenfile.write(rand_when()) # datetime string with tomorrow date and random hour

        # i wsm chyba tyle
        # jest pętla i ona sprawdza czy jest teraz ta data i godzina
        # i jeśli jest to wysyła wiadomość i generuje nową datę i godzinę (jutro)
        # teraz TODO: jak zrobić by oznaczało te błędy poznawcze, które już były
        # np. log 15 ostatnich i update pliku o jedną linijkę i spradzanie czy w tym logu jest wylosowany błąd


