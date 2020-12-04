import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands import guild_only
import random
import timeago
import time
print("Bot Logging In...")

prefix1 = '!' # ENTER YOUR PREFIX HERE [DEFAULT IS !]
TOKEN = 'YOUR_TOKEN_HERE' # ENTER YOUR TOKEN HERE
GAME_NAME = 'Example Game' # WRITE WHAT YOU WANT YOUR BOT TO BE PLAYING

bot = commands.Bot(command_prefix=prefix1)
bot.remove_command('help') # DELETES ORIGINAL HELP COMMAND TO REPLACE WITH CUSTOM EMBED

@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user.name} [{bot.user.id}]')
    await bot.change_presence(activity=discord.Game(name=GAME_NAME))

@bot.command()
async def ping(ctx):
    t_1 = time.perf_counter()
    await ctx.trigger_typing()
    t_2 = time.perf_counter()
    ms = round((t_2-t_1)*1000) # grabs ping and rounds it so it's not a stupid number
    embed = discord.Embed(color=0xff0000)
    embed.add_field(name=":ping_pong: Pong!", value = f"{ms}ms")
    await ctx.send(embed=embed)

@bot.command()
async def invite(ctx):
    await ctx.send(f"{ctx.author.mention} Here is the bot invite to add to your server https://discord.com/oauth2/authorize?{bot.user.id}&scope=bot&permissions=8")

@bot.command()
async def help(ctx):
    embed = discord.Embed(color=0x00ffff)
    embed.add_field(name=f"{bot.user.name}'s Commands List", value = "`ping` `help` `invite` `ban` `kick` `choose` `jointime` `8ball`")
    await ctx.send(embed=embed)

 
@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason: str = None):
    if reason == None:
        reason = 'No Reason Provided'
    await member.kick(reason=reason)
    embed = discord.Embed(color=0x0000ff)
    embed.add_field(name=f"{user} has been kicked by {ctx.message.author}", value = f"`{reason}`")
    await ctx.send(embed=embed)

@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason: str = None):
    if reason == None:
        reason = 'No Reason Provided'
    await member.kick(reason=reason)
    embed = discord.Embed(color=0x0000ff)
    embed.add_field(name=f"{user} has been banned by {ctx.message.author}", value = f"`{reason}`")
    await ctx.send(embed=embed)
    
@bot.command()
@guild_only()
async def jointime(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.message.author
    await ctx.send(f'{member.name} joined at `{member.joined_at}`')
    
@bot.command()
async def choose(ctx, *choice: str):
    await ctx.send(f"{ctx.message.author} - I choose **{choice}**!")
    
@bot.command(aliases=["8ball"])
async def eightball(ctx):
    responses_list = ['Yes.', 'No.', 'Maybe.', 'Definitely', 'Not at all.', 'Ask me another time.']
    choice = random.choice(responses_list)
    embed = discord.Embed(color=0xFFFFFF)
    embed.add_field(name=":8ball: 8Ball Says...", value=f'`{choice}`')
    await ctx.send(embed=embed)

bot.run(TOKEN)
