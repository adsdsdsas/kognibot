from datetime import datetime

from CBotD.cbotd_utils import rand_when, get_when, get_bias



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
    when = get_when()    # read whe from the whenfile.csv and return it or generate new one if the date isn't today nor tomorrow
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    if now == when: # if now (in string format "hh:mm") is when time
        bias = get_bias()   # get a random bias
        await channel.send(f"Todays Cognitive Bias of the Day is: {bias['bias']}\nBias category: {bias['group']}") # send message    # TODO: Pass wikipedia link and description here
        with open('CBotD/whenfile.csv', 'w') as whenfile:   # write to the file
            whenfile.write(rand_when()) # datetime string with tomorrow date and random hour
