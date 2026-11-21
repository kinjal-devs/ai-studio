# Mom's AI Studio

A mobile-first creative workspace built with Python and Flet. The app is designed to become an Android-first AI video creation gift.

## Current build

- Home dashboard and clear navigation
- Text-to-video and image-to-video creation screens
- Prompt and video setting controls
- Inspiration / Explore section
- Personal creations library (empty state)
- Settings and privacy guidance

**Important:** This is the interface foundation. It does not generate videos yet. Real generation requires integrating a video-generation provider and securely configuring its API key. The app will not pretend that a video was generated when no provider is connected.

## Run on Windows 11

1. Install Python 3.12.
2. Open this folder in VS Code.
3. Create and activate a virtual environment:

   ```powershell
   py -3.12 -m venv .venv
   .venv\\Scripts\\Activate.ps1
   ```

4. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Start the app:

   ```powershell
   flet run
   ```

## API key safety

Copy `.env.example` to `.env` when provider integration is added. Never commit a real API key to GitHub or share it in screenshots.
