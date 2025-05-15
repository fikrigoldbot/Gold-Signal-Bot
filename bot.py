import yfinance as yf
import ta
import pandas as pd
import schedule
import time
from telegram import Bot
from datetime import datetime

TELEGRAM_TOKEN = "ضع_توكن_البوت_هنا"
CHAT_ID = "ضع_chat_id_هنا"

def get_gold_signal():
    try:
        df = yf.download('GC=F', interval='15m', period='1d')
        if df.empty:
            return "لا يمكن تحميل بيانات الذهب حالياً."
        df.dropna(inplace=True)
        df['EMA20'] = ta.trend.ema_indicator(df['Close'], window=20).ema_indicator()
        df['EMA50'] = ta.trend.ema_indicator(df['Close'], window=50).ema_indicator()
        df['RSI'] = ta.momentum.RSIIndicator(df['Close']).rsi()
        last = df.iloc[-1]
        prev = df.iloc[-2]

        if prev['EMA20'] < prev['EMA50'] and last['EMA20'] > last['EMA50'] and last['RSI'] < 70:
            return "توصية الذهب: شراء (BUY XAU/USD)"
        elif prev['EMA20'] > prev['EMA50'] and last['EMA20'] < last['EMA50'] and last['RSI'] > 30:
            return "توصية الذهب: بيع (SELL XAU/USD)"
        else:
            return "توصية الذهب: لا توجد فرصة حالياً"
    except Exception as e:
        return f"حدث خطأ أثناء تحليل الذهب: {e}"

def send_telegram_message(message):
    bot = Bot(token=TELEGRAM_TOKEN)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    bot.send_message(chat_id=CHAT_ID, text=f"{message}\n(الوقت: {timestamp})")

def run_bot():
    signal = get_gold_signal()
    send_telegram_message(signal)

schedule.every(1).hours.do(run_bot)

while True:
    schedule.run_pending()
    time.sleep(60)
