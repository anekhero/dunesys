# main.py
import os
from flask import Flask
from threading import Thread
import discord
from discord.ext import commands

# Flask web server to keep bot alive
def keep_alive():
    app = Flask('')

    @app.route('/')
    def home():
        return "I'm alive!"

    def run():
        app.run(host='0.0.0.0', port=8080)

    Thread(target=run).start()

# Setup intents and bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Run everything
keep_alive()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
