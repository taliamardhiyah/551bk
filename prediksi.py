import requests
import json
import time
import asyncio
import random
import datetime
from colorama import init, Fore, Style
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

# Inisialisasi warna untuk CMD
init(autoreset=True)

# Menyimpan riwayat game dengan batas 25
history = []
bet_history = []

# Menyiapkan bot Telegram
TOKEN = '6668826178:AAE6oKYrvB2HX6_rlxtYW30F2ZjL6UZU1-U'
CHAT_IDS = ['-1004052064216', '-1002153469132']  # Ganti dengan ID grup Telegram
bot = Bot(token=TOKEN)

#Fungsi untuk mendapatkan timestamp
def get_timestamp():
    return int(time.time())

# Fungsi untuk mengirim pesan ke Telegram (asinkron)
async def send_to_telegram_with_button(message):
    # Membuat tombol yang mengarah ke URL
    keyboard = [
        [InlineKeyboardButton("DAFTAR 55FIVE", url="https://551bk.com/#/promotion/PromotionShare?code=sbJnv4801"),
         InlineKeyboardButton("BET PREDIKSI", url="https://551bk.com/#/home/AllLotteryGames/WinGo?id=1")],
        # Bisa menambahkan tombol lain jika perlu
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Mengirim pesan dengan tombol
    for chat_id in CHAT_IDS:
        await bot.send_message(chat_id=chat_id, text=message, reply_markup=reply_markup)

# Fungsi untuk mendapatkan data dari GetNoaverageEmerdList
def response_GetNoaverageEmerdList():
    headers = {
        'authority': 'newapi.55lottertttapi.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOiIxNzM4Mzc0MjAxIiwibmJmIjoiMTczODM3NDIwMSIsImV4cCI6IjE3MzgzNzYwMDEiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL2V4cGlyYXRpb24iOiIyLzEvMjAyNSA5OjEzOjIxIEFNIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiQWNjZXNzX1Rva2VuIiwiVXNlcklkIjoiNDgwMSIsIlVzZXJOYW1lIjoiNjI4NTgxMzY2ODUxNCIsIlVzZXJQaG90byI6IjIiLCJOaWNrTmFtZSI6IkJpc21pbGFoIiwiQW1vdW50IjoiNDcxLjM2IiwiSW50ZWdyYWwiOiIwIiwiTG9naW5NYXJrIjoiSDUiLCJMb2dpblRpbWUiOiIyLzEvMjAyNSA4OjQzOjIxIEFNIiwiTG9naW5JUEFkZHJlc3MiOiIxMjAuMTg4LjY2LjI0NSIsIkRiTnVtYmVyIjoiMCIsIklzdmFsaWRhdG9yIjoiMCIsIktleUNvZGUiOiIzNjQ4IiwiVG9rZW5UeXBlIjoiQWNjZXNzX1Rva2VuIiwiUGhvbmVUeXBlIjoiMCIsIlVzZXJUeXBlIjoiMCIsIlVzZXJOYW1lMiI6IiIsImlzcyI6Imp3dElzc3VlciIsImF1ZCI6ImxvdHRlcnlUaWNrZXQifQ.qybVfvGCmzyTeqxrw35Kpa2R_qwTdPhkTFXglpt_tJk',  # Ganti dengan token API Anda
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://www.551bk.com',
        'referer': 'https://www.551bk.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }
    data = json.dumps({
        "pageSize": 10,
        "pageNo": 1,
        "typeId": 1,
        "language": 0,
        "random": "2a48076cb5704c94962526254ac9a2cf",
        "signature": "76FC6D0CF6BEAE2BDD7A28D7C12DAC78",
        "timestamp": get_timestamp()
    })
    response = requests.post('https://newapi.55lottertttapi.com/api/webapi/GetNoaverageEmerdList', headers=headers, data=data)
    return response.json()

# Fungsi untuk mendapatkan data dari GetGameIssue
def response_GetGameIssue():
    headers = {
        'authority': 'newapi.55lottertttapi.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOiIxNzM4Mzc0MjAxIiwibmJmIjoiMTczODM3NDIwMSIsImV4cCI6IjE3MzgzNzYwMDEiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL2V4clyXRpb24iOiIyLzEvMjAyNSA5OjEzOjIxIEFNIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiQWNjZXNzX1Rva2VuIiwiVXNlcklkIjoiNDgwMSIsIlVzZXJOYW1lIjoiNjI4NTgxMzY2ODUxNCIsIlVzZXJQaG90byI6IjIiLCJOaWNrTmFtZSI6IkJpc21pbGFoIiwiQW1vdW50IjoiNDcxLjM2IiwiSW50ZWdyYWwiOiIwIiwiTG9naW5NYXJrIjoiSDUiLCJMb2dpblRpbWUiOiIyLzEvMjAyNSA4OjQzOjIxIEFNIiwiTG9naW5JUEFkZHJlc3MiOiIxMjAuMTg4LjY2LjI0NSIsIkRiTnVtYmVyIjoiMCIsIklzdmFsaWRhdG9yIjoiMCIsIktleUNvZGUiOiIzNjQ4IiwiVG9rZW5UeXBlIjoiQWNjZXNzX1Rva2VuIiwiUGhvbmVUeXBlIjoiMCIsIlVzZXJUeXBlIjoiMCIsIlVzZXJOYW1lMiI6IiIsImlzcyI6Imp3dElzc3VlciIsImF1ZCI6ImxvdHRlcnlUaWNrZXQifQ.qybVfvGCmzyTeqxrw35Kpa2R_qwTdPhkTFXglpt_tJk',  # Ganti dengan token API Anda
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://www.551bk.com',
        'referer': 'https://www.551bk.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }
    data = json.dumps({
        "typeId": 1,
        "language": 0,
        "random": "4431ad57be4f4c3b9e2fcaedd064bdba",
        "signature": "ABC935D9B1AF1DA76F556AF81737E834",
        "timestamp": get_timestamp()
    })
    response = requests.post('https://newapi.55lottertttapi.com/api/webapi/GetGameIssue', headers=headers, data=data)
    return response.json()

# Fungsi untuk menentukan jenis taruhan (kecil/besar)
def determine_bet(number):
    return "BESAR" if int(number) >= 5 else "KECIL"

# Fungsi untuk menghitung taruhan dan logika prediksi
def calculate_bet(last_bet, bet_index, is_loss):
    bets = [1000, 3000, 6000, 16000, 32000, 80000, 160000, 350000, 800000, 1700000, 4000000, 8000000, 18000000, 50000000] # jika 1000 tulis 1k jika 10000 tulis 10k jika 100000 tulis 100k jika 1000000 tulis 1jt dan seterusnya
    
    if is_loss:
        # Jika kalah, naik ke indeks berikutnya untuk kompensasi
        bet_index += 1
    else:
        # Jika menang, kembali ke indeks taruhan awal
        bet_index = 0  

    # Pastikan bet_index tidak melebihi batas array
    if bet_index >= len(bets):
        bet_index = len(bets) - 1  # Batasi ke indeks maksimum

    next_bet = bets[bet_index]
    return next_bet, bet_index

# Fungsi untuk countdown
def countdown():
    now = datetime.datetime.now()
    total_second = 60 - now.second
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'[{Fore.CYAN}Countdown{Style.RESET_ALL}] : {Fore.WHITE}{mins:02d}:{secs:02d} ', end='\r')
        time.sleep(1)
        total_second -= 1

# Fungsi utama untuk mendapatkan data dan mengirim prediksi
async def main():
    current_balance = 1000000  # Mulai dengan saldo awal, bisa disesuaikan
    profit_balance = 0  # Saldo akhir yang diinginkan, bisa disesuaikan
    last_bet = 1000  # Bet pertama dimulai dengan 1000
    bet_index = 0
    current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") # Waktu saat ini dalam format "dd-mm-yyyy HH:MM:SS"
    is_loss = False
    current_bet = 1000  # Set taruhan pertama
    previous_bet = 0  # Taruhan sebelumnya
    next_bet_type = ["BESAR", "KECIL", "BESAR", "KECIL", "KECIL", "KECIL", "BESAR"][random.randint(0, 7)]  # Set jenis taruhan pertama secara acak jika Besar atau Kecil sudah keluar lebih 3 kali maka taruhan akan berubah menjadi yang lain jika masih sama ikuti pola yang keluar lebih banyak
    
   # Tampilkan informasi di layar
    print(Fore.YELLOW + r"""
  _____ _____  __      ___  __
 | ____| ____| \ \    / (_)/ _|
 | |__ | |__    \ \  / / _| |_ ___
 |___ \|___ \    \ \/ / | |  _/ _ \
  ___) |___) |    \  /  | | ||  __/
 |____/|____/      \/   |_|_| \___|

 [+] Autor : @sulaeman
 [+] Tele  : @adaakuyea
 [+] Info script  : @adaakuyea
 [+] Versi : 1.18.2
    """)

    # Inisialisasi riwayat dari 0
    history.clear()

    while True:
        ("Mendapatkan data GetNoaverageEmerdList...")
        data1 = response_GetNoaverageEmerdList()
        (json.dumps(data1, indent=2))

        ("Mendapatkan data GetGameIssue...")
        data2 = response_GetGameIssue()
        (json.dumps(data2, indent=2))

        # Ambil nomor dari game terbaru
        latest_game = data1['data']['list'][0]
        issue_number = latest_game['issueNumber']
        number = latest_game['number']
        
        # Cek hasil prediksi sebelumnya
        if next_bet_type == "BESAR":
            if int(number) >= 5:
                is_loss = False
                result = "WIN"
                result_emoji = "✅"
                result_color = Fore.GREEN
                current_balance += current_bet  # Tambah saldo dengan taruhan
            else:
                is_loss = True
                result = "MIN"
                result_emoji = "☑️"
                result_color = Fore.RED
                current_balance -= current_bet  # Kurangi saldo dengan taruhan
        else:
            if int(number) < 5:
                is_loss = False
                result = "WIN"
                result_emoji = "✅"
                result_color = Fore.GREEN
                current_balance += current_bet  # Tambah saldo dengan taruhan
            else:
                is_loss = True
                result = "MIN"
                result_emoji = "☑️"
                result_color = Fore.RED
                current_balance -= current_bet  # Kurangi saldo dengan taruhan

        # Simpan taruhan sebelumnya
        previous_bet = current_bet # taruhan sebelumnya bukan taruhan saat ini (contoh periode 0000 Besar 1000 MIN dari hasil yang sebelumnya)
        # contoh periode 0000 Besar 1000 MIN dari hasil yang sebelumnya
        # prediksi berikutnya 0001 Kecil 3000 (jangan di simpan dulu di previous_bet jika sudah ada hasil baru simpan )
        # WIN MIN for record 0000 Besar 1000 MIN beri warna merah jika MIN dan warna hijau jika WIN
        # current_balance +-= current_bet # Update saldo dengan taruhan saat ini yang sesuai periode

        # Hitung taruhan berikutnya
        current_bet, bet_index = calculate_bet(last_bet, bet_index, is_loss)
        last_bet = current_bet  # Update last_bet untuk taruhan berikutnya

        # Menyimpan riwayat game terbaru, hanya 4 angka periode
        period_last4 = issue_number[-4:]  # Ambil 4 digit terakhir periode
        history.append(f"{period_last4:<4} │ {number:<4} │ ({next_bet_type[0]}){previous_bet:<6} │ {result}{result_emoji}") # previous_bet tampilkan di layar jika WIN beri warna fore.GREEN jika MIN beri warna fore.RED
        # contoh periode 0000 Besar 1000 MIN dari hasil yang sebelumnya
        # contoh periode 0001 Kecil 3000 WIN dari hasil yang sebelumnya
        if len(history) > 20:
            history.pop(0)  # Menghapus game yang paling lama

        # Prediksi periode berikutnya
        next_issue_number = data2['data']['issueNumber']
        next_bet_type = determine_bet(random.randint(0, 9))

        # Tambahkan pesan prediksi ke dalam pesan teks
        prediction_message = "📍55FIVE 1M📍\n"
        # Gabungkan riwayat dan prediksi menjadi satu pesan
        history_message = "┌────────┬─────┬─────────┬─────┐\n"
        history_message += "│ Perio  │ Data│ Betting │ L/W │\n"
        history_message += "├────────┼─────┼─────────┼─────┤\n"
        for record in history:
            history_message += f"│ {record} │\n"
        history_message += "└────────┴─────┴─────────┴─────┘\n"

        prediction_message += f"📶 Prediksi {next_issue_number[-4:]} {next_bet_type}\n"
        prediction_message += f"♻️ Taruhan: {current_bet} \n"
        prediction_message += f"💰 Saldo: {current_balance}\n"

        # Gabungkan keduanya dalam satu pesan
        full_message = f"{history_message}\n{prediction_message}"

        # Tampilkan riwayat dan prediksi di layar dengan warna dan format yang rapi
        print("\n" + Fore.YELLOW + "Riwayat 55FIVE WINGO 1M:")
        print(Fore.GREEN + history_message)
        print(Fore.CYAN + prediction_message)

        # Kirim pesan dengan tombol (link) ke Telegram
        await send_to_telegram_with_button(full_message)

        # Tampilkan countdown
        countdown()

# Menjalankan fungsi utama
if __name__ == "__main__":
    asyncio.run(main())  # Jalankan logika utama dengan asyncio
