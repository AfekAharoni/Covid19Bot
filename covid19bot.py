import discord
from discord.ext import commands
import db
import website
import datetime

client = commands.Bot(command_prefix="$")
TOKEN = "yourtoken"


@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")
    print("------")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    user = message.author.name
    msg = message.content
    print(f"{user} said {msg}")
    await client.process_commands(message)


async def chng_pr():
    ''' change status'''
    await client.wait_until_ready()
    status = "$covid19 for information"
    while not client.is_closed():
        await client.change_presence(activity=discord.Game(status))
        break


@client.command()
async def covid19(ctx):
    covid19_data = website.get_data("https://corona.mako.co.il/")
    connection = db.create_connection('covid19.db')
    query = f"""INSERT INTO covid19 (daily_man_sick, daily_infection_coefficient, man_vaccine, man_total_vaccine, date) 
    VALUES ('{covid19_data[0]}', '{covid19_data[1]}', '{covid19_data[2]}', '{covid19_data[3]}', '{covid19_data[4]}');"""
    db.execute_on_db(connection, query)
    query = "SELECT * from covid19"
    list_of_info = db.execute_read_query(connection, query)
    db.close_connection(connection)
    for index in range(len(list_of_info)):
        if list_of_info[index][5] == datetime.datetime.now().strftime("%x"):
            embed = discord.Embed(title="שגרת קורונה - תמונת מצב עדכנית!", colour=discord.Color.from_rgb(255, 0, 0),
                                  url='https://corona.mako.co.il/')
            embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.add_field(name="**__חולים אתמול:__**",value=list_of_info[index][1], inline=False)
            embed.add_field(name="**__מקדם ההדבקה:__**", value=list_of_info[index][2], inline=False)
            embed.add_field(name="**__התחסנו אתמול:__**", value=list_of_info[index][3], inline=False)
            embed.add_field(name="**__התחסנו סך הכל בישראל:__**", value=list_of_info[index][4], inline=False)
            embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/SARS-CoV-2_without_background.png/1200px-SARS-CoV-2_without_background.png')
            embed.set_footer(text=f"Made By AfeK#3702, Based On Mako. Updated to {datetime.datetime.now().strftime('%d %B %Y, %H:%M')}", icon_url="https://i.imgur.com/cafvEAY.gif")
            embed.set_author(name="Covid19 Information!", icon_url='https://i2.wp.com/freepngimages.com/wp-content/uploads/2016/11/hospital-bed-transparent-background.png?w=614')
    await ctx.send(embed=embed)


client.loop.create_task(chng_pr())
client.run(TOKEN)

