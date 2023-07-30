import os
from twitchio.ext import commands
from dotenv import load_dotenv

load_dotenv()


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            token=os.environ['TMI_TOKEN'],
            client_id=os.environ['CLIENT_ID'],
            nick=os.environ['BOT_NICK'],
            prefix=os.environ['BOT_PREFIX'],
            initial_channels=[os.environ['CHANNEL']]
        )


    async def event_ready(self):
        print(f"{os.environ['BOT_NICK']} is online!")
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')


    @commands.command(name='test')
    async def test(self, ctx):
        await ctx.send('test passed!')


    @commands.command(name='goose')
    async def goose(self, ctx):
        f = open('messages/goose.txt', 'r')
        for line in f.readlines():
            await ctx.send(line)


bot = Bot()
bot.run()
