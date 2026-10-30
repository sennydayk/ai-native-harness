"""L2 핵심 흐름 테스트 템플릿. 사용: python3 tests/e2e_flow.py (서버가 떠 있어야 함)"""
import os, sys
from playwright.sync_api import sync_playwright

BASE = f"http://localhost:{os.environ.get('PORT', '8000')}"
SHOTS = "tests/screenshots"
os.makedirs(SHOTS, exist_ok=True)

def main() -> int:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        errors = []
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        try:
            # 흐름 1: 메인 화면 열기 — 과제에 맞게 수정
            page.goto(BASE)
            page.wait_for_load_state("networkidle")
            page.screenshot(path=f"{SHOTS}/01_main.png", full_page=True)
            # 예: assert page.locator("table tr").count() > 1, "목록이 비어 있음"
            # 흐름 2: 항목 클릭 → 상세 확인
            # page.locator("text=상세").first.click(); page.wait_for_load_state("networkidle")
            # page.screenshot(path=f"{SHOTS}/02_detail.png", full_page=True)
            assert not errors, f"콘솔 에러: {errors}"
            print("PASS e2e flow"); return 0
        except Exception as e:
            page.screenshot(path=f"{SHOTS}/fail.png", full_page=True)
            print(f"FAIL e2e flow: {e}"); return 1
        finally:
            browser.close()

if __name__ == "__main__":
    sys.exit(main())
