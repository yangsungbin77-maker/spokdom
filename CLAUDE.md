# CLAUDE.md

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

## 5. No Closing Colons (Korean Output)

**End Korean sentences with a period, not a colon.**

When the user writes in Korean, your output is also Korean:
- Don't end sentences with `:` even if the next line is a list or example.
- LLMs trained on English docs leak the colon habit into Korean. Catch it.
- The test: every Korean sentence terminator should be `.`, `?`, or `!` — not `:`.
- Colons are fine inside code, key-value pairs, or labels. Not as sentence enders.

## 6. File Header Comments in Korean

**First line of every new source file: a one-line Korean comment stating its role.**

When creating a new file:
- TypeScript/JavaScript: `// 사용자 인증 상태를 관리하는 Context Provider`
- Python: `# KIS API 호출을 비동기로 래핑하는 클라이언트`
- SQL: `-- 일별 집계 결과를 저장하는 머티리얼라이즈드 뷰`
- Place it directly under required directives (`'use client'`, `'use server'`, shebang).
- Skip config files (`*.config.ts`, `package.json`, etc.).

Why: agents read files selectively, not whole codebases. A one-line Korean header gives instant context so the next session (human or agent) can navigate without re-reading the entire file.

## 7. Plan + Checklist + Context Notes

**Before any non-trivial task, produce three artifacts. Don't start coding without them.**

- **Plan** — what we're building and why.
- **Checklist** (`checklist.md`) — concrete tasks as checkboxes. Tick as you go.
- **Context Notes** (`context-notes.md`) — decisions made during the work and the reasoning behind them. Append continuously.

If the user gives only a plan and asks you to start coding, stop and ask: "Should I create the checklist and context notes first?" The next session — yours or someone else's — needs the notes to pick up where you left off without re-deriving every decision.

## 8. Run Tests Before Marking Complete

**If you touched code, run the tests before saying "done".**

- `npm test`, `pytest`, `cargo test`, whatever the project uses — run it.
- If tests pass, report results. If they fail, fix and re-run.
- No test setup? At minimum, verify the project builds/compiles.
- Run tests proactively, before the user signals "끝", "완료", "다 됐어" — not after.

This is the step LLMs skip most often. Treat it as non-negotiable.

## 9. Semantic Commits

**Commit when one logical change is complete. Don't wait for the user to ask.**

- The test: "Can I describe this commit in one sentence?" If yes, commit. If no, the changes are still mixed — split them.
- Good: "auth 미들웨어 추가". Bad: "auth 추가하고 UI도 고치고 버그도 수정" (split into 3).
- Don't accumulate 20 unrelated edits and lose the ability to roll back individually.
- Don't commit just to commit — meaningful units only.

Note: For solo prototypes or throwaway scripts, group commits loosely if it slows you down. The point is reversibility, not ceremony.

## 10. Read Errors, Don't Guess

**Read the actual error/log line. Don't pattern-match from memory.**

When something fails:
- Read the full error message and stack trace.
- Check the actual log output, not what you assume it should say.
- Don't apply a "common fix" before confirming the cause.
- If unclear, add a print/log to verify state — then fix.

This is the step LLMs skip most often after "run tests". They guess from error keywords and apply the most-recent-pattern fix. That's how a one-line bug becomes a three-file refactor.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.

---

## 프로젝트 정보 (Spokdom)

- **무엇**: 영어권 AI 툴·SaaS 리뷰/비교 블로그(`spokdom.com`). gameworld7 정적 사이트 틀을 복제해 수익형(어필리에이트) 영어 사이트로 구축.
- **니치 선정 근거**: 비(非)YMYL이라 신규 도메인 진입이 쉽고, SaaS 어필리에이트는 recurring(월 반복) 수수료라 방문자당 누적 수익이 높음. 금융·건강(YMYL)은 신규 도메인 + AI 자동발행에 부적합이라 제외. (deep-research 결론)
- **도메인**: `spokdom.com` — 1년 이상 묵힌 도메인이라 신규 샌드박스 우회, 과거 색인·아카이브 흔적 0(브랜드형 무의미 이름이라 주제 잠금 없음).
- **스택**: Astro(블로그 템플릿) + Markdown 글 + Git + Cloudflare Pages. 본문은 **영어**로 작성.
- **글 작성 방식**: `src/content/blog/`에 Markdown 파일을 추가하고 `git push` 하면 Cloudflare가 자동 배포. (자동 포스팅 파이프라인의 핵심 — `automation/PUBLISH.md` 참고)
- **수익 모델**: SaaS 어필리에이트(가능하면 recurring) + 추후 AdSense 승인 시 `consts.ts`의 `ADSENSE_CLIENT` 설정. 글 절반은 구매의도 키워드(alternatives·vs·pricing·best-for)로 채운다.
- **콘텐츠 언어 주의**: 채팅은 한국어(규칙 5 콜론 금지 적용), 그러나 **블로그 글·제목·설명은 영어**. 규칙 6(파일 헤더 한국어 주석)은 코드 파일에만 적용, 블로그 .md 본문은 영어.
- **자매 사이트**: gameworld7.com(게임)·sportskingdom24.com(스포츠)·click-gotraveling(여행). 같은 자동발행 틀을 공유.

### 자주 쓰는 명령

```powershell
# PATH에 node가 안 잡히면 먼저 실행
$env:Path = "C:\Program Files\nodejs;" + $env:Path

npm run dev      # 로컬 개발 서버 (http://localhost:4321)
npm run build    # 정적 빌드 (dist/ 생성, 배포 전 검증)
npm run preview  # 빌드 결과 미리보기
```

### 글 frontmatter 형식 (영어 본문)

```markdown
---
title: 'Keyword-first English title'
description: 'Keyword-rich 120–155 char summary (shows in search results)'
pubDate: 'Jun 18 2026'
---

Body in English (Markdown)
```

`heroImage`, `updatedDate`는 선택. 이미지 없이도 정상 작동.

### 주의

- 경로에 한글·공백이 있으면(`클로드 코드`) `npm create`/`npm install`이 깨질 수 있어, 프로젝트는 영문 경로(`C:\Users\use\spokdom`)에 둔다.
- 새 글 추가 후에는 `npm run build`로 빌드가 깨지지 않는지 먼저 확인한 뒤 push 한다(규칙 8).
- 블로그 글 본문은 **영어**로 쓴다(영어권 시장). 채팅 응답만 한국어.
