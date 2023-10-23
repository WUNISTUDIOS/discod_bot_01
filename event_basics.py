import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
intents = discord.Intents.default()
intents.typing = False


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
            return
        
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'{username} said: {user_message} ({channel})')

#     if user_message[0] == '?':
#         user_message = user_message[1:]
#         await send_message(message, user_message, is_private = True)
#     else:
#         await send_message(message, user_message, is_private = False)
    

@bot.event
async def on_member_join(member):
    guild = member.guild
    guildname = guild.name
    dmchannel = await member.create_dm()
    await dmchannel.send(f"welcome to {guildname}!")
    
@bot.event
async def on_raw_reacton_add(self, payload):
    emoji = payload.emoji.name
    member = payload.member
    message_id = payload.message_id
    guild_id = payload.guild.id
    guild = bot.get_guild(guild)

    if emoji == '🕷️' and message_id == 1164708883680481300:
        role = discord.utils.get(guild.roles, name = "Marvel Fan")
        await member.add_roles(role)

        print(f'{message_id} said: {guild} ({role})')




bot.run('MTE2NDAxMjIwODQzNTUwNzMwMQ.GH8MRA.St5BpfCWcKeaYFbDUlzsdTkS_HQb6G_aceZCdA')