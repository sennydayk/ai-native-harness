#!/usr/bin/env bash
# L1 스모크 테스트 템플릿. 사용: PORT=8000 bash tests/smoke.sh
set -u
BASE="http://localhost:${PORT:-8000}"
pass=0; fail=0
check() { # check <경로> <응답에 있어야 할 문자열>
  body=$(curl -s -m 10 "$BASE$1"); code=$(curl -s -o /dev/null -w '%{http_code}' -m 10 "$BASE$1")
  if [ "$code" = "200" ] && echo "$body" | grep -q -- "$2"; then echo "PASS $1"; pass=$((pass+1))
  else echo "FAIL $1 (status=$code, expected '$2')"; fail=$((fail+1)); fi
}
check "/" "<title>"          # 메인 화면
# check "/api/items" "\"id\""  # 핵심 API — 과제에 맞게 수정
echo "결과: PASS=$pass FAIL=$fail"; [ "$fail" -eq 0 ]
