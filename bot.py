import discord
import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE2NDAxMjIwODQzNTUwNzMwMQ.Gi6aat.m4XB7KZYrV4vA9V8Ucd7nL4GPKHs9E62_bnubs'
    intents = discord.Intents.default()
    intents.message_content = True
    intents.presences = False
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
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

    
    client.run(TOKEN)

# TOKEN = 'MTE2NDAxMjIwODQzNTUwNzMwMQ.Gi6aat.m4XB7KZYrV4vA9V8Ucd7nL4GPKHs9E62_bnubs'  # Replace with your bot's token

# intents = discord.Intents.default()
# intents.typing = False
# intents.presences = False

# client = discord.Client(intents=intents)

# @client.event
# async def on_ready():
#     print(f'We have logged in as {client.user}')

# @client.event
# async def on_message(message):
#     # Avoid responding to our own messages
#     if message.author == client.user:
#         return

#     if message.content.startswith('!hello'):
#         await message.channel.send('Hello!')

# def run_discord():
#     client.run(TOKEN)

# if __name__ == '__main__':
#     run_discord()