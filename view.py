@bot.command(brief="Shows files and folders in the directory")
async def view(ctx):
    files = os.listdir('.')
    files_str = '\n'.join(files)
    await ctx.send(f"Contents in current directory:\n```\n{files_str}\n```")