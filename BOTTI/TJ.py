#BOT
import asyncio
import discord
from discord.ext import commands, tasks
import datetime as dt
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
TOKEN = ""

today = dt.date.today()
target = dt.date(2023,7,31)
now = dt.datetime.now()
sender = False
velat = False

channelID = 1099777363593670686
bottestID = 1103303569333043270


def counter(start, end):
    fdate = start
    ldate = end

    delta = ldate - fdate
    final = delta.days
    return final


#Tasks
time = dt.time(hour=5, minute=0)
testtime = dt.time(hour=16, minute=10)
@bot.event
async def on_ready():
    called_once_a_day.start()
    bot.loop.create_task(called_once_a_day())


@tasks.loop(time=time)
async def called_once_a_day():
    if sender == True:
        date = today.strftime("%d/%m/%Y")
        tj = counter(today, target)
        message_channel = bot.get_channel(bottestID)
        print(f"Got channel {message_channel}")
        await message_channel.send("TÄNÄÄN: " + date)
        await message_channel.send("TJ: " + str(tj))
        if velat == False:
            await message_channel.send("Emil maksa velat!")

@called_once_a_day.before_loop
async def before():
    for _ in range(60*60*24):
        if dt.datetime.now().hour == 16:
            sender = True
            return
        await asyncio.sleep(1)

#Commands

# @bot.command()
# async def tj(ctx):
#     date = today.strftime("%d/%m/%Y")
#     tj = counter(today, target)
#     await ctx.send("TÄNÄÄN: " + date)
#     await ctx.send("TJ: " + str(tj))
#     if tj == 1:
#         pass
    
# @bot.command()
# async def Emil(ctx):
#     await ctx.send("Emil maksa velat")

bot.run(TOKEN)
