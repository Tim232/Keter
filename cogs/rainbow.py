import asyncio
import discord
import os
from discord.ext import commands
from evs import permissions, default, http, dataIO

cachelib = "./lib/cache/"
colour = []
def cring():
    cycle = -1
    while cycle <= 1534:
        cycle += 1
        if 0 <= cycle < 256:
            red = 255
            green = cycle
            blue = 0
        if 256 <= cycle < 512:
            red = 511 - cycle
            green = 255
            blue = 0
        if 512 <= cycle < 768:
            red = 0
            green = 255
            blue = cycle - 512
        if 768 <= cycle < 1024:
            red = 0
            green = 1023 - cycle
            blue = 255
        if 1024 <= cycle < 1280:
            red = cycle - 1536
            green = 0
            blue = 255
        if 1280 <= cycle < 1536:
            red = 255
            green = 0
            blue = 1535 - cycle
        colour.append(65536 * red + 256 * green + blue)
cring()


class Rainbow(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.command()
    @commands.check(permissions.is_owner)
    async def rainbow(self, ctx, role:str):
        for r in ctx.guild.roles:
            if r.name == role:
                print("detected role")
                await ctx.send("detected role")
                cycle = -1
                f = open(cachelib + str(ctx.guild.id) + ".ccf", "w")
                f.close()
                while os.path.isfile(cachelib + str(ctx.guild.id) + ".ccf"):
                    if cycle < 1536:
                        cycle += 1
                    else:
                        cycle = 0
                    try:
                        await r.edit(color=discord.Colour(colour[cycle]))
                    except Exception:
                        return await ctx.send("For some reason, I can no longer change the role ;-;")
                    await asyncio.sleep(0.04)
        await ctx.send(f"role with the name {role} not found")
        return print(f"role with the name {role} not found")

    @commands.command()
    @commands.check(permissions.is_owner)
    async def static_halt(self, ctx):
        try:
            os.remove(cachelib + str(ctx.guild.id) + ".ccf")
            await ctx.send("Stopped all the rainbow roles in this server")
        except:
            return await ctx.send("Error has been occured while processing the command")

def setup(bot):
    bot.add_cog(Rainbow(bot))
