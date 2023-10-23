import discord

bot = discord.Client()

def run_discord_bot_01():
    TOKEN = 'MTE2NDAxMjIwODQzNTUwNzMwMQ.GH8MRA.St5BpfCWcKeaYFbDUlzsdTkS_HQb6G_aceZCdA'
    bot = discord.Client(intents=discord.Intents.all())



    @bot.client
    async def on_ready():
        print('deathgrips is online')

    @bot.event
    async def on_member_join(member):
        guild = member.guild
        guildname = guild.name
        dmchannel = await member.create_dm()
        await dmchannel.send(f"welcome to {guildname}!")
        
    @bot.event
    async def on_raw_reacton_add(payload):
        emoji = payload.emoji.name
        member = payload.member
        message_id = payload.message_id
        guild_id = payload.guild.id
        guild = bot.get_guild(guild)

        if emoji == '🕷️' and message_id == 1164708883680481300:
            role = discord.utils.get(guild.roles, name = "Marvel Fan")
            await member.add_roles(role)
    
    bot.run(TOKEN)