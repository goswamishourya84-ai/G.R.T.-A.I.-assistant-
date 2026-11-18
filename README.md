# G.R.T. AI — Startup Edition

Original starter project; not ChatGPT source code and not a ready-made APK.

Includes animated startup screen, custom G.R.T. AI logo/icon, responsive chat UI, Hindi/English voice input where supported, optional spoken replies, local chat history, Neon Dark/Light/Midnight Purple themes, language preference, display-name personalization, and PWA install support.

## Publish from Android
1. Upload all files in this folder to your private GitHub repository. Do not upload API keys or `.env` files.
2. Connect the repository to a Python hosting provider such as Render.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`
5. Add `OPENAI_API_KEY` as a private environment variable in the hosting dashboard. Ask a parent/guardian to help with account and billing setup; API usage may cost money.
6. Deploy, open the HTTPS URL in Android Chrome, then menu > Install app / Add to Home screen.

PWA installation requires HTTPS. AI chat needs an online server and API key. Voice input depends on browser/device support. Preferences and chat history are saved locally in the browser.\n