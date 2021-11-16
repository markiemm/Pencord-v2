from os import popen
from discord import user
from discord.ext import commands
import discord
import whois


class Whois(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def whois(self, message, userinput):
        domain = whois.whois(userinput)
        embed=discord.Embed(title="test", description=domain, color=0xff0000)
        await message.send(embed=embed)
        


def setup(client):
    client.add_cog(Whois(client))
