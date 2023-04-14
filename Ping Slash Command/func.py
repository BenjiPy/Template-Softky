@bot.tree.command(name="ping", description="Pong !")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong! {round (bot.latency * 1000)} ms', ephemeral=True)