<!-- spokdom 자기갱신 운영 플레이북 — 에이전트가 글을 발행할 때마다 읽고, 새 교훈이 생기면 스스로 갱신한다. -->

# AGENT.md — Spokdom 운영 에이전트 플레이북

```
version:     v1.0
updated_at:  2026-06-24
role:        spokdom.com(영어 AI툴·SaaS 리뷰) 글 작성·발행을 자동 수행하는 에이전트의 운영 매뉴얼
```

## 0. 이 파일이 작동하는 방식 (가장 중요)

- 글 작업을 **시작하기 전에** 이 파일 전체(특히 §3 함정 변경이력)를 먼저 읽는다.
- 글을 **발행한 뒤에**, 이번 작업에서 새로 배운 함정·개선점·바뀐 사실이 있으면
  §3 변경이력에 `YYYY-MM-DD` 항목으로 **추가**하고, 맨 위 `updated_at`(필요시 `version`)을 갱신한다.
- 새로 배운 게 없으면 **건드리지 않는다**(의미 없는 갱신 금지).
- 한 항목은 "무엇을 겪었나 → 그래서 다음엔 어떻게" 한 줄로. 변명·장황함 금지.
- 절차 자체(SERP·키워드·분량 규칙)는 `PUBLISH.md`가 정본(正本)이다. 이 파일은 그 위에서
  **현장 교훈**을 누적하는 곳이다. 중복 서술하지 말고 함정만 적는다.

## 1. 작업 절차 (요약 — 정본은 PUBLISH.md)

1. `node automation/prepare.mjs`로 배정(또는 사용자 지정 키워드) → topic 확정
2. SERP 상위 10개 중 5개+ 직접 열어 분석(필수) + 가격·사실 팩트체크
3. `src/content/blog/<slug>.md` 작성 (비교표·콜아웃·FAQ 4개+·내부1·외부1·이미지2)
4. 증거 파일 `automation/research/<slug>.json` 기록
5. `node automation/finalize.mjs <slug>` → 빌드검증·커밋·푸시·Cloudflare 배포 (라이브 즉시 반영)

## 2. 발행 게이트 셀프체크 (finalize 돌리기 전)

- [ ] `assignment.json`이 **이번 글** 값인가 (외부링크·내부링크·imageFile·heroImage·topic)
- [ ] 본문 공백제외 5,000자+ / `##` 6개+ / FAQ 4개+
- [ ] 내부링크 = 같은 주제 클러스터의 글 / 외부링크 = 권위 출처(.edu·공식)
- [ ] 이미지 2장 모두 `src/assets/posts/`에 키워드 파일명 (pool/ 아님)
- [ ] 헤르메스 점수는 **별도 심판 에이전트**로 받는다 (research.json에 자가기입 금지)

## 3. 함정 변경이력 (auto-updated changelog)

### 2026-06-24
- **assignment.json 잔상 트랩**: `assignment.json`은 직전 글 값이 그대로 남아있다.
  finalize는 이 파일 기준으로 외부/내부링크·heroImage 일치를 검사하므로, 새 글마다
  **작성 직후 assignment.json을 이번 글에 맞게 먼저 갱신**해야 막히지 않는다.
- **finalize는 한 방에 라이브**: build+commit+push+`wrangler pages deploy`까지 자동 실행 →
  되돌리기 어려운 공개 작업. 자동발행 루틴이 아닌 수동 요청이면 **발행 전 사용자 확인**.
- **Higgsfield 크레딧 폴백**: recraft-v4-1 2k = 10cr. 잔액 부족 시 **1k = 1.25cr/장**으로 폴백
  가능(2장=2.5cr). 화질 차이 미미. 시네마틱+"No text" 프롬프트 유지.
- **ads.txt "찾을 수 없음" = 정상**: 파일이 라이브 200·내용 정확이면 손대지 말 것.
  AdSense 크롤 지연(며칠~몇 주)이라 재배포는 무의미. 진짜 관문은 사이트 "준비 중" 승인.
- **클러스터 내부링크 원칙**: 같은 의도끼리 연결(예: graduate-students ↔ review-paper).
  prepare가 엉뚱한 내부링크를 배정하면 더 관련 있는 기존 글로 교체.
- **심판 루프**: hermes_score는 작가(나)가 적으면 무효. API 과부하(529) 시 재시도하되,
  통과 전 자가점수로 90 채웠다고 보고하지 말 것.

<!-- 다음 발행 때 새 교훈이 생기면 위에 날짜 항목을 추가하고 updated_at을 갱신한다. -->
