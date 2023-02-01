from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

asosiy_menu =ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎧audio"),
            KeyboardButton(text="🎬video"),
            KeyboardButton(text="📷rasm")
        ],
        [
            KeyboardButton(text="😃stiker"),
            KeyboardButton(text="🗂gif"),
            KeyboardButton(text="📍lakatsiya")
        ]
    ],
    resize_keyboard=True
)