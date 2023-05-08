@bot.command(brief="Replace ids in id.txt")
async def id(ctx, new_text, filename):
    with open(filename, 'r') as file:
        original_contents = file.read()

    command = f"sed -i 's/[^\\n]*/{new_text}/g' {filename}"
    result = subprocess.run(command, shell=True)
    with open(filename, 'r') as file:
       new_contents = file.read()

    if result.returncode == 0:
        await ctx.send(f"Limited ID have succesfully changed from \n```\n{original_contents}\n``` to \n```\n{new_contents}\n```")
    else:
        await ctx.send(f"Error replacing ID lol")