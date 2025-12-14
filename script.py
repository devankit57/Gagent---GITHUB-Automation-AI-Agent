import os
import re
import requests
import google.generativeai as genai
from github import Github, Auth
from datetime import datetime 
from dotenv import load_dotenv

# load .env from same folder
load_dotenv()

# Configuration from environment (.env)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME", "REPO")
EMAIL_API_URL = os.getenv("EMAIL_API_URL", "EMAIL API")

SENDER_FIRST_NAME = os.getenv("SENDER_FIRST_NAME", "Ankit")
SENDER_LAST_NAME = os.getenv("SENDER_LAST_NAME", "Mishra")
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "ankit@batworks.in")

# -------------------------------------------------
# HELPERS
# -------------------------------------------------
def sanitize_folder_name(title):
    folder = re.sub(r"[^\w\s-]", "", title)
    folder = re.sub(r"[-\s]+", "-", folder)
    return folder.strip("-").lower()


# -------------------------------------------------
# GEMINI FUNCTIONS
# -------------------------------------------------
def get_random_dsa_problem():
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = """
    Generate a random Data Structures and Algorithms problem.
    Return ONLY the problem title.
    """

    response = model.generate_content(prompt)
    title = response.text.strip().replace("*", "")
    return title


def generate_code_with_gemini(prompt):
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text


# -------------------------------------------------
# GITHUB PUSH
# -------------------------------------------------
def push_to_github(code_content, problem_title, commit_message):
    try:
        auth = Auth.Token(GITHUB_TOKEN)
        g = Github(auth=auth)
        repo = g.get_repo(REPO_NAME)

        folder_name = sanitize_folder_name(problem_title)
        file_path = f"{folder_name}/solution.py"

        try:
            # Update if exists
            contents = repo.get_contents(file_path)
            repo.update_file(
                contents.path,
                commit_message,
                code_content,
                contents.sha
            )
            print(f"✓ Updated {file_path}")
        except:
            # Create if new
            repo.create_file(
                file_path,
                commit_message,
                code_content
            )
            print(f"✓ Created {file_path}")

        folder_url = f"https://github.com/{REPO_NAME}/tree/main/{folder_name}"
        return True, folder_url

    except Exception as e:
        print("❌ GitHub Error:", str(e))
        return False, str(e)


# -------------------------------------------------
# EMAIL API CALL
# -------------------------------------------------
def trigger_email_api(first_name, last_name, email, message, repo_link=""):
    payload = {
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "message": message,
        "repo": repo_link
    }

    try:
        resp = requests.post(EMAIL_API_URL, json=payload, timeout=10)

        # Try parsing JSON
        try:
            data = resp.json()
        except:
            data = resp.text

        if resp.status_code == 200:
            print("✉️ Email sent successfully:", data)
            return True, data
        else:
            print("⚠️ Email API returned error:", data)
            return False, data

    except Exception as e:
        print("❌ Email API Error:", str(e))
        return False, str(e)


# -------------------------------------------------
# MAIN FLOW
# -------------------------------------------------
def main():
    print("🎲 Generating random DSA problem...")
    problem_title = get_random_dsa_problem()
    print("📝 Problem:", problem_title)

    prompt = f"""
    Create a Python solution for the "{problem_title}" problem.
    Include:
    - Problem description
    - Clean code + comments
    - Time + space complexity
    - Test cases
    Return only Python code.
    """

    print("⚙️ Generating solution...")
    generated_code = generate_code_with_gemini(prompt)

    print("📤 Pushing to GitHub...")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = f"Add solution for {problem_title} - {timestamp}"

    success, repo_url = push_to_github(generated_code, problem_title, commit_msg)

    if success:
        print("✅ GitHub push successful:", repo_url)

        # Trigger email
        email_msg = f"Solution added for '{problem_title}'. Commit: {commit_msg}"

        sent, resp = trigger_email_api(
            SENDER_FIRST_NAME,
            SENDER_LAST_NAME,
            SENDER_EMAIL,
            email_msg,
            repo_link=repo_url
        )

        if sent:
            print("📧 Email notification sent.")
        else:
            print("⚠️ Email sending failed.")

    else:
        print("❌ GitHub push failed — email not sent.")


if __name__ == "__main__":
    main()


