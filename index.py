from dotenv import dotenv_values
import nextcord, logging, os
from nextcord.ext import commands

config = dotenv_values(".env")
TOKEN = config['TOKEN']
PREFIX = config['PREFIX']

intentsa = nextcord.Intents().all()
client = commands.Bot(command_prefix= f"{PREFIX}", Intents=intentsa)


# Cogs 불러오기
print('\033[93m-------------------------------------')
for filename in os.listdir("Cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"Cogs.{filename[:-3]}")

# 봇이 성공적으로 시작하면 출력하는 문구
@client.event
async def on_ready():
    print('\033[93m-------------------------------------\u001b[37m')
    print("\033[95mSystem login SUCCESS\u001b[37m")
    server_count = len(client.guilds)
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name=f'{PREFIX}help | {server_count} Guilds'))

@client.event
async def on_command_error(ctx, error):
    logger.warning(f'\033[91m{error}\u001b[37m')

# 로깅 설정 ( 로깅 기능이 필요없으면 32~38줄을 지워도 됩니다! :)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s %(levelname)s] [%(name)s]: %(message)s', datefmt='%H:%M:%S')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# Client 로그인
client.run(TOKEN)
