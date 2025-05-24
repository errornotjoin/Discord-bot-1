import datetime

import discord
import sql_login

###

my_sql_code = sql_login.db.cursor(buffered=True)
async def Create_an_report(Type_of_report,user_name1,message,Table_number):
    DataBase_table_names = ["user_report", "bot_report"]
    Need_checks = ["Need Help", "Used Banned Word", "Used Banned Link"]
    the_time = datetime.datetime.now()
    chennels = discord_items.The_bot.get_channel(1330313688221220864)

    sql_code = f"SELECT * FROM user_report WHERE user_name = '{user_name1}' limit 1 DESC"
    my_sql_code.execute(sql_code)
    for x in my_sql_code:
        Total_banned_words = x[2]
        Total_banned_links = x[3]
        Total_help_words = x[4]

    if Type_of_report == "Need Help":    
        Total_help_words = Total_help_words + 1
    elif Type_of_report == "Used Banned Word":
        Total_banned_words = Total_banned_words + 1
    elif Type_of_report == "Used Banned Link":
        Total_banned_links = Total_banned_links + 1
    else:
        await chennels.send("An Error Has Happened, Please Contact An Admin")
        return
    for x in range(len(DataBase_table_names)):
        if DataBase_table_names[x] == "user_report":
            sql_code = f"INSERT INTO user_report (`user_name`, `Total_banned_words`, `Total_banned_links`, `Total_help_words`, `When_updated`) VALUES (%s, %s, %s, %s, %s)"
            val = (f"{user_name1}", f"{Total_banned_words }", f"{Total_banned_links}", f"{Total_help_words}", f"{the_time.strftime('%Y-%m-%d')}")
            my_sql_code.execute(sql_code, val)

        elif DataBase_table_names[x] == "bot_report":
            sql_code = f"INSERT INTO bot_report (`Name`, `Report`, `When_made`) VALUES (%s, %s, %s)"
            val = (f"{user_name1}", f"Message: {message.content}", f"{the_time.strftime('%Y-%m-%d')}")
            my_sql_code.execute(sql_code, val)
            await chennels.send(f"Report:\n {user_name1.mention} has used a banned word in channel: {message.channel.name} \n at {the_time.strftime('%X')}")
            




@discord_items.The_bot.event
async def on_ready():
    chennels = discord_items.The_bot.get_channel(1330313688221220864)
    await chennels.send("The The Great Eye Of ErrorNotJoin Is Online ✔ ")



@discord_items.The_bot.event
async def on_message(message):
    Table_number = 0 
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
          sql_code = f"SELECT user_name FROM user WHERE user_name == `{message.author}` "
          my_sql_code.execute(sql_code)
          for x in my_sql_code:
              x = str(x).replace("(", "").replace(")", "").replace(".", "").replace("[", "").replace("]", "").replace("'", "").replace(",", "")
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









discord_items.The_bot.run(discord_items.The_key)























####
