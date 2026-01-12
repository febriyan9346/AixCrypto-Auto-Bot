# AixCrypto Auto Bot

🎮 **[Join AixCrypto Hub](https://hub.aixcrypto.ai?invite=N88N2D)** 🎮
Join to my team : febriyan93

Automated bot for AixCrypto platform that handles daily check-ins, betting sessions, and reward collection.

## Features

- ✅ **Automatic Daily Check-in** - Claims daily rewards automatically
- 🎲 **Automated Betting** - Places bets with random UP/DOWN predictions
- 🔄 **Multi-Account Support** - Manage multiple wallets simultaneously
- 🌐 **Proxy Support** - Use proxies for enhanced security and multi-accounting
- 🤖 **Captcha Solving** - Supports both 2Captcha and SCTG solvers
- 📊 **Detailed Logging** - Color-coded console output with timestamps
- ⏰ **Auto Cycling** - Runs continuously with 24-hour cycles

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Ethereum wallet private keys
- Captcha solver API key (2Captcha or SCTG)

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/febriyan9346/AixCrypto-Auto-Bot.git
cd AixCrypto-Auto-Bot
```

2. **Install required dependencies:**
```bash
pip install -r requirements.txt
```

## Configuration

### 1. Create Required Files

Create the following text files in the root directory:

#### `accounts.txt`
Add your Ethereum private keys (one per line):
```
0xyourprivatekey1
0xyourprivatekey2
0xyourprivatekey3
```

#### `2captcha.txt` (Optional)
Add your 2Captcha API key:
```
your_2captcha_api_key_here
```

#### `sctg.txt` (Optional)
Add your SCTG API key:
```
your_sctg_api_key_here
```

#### `proxy.txt` (Optional)
Add your proxies in one of these formats (one per line):
```
ip:port
ip:port:username:password
http://ip:port
http://username:password@ip:port
socks5://ip:port
```

### 2. File Structure
```
AixCrypto-Auto-Bot/
├── bot.py
├── requirements.txt
├── README.md
├── accounts.txt
├── 2captcha.txt (optional)
├── sctg.txt (optional)
└── proxy.txt (optional)
```

## Usage

1. **Run the bot:**
```bash
python bot.py
```

2. **Select your preferences:**
   - Choose whether to use proxies (1) or not (2)
   - Select captcha solver: 2Captcha (1) or SCTG (2)
   - Enter maximum bets per account per session

3. **Let it run!** The bot will:
   - Process each account sequentially
   - Claim daily rewards
   - Execute betting sessions
   - Wait 24 hours and repeat

## Requirements.txt

```txt
colorama
curl-cffi
eth-account
pytz
requests
```

## Features Breakdown

### Daily Check-in
- Automatically claims daily rewards for each account
- Handles already-claimed status gracefully
- Displays reward amounts

### Automated Betting
- Random UP/DOWN predictions for each bet
- Configurable number of bets per session
- Real-time result tracking (WIN/LOSE)
- Rate limit handling with automatic retries

### Proxy Rotation
- Supports multiple proxy formats
- Rotates proxies across accounts
- Automatic fallback to no-proxy mode if proxy fails

### Captcha Solving
- **2Captcha Integration:** Industry-standard captcha solver
- **SCTG Integration:** Alternative captcha solving service
- Automatic fallback between solvers
- Turnstile captcha support

## Console Output

The bot provides color-coded logging for easy monitoring:

- 🔵 **CYAN** - General information and system messages
- 🟢 **GREEN** - Successful operations
- 🔴 **RED** - Errors and failures
- 🟡 **YELLOW** - Warnings and skipped operations
- 🟣 **MAGENTA** - Cycle and task information

## Security Notes

⚠️ **Important Security Information:**

- Never share your `accounts.txt` file or private keys
- Store your private keys securely
- Use proxies to protect your IP address
- Keep your API keys confidential
- This bot is for educational purposes only

## Troubleshooting

### Common Issues

**Issue:** "File missing" error
- **Solution:** Ensure all required files exist (accounts.txt and at least one captcha API key file)

**Issue:** Captcha solving fails
- **Solution:** Check your API key balance and validity

**Issue:** Proxy connection errors
- **Solution:** Verify proxy format and connectivity, or switch to no-proxy mode

**Issue:** Login fails
- **Solution:** Verify private key format (should include or exclude '0x' prefix)

**Issue:** Rate limit errors (429)
- **Solution:** Bot automatically waits 60 seconds, but consider reducing bet frequency

## Disclaimer

This bot is provided for educational purposes only. Use at your own risk. The authors are not responsible for:

- Account bans or restrictions
- Loss of funds or rewards
- Any violations of AixCrypto's terms of service
- Any other damages or losses

Always review and comply with the platform's terms of service before using automation tools.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open source and available under the MIT License.

## Changelog

### Version 1.0.0
- Initial release
- Multi-account support
- Proxy integration
- Dual captcha solver support (2Captcha & SCTG)
- Automated daily check-in
- Automated betting system
- 24-hour cycle automation

---

## Support Us with Cryptocurrency

You can make a contribution using any of the following blockchain networks:

| Network | Wallet Address |
|---------|----------------|
| **EVM** | `0x216e9b3a5428543c31e659eb8fea3b4bf770bdfd` |
| **TON** | `UQCEzXLDalfKKySAHuCtBZBARCYnMc0QsTYwN4qda3fE6tto` |
| **SOL** | `9XgbPg8fndBquUYXkGpNYKHHhymdmVhmF6nMkPxhXTki` |
| **SUI** | `0x8c3632ddd46c984571bf28f784f7c7aeca3b8371f146c4024f01add025f993bf` |

---

**Made with ❤️ by FEBRIYAN**

⭐ If you find this bot helpful, please give it a star on GitHub!
