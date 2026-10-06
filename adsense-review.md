<!-- spokdom.com 애드센스 승인 준비 점검 결과와 운영자 후속 조치를 정리한 내부 문서(사이트에 배포되지 않음) -->

# spokdom.com 애드센스 승인 준비 점검 (2026-10-06)

이 파일은 저장소 루트에 있어 `public/`에 포함되지 않으므로 사이트에 배포되지 않는다.

## 1. 진단 요약

- **사이트 성격 확인.** 작업 지시는 "스포츠 블로그일 것"으로 가정했지만, spokdom.com은 **영어권 AI 툴·SaaS 리뷰/비교 블로그**다(CLAUDE.md, consts.ts, 글 17편 모두 해당). 그래서 베팅·토토·불법 중계 점검은 해당 사항이 없었고, 실제 grep 결과도 0건이다.
- **sportskingdom24와 중복 여부.** 제목·주제·언어(한국어 스포츠 vs 영어 SaaS)가 전혀 달라 중복 콘텐츠 위험은 없다.
- **애드센스 미연결 상태.** `src/consts.ts`의 `ADSENSE_CLIENT`가 빈 문자열이라 애드센스 스크립트가 어떤 페이지에도 출력되지 않고, `public/ads.txt`도 없다(초기 구축 커밋 29d33b2에서 gameworld의 ads.txt를 의도적으로 제거). 즉 이 도메인이 애드센스에 연결되었는지 저장소만으로는 확인할 수 없다.
- **소프트 404.** `src/pages/404.astro`가 없었다. 이 사이트는 `wrangler pages deploy`(Cloudflare **Pages**)로 배포되는데, Pages는 최상위 404.html이 없으면 SPA로 간주해 없는 주소에도 홈을 200으로 돌려준다(Cloudflare 문서 기준 기억에 의존, 라이브 확인 불가). 404 페이지를 추가해 해결했다.
- **개인정보처리방침이 실제와 불일치.** 모든 페이지에 GA4(G-VD0J9275NE)와 Google Fonts가 로드되는데 방침에는 GA4·Google Fonts·호스팅이 빠져 있었고, 실제로는 출력되지 않는 애드센스를 "표시할 수 있다"고만 적고 있었다. 파트너 사이트 링크, EEA 동의 안내, 운영자·연락처, 수정일도 없었다.
- **AI 자동발행 미고지 + 저자명 불일치.** `automation/`의 자동발행 파이프라인(prepare → AI 작성 → finalize가 빌드·커밋·배포까지 자동)이 글을 쓰는데 About·Author 어디에도 AI 사용 고지가 없었다. 구조화 데이터의 저자는 `Dom`(커밋 44c1b33에서 추가)인데 Author·푸터의 실제 운영자는 Sungbin이었다.
- **검증되지 않은 직접 테스트 주장.** 홈에 "Hands-on testing", "Updated monthly", "How we test", 사이트 설명에 "hands-on reviews"가 있었다. 글 본문은 대부분 "공개 가격·기능 데이터로 비교했다"고 정직하게 밝히고 있어 사이트 문구와 어긋났고, 마지막 발행이 2026-08-21이라 "매달 갱신"도 사실이 아니다.
- **양호한 항목.** robots.txt는 전체 허용 + 사이트맵 지정, sitemap-index.xml 생성됨, 글 17편 모두 1,473~2,257단어로 얇은 글 없음, 더미 텍스트·빈 카테고리 없음, 내부 링크 깨짐 0건, 이미지 전부 AI 생성(메타데이터에 Higgsfield `hf-job-id`·Recraft 서명, 또는 fal flux 생성 스크립트) 또는 자체 제작 도식이며 로고·스크린샷·선수 사진 없음.

## 2. 조건별 상태 (A–D)

| 조건 | 내용 | 작업 전 | 작업 후 |
|---|---|---|---|
| A. 사이트 연결 | 애드센스 코드 또는 ads.txt로 소유 확인 | 코드 없음, ads.txt 없음 | **변경 없음(운영자 결정 필요)** |
| B. 정책 페이지 | 개인정보처리방침·소개·연락처 | 방침이 실제 서비스와 불일치, AI 고지 없음 | 방침 재작성, About·Author에 AI 고지 |
| C. 콘텐츠 품질·신뢰 | 얇은 글·더미·직접경험 과장·저작권 | 사이트 문구에 테스트 과장, 저자명 불일치 | 사이트 문구 정정, 저자 Sungbin 통일. 글 본문 표현은 운영자 검토 대상으로 남김 |
| D. 기술 | 404, robots, sitemap, 깨진 링크 | 404 없음(소프트 404) | 404.html(noindex, 광고 제외) 추가 |

## 3. 커밋 (브랜치 `claude/google-adsense-approval-dfvgr8`)

| 해시 | 내용 |
|---|---|
| 6195d3f | 404 페이지 추가(noindex·광고 제외) 및 BaseHead noAds·noindex 옵션 추가 |
| dc771d7 | 개인정보처리방침을 실제 로드되는 서비스 기준으로 갱신 |
| 160b95a | 소개·운영자 페이지에 AI 활용 고지 추가 및 저자 표기를 Sungbin으로 통일 |
| bfd9b3b | 홈·푸터·목록 문구에서 검증되지 않은 직접 테스트 주장 제거 |
| (이 파일) | 애드센스 점검 보고서 추가 |

## 4. 검증 결과

| 항목 | 방법 | 결과 |
|---|---|---|
| `npm ci` + `npm run build` | 로컬 실행 | PASS (24페이지) |
| dist/404.html 생성, noindex, canonical 없음 | dist 확인 | PASS |
| 404에 애드센스 스크립트 없음 | `noAds` + 현재 ADSENSE_CLIENT 비어 있음 | PASS |
| 404가 사이트맵에 없음 | sitemap-0.xml grep | PASS |
| 내부 링크(루트 상대 href/src) | dist 전체 스캔 661개 | PASS (깨짐 0) |
| robots.txt 크롤러 허용 + Sitemap 지정 | 파일 확인 | PASS |
| 개인정보처리방침에 partner-sites 링크 | dist/privacy 확인 | PASS |
| 외부 로드 서비스 = GA4·Google Fonts만 | dist 전체 src/href 호스트 집계 | PASS (iframe·YouTube 없음) |
| 이미지 EXIF 저작권 표기 | Python PIL | PASS (Copyright/Artist 태그 없음, AI 생성 메타데이터 확인) |
| 라이브 사이트 404 응답 코드 | 외부망 차단 | UNKNOWN |
| 라이브 ads.txt / 애드센스 사이트 상태 | 외부망 차단 | UNKNOWN |
| Cloudflare 실제 배포 형태(Pages인지) | finalize.mjs의 `wrangler pages deploy`로 추정 | UNKNOWN(대시보드 확인 필요) |

참고로 `wrangler.jsonc`는 Pages 형식(`pages_build_output_dir`)이라, 자매 사이트처럼 Workers 정적 자산용 `assets.not_found_handling: "404-page"`를 넣지 않았다. Pages는 dist/404.html만 있으면 404로 응답한다. 만약 실제로 Workers로 배포 중이라면 그 설정을 추가해야 한다.

## 5. 운영자 조치 (직접 해야 할 일)

1. **애드센스 연결 여부 결정.** 자매 사이트의 게시자 ID는 `pub-8312549013849190`이지만, spokdom.com이 그 계정에 사이트로 추가되었는지는 확인되지 않았다. 애드센스 대시보드 > 사이트에서 spokdom.com을 추가한 뒤에만 아래를 진행한다.
   - `src/consts.ts`의 `ADSENSE_CLIENT`에 `'ca-pub-8312549013849190'` 입력
   - `public/ads.txt`에 `google.com, pub-8312549013849190, DIRECT, f08c47fec0942fa0` 한 줄 추가
   - 이렇게 하면 개인정보처리방침의 애드센스 문구가 자동으로 "코드를 로드한다"로 바뀐다.
2. **배포.** 이 브랜치는 푸시만 했고 배포하지 않았다. main에 병합한 뒤 `npm run build` → `npx wrangler pages deploy dist --project-name=spokdom --branch=main`으로 배포하고, 없는 주소(예: `/zzz-test`)가 404를 돌려주는지 확인한다.
3. **AI 고지 문구 확인.** About·Author에 넣은 "AI로 조사·초안 작성, 모든 글을 발행 전에 손으로 검토하지는 않음" 문구가 실제 운영과 맞는지 확인하고, 사람이 검토한다면 그에 맞게 고친다.
4. **글 본문의 직접경험 표현 검토(아래 6절).**
5. **EEA·영국·스위스 동의 관리(CMP).** GA4가 동의 없이 로드되고, 애드센스를 켜면 이 지역에 대해 Google 인증 CMP가 필요하다. 애드센스의 "개인정보 보호 및 메시지"에서 설정할지 결정한다. 설정 전까지 방침에는 약속 없이 "아직 없다"고만 적었다.
6. **제휴 링크 고지.** About·Author는 "Some links are affiliate links"라고 단정하지만 현재 글에서 제휴 링크(ref=, via= 등)는 발견되지 않았다. 제휴 승인 전이라면 About 문구를 "may be"로 낮출지 결정한다(방침은 "may be"로 작성).
7. **발행 공백.** 마지막 글이 2026-08-21이다. "이틀에 한 번" 자동발행 루틴이 멈춘 것으로 보이는데, 예약 작업은 건드리지 않았다.
8. **자잘한 정리(선택).** `public/llms.txt`의 글 목록이 8편에서 멈춤, `package.json`의 name이 `gameworld7`, `automation/AGENT.md`의 "ads.txt 찾을 수 없음 = 정상" 메모는 이 사이트에 ads.txt가 없으므로 해당되지 않음.

## 6. 직접경험(1인칭) 표현 — 사람 검토 필요

모두 자동발행 커밋에서 들어간 표현이며, 운영자가 실제로 써 봤는지 저장소로는 확인할 수 없어 본문은 수정하지 않았다.

| 파일 | 위치 | 표현 | 들어간 커밋 | 권고 |
|---|---|---|---|---|
| src/content/blog/best-notion-alternatives-small-teams.md | 2행 title | "(2026, Tested)" | 5d39d48 | 실제 테스트가 없으면 "Tested" 삭제 |
| src/content/blog/free-zapier-alternatives-for-automation.md | 2행 title | "(2026, Tested)" | 356fe4f | 위와 같음 |
| src/content/blog/best-ai-tools-for-solo-founders.md | 14행 | "plus hands-on familiarity with the mainstream options" | 9eb7210 | 써 본 도구가 없으면 문구 삭제 |
| src/content/blog/best-canva-alternatives.md | 10행 | 같은 문구 | 840f549 | 위와 같음 |
| src/content/blog/best-ai-tools-for-data-analysis.md | 12행 | 같은 문구 | 5f363aa | 위와 같음 |
| src/content/blog/best-chatgpt-alternatives.md | 10행 | 같은 문구 | 894603e | 위와 같음 |
| src/content/blog/free-loom-alternatives.md | 10행 | 같은 문구 | d8fbbaf | 위와 같음 |
| src/content/blog/notion-vs-obsidian-note-taking.md | 10행 | "I opened the current top-ranking articles" | 50318b9 | 파이프라인이 실제로 SERP를 연 것이라 사실에 가깝지만 "I"의 주체 확인 |

파이프라인 측 원인도 있다. `automation/PUBLISH.md` 133행이 "First-hand experience & concrete scenarios"를 10x 요소로 요구하고, `_context/03_사이트_소개.md`·`06_팩트체크_품질기준.md`가 "hands-on familiarity"를 안전한 1인칭으로 규정한다. 실제 사용 경험이 없으면 이 지시를 "구체적 시나리오"로 한정하도록 고치는 것을 권한다.

## 7. 페이지별 사람 검토 체크리스트

- [ ] `/` 홈 — 바뀐 신뢰 문구("Prices checked on official pages", "AI-assisted, disclosed")가 사실인지
- [ ] `/about/` — "How articles are made" 문단이 실제 운영과 맞는지, 제휴 링크 문구
- [ ] `/author/` — "How AI is used here" 문단
- [ ] `/privacy/` — 나열한 서비스(GA4, Google Fonts, Cloudflare)가 전부인지, 애드센스 연결 후 문구 자동 전환 확인
- [ ] `/contact/` — 이메일 주소 확인(변경 없음)
- [ ] 404 — 배포 후 없는 주소에서 HTTP 404와 안내 화면 확인
- [ ] 6절 표의 글 8편 — 직접경험 표현 유지·삭제 결정
- [ ] 각 글의 가격 표기 시점(June~August 2026)이 오래되었으면 갱신 여부 결정
