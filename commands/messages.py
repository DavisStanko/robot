from commands import media

def get_help():
    reply = "I can help you with the following commands:\n" \
            "`!help` - Displays this help message.\n" \
            "`!media` - Lists media commands.\n" \
            "`!games` - Lists game commands.\n" \
            "`!info` - Links to my GitHub page.\n" \
            "`!schedule` - Explains scheduled events.\n" \
            "`!admin` - Lists admin commands.\n"
            
    return reply

def get_admin():
    reply = "I react to the following admin commands:\n" \
            "`!setlocation [city] [country code]` - (e.g. `!setlocation Toronto CA`) - Sets the location for the server.\n" \
            "`!setnewschannel` - Sets the channel for news reports to the current channel.\n"
    
    return reply

def get_media():
    media_commands = "\n".join([f"`!{key}`" for key in media.get_commands()])
    reply = f"I react to the following media commands by sending a random media file from the specified directory:\n{media_commands}"
    return reply

def get_game():
    reply = f"I react to the following game commands:\n" \
            "`!start` - **Create a new account** with 1000 points.\n" \
            "`!points` - Display your current points.\n" \
            "`!leaderboard` - Display the top 10 users.\n" \
            "`!income` - Gain 100 points. Can only be used once every 30 minutes.\n" \
            "`!trivia` - Start a game of trivia. Correct answers give you 10 points.\n" \
            "`!wordscramble` - Start a game of word scramble. Correct answers give you 10 points per letter.\n" \
            "`!roulette [wager] [red|black|green]` - Play a game of roulette.\n" \
            "`!slots [wager]` - Play a game of slots.\n" \
            "`!NdM` - Rolls N M-sided dice where N and M are positive integers.\n"
    return reply

def get_info():
    reply = f"I react to the following info commands:\n" \
            "`!info` - Links to my GitHub page.\n"
    return reply

def get_schedule():
    reply = f"Every 6 hours I will send the current weather and top 3 news articles for the locations specified by the server owner.\n" \
            "If you are the admin and would like to set your location, please reply with `!admin`."
    return reply