import datetime
import discord_items
import admin_items
import discord
import sql_login

###

my_sql_code = sql_login.db.cursor(buffered=True)
banned_words = []
Safe_account = []
async def Create_an_report(Type_of_report,user_name1,message):
    the_time = datetime.datetime.now()
    chennels = discord_items.The_bot.get_channel(1330313688221220864)
    if Type_of_report == "Banned Words":
        sql_code = f"INSERT INTO bot_report (`name`, `Report`, `When_made`) VALUES (%s, %s, %s)"
        val = (f"{user_name1}",f"{user_name1} has sent Banned Word: {message.content} into {message.channel.name} channel", f"{the_time.strftime('%Y-%m-%d')}")
    elif Type_of_report == "Help Needed":
        sql_code = f"INSERT INTO bot_report (`name`, `Report`, `When_made`) VALUES (%s, %s, %s)"
        val = (f"{user_name1}",f"{user_name1} need help,  into <#{message.channel.name}> channel", f"{the_time.strftime('%Y-%m-%d')}")
    elif Type_of_report == "Banned Linked":
        sql_code = f"INSERT INTO bot_report (`name`, `Report`, `When_made`) VALUES (%s, %s, %s)"
        val = (f"{user_name1}",f"{user_name1} has sent Banned Linked: {message.content} into <#{message.channel.name}> channel", f"{the_time.strftime('%Y-%m-%d')}")
    my_sql_code.execute(sql_code,val)
    await chennels.send(f"REPORT: {message.author.mention} Has Sent {message.content} In <#{message.channel.id}> channel at {the_time.strftime('%Y-%m-%d')}")



@discord_items.The_bot.event
async def on_ready():
    my_sql_code = sql_login.db.cursor(buffered=True)
    chennels = discord_items.The_bot.get_channel(1330313688221220864)
    await chennels.send("The The Great Eye Of ErrorNotJoin Is Online ✔ ")
    sql_code = "SELECT User_name FROM admin_accounts"
    my_sql_code.execute(sql_code)
    for x in my_sql_code:
        new_x = str(x).replace("(", "").replace(")", "").replace(".", "").replace("[", "").replace("]", "").replace("'", "'").replace(".", "'")
        Safe_account.append(new_x)



@discord_items.The_bot.event
async def on_message(message):
    list_of_help_words = []
    the_time = datetime.datetime.now()
    my_sql_code = sql_login.db.cursor(buffered=True)
    chennels = discord_items.The_bot.get_channel(1330313688221220864)
    try:
        if message.author == discord_items.The_bot or message.author.id == 1330282462722527242:
            print("_____________________________________________________________________________\n")
            print(f"I can't send messages to my self. Time Of Report: {the_time.strftime('%X')}")
            print("_____________________________________________________________________________\n")
            return
        elif message.channel.id == chennels.id:
            print("_____________________________________________________________________________\n")
            print(f"Can't check messages from {message.channel.name} Channel. Time OF Report: {the_time.strftime('%X')}")
            print("_____________________________________________________________________________\n")
            return
    except:
        await chennels.send("Unable To Check These Message Beacuse An Error Has Happened")
    sql_code = "SELECT Name FROM banned_words"
    my_sql_code.execute(sql_code)
    for x in my_sql_code:
        x = str(x).replace("(", "").replace(")", "").replace(".", "").replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(x.lower())
        if x.lower() in message.content.lower():
          mess = message
          user_account = message.author
          await message.delete()
          await message.channel.send( f"{user_account.mention} You Can't Use That Word. An Report Has Been Made.")
          await Create_an_report("Banned Words",user_account,mess)
          return
    sql_code = "SELECT Name FROM banned_link"
    my_sql_code.execute(sql_code)
    for x in my_sql_code:
         x = str(x).replace("(", "").replace(")", "").replace("", "").replace("[", "").replace("]", "").replace("'", "").replace(",", "")
         if x in message.content:
          mess = message
          user_account = message.author
          await message.delete()
          await message.channel.send( f"{user_account.mention} You Can't Use That Link. An Report Has Been Made.")
          await Create_an_report("Banned Words", user_account, mess)
          return
    for x in list_of_help_words:
        if x in message.content:
         mess = message
         user_account = message.author
         await message.channel.send( f"{user_account.mention} I Sent Message To All the Mods/admins. An Report Has Been Made.")
         await Create_an_report("Banned Words",user_account,mess)

@discord_items.The_bot.event
async def on_member_join(member):
    chennels = discord_items.The_bot.get_channel(1330313688221220864)
    channel_Are_you_human = 1256078575434465361
    Report_channel = 1330313688221220864
    with open(r"imgs\WelcomeToTheServer.jpg", "rb") as f :
        welcome_imamges = discord.File(f)
        welcome_back_channel = discord.utils.get(member.guild.text_channels, name="welcome")
        await welcome_back_channel.send(f"Welcome {member.mention} to the server: goto <#{channel_Are_you_human}> to get accese the server chennels: , A report has been made", file=welcome_imamges)
    the_time = discord_items.datetime.datetime.now()

    await chennels.send(f"Report:\n {member.mention}has Joinned The Server' \n in channel: <#{Report_channel}> \n at {the_time.strftime('%X')}")
    sql_code = f"INSERT INTO bot_report (`Name` `Report`, `When_made`) VALUES (%s, %s, %s)"
    val = (f"{member}",f"{member} Has Joinned The Server", f"{the_time.strftime('%Y-%m-%d')}")
    my_sql_code.execute(sql_code,val)

    Sql_code = "UPDATE `total` SET `Number` = `Number` + 1  WHERE `ID` = 1";
    my_sql_code.execute(Sql_code)
@discord_items.The_bot.event
async def on_member_remove(member):
    chennels = discord_items.The_bot.get_channel(1330313688221220864)
    the_time = discord_items.datetime.datetime.now()

    await chennels.send(f"Report:\n {member.mention} has left The Server' \n in channel: none \n at {the_time.strftime('%X')}")

    sql_code = f"INSERT INTO bot_report (`Name` `Report`, `When_made`) VALUES (%s, %s, %s)"
    val = (member, f"{member}Has left The Server", f"{the_time.strftime('%Y-%m-%d')}")
    my_sql_code.execute(sql_code,val)

    Sql_code = "UPDATE `total` SET `Number` = `Number` - 1  WHERE `ID` = 1";
    my_sql_code.execute(Sql_code)
@discord_items.The_bot.command
async def User_report(ctx):
    admin_item_role = discord_items.utils.get(ctx.guild.roles, name="admin")
    mods_item_role = discord_items.utils.get(ctx.guild.roles, name="mods")
    if ctx.author.roles == admin_item_role:
       await ctx.send("Create The Report for the user")
    elif ctx.author.roles == mods_item_role:
       await ctx.send("Plaze Contack AM admin to create a report for ypu ")
    else:
       await ctx.send("You Don't have the correct Rolse to create an Report ")

#this send message to people when it get the code






discord_items.The_bot.run(discord_items.The_key)























####
