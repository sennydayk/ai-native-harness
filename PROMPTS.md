# PROMPTS — 단계별 프롬프트 셋
> `< >` 부분만 바꿔서 쓴다. 짧게 보내고, 한 번에 한 가지만 시킨다.

## 0. 세팅 (sh 터미널)
```bash
git status >/dev/null 2>&1 || git init -q
git add -A && git commit -qm "init: 제공 원본" --allow-empty
git clone --depth 1 https://github.com/sennydayk/ai-native-harness harness && rm -rf harness/.git
[ -f AGENTS.md ] && cat harness/AGENTS.md >> AGENTS.md || cp harness/AGENTS.md .
git add -A && git commit -qm "chore: 작업 하네스 추가"
# (허용 확인된 경우만) mkdir -p ~/.codex/skills && cp -r harness/skills/* harness/third_party/* ~/.codex/skills/
```

## P0. 부팅 확인
```
AGENTS.md를 읽고 적용할 원칙을 5줄로 요약하고, 스킬 목차에서 어떤 상황에 어떤 파일을 읽는지 확인해줘. 아직 아무 파일도 수정하지 마.
```

## P1. 과제 분해 — brief-breakdown
```
brief-breakdown 스킬을 따라 README를 분해해서 BRIEF.md를 만들어줘. 제출 요구사항은 원문 그대로 빠짐없이, 질문 후보는 어떤 설계 결정에 영향을 주는지 함께 적어줘. 코드는 쓰지 마.
```

## P2. 데이터 탐색 — data-recon (두 번째 Codex 세션)
```
data-recon 스킬을 따라 제공된 파일을 읽기만 하고 EXPLORE.md로 정리해줘. 큰 파일은 head와 통계로만 보고, 품질 이슈의 처리 방법은 정하지 말고 질문으로 남겨줘.
```

## P3. 실무자 답변 반영 — domain-notes (답변 받을 때마다)
```
domain-notes 스킬로 아래 실무자 답변을 DOMAIN.md에, 대화 요지를 INTERVIEW.md에 반영해줘. 실무자 표현과 기준값은 바꾸지 말고, 기존 내용과 충돌하면 표시해줘.
질문: <내가 보낸 질문>
답변: <실무자 답변>
```

## P4. 실무자 메시지 초안 — ask-draft
```
ask-draft 스킬로 <확인형/선택형/예외형/범위 협상형/중간 피드백형> 메시지 초안을 짧은 버전과 자세한 버전으로 만들어줘.
고민: <지금 판단이 필요한 것>
```

## P5. 요구 정리 — spec-agree
```
spec-agree 스킬로 BRIEF·INTERVIEW·DOMAIN을 근거로 PLAN.md를 만들어줘. MVP는 작게, 제외 항목은 이유와 함께. 마지막에 실무자에게 보낼 확인 메시지(범위 협상형) 초안도 줘.
```
(답을 받은 뒤)
```
실무자 답변을 PLAN.md에 반영하고 변경 이력에 남겨줘: <답변>
```

## P6. 구조 결정 — design-options
```
design-options 스킬로 PLAN.md 기준 구조 2~3안을 표로 비교하고 적정 설계 체크까지 해줘. 추천안과 이유를 주되 결정은 내가 할게. 코드는 아직 쓰지 마.
```
(결정 후)
```
<B안>으로 간다. 이유: <한 줄>. DECISIONS.md에 버린 대안과 함께 기록해줘.
```

## P7. 최소 E2E
```
slice-loop 스킬을 따라 최소 E2E부터 만들어줘: 서버가 0.0.0.0에서 뜨고 화면에 실제 데이터가 한 번 표시되는 것까지만. 먼저 계획 3줄을 보여주고 내가 OK하면 진행해.
```

## P8. 기능 위임 (slice 하나)
```
slice-loop로 다음 기능을 구현해줘.
목표: <기능>
입력: <파일/모듈>
제약: <PLAN·DOMAIN의 규칙>, 새 의존성 금지, 범위 밖 기능 추가 금지
완료 조건: <테스트 통과 / 화면에서 무엇이 보이면>
계획 3줄 먼저 보여줘.
```

## P9. 검증 — verify
```
verify 스킬로 방금 기능을 검증해줘. 손으로 계산 가능한 작은 입력으로 기대값을 먼저 만들고, 테스트를 실행해서 출력을 보여줘. 엣지 케이스 2개 포함.
```

## P10. E2E — e2e-check
```
e2e-check 스킬로 PLAN의 성공 기준에서 핵심 흐름 1~3개를 골라 L1 스모크를 만들고 실행해줘. playwright가 이미 있거나 5분 안에 설치되면 L2도 작성해서 실행하고, 결과를 E2E_RESULT.md에 남겨줘.
```

## P11. 막혔을 때 — systematic-debugging
```
harness/third_party/systematic-debugging/SKILL.md를 따라 이 문제의 원인부터 조사해줘. 수정은 원인 가설을 내가 확인한 뒤에 해.
증상: <에러 메시지 / 기대와 다른 동작>
```

## P12. 감사 — right-size-audit
```
right-size-audit 스킬로 PLAN 대비 과한 코드·의존성·추상화 목록과 문서-코드 불일치 목록을 보여줘. 제거 여부는 내가 정할게.
```

## P13. 세션 전환 — handoff (세션 모드)
(기존 세션)
```
handoff 스킬 세션 모드로 HANDOFF.md를 작성하고 커밋해줘.
```
(새 세션 첫 요청)
```
AGENTS.md와 HANDOFF.md를 읽고, 필요한 경우에만 PLAN.md·DOMAIN.md의 관련 섹션을 읽은 뒤 '다음 할 일' 1번부터 진행해줘. 시작 전에 이해한 현재 상태를 3줄로 말해줘.
```

## P14. 마무리 — risks + handoff (현업 모드)
```
risks 스킬로 RISKS.md를 만들고, 이어서 handoff 현업 모드로 USER_GUIDE.md를 실무자 언어로 써줘. 구현되지 않은 건 되는 것처럼 쓰지 마.
```

## P15. 제출 점검 — submit-check
```
submit-check 스킬로 제출 체크리스트를 1:1 대조하고, README 실행 방법을 그대로 따라 실행해서 확인한 뒤 결과를 표로 보고해줘.
```

## P16. 서술형 대비 — oral-prep
```
oral-prep 스킬로 이 결과물과 작업 기록 기준 확인 질문 10개를 만들어줘. 답은 쓰지 말고 근거 파일 위치만.
```

## 교정용 한 줄
- `잠깐, 그건 PLAN 범위 밖이야. 되돌리고 제안으로만 남겨줘.`
- `코드 쓰기 전에 계획 3줄만 먼저.`
- `완료라고 하기 전에 실행 결과를 보여줘.`
- `그 용어/기준은 DOMAIN.md 기준으로 다시 맞춰줘.`
- `지금까지 결정한 것 중 DECISIONS.md에 빠진 게 있으면 추가해줘.`
