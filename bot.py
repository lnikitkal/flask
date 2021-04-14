import asyncio
import random
import discord

TOKEN = "secret"


class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_message(self, message):
        global bot, user, smiles
        if message.author == self.user:
            return
        if '/help' == message.content:
            await message.channel.send(
                f"Привет, этот бот поможет ориентироваться в темах Яндекс.Лицея, снизу предстаавлены\n"
                f"  все темы и подтемы, для того что бы получить сводку по одной из них достаточно\n"
                f"  отправить сообщение с текстом '/lib[путь до темы]'\n"
                f" Например: /lib62 выведет информацию про функцию map")
            await message.channel.send(self.full_list())
        else:
            if '/lib' == message.content[:4]:
                self.library(message.content)

    def library(self, number):
        print(number)

    def full_list(self):
        list = open("list.txt", encoding="utf8")
        data = list.read()
        return data


client = YLBotClient()
client.run(TOKEN)
