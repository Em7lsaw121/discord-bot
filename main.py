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
async def on_ready():
    print(f'{bot.user} ist online!')
    await bot.change_presence(activity=discord.Game(name="!help"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content == '!ping':
        await message.channel.send(f'Pong! {round(bot.latency * 1000)}ms')
    
    await bot.process_commands(message)

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hallo {ctx.author.name}!')

@bot.command(name='help')
async def help_command(ctx):
    embed = discord.Embed(title="Bot Commands", color=discord.Color.blue())
    embed.add_field(name="!ping", value="Zeigt die Latenz", inline=False)
    embed.add_field(name="!hello", value="Bot grüßt dich", inline=False)
    await ctx.send(embed=embed)

# Starten
if __name__ == '__main__':
    start_server()
    token = os.getenv('DISCORD_TOKEN')
    bot.run(token)
