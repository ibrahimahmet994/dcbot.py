import discord
from discord.ext import commands
import random
import os

description = '''Bir Discord sohbet botu örneği.
Bu bot, çeşitli yardımcı komutları sergileyerek Discord için etkileşimli özellikler sunar.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
@bot.command()
async def lig(ctx):
    """Dünyadaki bazı büyük futbol liglerindeki takımları listeler."""
    leagues_teams = {
        "Premier League": ["Manchester City", "Liverpool", "Chelsea", "Arsenal", "Manchester United"],
        "La Liga": ["Real Madrid", "Barcelona", "Atletico Madrid", "Sevilla", "Valencia"],
        "Bundesliga": ["Bayern Munich", "Borussia Dortmund", "RB Leipzig", "Bayer Leverkusen", "Union Berlin"],
        "Serie A": ["Juventus", "Inter Milan", "AC Milan", "Napoli", "Roma"],
        "Ligue 1": ["Paris Saint-Germain", "Marseille", "Lyon", "Monaco", "Lille"],
        "Süper Lig": ["Galatasaray", "Fenerbahçe", "Beşiktaş", "Başakşehir"]
    }

    message = "**Dünyadaki bazı büyük futbol ligleri ve En Büyük takımları:**\n"
    for lig, teams in leagues_teams.items():
        message += f"\n**{lig}**: {', '.join(teams)}"

    await ctx.send(message)
    
@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """İki sayıyı toplar."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Zar atar. Format: NdN"""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format NdN şeklinde olmalı!')
        return
    result = ', '.join(str(random.randint(1, limit)) for _ in range(rolls))
    await ctx.send(result)

@bot.command(description='Başka bir şekilde karar vermek için.')
async def choose(ctx, *choices: str):
    """Birden fazla seçenek arasından rastgele seçim yapar."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='Tekrar ediliyor...'):
    """Bir mesajı belirli bir kez tekrarlar."""
    for _ in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Bir üyenin sunucuya ne zaman katıldığını söyler."""
    await ctx.send(f'{member.name}, {discord.utils.format_dt(member.joined_at)} tarihinde katıldı.')

@bot.group()
async def cool(ctx):
    """Bir kullanıcının havalı olup olmadığını söyler."""
    if ctx.invoked_subcommand is None:
        await ctx.send(f'Hayır, {ctx.subcommand_passed} havalı değil.')

@cool.command(name='bot')
async def _bot(ctx):
    """Bot havalı mı?"""
    await ctx.send('Evet, bot havalı.')


bot.run("TOKEN")

