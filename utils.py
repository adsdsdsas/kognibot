import random, json
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

# generate a new datetime string and save it in the file
def rand_when(today=False):
    delta = timedelta(days=1)   # date delta (set the date for tomorrow but if today=True, set it for today
    hh = random.randint(10, 18) # random hour between 10 and 18
    mm = random.randint(0, 59)  # random minute

    if today:   # when today=True do the following:
        now_hour = datetime.now().time().hour    # take current hour
        if 9 < now_hour < 18:   # if current hour is between 10 and 18
            delta = timedelta(days=0)  # set the date for today
            hh = now_hour + 1   # don't generate random hour, set it for next hour instead (with random minutes)
        else:   # if current hour is not between 10 and 18
            if now_hour < 9:    # if it's before nine o'clock
                delta = timedelta(days=0)   # set teh date for today
            hh = 10 # and set it for 10 (with random minutes) next day (or today due to above line)
            #this block if for generating random hour/minute that

    #       combine these: (          todays date +1  AND   random generated hour & minute )  and change it into str with format "YYYY-MM-DD HH:MM"
    when = datetime.combine(datetime.now().date() + delta, time(hour=hh, minute=mm)).strftime("%Y-%m-%d %H:%M")
    return when # return datetime string

# load a string with date and time for next message
def get_when():
    nowdate = datetime.now().date()     # get todays date
    today = nowdate.strftime("%Y-%m-%d")  # get todays date in format "YYYY-MM-DD"
    tomorrow = (nowdate + timedelta(days=1)).strftime("%Y-%m-%d")   # get tomorows date in format "YYYY-MM-DD"
    with open('CBotD/whenfile.csv', 'r') as whenfile:   # open a file
        when = whenfile.readline()  # read first line and pass it into when variable
    if when[:10] == today: # if when date is today
        print('today:') # TODO: del later
        return when
    elif when[:10] == tomorrow:  # if when date is tomorrow
        print('tomorrow:') # TODO: del later
        return when
    else:   # if when date isn't today nor tomorrow
        print('rand when:') # TODO: del later
        when = rand_when(today=True)    # generate a new datetime string
        with open('CBotD/whenfile.csv', 'w') as whenfile:   # write it to the file
            whenfile.write(when)
        return when     # and return it
