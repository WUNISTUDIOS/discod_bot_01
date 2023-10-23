import discord
import responses
# import ssl

# ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# ssl_context.check_hostname = False
# ssl_context.verify_mode = ssl.CERT_NONE
# client = discord.Client(ssl=ssl_context)


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE2NDAxMjIwODQzNTUwNzMwMQ.GH8MRA.St5BpfCWcKeaYFbDUlzsdTkS_HQb6G_aceZCdA'
    # bot = discord.Bot(intents=discord.Intents.all())
    intents = discord.Intents.default()
    intents.message_content = True
    intents.presences = True
    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        print(f'{client.user} is now running')


    @client.event
    async def on_message(message):
        username = message.author.display_name
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: {user_message} ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private = True)
        else:
            await send_message(message, user_message, is_private = False)
    
    # does not work yet, dm on server enter
    @client.event
    async def on_member_join(member):
        guild = member.guild
        guildname = guild.name
        dmchannel = await member.create_dm()
        await dmchannel.send(f"welcome to {guildname}!")
    
    @client.event
    async def on_raw_reacton_add(payload):
        emoji = payload.emoji.name
        member = payload.member
        message_id = payload.message_id
        guild_id = payload.guild.id
        guild = client.get_guild(guild)

        if emoji == '🕷️' and message_id == 1164708883680481300:
            role = discord.utils.get(guild.roles, name = "Marvel Fan")
            await member.add_roles(role)


    
    client.run(TOKEN)
