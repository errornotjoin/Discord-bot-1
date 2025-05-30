import mysql.connector
import datetime
import discord_items
error_has_happen = False

def Error(error_has_happen):
  
  if error_has_happen == True:
   @discord_items.The_bot.event
   async def on_ready():
      await send_error_message()
   discord_items.The_bot.run(discord_items.The_key)


async def send_error_message():
    time = datetime.datetime.now()
    chennels = discord_items.The_bot.get_channel(1330313688221220864)
    await chennels.send(f"I was Unable to connect to the Sql Server, at {time.now()}\n the file has been updated with the error that has occurred ")

@discord_items.tasks.loop(seconds=1500)
async def Reconnect():
  # This function will try to reconnect to the database every 1500 seconds (25 minutes)
  # just in case something went wrong with the connection
   if error_has_happen == True:
     Login()
   else:
     Reconnect.cancel()
def Login():
 try:
     db = mysql.connector.connect(
        host = "Localhost",
        user = "root",
        password = "",
        database = "discor",
        autocommit=True
       )
       
 except:
     error_has_happen = True
     time = datetime.datetime.now()
     print(f"Unable to Connect To The Server, on {time.now()}")
     with open("errorMessages.txt", "a") as error_file:
           error_file.write(f"\nUnable to Connect To The Server, on {time.now()}")
     Error(error_has_happen)
    

Login()