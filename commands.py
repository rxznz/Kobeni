@bot.command(brief="Shows command list")
async def commands(ctx):
    commands = []
    for command in bot.commands:
        commands.append(command.name)
    command_list = '\n'.join(commands)
    await ctx.send(f"Available commands:\n```\n{command_list}\n```")
list}\n```")