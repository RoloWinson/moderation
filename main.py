import disnake
from disnake.ext import commnads

import disnake
from disnake.ext import commands
import asyncio


intents = disnake.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents,test_guilds=[id вашего сервера])


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.command()
async def снятьмут(ctx, участник: disnake.Member):
    мут_роль = disnake.utils.get(ctx.guild.roles, name='Мут')  # Замените 'Мут' на имя вашей роли мута

    if мут_роль in участник.roles:
        await участник.remove_roles(мут_роль)

        log_channel_id = 1180142294607863910  # Замените на ID вашего канала
        log_channel = client.get_channel(log_channel_id)

        embed = disnake.Embed(
            title='Мут снят',
            description=f'**Модератор:** {ctx.author.mention}\n'
                        f'**Участник:** {участник.mention}',
            color=0x00FF00  # Зеленый цвет
        )

        await log_channel.send(embed=embed)
        await ctx.send(f'{участник.mention} был размучен.')

    else:
        await ctx.send(f'{участник.mention} не имеет мута.')


@client.command()
async def мут(ctx, участник: disnake.Member, срок: int, *, причина: str):
    мут_роль = disnake.utils.get(ctx.guild.roles, name='Мут')  # Замените 'Мут' на имя вашей роли мута

    if not мут_роль:
        # Если роль не существует, создаем её
        мут_роль = await ctx.guild.create_role(name='Мут')

        # Настроим разрешения для роли
        for канал in ctx.guild.channels:
            await канал.set_permissions(мут_роль, send_messages=False)

    await участник.add_roles(мут_роль, reason=причина)

    # Логирование в указанном канале
    log_channel_id = 1180142294607863910  # Замените на ID вашего канала
    log_channel = client.get_channel(log_channel_id)

    embed = disnake.Embed(
        title='Мут выдан',
        description=f'**Модератор:** {ctx.author.mention}\n'
                    f'**Участник:** {участник.mention}\n'
                    f'**Срок:** {срок} минут\n'
                    f'**Причина:** {причина}',
        color=0xFF0000  # Красный цвет
    )

    await log_channel.send(embed=embed)

    await ctx.send(f'{участник.mention} был замучен на {срок} минут по причине: {причина}')

    # Ждем указанное количество минут, затем снимаем мут
    await asyncio.sleep(срок * 3600)
    await участник.remove_roles(мут_роль)

    # Логирование снятия мута
    embed.description = f'**Модератор:** {ctx.author.mention}\n' \
                        f'**Участник:** {участник.mention}\n' \
                        f'**Снятие мута после:** {срок} минут\n' \
                        f'**Причина:** {причина}'

    await log_channel.send(embed=embed)
    await ctx.send(f'{участник.mention} был размучен после {срок} минут', delete_after=30)











@client.command()
async def снятьбан(ctx, участник: disnake.Member):
    бан_роль = disnake.utils.get(ctx.guild.roles, name='ban')  # Замените 'Мут' на имя вашей роли мута

    if бан_роль in участник.roles:
        await участник.remove_roles(бан_роль)

        log_channel_id = 1180142294607863910  # Замените на ID вашего канала
        log_channel = client.get_channel(log_channel_id)

        embed = disnake.Embed(
            title='Бан снят',
            description=f'**Модератор:** {ctx.author.mention}\n'
                        f'**Участник:** {участник.mention}',
            color=0x00FF00  # Зеленый цвет
        )

        await log_channel.send(embed=embed)
        await ctx.send(f'{участник.mention} был разбанен.')

    else:
        await ctx.send(f'{участник.mention} не имеет бана.')


@client.command()
async def бан(ctx, участник: disnake.Member, срок: int, *, причина: str):
    бан_роль = disnake.utils.get(ctx.guild.roles, name='ban')  # Замените 'Мут' на имя вашей роли мута

    if not бан_роль:
        # Если роль не существует, создаем её
        бан_роль = await ctx.guild.create_role(name='ban')

        # Настроим разрешения для роли
        for канал in ctx.guild.channels:
            await канал.set_permissions(бан_роль, send_messages=False)

    await участник.add_roles(бан_роль, reason=причина)

    # Логирование в указанном канале
    log_channel_id = 1180142294607863910  # Замените на ID вашего канала
    log_channel = client.get_channel(log_channel_id)

    embed = disnake.Embed(
        title='Бан выдан',
        description=f'**Модератор:** {ctx.author.mention}\n'
                    f'**Участник:** {участник.mention}\n'
                    f'**Срок:** {срок} дней\n'
                    f'**Причина:** {причина}',
        color=0xFF0000  # Красный цвет
    )

    await log_channel.send(embed=embed)

    await ctx.send(f'{участник.mention} был забанен на {срок} дней по причине: {причина}')

    # Ждем указанное количество минут, затем снимаем мут
    await asyncio.sleep(срок * 86400)
    await участник.remove_roles(бан_роль)

    # Логирование снятия мута
    embed.description = f'**Модератор:** {ctx.author.mention}\n' \
                        f'**Участник:** {участник.mention}\n' \
                        f'**Снятие бана после:** {срок} дней\n' \
                        f'**Причина:** {причина}'

    await log_channel.send(embed=embed)
    await ctx.send(f'{участник.mention} был разбанен после {срок} днеей', delete_after=30)

# Токен вашего бота
token = ''
client.run(token)