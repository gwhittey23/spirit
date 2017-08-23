def is_event(message):
    """Check if a message contains event data"""
    if len(message.embeds) > 0:
        embed = message.embeds[0]
        return (message.channel.name == 'upcoming-events'
                and embed.fields
                and embed.fields[0]
                and embed.fields[1]
                and embed.fields[2]
                and embed.fields[0].name == "Time"
                and embed.fields[1].name.startswith("Accepted")
                and embed.fields[2].name.startswith("Declined"))


def is_admin(user, channel):
    """Check if the user has admin privileges"""
    if channel.permissions_for(user).administrator:
        return True

def is_int(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b
