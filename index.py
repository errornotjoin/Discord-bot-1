#-------------------Download Files----------------------#
#you need to install these files to get the bot working
import datetime
import discord
#-------------------------------------------------------#

#---------------loacl files----------------------#
#discord_items holds the discord bot API KEY
#sql_login Holds the Sql Connects to the database 
import discord_items
import sql_login
#-------------------------------------------------#

#--------------the discord bot API----------------#
#saveing the Bot Here
the_Discord_bot = discord_items.The_bot
#-------------------------------------------------#

#--------------the DateTime Here----------------#
#this is just to get the date and time of the report
The_date = datetime.datetime.now()
#-------------------------------------------------#
##-----you Will Need To Change these List----------#
#safe chennels is where the bot can't read the messages

Safe_Chennels = []
#tables are sql tables where the data is safe 
list_of_tables = ["banned_words", "banned_link"]
##-------------------------------------------------#


the_time = datetime.datetime.now()
my_sql_code = sql_login.db.cursor(buffered=True)

async def Create_an_report(Name_of_table, The_message):
   sql_code = f"SELECT {The_message.author} FROM user_report WHERE User_ID = {The_message.author}"
   my_sql_code.execute(sql_code)
   if my_sql_code.fetchone() is None:
         sql_code = f"INSERT INTO user_report (User_Name, Reported) VALUES ({The_message.author}, '', '', '')"
         my_sql_code.execute(sql_code)
   for x in my_sql_code:
    if Name_of_table == "banned_words":
         print("User Has Entered A Banned Word")
    elif Name_of_table == "banned_link":
        print("User Has Entered A Banned Link")
       
            




@the_Discord_bot.event
async def on_ready():
    #this just say if the bot is online
    #and also adds the channels that are safe to the list
    #change the channel ID (That is in your server) to make sure that the bot doesn't read the messages from those channels
    Report_channel = discord_items.The_bot.get_channel(1330313688221220864)
    Welcome_channel = discord_items.The_bot.get_channel(1256071306256973879)
    Safe_Chennels.append(Report_channel)
    Safe_Chennels.append(Welcome_channel)
    await Report_channel.send("The The Great Eye Of ErrorNotJoin Is Online ✔ ")



@the_Discord_bot.event
async def on_message(message):
    try:
        #this is just to make sure that it can't send message to itself or to the chennels that you said are safe 
        if message.author == the_Discord_bot or message.author.id == 1330282462722527242:
            print("                                _____")
            print("_______________________________/Error\_______________________________________\n")
            print(f"I can't send messages to my self. Time Of Report: {the_time.strftime('%X')}")
            print("_____________________________________________________________________________\n")
            return
        elif message.channel.id == Safe_Chennels[0]:
            print("                                _____")
            print("_______________________________/Error\_______________________________________\n")
            print(f"Can't check messages from {message.channel.name} Channel. Time OF Report: {the_time.strftime('%X')}")
            print("_____________________________________________________________________________\n")
            return
    except:
        #just in case there an error 
        await  Errors("Unkown ID or Chennel", 62, 72)
    try:
        for x in range(len(list_of_tables)):
            sql_code = f"SELECT Name FROM {list_of_tables[x]}"
            my_sql_code.execute(sql_code)
            for y in my_sql_code:
                Remove_items = str(y).replace(",", "").replace("[", "").replace("]", "").replace("'", "").replace("(", "").replace(")", "")
                if Remove_items.lower() in message.content.lower():
                    print("User has Enter That Has Been Banned From The Server")
                    await Create_an_report(list_of_tables[x], message)
                elif Remove_items not in message.content.lower():
                    print("Cheeking for something")
    except:
        await Errors("Error With SQL", 77, 88)
    


@the_Discord_bot.event
async def on_member_join(member):
#this is just to add the user to the database if they are not already in it
#And Till the User Where to go to full access the server
   sql_code = f"SELECT {member.author} FROM user_report WHERE user_name = {member.author}"
   my_sql_code.execute(sql_code)
   if my_sql_code.fetchone() is None:
        sql_code = f"INSERT INTO user_report (User_Name, banned_word, Banned_Link, When_added ) VALUES ({member.author}, '0', '0', {The_date.strftime("%Y-%m-%d")} )"
        my_sql_code.execute(sql_code)
   else:
        print("User Already In The Database")
    

@the_Discord_bot.event
async def on_member_remove(member):
#this need to be redo
 print("Someone has Left")

async def Errors(Type_of_error, Line_start, Line_Ends):
    await Safe_Chennels[0].send(f"{Type_of_error}\nLine:{Line_start} To Line:{Line_Ends}" )




#----------turns on the discord bot-------------
# you may need to change this is you are useing 
# a diffrent file or name for the API KEY 
discord_items.The_bot.run(discord_items.The_key)
#-----------------------------------------------



