from aiogram import types,Bot, Dispatcher, executor
from data import Api_Token
from buttons import asosiy_menu

bot = Bot(token=Api_Token)
dp = Dispatcher(bot)



@dp.message_handler(commands=["start"])
async def start_hendler(message:types.Message):
     await message.answer("Asalomu alaykum, bu Bot sizga turli xildagi xabarlang yuboradi",reply_markup=asosiy_menu)


     
@dp.message_handler(text ="🎬video")
async def video_hendler(message:types.Message):
     await message.answer("Videolar toplami")
     await message.answer_video("https://t.me/alisher_sadullaev/3420")


    
@dp.message_handler(text="📷rasm")
async def rasim_hendler(message:types.Message):
     await message.answer("Rasimlar toplami")
     await message.answer_photo("https://t.me/alisher_sadullaev/3419")




 
@dp.message_handler(text ="🎧audio")
async def audio_hendler(message:types.Message):
     await message.answer("Audio toplami")
     await message.answer_audio("https://t.me/iphoneringtones/558")





@dp.message_handler(text ="🗂gif")
async def gif_hendler(message:types.Message):
     await message.answer("Gif toplami")
     await message.answer_contact("https://t.me/Warm_Mafiabs/6378")





@dp.message_handler(text ="😃stiker")
async def stiker_hendler(message:types.Message):
     await message.answer("stiker toplami")
     await message.answer_sticker("https://t.me/python_9_00/310")





@dp.message_handler(text ="📍lakatsiya")
async def lakatsiya_hendler(message:types.Message):
     await message.answer("lakatsiya toplami")
     await message.answer_location(41.33488874131714, 69.21560193048435)






if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)