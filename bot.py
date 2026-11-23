import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = open(".env").read().strip()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Try /price bitcoin")

async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    await update.message.reply_text("Hi " + name + "!")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /price bitcoin")
        return
    coin = context.args[0].lower()
    try:
        r = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": coin, "vs_currencies": "usd"},
            timeout=10,
        )
        data = r.json()
        if coin in data:
            await update.message.reply_text(coin + ": $" + str(data[coin]["usd"]))
        else:
            await update.message.reply_text("Coin not found. Try bitcoin or ethereum.")
    except Exception:
        await update.message.reply_text("Could not get the price. Try again later.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hi", hi))
app.add_handler(CommandHandler("price", price))
print("Bot running...")
app.run_polling()
