import os
from twitchio.ext import commands
from dotenv import load_dotenv

load_dotenv()


# set up the bot
bot = commands.Bot(
    token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)


@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")


@bot.event
async def event_message(ctx):
    print(ctx.author.name)



@bot.command(name='test')
async def test(ctx):
    await ctx.send('test passed!')


@bot.command(name='goose')
async def goose(ctx):
    f = open('messages/goose.txt', 'r')
    for line in f.readlines():
        await ctx.send(line)


if __name__ == '__main__':
    bot.run()
