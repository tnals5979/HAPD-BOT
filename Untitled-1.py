# 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
import discord, asyncio, pytz, datetime

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("제작자 : 한숲#1234"))

@client.event
async def on_message(message):
    if message.content.startswith ("!청소"):
        if message.author.guild_permissions.administrator:
            amount = message.content[4:]
            await message.delete()
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
            embed.set_footer(text="Bot Made by. 한숲 #1234", icon_url="https://discordapp.com/channels/691615852620939274/703908401381376000/711859989177958410")
            await message.channel.send(embed=embed)
        
        else:
            await message.delete()
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))

async def on_ready(): 
  async def message(games):
    await client.wait_until_ready()

    while not client.is_closed():
        for g in games:
            await client.change_presence(status = discord.Status.online, activity = discord.Game(g))
            await asyncio.sleep(10)

  print("[ Bot Start ] \n-- 봇이 시작되었습니다 -- \n봇 제작자 : 한숲 #1234\n")
  print(("""[ Bot Info ]\n[1] Bot Name : {} \n[2] Bot Discord ID : {}""").format(client.user.name, client.user.id))
  await message(['제작자 : 한숲#1234','🙇 모든 문의 DM!'])           

@client.event
async def on_message(message):
    if message.content.startswith ("!인증 "):
        if message.author.guild_permissions.administrator:
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="인증 시스템", description="인증이 정상적으로 완료 되었습니다 !",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.add_field(name="인증 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
            embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_footer(text="Bot Made by. 한숲 #1234")
            await message.author.send (embed=embed)
            role = discord.utils.get(message.guild.roles, name = '👮‍♂️ㅣ경찰청')
            await user.add_roles(role)

        else:
            await message.delete()
            await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 권한이 없습니다", color = 0xff0000))

# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('ODc5NjEyMjAxMDcyMjE0MDE2.YSSQsw.-Wt3lPxmwO91Mhk6Ji002o-DwaM')