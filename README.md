# GitHub Automation Agent 🤖
### AI-Powered DSA Code Generator | Automated Daily Commits with Gemini API

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Gemini API](https://img.shields.io/badge/Gemini-API-4285F4?style=flat&logo=google&logoColor=white)](https://ai.google.dev/)
[![GitHub](https://img.shields.io/badge/GitHub-API-181717?style=flat&logo=github&logoColor=white)](https://github.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat)](LICENSE)
[![Automation](https://img.shields.io/badge/Automation-Cron_Jobs-FF6B6B?style=flat&logo=clockify&logoColor=white)]()

---

## 👋 About

```python
automation_agent = {
  "purpose": "Generate & push DSA problems to GitHub automatically",
  "ai_engine": "Google Gemini 2.5 Flash",
  "automation": "Cron Jobs (Daily Schedule)",
  "notification": "Email API Integration",
  "status": "Production Ready 🚀"
}
```

A Python-based AI agent that uses **Google Gemini API** to automatically generate Data Structures & Algorithms problems with solutions and pushes them to your GitHub repository daily. Includes email notifications for every commit!

---

## ✨ Features

- 🤖 **AI-Powered**: Uses Gemini 2.5 Flash for intelligent DSA problem generation
- ⏰ **Automated Daily Commits**: Schedule with cron jobs
- 📁 **Organized Structure**: Each problem in its own folder
- 📧 **Email Notifications**: Get notified on every successful commit
- 🔄 **Smart Updates**: Updates existing files or creates new ones
- 📝 **Complete Solutions**: Includes problem description, code, complexity analysis, and test cases

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gemini API](https://img.shields.io/badge/Gemini_API-4285F4?style=for-the-badge&logo=google&logoColor=white)
![GitHub API](https://img.shields.io/badge/GitHub_API-181717?style=for-the-badge&logo=github&logoColor=white)

---

## 📋 Prerequisites

- ✅ Python 3.8+
- ✅ GitHub Account & Personal Access Token
- ✅ Google Gemini API Key ([Get it here](https://ai.google.dev/))
- ✅ Email API endpoint (optional for notifications)

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/devankit57/Gagent---GITHUB-Automation-AI-Agent.git
cd Gagent---GITHUB-Automation-AI-Agent
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```bash
# Required: Gemini API
GEMINI_API_KEY=your_gemini_api_key_here

# Required: GitHub Configuration
GITHUB_TOKEN=your_github_personal_access_token
REPO_NAME=yourusername/your-repo-name

# Optional: Email Notification API
EMAIL_API_URL= Create your email server
SENDER_FIRST_NAME=Your_First_Name
SENDER_LAST_NAME=Your_Last_Name
SENDER_EMAIL=your.email@example.com
```

### 4. Run the Script
```bash
python script.py
```

---

## 📁 Project Structure

```
Gagent---GITHUB-Automation-AI-Agent/
│
├── script.py              # Main automation script
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── .gitignore            # Git ignore file
└── README.md             # This file
```

---

## 📦 Requirements

### `requirements.txt`
```txt
google-generativeai>=0.3.0
PyGithub>=2.1.1
python-dotenv>=1.0.0
requests>=2.31.0
```

---

## ⚙️ How It Works

```python
1. 🎲 Generate random DSA problem using Gemini API
2. ⚙️ Create complete solution with Gemini
3. 📤 Push to GitHub in organized folder structure
4. 📧 Send email notification with commit details
```

### Generated Folder Structure

```
your-dsa-repo/
├── two-sum/
│   └── solution.py
├── binary-search/
│   └── solution.py
├── merge-sort/
│   └── solution.py
└── ...
```

---

## 🤖 Automate with Cron Jobs

### Linux/Mac Setup

1. Open crontab editor:
```bash
crontab -e
```

2. Add a schedule (examples):

```bash
# Run every day at 9:00 AM
0 9 * * * cd /path/to/Gagent---GITHUB-Automation-AI-Agent && /usr/bin/python3 script.py >> logs/automation.log 2>&1

# Run every day at 6:00 PM
0 18 * * * cd /path/to/Gagent---GITHUB-Automation-AI-Agent && /usr/bin/python3 script.py >> logs/automation.log 2>&1

# Run twice daily (9 AM and 9 PM)
0 9,21 * * * cd /path/to/Gagent---GITHUB-Automation-AI-Agent && /usr/bin/python3 script.py >> logs/automation.log 2>&1
```

3. Create logs directory:
```bash
mkdir logs
```

4. Verify cron job:
```bash
crontab -l
```

### Windows Setup

1. Open **Task Scheduler**
2. Create **Basic Task**
3. Set **Trigger**: Daily at 9:00 AM
4. Set **Action**: Start a program
   - Program: `python.exe`
   - Arguments: `script.py`
   - Start in: `C:\path\to\Gagent---GITHUB-Automation-AI-Agent`

---

## 🔧 Configuration Guide

### Getting GitHub Token

1. Go to [GitHub Settings > Developer Settings > Personal Access Tokens](https://github.com/settings/tokens)
2. Click **Generate new token (classic)**
3. Select scopes: `repo` (Full control of private repositories)
4. Copy the token to `.env` file

### Getting Gemini API Key

1. Visit [Google AI Studio](https://ai.google.dev/)
2. Click **Get API Key**
3. Create new API key
4. Copy to `.env` file

### Email API (Optional)

If you want email notifications:
- Set up your email API endpoint
- Configure sender details in `.env`
- The script sends a POST request with commit details

---

## 📊 Example Output

```
🎲 Generating random DSA problem...
📝 Problem: Reverse a Linked List
⚙️ Generating solution...
📤 Pushing to GitHub...
✓ Created reverse-a-linked-list/solution.py
✅ GitHub push successful: https://github.com/yourusername/DSA-Codes/tree/main/reverse-a-linked-list
✉️ Email sent successfully: {'status': 'success'}
📧 Email notification sent.
```

---

## 🔒 Security Best Practices

⚠️ **Important:**
- Never commit your `.env` file
- Keep API keys and tokens private
- Add `.env` to `.gitignore`
- Regularly rotate your GitHub tokens
- Use environment variables for all secrets

### `.gitignore`
```gitignore
# Environment variables
.env

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
venv/
env/

# Logs
logs/
*.log

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db
```

---

## 🐛 Troubleshooting

### GitHub Push Failed
- ✓ Check if `GITHUB_TOKEN` has `repo` scope
- ✓ Verify `REPO_NAME` format: `username/repo-name`
- ✓ Ensure repository exists and you have write access

### Gemini API Error
- ✓ Verify `GEMINI_API_KEY` is correct
- ✓ Check API quota limits
- ✓ Ensure internet connection is stable

### Cron Job Not Running
- ✓ Check cron service: `sudo systemctl status cron`
- ✓ Use absolute paths in crontab
- ✓ Check logs: `cat logs/automation.log`
- ✓ Verify Python path: `which python3`

### Email Notification Failed
- ✓ Check `EMAIL_API_URL` is reachable
- ✓ Verify API endpoint accepts POST requests
- ✓ Review API response in console output

---

## 🎯 Customization

### Change Problem Generation Prompt

Edit the prompt in `script.py`:

```python
prompt = f"""
Create a Python solution for the "{problem_title}" problem.
Include:
- Problem description (add more details here)
- Clean code + comments
- Time + space complexity
- Multiple test cases (increase number)
- Edge cases
Return only Python code.
"""
```

### Add More Languages

Modify the file extension and prompt:

```python
file_path = f"{folder_name}/solution.cpp"  # For C++
file_path = f"{folder_name}/solution.java"  # For Java
```

---

## 📈 Features to Add

- [ ] Support for multiple programming languages
- [ ] Difficulty level selection (Easy/Medium/Hard)
- [ ] Topic-specific problem generation
- [ ] Leetcode problem integration
- [ ] Statistics dashboard
- [ ] Problem tracking database

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔗 Repository

**GitHub:** [https://github.com/devankit57/Gagent---GITHUB-Automation-AI-Agent](https://github.com/devankit57/Gagent---GITHUB-Automation-AI-Agent)
