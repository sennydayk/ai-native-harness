---
name: e2e-check
description: 서버가 뜬 뒤 핵심 사용자 흐름을 L1(curl 스모크) → L2(헤드리스 Playwright 스크립트) → L3(수동 체크리스트) 순으로 테스트하고 E2E_RESULT.md에 증거를 남긴다.
---
# e2e-check — 끝에서 끝까지 테스트

## 0. 환경 확인 (처음 한 번)
`node --version; python3 --version; python3 -c "import playwright" 2>&1; npx playwright --version 2>&1; free -h`

## 1. 흐름 고르기
- PLAN.md 성공 기준에서 **핵심 사용자 흐름 1~3개**만 고른다. (예: 페이지 열기 → 목록 표시 → 항목 상세 열기)

## 2. L1 — 스모크 (항상)
- `harness/skills/e2e-check/smoke_template.sh`를 `tests/smoke.sh`로 복사해 경로·기대 문자열을 채운다.
- 서버가 떠 있는 상태에서 실행. 기능을 추가할 때마다 다시 돌린다 (회귀 확인).

## 3. L2 — 헤드리스 Playwright (가능할 때만)
- playwright가 이미 있으면 바로, 없으면 설치를 **5분 이내로 한 번만** 시도한다 (`pip install playwright && python3 -m playwright install chromium`). 실패하거나 메모리가 부족하면 L3로 간다.
- `harness/skills/e2e-check/flow_template.py`를 `tests/e2e_flow.py`로 복사해 흐름을 채운다. 서버 기동이 필요하면 `third_party/webapp-testing/scripts/with_server.py`를 쓴다 (`--help` 먼저).
- 스크린샷은 `tests/screenshots/`에 저장한다.
- 테스트는 **스크립트를 작성해 터미널에서 실행**한다. 에이전트가 브라우저를 대화형으로 직접 조작하지 않는다.

## 4. L3 — 수동 (항상 가능)
- 내장 Browser 미리보기에서 흐름을 직접 클릭하고 결과를 기록한다.

## 5. 기록
- `E2E_RESULT.md`(templates 복사)에 시각 / 단계 / 흐름 / 결과 / 증거 / 실패 시 원인·조치 → 커밋.
