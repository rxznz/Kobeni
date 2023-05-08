@bot.command(brief="Shows contents of chosen files") 
async def read(ctx, filename):
    try:
        with open(filename, "r") as file:
            contents = file.read()
            await ctx.send(f"Current content in {filename}:\n```\n{contents}\n```")
    except FileNotFoundError:
        await ctx.send(f"File not found: {filename}")