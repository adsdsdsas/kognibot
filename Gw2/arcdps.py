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
from kognibot.kognicommands import deletemessage


async def login_logs(ctx, bot):
    await deletemessage(ctx)
    # with open('Logs/logs.json', 'r') as logs_data:
    #     logs = json.load(logs_data)
    with open('Gw2/Logs/user.json', 'r') as user_info:
        key = json.load(user_info)
    key['id'] = ctx.author.id
    bot.owner_id = ctx.author.id
    key['name'] = ctx.author.name
    await bot.update_status(key['name'])

    confirmed = False
    while len(bot.owner_filepath) == 0 or not confirmed:
        out = 'Please use the file explorer to select your arcdps.cbtlogs folder.'
        try:
            target = await ctx.author.send(out)
        except discord.Forbidden:
            target = await ctx.send(out)
        root = Tk()
        root.withdraw()
        key['filepath'] = filedialog.askdirectory(initialdir="/", title="Select your arcdps.cbtlogs folder")
        bot.owner_filepath = key['filepath']

        try:
            message = await ctx.author.send(
                'Your selected filepath is:\n```{}\nClick ✅ to confirm, ❌ to reselect```'.format(
                    bot.owner_filepath))
        except discord.Forbidden:
            message = await ctx.send('Your selected log order is:\n```{}\nClick ✅ to confirm, ❌ to reselect```'.format(
                bot.owner_filepath))
        await message.add_reaction('✅')
        await message.add_reaction('❌')

        def r_check(r, user):
            return user == ctx.author and r.count > 1

        ans, user = await bot.wait_for('reaction_add', check=r_check)
        if str(ans.emoji) == '✅':
            confirmed = True
        await message.delete()
        await target.delete()

    with open('Logs/user.json', 'w') as user_info:
        json.dump(key, user_info, indent=4)
    target = await ctx.send('Login successful ✅ : Ready to upload logs.')
    bot.clear_list.append(target)

