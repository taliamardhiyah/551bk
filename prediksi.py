import requests
import json
import time
import asyncio
import random
from telegram import Bot
from colorama import init, Fore

# Inisialisasi warna untuk CMD
init(autoreset=True)

# Menyimpan riwayat game dengan batas 25
history = []
bet_history = []

# Menyiapkan bot Telegram
TOKEN = '6668826178:AAE6oKYrvB2HX6_rlxtYW30F2ZjL6UZU1-U'
CHAT_IDS = ['-1004052064216', '-1002153469132']  # Ganti dengan ID grup Telegram
bot = Bot(token=TOKEN)

# Fungsi untuk mendapatkan timestamp
def get_timestamp():
    return int(time.time())

# Fungsi untuk mengirim pesan ke Telegram (asinkron)
async def send_to_telegram(message):
    for chat_id in CHAT_IDS:
        await bot.send_message(chat_id=chat_id, text=message)

# Fungsi untuk mendapatkan data hasil periode dari API
def get_game_result(issue_number):
    headers = {
        'authority': 'newapi.55lottertttapi.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOiIxNzM4MjQ1OTk0IiwibmJmIjoiMTczODI0NTk5NCIsImV4cCI6IjE3MzgyNDc3OTQiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL2V4cGlyYXRpb24iOiIxLzMwLzIwMjUgOTozNjozNCBQTSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFjY2Vzc19Ub2tlbiIsIlVzZXJJZCI6Ijc0MzM1IiwiVXNlck5hbWUiOiI2Mjg1NzE4MzczMzgwIiwiVXNlclBob3RvIjoiaHR0cHM6Ly9hcGkubGlnaHRzcGFjZWNkbi5jb20vaW1nL2F2YXRhci5jZmE4ZGQ5ZC5zdmciLCJOaWNrTmFtZSI6IkRlc2FrdSIsIkFtb3VudCI6IjY5OC45NCIsIkludGVncmFsIjoiMCIsIkxvZ2luTWFyayI6Ikg1IiwiTG9naW5UaW5lIjoiMS8zMC8yMDI1IDk6MDY6MzQgUE0iLCJMb2dpbklQQWRkcmVzcyI6IjEyMC4xODguOTMuOTUiLCJEYk51bWJlciI6IjAiLCJJc3ZhbGlkYXRvciI6IjAiLCJLZXlDb2RlIjoiOTI5IiwiVG9rZW5UeXBlIjoiQWNjZXNzX1Rva2VuIiwiUGhvbmVUeXBlIjoiMCIsIlVzZXJUeXBlIjoiMCIsIlVzZXJOYW1lMiI6IiIsImlzcyI6Imp3dElzc3VlciIsImF1ZCI6ImxvdHRlcnlUaWNrZXQifQ.HKoQE36HtLF5197bKMEQxNCRg85tBk5mcLUj99nPoxTR',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://www.551bk.com',
        'referer': 'https://www.551bk.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }
    data = json.dumps({
        "issueNumber": issue_number
    })
    response = requests.post('https://newapi.55lottertttapi.com/api/webapi/GetGameResult', headers=headers, data=data)
    return response.json()

# Fungsi untuk menentukan jenis taruhan (kecil/besar)
def determine_bet(number):
    if int(number) >= 5:
        return "BESAR"
    else:
        return "KECIL"

# Fungsi untuk menghitung taruhan dan logika prediksi
def calculate_bet(last_bet, bet_index, is_loss):
    bets = [ 1000, 3000, 6000, 16000, 32000, 80000, 160000, 350000, 800000, 1700000, 4000000, 8000000, 18000000, 50000000 ]
    
    # Jika kalah, lipatkan taruhan
    if is_loss:
        next_bet = bets[bet_index] * 3  # Mengalikan dengan 3 sesuai dengan pola kelipatan
        bet_type = random.choice(["BESAR", "KECIL", "KECIL", "KECIL", "BESAR"])  # Pilih prediksi acak
    else:
        next_bet = bets[bet_index]
        bet_type = random.choice(["BESAR", "KECIL", "KECIL", "KECIL", "BESAR"])  # Pilih prediksi acak
    
    bet_message = f"Prediksi berikutnya: {bet_type} - Taruhan mulai dari: {next_bet}"
    
    return bet_message, next_bet, bet_type

# Fungsi untuk menghitung waktu countdown
def get_countdown(end_time):
    current_time = time.time()
    end_time_seconds = time.mktime(time.strptime(end_time, "%Y-%m-%d %H:%M:%S"))
    remaining_time = int(end_time_seconds - current_time)
    return remaining_time

# Fungsi untuk menampilkan riwayat dan mengirim prediksi ke Telegram
async def display_and_send_results(last_sent_period, last_bet, bet_index, is_loss, is_first_prediction):
    global history
    global bet_history
    
    # Ambil data hasil game terakhir dan prediksi
    current_issue_data = response_GetGameIssue()
    last_result_data = response_GetNoaverageEmerdList()
    
    # Menampilkan riwayat di layar
    print(Fore.GREEN + "Riwayat 55FIVE WINGO CEPAT:")
    print("issueNumber | number  | rekaman prediksi berikutnya | BET   | ODD")
    for item in last_result_data['data']['list']:
        issue_number = item['issueNumber'][-4:]  # Hanya ambil 4 digit terakhir
        bet_result = "WIN" if item['colour'] == "red" else "LOSE"
        print(f"{issue_number:4} | {item['number']:5} | {determine_bet(item['number'])} | {1000 if bet_result == 'WIN' else last_bet:6} | {bet_result}")
        bet_history.append(f"{issue_number:4} | {item['number']:5} | {determine_bet(item['number'])} | {1000 if bet_result == 'WIN' else last_bet:6} | {bet_result}")

    # Prediksi dan informasi periode yang akan datang
    next_bet_message, next_bet, bet_type = calculate_bet(last_bet, bet_index, is_loss)
    
    # Menampilkan prediksi di layar
    print(Fore.YELLOW + f"Prediksi periode {current_issue_data['data']['issueNumber'][-4:]}")
    print(Fore.YELLOW + next_bet_message)

    # Menghitung sisa waktu (Countdown)
    remaining_time = get_countdown(current_issue_data['data']['endTime'])
    
    if remaining_time > 0:
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        print(Fore.CYAN + f"[Countdown] : {minutes:02d}:{seconds:02d}")
    else:
        print(Fore.CYAN + "[Countdown] : 00:00")

    # Cek apakah periode berubah, jika ya kirim pesan
    current_period = current_issue_data['data']['issueNumber'][-4:]
    if current_period != last_sent_period:
        # Cek hasil dari API berdasarkan issueNumber
        api_data = get_game_result(current_period)
        result_number = api_data.get('number')
        result_color = api_data.get('colour')

        # Tentukan apakah prediksi menang atau kalah
        if result_color == 'red' and determine_bet(result_number) == "BESAR":
            bet_result = "WIN"
            is_loss = False
        elif result_color == 'green' and determine_bet(result_number) == "KECIL":
            bet_result = "WIN"
            is_loss = False
        else:
            bet_result = "LOSE"
            is_loss = True

        # Kirim pesan ke Telegram jika ada perubahan
        message = "Riwayat 55FIVE WINGO CEPAT:\n"
        message += "issueNumber | number | rekaman prediksi berikutnya | BET   | ODD\n"
        for item in bet_history[-5:]:  # Hanya menampilkan 5 riwayat terakhir
            message += f"{item}\n"

        message += f"\nPrediksi periode {current_issue_data['data']['issueNumber'][-4:]}\n"
        message += next_bet_message
        message += f"\n[Countdown] : {minutes:02d}:{seconds:02d}"

        # Kirim pesan ke Telegram hanya jika sudah ada hasil dari periode pertama
        if not is_first_prediction:
            await send_to_telegram(message)

        return current_period, next_bet, bet_index + 1 if bet_index < len([1000, 3000, 9000, 27000, 81000, 243000, 729000, 2187000, 6561000, 19683000, 59049000, 177147000, 531441000]) - 1 else 0, is_loss

    return last_sent_period, last_bet, bet_index, is_loss, is_first_prediction

# Menjalankan fungsi utama
async def main():
    last_sent_period = ""
    last_bet = 1000 opil# Misalnya, Anda bisa mulai dari 1000 sebagai taruhan pertama
