import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
import logging

# Replace 'YOUR_TOKEN' with your bot token
TOKEN = 'YOURTOKEN'

# Set up logging
logging.basicConfig(level=logging.INFO)

# Get Raspberry Pi CPU temperature
def get_cpu_temp():
    return os.popen("vcgencmd measure_temp").readline().strip().replace("temp=", "")

# Handle the /start command
async def start(update: Update, context):
    logging.info(f"Accessed by: {update.effective_user.first_name}")
    await update.message.reply_text('Hi! Send /temperature to check the CPU temperature.')

# Handle the /temperature command
async def temperature(update: Update, context):
    logging.info(f"Temperature requested by: {update.effective_user.first_name}")
    await update.message.reply_text(f'CPU Temperature: {get_cpu_temp()}')

# Set up the bot and commands
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("temperature", temperature))

# Start the bot
app.run_polling()