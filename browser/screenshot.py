from playwright.sync_api import sync_playwright, TimeoutError
from pathlib import Path
import uuid


def take_screenshot(url: str):
    try:
        # 📁 Base directory
        BASE_DIR = Path.cwd()
        screenshot_dir = BASE_DIR / "assets" / "screenshots"
        screenshot_dir.mkdir(parents=True, exist_ok=True)

        # 🆔 Unique filename
        filename = f"{uuid.uuid4().hex}.png"
        screenshot_path = screenshot_dir / filename

        # 🌐 Playwright logic
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            try:
                page.goto(url, timeout=60000)
            except TimeoutError:
                print("Page load timeout")
                browser.close()
                return None

            page.screenshot(path=str(screenshot_path), full_page=True)
            browser.close()

        print(f"Screenshot saved: {screenshot_path}")
        return screenshot_path

    except Exception as e:
        print("Unexpected error occurred")
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    print(take_screenshot("https://scholarships.gov.in/Institute"))
