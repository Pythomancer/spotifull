import discord
import spotipy
from youtubesearchpython import VideosSearch
from urllib.parse import urlparse
from spotipy.oauth2 import SpotifyClientCredentials

spotifyclientid = "spotifyclientidtoken"
spotifysecret = "spotifyclientsecret"

bot = discord.Client()
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=spotifyclientid,
                                                           client_secret=spotifysecret))


@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1
    print("spotifull is in " + str(guild_count) + " guilds.")


@bot.event
async def on_message(message):
    if message.content == "cum":
        await message.channel.send("it works")
    if "https://open.spotify.com/track" in message.content:
        results = sp.track(urlparse(message.content).path[7:])
        videosSearch = VideosSearch(
            results["album"]["artists"][0]["name"] + " " + results["name"], limit=1)
        await message.reply(videosSearch.result()["result"][0]["link"])

bot.run("discordtoken")
