# 🚀 Naukri Profile Headline Updater

Automate updating your Naukri.com profile headline using **Playwright** - runs daily via cron on EC2 or local machine. Say goodbye to manual profile updates!

## ✨ Features

- 🤖 Fully automated headline rotation
- 🔐 Session persistence (login only once)
- 🌐 Headless browser support (EC2/Linux)
- ⏰ Cron job integration for daily updates
- 🛡️ Anti-detection measures to avoid blocking
- 📸 Debug screenshots on failure

## 📋 Prerequisites

- Python 3.8+
- AWS EC2 instance (or any Linux server) OR local machine with Python
- Naukri.com account

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/naukri-bot.git
cd naukri-bot
