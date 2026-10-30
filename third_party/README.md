# third_party — 공개 스킬 사본

원문을 수정하지 않고 그대로 복사했다. 각 폴더의 LICENSE를 따른다.

| 폴더 | 출처 | 커밋 | 라이선스 | 고른 이유 | 이 하네스에서 쓰는 곳 |
|---|---|---|---|---|---|
| systematic-debugging | [obra/superpowers](https://github.com/obra/superpowers) `skills/systematic-debugging` | `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b` | MIT | 원인 조사 없이 증상만 고치는 반복 수정(토큰 낭비)을 막는다 | slice-loop, verify |
| verification-before-completion | [obra/superpowers](https://github.com/obra/superpowers) `skills/verification-before-completion` | `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b` | MIT | 실행 증거 없이 "완료"라고 말하지 않게 한다. 문서-코드 정직성과 같은 원칙 | verify, submit-check |
| webapp-testing | [anthropics/skills](https://github.com/anthropics/skills) `skills/webapp-testing` | `ca45fc496a3436251f191354091d557da31c15b5` | Apache-2.0 | 서버 기동 보조 스크립트(with_server.py)와 헤드리스 Playwright 스크립트 패턴 | e2e-check L2 |
| frontend-design (선택) | [anthropics/skills](https://github.com/anthropics/skills) `skills/frontend-design` | `ca45fc496a3436251f191354091d557da31c15b5` | Apache-2.0 | UI 문구·구조·접근성 가이드. 화면 완성도 보강용 | 화면 다듬을 때만 |

## 사용 시 주의 (이 하네스 기준)
- **systematic-debugging**: 원본의 `root-cause-tracing.md`만 함께 복사했다. 본문이 참조하는 `defense-in-depth.md`, `condition-based-waiting.md`, `test-driven-development` 스킬은 포함하지 않았다.
- **webapp-testing**: `examples/`의 저장 경로(`/mnt/user-data/outputs`, `/tmp`)는 원본 예시 값이다. 이 하네스에서는 `tests/screenshots/`에 저장한다. 테스트는 스크립트로 작성해 터미널에서 실행하며, 에이전트가 브라우저를 대화형으로 조작하지 않는다.
- **frontend-design**: 원본은 "독창적이고 과감한 미적 방향"을 지향한다. 현업 업무 도구에서는 **명료함·가독성·실무자의 용어**를 우선하고, 문구(writing)·접근성·구조 원칙 위주로 참고한다.
