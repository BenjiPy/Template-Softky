@bot.tree.command(name="ticket", description="Ouvrir un ticket pour contacter l'administration !")
async def ticket(interaction: discord.Interaction):
    # Constantes
    MAX_TICKET_PER_USER = 1
    CATEGORY_TICKET_ID = 1096055386320158720

    # Récupération de la catégorie TICKET
    category = bot.get_channel(CATEGORY_TICKET_ID)

    # Vérification que l'utilisateur n'a pas déjà des tickets d'ouverts
    text_channel_list = [chan for chan in interaction.user.guild.text_channels if chan.topic == f'Ticket {interaction.user.id}']

    if len(text_channel_list) >= MAX_TICKET_PER_USER:
        await interaction.response.send_message(f"Vous avez déjà un ticket d'ouvert !", ephemeral=True)
    else:
        # Permissions
        overwrites = {
            interaction.user.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            interaction.user: discord.PermissionOverwrite(read_messages=True)
        }

        # Création du channel
        channel = await interaction.user.guild.create_text_channel(f'ticket-{interaction.user.name}', overwrites=overwrites, category=category, topic=f'Ticket {interaction.user.id}')

        # Réponse de l'interaction
        await interaction.response.send_message(f"Ticket Créé ! | {channel.mention} !", ephemeral=True)