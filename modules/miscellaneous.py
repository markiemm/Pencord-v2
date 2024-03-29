import discord
from discord.ext import commands
from config import COMMAND_PREFIX


class Miscellaneous(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def help(self, message):
        embed=discord.Embed(title="Pencord Command List", description=f"Prefix for this server is {COMMAND_PREFIX} \nTo find out more about a command, type {COMMAND_PREFIX} help <command>`` replacing ``<command>`` with one of the commands listed below.", color=0x6647ff)
        embed.set_author(name="Pencord V2")
        embed.add_field(name="General", value="```help```", inline=True)
        embed.add_field(name="Pentesting", value="```whois```", inline=True)
        embed.set_footer(text="Command .help")
        await message.send(embed=embed)
        
        



def setup(client):
    client.add_cog(Miscellaneous(client))