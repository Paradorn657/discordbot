import discord
from discord.ext import commands

token_bot = "NzM4MDA4MjI2NDU2NDA0MTAw.XyFpuA.LH4_YJFzXyrt5zL1-8nStOaEc7Q"
server_id = 450632575485083648
client = discord.Client()

people_on_server = []


bot = commands.Bot(command_prefix="!")
channels_ = ["ห้องบอส","ส่วนตัว"]
admin_bot = ["บอส#4283","BOSSBOT#7743"]

@client.event
async def on_message(message):

    id_from_client = client.get_guild(server_id)

    if str(message.channel) in channels_ and str(message.author) in admin_bot:


        if message.content == ("!hello"):
            await message.channel.send("**`HI`**")
            
        # elif message.content == ("!activate"):
        #     print("{} use !activate command".format(message.author))
        #     await message.author.voice.channel.connect()

        # elif message.content == ("!move"):
        #     print("{} use !move command".format(message.author))
        #     await message.guild.voice_client.disconnect()
        #     await message.author.voice.channel.connect()


        elif message.content == "!user" :
            await message.channel.send(f"""**`# This server have {id_from_client.member_count} Member`**""")

        # elif message.content == ("!disconnect"):
        #     # voice_client = client.voice_client_in(channel)
        #     print(message.author.voice.channel)
        #     print("{} use !disconnect command".format(message.author))
        #     server = message.guild.voice_client
        #     await server.disconnect()

        elif message.content.find("!clearbotcmd ") != -1:
            message_cmd = message.content
            limit_purge = int(message_cmd.split(" ")[1])
            text_channel = message.channel
            delete = await text_channel.purge(limit=limit_purge,check=is_have_prefix_Cmd)
            await message.channel.send(f"""**`ลบคำสั่งของบอทแล้ว !!`**""")

        elif message.content.find("!clear ") != -1:
            message_cmd = message.content
            limit_purge = int(message_cmd.split(" ")[1])
            text_channel = message.channel
            delete = await text_channel.purge(limit=limit_purge)
            await message.channel.send(f"""**`ลบข้อความแล้ว !!`**""")

        elif message.content.find("!เพิ่มยศ -") != -1:
            message_cmd = message.content
            name = message_cmd.split("-")[1]
            member = message.guild.members
            for i in member:
                user_id = str(i.discriminator)
                user = i.name
                nameandid = user+"#"+user_id
                people_on_server.append(nameandid)
            if name in people_on_server:
                admin_bot.append(name)
                await message.channel.send(f"""**`เพิ่มยศให้ {name} แล้ว !!`**""")
                print(admin_bot)  
            else:
                await message.channel.send(f"""**`ไม่มีคนชื่อ {name} ใน SERVER !!`**""")
    elif message.author not in admin_bot and "!" in message.content:
        await message.channel.send(f"""**`คุณไม่สามารถใช้คำสั่งนี้ได้ หรือคำสั่งนี้ไม่มีในบอทของเรา!!`**""")
            
def is_have_prefix_Cmd(m):
    message = m.content
    return "!" in message


client.run(token_bot)

