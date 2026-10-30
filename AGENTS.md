# AGENTS.md — 작업 원칙
> 과제에 원래 AGENTS.md가 있으면 그 내용이 우선이고, 이 내용은 그 아래에 덧붙여 쓴다.

## 역할
- 결정은 사람이 한다. 에이전트는 선택지·근거·구현·검증을 맡는다. 요구가 모호하면 추측하지 말고 질문한다.

## 범위
- 범위의 기준은 PLAN.md다. PLAN에 없는 기능·추상화·의존성·레이어는 추가하지 말고 먼저 제안만 한다 (오버엔지니어링 금지).
- 도메인 용어와 판단 규칙은 DOMAIN.md를 따른다. 임의로 재정의하지 않는다.

## 작업 방식
- 한 번에 한 기능. 변경 전에 계획 3줄, 변경 후에 실행·테스트 명령과 그 출력을 보여준다.
- 계산·판정은 결정론적 코드로 처리하고, LLM은 해석·요약·초안에만 쓴다.
- 완료라고 말하기 전에 검증 증거를 제시한다 (`harness/third_party/verification-before-completion`).
- 버그는 원인 조사부터 한다 (`harness/third_party/systematic-debugging`).

## 비용
- 큰 파일은 head·통계로만 확인한다. 파일 전체를 다시 쓰지 말고 최소 diff로 수정한다. 같은 내용을 반복 출력하지 않는다.

## 기록과 정직
- 결정은 DECISIONS.md에 한 줄로 남긴다 (시각 / 결정 / 근거). 커밋은 기능 단위로, 메시지에 의도를 쓴다.
- 문서에는 구현된 것만 쓴다. 부분 구현·미구현은 그대로 표기한다.

## 환경
- 서버는 0.0.0.0에 바인딩하고 실제 포트를 출력한다. git push, 외부 전송, 비밀값 노출은 하지 않는다.

## 스킬 목차 — 해당 상황이면 해당 파일을 먼저 읽고 따른다
| 상황 | 파일 |
|---|---|
| 과제를 처음 받음 | `harness/skills/brief-breakdown/SKILL.md` |
| 실무자 인터뷰 진행 | `harness/skills/discovery/SKILL.md` |
| 실무자 답변을 받음 | `harness/skills/domain-notes/SKILL.md` |
| 제공 데이터·코드 파악 | `harness/skills/data-recon/SKILL.md` |
| 실무자에게 보낼 메시지 작성 | `harness/skills/ask-draft/SKILL.md` |
| 요구 정리와 합의 | `harness/skills/spec-agree/SKILL.md` |
| 구조 결정 | `harness/skills/design-options/SKILL.md` |
| 기능 구현 | `harness/skills/slice-loop/SKILL.md` |
| 기능 검증 | `harness/skills/verify/SKILL.md` |
| 화면·흐름 테스트 | `harness/skills/e2e-check/SKILL.md` |
| 과한 코드·문서 불일치 점검 | `harness/skills/right-size-audit/SKILL.md` |
| 리스크 정리 | `harness/skills/risks/SKILL.md` |
| 세션 전환 / 현업 인수인계 | `harness/skills/handoff/SKILL.md` |
| 제출 전 점검 | `harness/skills/submit-check/SKILL.md` |
| 제출 직전 이해도 점검 | `harness/skills/oral-prep/SKILL.md` |
