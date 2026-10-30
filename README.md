# ai-native-harness

AI 코딩 에이전트(Codex CLI 등)와 함께 **3시간 안팎의 실무형 과제**를 수행하기 위한 가벼운 작업 하네스.
현업 담당자와 대화하며 문제를 정의하고, 요구에 맞는 크기로 만들고, 검증하고, 근거를 남기는 흐름을 스킬로 정리했다.

## 원칙
1. 결정은 사람이, 선택지·구현·검증은 에이전트가
2. 요구에 딱 맞게 — 범위 밖 기능·추상화는 제안만
3. 실무자의 판단 기준과 노하우를 끌어내 결과물에 녹인다
4. 작게 위임하고, 실행 증거로 검증하고, 기능 단위로 커밋한다
5. 모든 판단에 "왜"를 남긴다 (DECISIONS / DOMAIN / RISKS)
6. 좋은 공개 스킬은 가져다 쓴다 (`third_party/`)

## 빠른 시작
```bash
git clone https://github.com/<계정>/ai-native-harness harness
cp harness/AGENTS.md .            # 과제에 AGENTS.md가 이미 있으면: cat harness/AGENTS.md >> AGENTS.md
# (선택) Codex 스킬 디렉터리를 쓸 수 있는 환경이면: mkdir -p ~/.codex/skills && cp -r harness/skills/* ~/.codex/skills/
```
- 템플릿은 필요할 때 `harness/templates/`에서 루트로 복사한다.
- 스킬 기능이 없는 환경에서도 AGENTS.md의 **스킬 목차**를 통해 에이전트가 해당 SKILL.md를 읽고 따른다.

## 흐름과 스킬
| 단계 | 스킬 | 산출물 |
|---|---|---|
| 이해 | ★brief-breakdown → ★discovery → ★domain-notes(답변마다) → data-recon | BRIEF, INTERVIEW, DOMAIN, EXPLORE |
| 소통 (수시) | ★ask-draft | 실무자 메시지 초안 |
| 합의·설계 | ★spec-agree → design-options | PLAN, DECISIONS |
| 구현·검증 | ★slice-loop → verify → ★e2e-check → right-size-audit | 커밋, 테스트 로그, E2E_RESULT |
| 마무리 | risks → handoff(세션/현업) → submit-check → ★oral-prep | RISKS, HANDOFF, USER_GUIDE |

★ = 시간이 부족할 때 꼭 쓸 8개

## 시간 배분 예 (180분 기준)
| 분 | 단계 |
|---|---|
| 0~10 | 환경 세팅, 원본 첫 커밋, 하네스 clone |
| 10~35 | brief-breakdown, discovery, domain-notes (병렬: data-recon) |
| 35~45 | spec-agree, 실무자 확인 |
| 45~120 | design-options → 최소 E2E → slice-loop (90분 무렵 실무자 중간 확인) |
| 120~150 | verify, e2e-check, right-size-audit |
| 150~170 | risks, handoff(현업), submit-check, oral-prep |

## 구성
```
AGENTS.md            항상 적용되는 작업 원칙 + 스킬 목차
skills/<name>/       직접 작성한 스킬 15개 (SKILL.md, e2e-check는 테스트 템플릿 포함)
templates/           BRIEF, INTERVIEW, DOMAIN, PLAN, DECISIONS, RISKS, HANDOFF, USER_GUIDE, E2E_RESULT
third_party/         공개 스킬 사본 (출처·커밋·라이선스는 third_party/README.md)
```

## 라이선스
- `skills/`, `templates/`, `AGENTS.md`, 이 README: MIT
- `third_party/`: 각 폴더의 원본 라이선스 (MIT, Apache-2.0)
