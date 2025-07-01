import os
import time
import requests

TG_TOKEN = os.getenv("BOT_TOKEN")
TG_CHAT_ID = os.getenv("CHAT_ID")
BTC_ADDRESS = os.getenv("BTC_ADDRESS")

def send_message(text):
    url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    data = {"chat_id": TG_CHAT_ID, "text": text, "parse_mode": "Markdown"}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Telegram ERROR:", e)

def get_price():
    try:
        r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT").json()
        return float(r["price"])
    except:
        return 0

def get_latest_btc_tx(address):
    url = f"https://blockchain.info/rawaddr/{address}"
    try:
        r = requests.get(url).json()
        return r.get("txs", [])[0] if r.get("txs") else None
    except:
        return None

def main():
    last_seen = None
    while True:
        btc_price = get_price()
        tx = get_latest_btc_tx(BTC_ADDRESS)
        if tx and tx["hash"] != last_seen:
            total = sum([out["value"] for out in tx["out"] if out.get("addr") == BTC_ADDRESS]) / 1e8
            from_addr = tx.get("inputs", [{}])[0].get("prev_out", {}).get("addr", "不明")
            usd_val = total * btc_price
            msg = f"""🟢 *BTC 入金*
👤 จาก: `{from_addr}`
👥 ถึง: `{BTC_ADDRESS}`
💰 {total:.8f} BTC ≈ ${usd_val:,.2f}
🔗 TXID: `{tx['hash']}`"""
            send_message(msg)
            last_seen = tx["hash"]
        time.sleep(10)

if __name__ == "__main__":
    main()
