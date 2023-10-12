import discord 
from discord.ext import commands 
from config import settings
import requests
from io import BytesIO
import base64
from bs4 import BeautifulSoup
import random
import urllib.parse
from PIL import Image
import urllib.request
from character import commands_dict

intents = discord.Intents.default() 
intents.message_content = True

bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)

@bot.event
async def on_message(message):
    if message.channel.id == you channel id:
        await bot.process_commands(message)

@bot.command()
async def chnl(ctx,command:str):
    if command in commands_dict:
        url = f"https://somelink/{commands_dict[command]}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        image_tags = soup.find_all('img')
        image_urls = []
        for img in image_tags:
            img_url = img['src']
            img_url = img_url.replace("data:image/svg+xml;base64,", "")
            img_url = base64.b64decode(img_url).decode('utf-8')
            img_url = urllib.parse.unquote(img_url)
            img_url = img_url.split("data-u=")[1].split('"')[1]
            img_url = img_url.replace("https://somelink","https://cdn.shortpixel.ai/spai/q_lossy+ret_img+to_auto/somelink.com")
            image_urls.append(img_url)
        random_image_url = random.choice(image_urls)
        image_number = random_image_url.split("-")[1].split(".")[0]
        number = random_image_url.split("-")[-1].split(".")[0]
        message = f"{number} из {len(image_urls)}"
        await ctx.send(message)
        await ctx.send(random_image_url)
    
@bot.command()
async def rule(ctx,command: str):
        tag = command
        url = f"https://www.example.com/{random.randint(1, 10)}/{tag}+score:%3E10"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        a_id = soup.find_all('a')
        id_img = []
        for a in a_id:
            if 'id' in a.attrs:
                id_img.append(a['id'])
        new_url = f"https://www.example.com/{random.randint(1, 10)}/{tag}+score:{urllib.parse.quote('>')}10?id={random.choice(id_img)}"
        responses = requests.get(new_url)
        soup = BeautifulSoup(responses.text, 'html.parser')
        image_tags = soup.find_all('img')
        image_urls = []
        for img in image_tags:
            img_url = img['src']
            image_urls.append(img_url)
        random_urls = random.choice(image_urls)
        await ctx.send(random_urls)


    
        
   
    


    
    
names = ', '.join(commands_dict.keys())
@bot.command()
async def chnl_help(ctx):
    await ctx.send(f"```{names}```")
bot.run(settings['token']) 