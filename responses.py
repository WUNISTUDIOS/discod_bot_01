import random

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'yo ! whats good ! '
    
    if p_message == 'roll':
        return str(random.randint(1,10))
    
    if p_message == '!help':
        return '`this is a help message...to help you`'
    
    