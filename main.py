import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

# Bot Setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Keep-Alive Server
app = Flask('')

@app.route('/')
def home():
    return "Bot is online!"

def run_server():
    app.run(host='0.0.0.0', port=8080)

def start_server():
    server = Thread(target=run_server)
    server.daemon = True
    server.start()

# Events
@bot.event
@bot.event
async def on_ready():
    print(f'{bot.user} ist online!')
    await bot.change_presence(activity=discord.Game(name="ZYXE CASINO"))


# Starten
if __name__ == '__main__':
    start_server()
    token = os.getenv('DISCORD_TOKEN')
    bot.run(token)
