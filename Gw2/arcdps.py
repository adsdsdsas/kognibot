import json
import calendar
import datetime
import time
import glob
import os
import copy
import re
from tkinter import filedialog
from tkinter import *
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import requests
from deletemessage import deletemessage
from discord.utils import get


async def login_logs(ctx, bot):
    await deletemessage(ctx)
    with open('Gw2/Logs/user.json', 'r') as user_info:
        key = json.load(user_info)
    key['id'] = ctx.author.id
    bot.owner_id = ctx.author.id
    key['name'] = ctx.author.name
    await bot.update_status(key['name'])

    if len(bot.owner_filepath) == 0:

        confirmed = False
        while len(bot.owner_filepath) == 0 or not confirmed:
            target = await ctx.author.send('Please use the file explorer to select your arcdps.cbtlogs folder.')
            root = Tk()
            root.withdraw()
            key['filepath'] = filedialog.askdirectory(initialdir="/", title="Select your arcdps.cbtlogs folder")
            bot.owner_filepath = key['filepath']

            message = await ctx.author.send(
                'Your selected filepath is:\n```{}\nClick ✅ to confirm, ❌ to reselect```'.format(
                    bot.owner_filepath))
            await message.add_reaction('✅')
            await message.add_reaction('❌')

            def r_check(user, reactions):
                reactions = get(message.reactions, emoji="✅")
                print(reactions)
                if user == ctx.author and reactions == 2:
                    return True

            await bot.wait_for('reaction_add', check=r_check)

            confirmed = True
            await message.delete()
            await target.delete()

        with open('Logs/user.json', 'w') as user_info:
            json.dump(key, user_info, indent=4)
        await ctx.author.send('Login successful ✅ : Ready to upload logs.')
        # bot.clear_list.append(target)

    else:
        await ctx.author.send('You already picked up filepath.')

