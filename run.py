@bot.command(brief="Run chosen script")
async def run(ctx, script_name):
    script_path = f'{script_name}'
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    if result.returncode == 0:
        await ctx.send(f"Script '{script_name}' executed successfully.\nOutput:\n```\n{result.stdout}\n```")
    else:
        await ctx.send(f"Error executing script '{script_name}'.\nOutput:\n```\n{result.stderr}\n```")