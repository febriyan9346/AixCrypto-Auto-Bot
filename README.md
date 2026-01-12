# AixCrypto Auto Bot

🔗 **[Join AixCrypto Hub](https://hub.aixcrypto.ai?invite=N88N2D)**  
👥 **Join Team:** `febriyan93`

---

## 📋 Description

AixCrypto Auto Bot is an automated trading bot designed for the AixCrypto platform. It features AI-powered market prediction, automatic daily check-ins, task claiming, and intelligent betting strategies.

## ✨ Features

- 🤖 **AI-Powered Predictions**: Advanced pattern recognition and market analysis
- 🎯 **Smart Trading Strategies**: 
  - Anti-Streak Detection (Overbought/Oversold Reversal)
  - Zig-Zag Pattern Detection
  - Pattern Matching Algorithm
  - Trend Exhaustion Analysis
- 🔄 **Automatic Daily Check-in**: Never miss your daily rewards
- 📊 **Task Auto-Claim**: Automatically claims all available tasks
- 🔐 **Multi-Account Support**: Manage multiple wallets simultaneously
- 🌐 **Proxy Support**: Built-in proxy rotation for enhanced privacy
- 🧩 **Captcha Solving**: Supports both 2Captcha and SCTG solvers
- 📈 **Real-time Statistics**: Track your performance with detailed metrics
- 🎨 **Colorful UI**: Beautiful console interface with real-time updates

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/febriyan9346/AixCrypto-Auto-Bot.git
cd AixCrypto-Auto-Bot
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

## 📝 Configuration

### Required Files

Create the following files in the bot directory:

#### 1. `accounts.txt`
Add your private keys (one per line):
```
your_private_key_1
your_private_key_2
your_private_key_3
```

#### 2. `2captcha.txt` (Optional)
Add your 2Captcha API key:
```
your_2captcha_api_key
```

#### 3. `sctg.txt` (Optional)
Add your SCTG API key:
```
your_sctg_api_key
```

#### 4. `proxy.txt` (Optional)
Add your proxies (one per line):
```
ip:port:username:password
ip:port
http://ip:port
socks5://ip:port
```

### File Structure
```
AixCrypto-Auto-Bot/
├── bot.py
├── requirements.txt
├── accounts.txt
├── 2captcha.txt (optional)
├── sctg.txt (optional)
└── proxy.txt (optional)
```

## 🎮 Usage

### Run the Bot

```bash
python bot.py
```

### Configuration Options

When you start the bot, you'll be prompted to configure:

1. **Proxy Mode**
   - Option 1: Run with Proxy
   - Option 2: Run without Proxy

2. **Captcha Solver**
   - Option 1: 2Captcha
   - Option 2: SCTG

3. **Max Bets per Account**
   - Enter the number of bets each account should make per cycle
   - Default: 5 bets

## 🧠 AI Prediction System

The bot uses multiple sophisticated strategies:

### 1. Anti-Streak Detection
Identifies overbought/oversold conditions:
- 3+ consecutive UPs → Predicts DOWN (Reversal)
- 3+ consecutive DOWNs → Predicts UP (Reversal)

### 2. Zig-Zag Pattern Detection
Recognizes alternating patterns:
- U-D-U pattern → Predicts DOWN
- D-U-D pattern → Predicts UP

### 3. Pattern Matching
Analyzes historical data to find recurring patterns and predicts based on past outcomes.

### 4. Smart Reversal
Default strategy when no clear pattern is detected, betting against the last move (Trend Exhaustion).

## 📊 Statistics

The bot provides comprehensive statistics:
- Total Credits
- Battery Level
- Total Bets
- Wins & Losses
- Win Rate Percentage
- Daily Bet Count

## 🔒 Security

- ⚠️ **Never share your private keys**
- 🔐 Keep your `accounts.txt` file secure
- 🌐 Use trusted proxies only
- 🔑 Protect your captcha solver API keys

## ⚙️ Requirements

```
curl-cffi
eth-account
colorama
pytz
```

## 🐛 Troubleshooting

### Common Issues

1. **Captcha Failed**
   - Check your API key validity
   - Ensure you have sufficient balance in your captcha service
   - Try switching between 2Captcha and SCTG

2. **Login Failed**
   - Verify your private keys are correct
   - Check if proxies are working (if enabled)
   - Ensure captcha is solving successfully

3. **Bet Failed**
   - Check your battery level
   - Verify you have sufficient credits
   - Wait for the next round if current round is locked

4. **Rate Limit Error (429)**
   - The bot will automatically wait 60 seconds
   - Consider using proxies to avoid rate limits

## 📈 Performance Tips

1. **Use Quality Proxies**: Improve success rate and avoid rate limits
2. **Set Reasonable Bet Counts**: Don't exhaust your battery too quickly
3. **Monitor Win Rate**: Adjust strategies based on performance
4. **Daily Check-ins**: Maximize rewards by running at least once per day

## 🔄 Update Cycle

The bot runs in continuous cycles:
- Completes all accounts
- Waits 24 hours
- Repeats the cycle

## ⚠️ Disclaimer

This bot is for educational purposes only. Use at your own risk. Always:
- Understand the risks involved in automated trading
- Start with small amounts
- Never invest more than you can afford to lose
- Comply with the platform's terms of service

## 📞 Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Join the AixCrypto community

## 📜 License

This project is open source and available under the MIT License.

---

## 💰 Support Us with Cryptocurrency

You can make a contribution using any of the following blockchain networks:

| Network | Wallet Address |
|---------|----------------|
| **EVM** | `0x216e9b3a5428543c31e659eb8fea3b4bf770bdfd` |
| **TON** | `UQCEzXLDalfKKySAHuCtBZBARCYnMc0QsTYwN4qda3fE6tto` |
| **SOL** | `9XgbPg8fndBquuYXkGpNYKHHhymdmVhmF6nMkPxhXTki` |
| **SUI** | `0x8c3632ddd46c984571bf28f784f7c7aeca3b8371f146c4024f01add025f993bf` |

---

**Made with ❤️ by FEBRIYAN**