import discord
from discord.ext import commands

# === CONFIG ===
BOT_TOKEN = "Token" # Bot TOken To replace "Token" To Bot Token  to work for bot 
SOURCE_CHANNEL_ID = 1408946815356899440   # replace with your source channel ID To FOrward Msg 
DEST_CHANNEL_ID   = 1270391742071312404   # Where To Forward

# Main Bot Setupppp 
intents = discord.Intents.default()
intents.message_content = True  
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_message(message: discord.Message):
    # Bot ITself Msg To Ignore 
    if message.author == bot.user:
        return

    # This Cond is For  Forarding Msg From 1 CHannel
    if message.channel.id == SOURCE_CHANNEL_ID:
        dest_channel = bot.get_channel(DEST_CHANNEL_ID)
        if dest_channel:
            # This Cond is For Message
            if message.content:
                await dest_channel.send(message.content)

            #This Cond is For Attachments 
            for attachment in message.attachments:
                await dest_channel.send(file=await attachment.to_file())

# to Runt Bot With Token Main Cond
bot.run(BOT_TOKEN)
