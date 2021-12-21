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

