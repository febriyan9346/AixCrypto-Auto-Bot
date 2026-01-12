import os
import time
import sys
import json
import random
import warnings
from datetime import datetime, timezone
import pytz 
from colorama import Fore, Style, init
from curl_cffi import requests
from eth_account import Account
from eth_account.messages import encode_defunct

os.system('clear' if os.name == 'posix' else 'cls')
warnings.filterwarnings('ignore')
if not sys.warnoptions:
    os.environ["PYTHONWARNINGS"] = "ignore"
init(autoreset=True)

class AixCryptoBot:
    def __init__(self):
        self.sitekey = "0x4AAAAAAAM8ceq5KhP1uJBt"
        self.page_url = "https://hub.aixcrypto.ai/"
        self.privy_app_id = "cmk3zw8d704bxl70chtewm6hd"
        self.api_key_2captcha = ""
        self.api_key_sctg = ""
        self.accounts = []
        self.proxies = []
        self.max_bets = 5 
        self.use_proxy = False
        self.solver_type = "2captcha"

    def get_wib_time(self):
        try:
            wib = pytz.timezone('Asia/Jakarta')
            return datetime.now(wib).strftime('%H:%M:%S')
        except:
            return datetime.now().strftime('%H:%M:%S')
    
    def print_banner(self):
        banner = f"""
{Fore.CYAN}AIXCRYPTO AUTO BOT{Style.RESET_ALL}
{Fore.WHITE}By: FEBRIYAN{Style.RESET_ALL}
{Fore.CYAN}============================================================{Style.RESET_ALL}
"""
        print(banner)
    
    def log(self, message, level="INFO"):
        time_str = self.get_wib_time()
        colors = {
            "INFO": Fore.CYAN, "SUCCESS": Fore.GREEN, "ERROR": Fore.RED,
            "WARNING": Fore.YELLOW, "BET": Fore.BLUE, "CYCLE": Fore.MAGENTA,
            "TASK": Fore.MAGENTA, "WIN": Fore.GREEN, "LOSE": Fore.RED
        }
        color = colors.get(level, Fore.WHITE)
        
        if message == "Processing Daily Check-in...":
            color = Fore.GREEN

        print(f"[{time_str}] {color}[{level}] {message}{Style.RESET_ALL}")
    
    def format_proxy(self, proxy_str):
        if not proxy_str: return None
        if proxy_str.startswith("http") or proxy_str.startswith("socks"): return proxy_str
        
        parts = proxy_str.split(':')
        if len(parts) == 4: 
            return f"http://{parts[2]}:{parts[3]}@{parts[0]}:{parts[1]}"
        elif len(parts) == 2: 
            return f"http://{proxy_str}"
        return f"http://{proxy_str}"

    def load_files(self):
        try:
            try:
                with open("2captcha.txt", "r") as f:
                    self.api_key_2captcha = f.read().strip()
            except FileNotFoundError:
                self.api_key_2captcha = ""
            
            try:
                with open("sctg.txt", "r") as f:
                    self.api_key_sctg = f.read().strip()
            except FileNotFoundError:
                self.api_key_sctg = ""
            
            with open("accounts.txt", "r") as f:
                self.accounts = [line.strip() for line in f if line.strip()]

            try:
                with open("proxy.txt", "r") as f:
                    raw_proxies = [line.strip() for line in f if line.strip()]
                    self.proxies = [self.format_proxy(p) for p in raw_proxies]
            except FileNotFoundError:
                self.proxies = []
                
        except Exception as e:
            self.log(f"File missing: {e}", "ERROR")
            sys.exit()

    def show_menu(self):
        print(f"{Fore.CYAN}============================================================{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Select Proxy Mode:{Style.RESET_ALL}")
        
        print(f"1. Run with Proxy")
        print(f"2. Run without Proxy")
        print(f"{Fore.CYAN}============================================================{Style.RESET_ALL}")
        
        choice = input(f"{Fore.GREEN}Select Mode (1/2): {Style.RESET_ALL}").strip()
        
        if choice == '1':
            if not self.proxies:
                print(f"{Fore.RED}Error: proxy.txt is empty! Switching to No Proxy.{Style.RESET_ALL}")
                self.use_proxy = False
            else:
                self.use_proxy = True
                print(f"{Fore.GREEN}> Running with {len(self.proxies)} proxies loaded.{Style.RESET_ALL}")
        else:
            self.use_proxy = False
            print(f"{Fore.YELLOW}> Running without proxy.{Style.RESET_ALL}")

        print(f"{Fore.CYAN}============================================================{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Select Captcha Solver:{Style.RESET_ALL}")
        
        print(f"1. 2Captcha")
        print(f"2. SCTG")
        print(f"{Fore.CYAN}============================================================{Style.RESET_ALL}")
        
        solver_choice = input(f"{Fore.GREEN}Select Solver (1/2): {Style.RESET_ALL}").strip()
        
        if solver_choice == '2':
            if not self.api_key_sctg:
                print(f"{Fore.RED}Error: sctg.txt is empty! Switching to 2Captcha.{Style.RESET_ALL}")
                self.solver_type = "2captcha"
            else:
                self.solver_type = "sctg"
                print(f"{Fore.GREEN}> Using SCTG Solver.{Style.RESET_ALL}")
        else:
            if not self.api_key_2captcha:
                print(f"{Fore.RED}Error: 2captcha.txt is empty!{Style.RESET_ALL}")
                if self.api_key_sctg:
                    print(f"{Fore.YELLOW}Switching to SCTG Solver.{Style.RESET_ALL}")
                    self.solver_type = "sctg"
                else:
                    print(f"{Fore.RED}No valid API keys found! Exiting...{Style.RESET_ALL}")
                    sys.exit()
            else:
                self.solver_type = "2captcha"
                print(f"{Fore.GREEN}> Using 2Captcha Solver.{Style.RESET_ALL}")

        print(f"{Fore.CYAN}============================================================{Style.RESET_ALL}")

        try:
            input_bet = input(f"{Fore.GREEN}Enter Max Bets per Account : {Style.RESET_ALL}").strip()
            self.max_bets = int(input_bet) if input_bet else 5
        except:
            self.max_bets = 5
            
        print(f"{Fore.CYAN}============================================================{Style.RESET_ALL}")

    def solve_turnstile_2captcha(self):
        self.log("Solving Captcha with 2Captcha...", "INFO")
        import requests as r_sync
        
        url_in = "http://2captcha.com/in.php"
        payload = {
            "key": self.api_key_2captcha, "method": "turnstile",
            "sitekey": self.sitekey, "pageurl": self.page_url, "json": 1
        }
        try:
            resp = r_sync.post(url_in, data=payload).json()
            if resp.get('status') != 1: return None
            req_id = resp.get('request')
        except: return None

        for _ in range(30):
            time.sleep(4)
            try:
                res = r_sync.get(f"http://2captcha.com/res.php?key={self.api_key_2captcha}&action=get&id={req_id}&json=1").json()
                if res.get('status') == 1: return res.get('request')
            except: pass
        return None

    def solve_turnstile_sctg(self):
        self.log("Solving Captcha with SCTG...", "INFO")
        import requests as r_sync
        from urllib.parse import urlencode
        
        params = {
            "key": self.api_key_sctg,
            "method": "turnstile",
            "pageurl": self.page_url,
            "sitekey": self.sitekey
        }
        
        query_string = urlencode(params)
        url = "https://sctg.xyz/in.php?" + query_string
        
        try:
            response = r_sync.get(url, timeout=30)
            result = response.text.strip()
            
            if "|" not in result:
                return None
                
            status, task_id = result.split("|", 1)
            
            max_wait = 300
            poll_interval = 5
            start_time = time.time()
            
            while (time.time() - start_time) < max_wait:
                time.sleep(poll_interval)
                
                poll_params = {
                    "key": self.api_key_sctg,
                    "id": task_id,
                    "action": "get"
                }
                poll_query = urlencode(poll_params)
                poll_url = "https://sctg.xyz/res.php?" + poll_query
                
                poll_response = r_sync.get(poll_url, timeout=30)
                poll_result = poll_response.text.strip()
                
                if "NOT_READY" not in poll_result and "PROCESSING" not in poll_result:
                    if "|" in poll_result:
                        return poll_result.split("|", 1)[1]
                    return poll_result
                    
            return None
        except Exception as e:
            self.log(f"SCTG Error: {str(e)}", "ERROR")
            return None

    def solve_turnstile(self):
        if self.solver_type == "sctg":
            return self.solve_turnstile_sctg()
        else:
            return self.solve_turnstile_2captcha()

    def claim_daily(self, session, session_id):
        self.log("Processing Daily Check-in...", "INFO")
        url = "https://hub.aixcrypto.ai/api/tasks/claim"
        payload = {"taskId": 1, "sessionId": session_id}
        
        try:
            resp = session.post(url, json=payload)
            
            if resp.status_code == 200:
                data = resp.json()
                if data.get("success"):
                    reward = data.get("reward", 0)
                    self.log(f"Daily Claim Success! Reward: +{reward}", "SUCCESS")
                else:
                    self.log("Daily Claim Failed (Maybe Already Claimed)", "WARNING")
            elif resp.status_code == 400:
                self.log("Daily Claim Failed (Likely Already Claimed)", "WARNING")
            else:
                self.log(f"Daily Claim HTTP Error: {resp.status_code}", "ERROR")
        except Exception as e:
            self.log(f"Daily Claim Error: {str(e)[:50]}", "ERROR")

    def check_bet_result(self, session, address, round_id):
        url = f"https://hub.aixcrypto.ai/api/game/bet-history?address={address}&page=1&pageSize=10"
        try:
            resp = session.get(url)
            if resp.status_code == 200:
                data = resp.json()
                history_list = data.get("list", [])
                
                for bet in history_list:
                    if str(bet.get("round_id")) == str(round_id):
                        result = bet.get("result", "PENDING")
                        reward = bet.get("credits_reward", 0)
                        return result, reward
            return "UNKNOWN", 0
        except Exception:
            return "ERROR", 0

    def start_betting(self, session, session_id, address):
        self.log(f"Starting Game Session ({self.max_bets} Rounds)", "BET")
        
        url_bet = "https://hub.aixcrypto.ai/api/game/bet"
        success_count = 0
        i = 0
        
        while i < self.max_bets:
            prediction = random.choice(["UP", "DOWN"])
            payload = {"prediction": prediction, "sessionId": session_id}
            
            try:
                resp = session.post(url_bet, json=payload)
                
                if resp.status_code in [200, 201]:
                    data = resp.json()
                    if data.get("success"):
                        bet_info = data.get("bet", {})
                        round_id = bet_info.get("roundId", "N/A")
                        daily = data.get("dailyBetCount", "N/A")
                        
                        pred_str = f"{Fore.GREEN}{prediction}{Style.RESET_ALL}"
                        self.log(f"Bet #{i+1} | {pred_str} | Round: {round_id} | Daily: {daily}", "SUCCESS")
                        
                        time.sleep(12) 
                        
                        res_status, reward = self.check_bet_result(session, address, round_id)
                        
                        if res_status == "WIN":
                            self.log(f"Result: WIN | Reward: +{reward}", "INFO")
                            success_count += 1
                        elif res_status == "LOSE":
                            self.log(f"Result: LOSE | Reward: {reward}", "INFO")
                        else:
                            self.log(f"Result: {res_status}", "WARNING")

                        i += 1
                        
                        if i < self.max_bets:
                            sleep_time = random.randint(3, 5)
                            time.sleep(sleep_time)
                    else:
                        self.log(f"Bet #{i+1} Failed (API Success False)", "WARNING")
                        time.sleep(5)

                elif resp.status_code == 429:
                    self.log(f"Rate Limit (429)! Sleeping 60s...", "ERROR")
                    time.sleep(60)

                elif resp.status_code == 400:
                    self.log(f"Round Locked/Closed. Waiting 20s...", "WARNING")
                    time.sleep(20)

                else:
                    self.log(f"Bet #{i+1} Failed Status: {resp.status_code}", "ERROR")
                    i += 1

            except Exception as e:
                self.log(f"Bet Error: {str(e)[:30]}", "ERROR")
                time.sleep(5)

        self.log(f"Session Complete | Wins: {success_count}", "BET")

    def generate_privy_ca_id(self):
        return f"{random.randint(0x10000000, 0xffffffff):08x}-{random.randint(0x1000, 0xffff):04x}-{random.randint(0x1000, 0xffff):04x}-{random.randint(0x1000, 0xffff):04x}-{random.randint(0x100000000000, 0xffffffffffff):012x}"

    def login_process(self, private_key, proxy=None):
        try:
            if not private_key.startswith("0x"): private_key = "0x" + private_key
            account = Account.from_key(private_key)
            addr = account.address
            
            proxies_dict = {"http": proxy, "https": proxy} if proxy else None
            proxy_log = proxy.split('@')[-1] if proxy else "No Proxy"
            
            self.log(f"Wallet : {addr[:6]}...{addr[-4:]}", "INFO")
            if self.use_proxy:
                self.log(f"Proxy  : {proxy_log}", "INFO")

            captcha_token = self.solve_turnstile()
            if not captcha_token:
                self.log("Captcha Failed", "ERROR")
                return

            with requests.Session(impersonate="chrome124", proxies=proxies_dict) as s:
                privy_ca_id = self.generate_privy_ca_id()
                
                s.headers.update({
                    "authority": "auth.privy.io",
                    "accept": "application/json",
                    "accept-language": "en-US,en;q=0.9",
                    "content-type": "application/json",
                    "origin": "https://hub.aixcrypto.ai",
                    "referer": "https://hub.aixcrypto.ai/",
                    "sec-ch-ua": '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "cross-site",
                    "sec-fetch-storage-access": "active",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
                    "privy-app-id": self.privy_app_id,
                    "privy-ca-id": privy_ca_id,
                    "privy-client": "react-auth:3.10.1"
                })

                init_payload = {"address": addr, "token": captcha_token}
                init_res = s.post("https://auth.privy.io/api/v1/siwe/init", json=init_payload)
                
                if init_res.status_code != 200: 
                    self.log(f"Privy Init Failed: {init_res.status_code}", "ERROR")
                    try:
                        error_detail = init_res.json()
                        self.log(f"Error Detail: {error_detail}", "ERROR")
                    except:
                        self.log(f"Response: {init_res.text[:200]}", "ERROR")
                    return
                    
                init_data = init_res.json()
                nonce = init_data['nonce']
                
                now = datetime.now(timezone.utc)
                issued_at = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
                
                msg = f"hub.aixcrypto.ai wants you to sign in with your Ethereum account:\n{addr}\n\nBy signing, you are proving you own this wallet and logging in. This does not initiate a transaction or cost any fees.\n\nURI: https://hub.aixcrypto.ai\nVersion: 1\nChain ID: 560048\nNonce: {nonce}\nIssued At: {issued_at}\nResources:\n- https://privy.io"
                
                message_hash = encode_defunct(text=msg)
                signed = account.sign_message(message_hash)
                sig = '0x' + signed.signature.hex() if not signed.signature.hex().startswith('0x') else signed.signature.hex()

                auth_payload = {
                    "chainId": "eip155:560048",
                    "connectorType": "injected",
                    "message": msg,
                    "mode": "login-or-sign-up",
                    "signature": sig,
                    "walletClientType": "metamask"
                }
                
                auth_res = s.post("https://auth.privy.io/api/v1/siwe/authenticate", json=auth_payload)
                
                if auth_res.status_code != 200: 
                    self.log(f"Privy Auth Failed: {auth_res.status_code}", "ERROR")
                    try:
                        error_detail = auth_res.json()
                        self.log(f"Error Detail: {error_detail}", "ERROR")
                    except:
                        self.log(f"Response: {auth_res.text[:200]}", "ERROR")
                    return
                    
                auth_data = auth_res.json()
                privy_token = auth_data['token']

                s.cookies.set("privy-token", privy_token, domain="hub.aixcrypto.ai")
                s.cookies.set("privy-session", "t", domain="hub.aixcrypto.ai")
                
                s.headers.update({
                    "authority": "hub.aixcrypto.ai",
                    "referer": "https://hub.aixcrypto.ai/",
                    "origin": "https://hub.aixcrypto.ai"
                })
                s.headers.pop("privy-app-id", None)
                s.headers.pop("privy-ca-id", None)
                s.headers.pop("privy-client", None)

                ts = int(time.time() * 1000)
                msg_app = f"Sign this message to authenticate with AIxCrypto.\n\nWallet: {addr.lower()}\nTimestamp: {ts}\n\nThis signature will not trigger any blockchain transaction or cost any gas fees."
                
                message_hash_app = encode_defunct(text=msg_app)
                signed_app = account.sign_message(message_hash_app)
                sig_app = '0x' + signed_app.signature.hex() if not signed_app.signature.hex().startswith('0x') else signed_app.signature.hex()

                login_payload = {
                    "address": addr,
                    "message": msg_app,
                    "signature": sig_app
                }
                
                login_res = s.post("https://hub.aixcrypto.ai/api/login", json=login_payload)

                if login_res.status_code == 200:
                    data = login_res.json()
                    user = data.get("username", "NoUsername")
                    creds = data.get("credits", 0)
                    sess_id = data.get("sessionId")
                    
                    self.log(f"Login Success!", "SUCCESS")
                    self.log(f"User: {user} | Credits: {creds}", "INFO")
                    
                    time.sleep(2)
                    self.claim_daily(s, sess_id)

                    time.sleep(3)
                    self.start_betting(s, sess_id, addr)

                else:
                    self.log(f"App Login Failed: {login_res.status_code}", "ERROR")
                    try:
                        error_detail = login_res.json()
                        self.log(f"Error Detail: {error_detail}", "ERROR")
                    except:
                        self.log(f"Response: {login_res.text[:200]}", "ERROR")

        except Exception as e:
            self.log(f"Account Error: {e}", "ERROR")
            import traceback
            self.log(f"Traceback: {traceback.format_exc()[:200]}", "ERROR")

    def run(self):
        self.load_files()
        self.print_banner()
        self.show_menu()
        
        self.log(f"Loaded {len(self.accounts)} accounts successfully", "INFO")
        print(f"\n{Fore.CYAN}============================================================{Style.RESET_ALL}\n")
        
        cycle = 1
        while True:
            self.log(f"Cycle #{cycle} Started", "CYCLE")
            print(f"{Fore.CYAN}------------------------------------------------------------{Style.RESET_ALL}")
            
            for i, pk in enumerate(self.accounts):
                self.log(f"Account #{i+1}/{len(self.accounts)}", "INFO")
                
                current_proxy = None
                if self.use_proxy and self.proxies:
                    current_proxy = self.proxies[i % len(self.proxies)]
                
                self.login_process(pk, current_proxy)
                
                if i < len(self.accounts) - 1:
                    print(f"{Fore.WHITE}............................................................{Style.RESET_ALL}")
                    time.sleep(3) 
            
            print(f"{Fore.CYAN}------------------------------------------------------------{Style.RESET_ALL}")
            self.log(f"Cycle #{cycle} Complete", "CYCLE")
            print(f"{Fore.CYAN}============================================================{Style.RESET_ALL}\n")
            
            cycle += 1
            
            for x in range(86400, 0, -1):
                hours = x // 3600
                minutes = (x % 3600) // 60
                secs = x % 60
                print(f"\r[COUNTDOWN] Next cycle in: {hours:02d}:{minutes:02d}:{secs:02d} ", end="", flush=True)
                time.sleep(1)
            print("\r" + " " * 60 + "\r", end="", flush=True)

if __name__ == "__main__":
    try:
        bot = AixCryptoBot()
        bot.run()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Program terminated by user.{Style.RESET_ALL}")
        sys.exit()
