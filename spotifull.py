import os
from urllib.parse import urlparse

import discord

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from youtubesearchpython import VideosSearch


spotifyclientid = os.environ["CLIENT_ID"]
spotifysecret = os.environ["CLIENT_SECRET"]

auth_manager = SpotifyClientCredentials(
    client_id = os.environ["CLIENT_ID"],
    client_secret = os.environ["CLIENT_SECRET"]
)

bot = discord.Client()
sp = spotipy.Spotify(auth_manager=auth_manager)


@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
    print(f"spotifull is in {len(bot.guilds)} guilds.")


@bot.event
async def on_message(message):
    if message.content == "cum":
        await message.channel.send("it works")
    if "https://open.spotify.com/track" in message.content:
        results = sp.track(urlparse(message.content).path[7:])
        videosSearch = VideosSearch(
            results["album"]["artists"][0]["name"] + " " + results["name"], limit=1)
        await message.reply(videosSearch.result()["result"][0]["link"])

bot.run(os.environ["TOKEN"])
