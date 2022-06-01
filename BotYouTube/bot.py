from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import pytube
from pytube import YouTube



async def hello(update: Update, context: ContextTypes):
  await update.message.reply_text(f'Hello {update.effective_user.first_name}')
  
app = ApplicationBuilder().token('5522933104:AAFGHQKez5rXdVLvyH08ZaeWv0shqfbBiaE').build()

app.add_handler(CommandHandler("hello", hello))
async def save_video(update: Update, context: ContextTypes):
 global app
 msg = update.message.text
 print(msg)
 items = msg.split(' ')
 yt = YouTube(items[1])
 yt.streams.filter(progressive=True, file_extension='mp4')
 yt.streams.order_by('resolution')
 yt.streams.desc()
 yt.streams.first().download(output_path=r'C:\Users\User\Desktop\vid', filename='yt_video.mp4'
)
 video = open(r'C:\Users\User\Desktop\vid\yt_video.mp4', 'rb')
 await update.message.reply_video(video)
app.add_handler(CommandHandler('save', save_video))

print('server start')
app.run_polling(stop_signals=None)

