import discord
from discord.ext import commands
from botUtils.utils import con

con = con()


class UnloadCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        con.log(f'{ctx.author.name} ({ctx.author.id}) is attempting to unload extension {cog}...')
        try:
            self.bot.unload_extension(cog)
            con.log(f'Successfully unloaded extension {cog}.')
        except Exception as e:
            embed = discord.Embed(title='Error', description=str(e), color=0xff0000)
            await ctx.send(embed=embed)
            con.log(f"Couldn't unload extension {cog}: {e}")
        else:
            color = 0xB1FBFF
            embed = discord.Embed(title='Success', description=f'Successfully unloaded extension {cog}', color=color)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(UnloadCMD(bot))
