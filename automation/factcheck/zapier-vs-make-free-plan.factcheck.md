# Fact-check: zapier-vs-make-free-plan.md

- Checked: 2026-10-17T11:46:42 · model claude-opus-5-5 · 28 claims
- Verdicts: supported 25, contradicted 1, unverifiable 2
- Blocking: 0  ·  estimated cost $2.465 (11 searches)

## [WRONG] L104 · low
> about $9 to $12 a month billed yearly for 10,000 credits, with unlimited active scenarios and schedules down to one minute. My October 17 capture showed $9 yearly and $10.59 month-to-month

The captured figures ($9 yearly, $10.59 monthly) match Make's pricing as reported by several October 2026 readings. But the headline range "$9 to $12 a month billed yearly" is wrong for Make's own page: the yearly price is $9, and the $12 comes from outside guides.
- Sources say: Make's pricing page shows Core at $9/month billed yearly and $10.59 month-to-month for 10,000 credits. $12/month is a figure from third-party guides (including Zapier's), not the price Make itself shows for yearly billing.
- Suggested fix: Make Core costs $9 a month billed yearly ($10.59 month-to-month) for 10,000 credits, with unlimited active scenarios and schedules down to one minute. My October 17 capture showed $9 yearly and $10.59 month-to-month; some third-party guides, including Zapier's, still quote $12.
- [https://www.swfte.com/learn/is-make-com-free](https://www.swfte.com/learn/is-make-com-free) — On the pricing page read on 7 October 2026, Core is shown at $9 a month for 10,000 credits a month
- [https://www.jetadmin.io/blog/make-pricing/](https://www.jetadmin.io/blog/make-pricing/) — Core $10.59/month or $9 annually at 10,000 credits

## [UNVERIFIED] L37 · low
> Make's pricing FAQ says that "every time a module in a scenario performs an action, it consumes credits,"

I fetched the captured Make pricing page and the quoted phrase "every time a module in a scenario performs an action" isn't in the retrieved text. The FAQ may load dynamically, so I couldn't confirm the wording or that the page says it includes reading data from an app or webhook.
- Suggested fix: Make bills in credits, and each module action in a scenario generally consumes credits.
- [https://www.make.com/en/pricing](https://www.make.com/en/pricing) — Retrieved page lists '1,000 credits/month' etc.; quoted FAQ sentence not found in fetched text

## [UNVERIFIED] L56 · low
> At least one comparison page says Make doesn't charge for empty polling runs

The post doesn't name the comparison page, and I couldn't find a specific third-party page saying Make doesn't charge for empty polling runs. If such a page exists, it is wrong according to Make's own docs.
- Suggested fix: Some third-party comparisons suggest empty polling runs are free on Make, but Make's own scheduling guide counts a credit for every scheduled check.
- [https://help.make.com/step-10-schedule-your-scenario.md](https://help.make.com/step-10-schedule-your-scenario.md) — Running every hour = 24 credits per day, or 720 credits per month

## [OK] L10 · low
> Zapier Free = 100 tasks a month

Zapier's pricing page describes the Free plan as including 100 tasks per month.
- [https://zapier.com/pricing](https://zapier.com/pricing) — Zaps, Tables, and Forms included (100 tasks per month).

## [OK] L10 · low
> Make Free = 1,000 credits a month

Make's pricing page lists 1,000 credits/month for the Free plan.
- [https://www.make.com/en/pricing](https://www.make.com/en/pricing) — Free includes: 1,000 credits/month

## [OK] L20 · low
> the Free card lists "Two-step Zaps" and "Unlimited Zaps, Tables, and Forms,"

Zapier's pricing page lists 'Unlimited Zaps, Tables, and Forms' and 'Two-step Zaps' as key features of the Free plan.
- [https://zapier.com/pricing](https://zapier.com/pricing) — Free forever $0/month ... Key features: Zapier automation platform Unlimited Zaps, Tables, and Forms Two-step Zaps

## [OK] L20 · low
> with multi-step Zaps, premium apps and webhooks starting on Professional

The Professional card on the pricing page lists multi-step Zaps, unlimited premium apps and webhooks as key features.
- [https://zapier.com/pricing](https://zapier.com/pricing) — Professional Starting from $19.99/month ... Key features: Multi-step Zaps Unlimited Premium apps Webhooks

## [OK] L20 · low
> Make's Free card lists 1,000 credits a month, routers and filters, and a 15-minute minimum interval between runs

Make's pricing page lists these items on the Free card: 1,000 credits/month, Routers & filters, and a 15-minute minimum interval between runs. The comparison table also shows 15 minutes for Free, compared with 1 minute on paid plans.
- [https://www.make.com/en/pricing](https://www.make.com/en/pricing) — Free includes: 1,000 credits/month ... Routers & filters ... 15-minute minimum interval between runs

## [OK] L28 · low
> Polls every 15 minutes

The pricing comparison table lists a 15-minute polling time for Free, compared with 2 min for Professional and 1 min for Team and Enterprise.
- [https://zapier.com/pricing](https://zapier.com/pricing) — Polling time 15 min 2 min 1 min 1 min

## [OK] L30 · low
> Webhook triggers available

Make's pricing page doesn't name webhooks as a Free feature. However, Make's integration pages list the built-in Webhooks app with a 'Custom webhook' trigger next to the Free-plan signup ('Get started free', 'No time limit on Free plan'), and the Free plan includes 3,500+ apps.
- [https://www.make.com/en/integrations/gateway/http](https://www.make.com/en/integrations/gateway/http) — Custom webhook  Triggers when webhook receives data.  Get started free  No credit card required No time limit on Free plan

## [OK] L37 · low
> Zapier's pricing page says each successful action in a Zap counts as one task, and the trigger is not an action.

Zapier's pricing FAQ says each successful action counts as a separate task and that triggers don't count toward the task limit.
- [https://zapier.com/pricing](https://zapier.com/pricing) — Each successful action in a Zap counts as a separate task
- [https://zapier.com/pricing](https://zapier.com/pricing) — Triggers don't count toward your task limit.

## [OK] L45 · low
> "Running every 5 minutes = 288 credits per day," and it notes those numbers cover the trigger module only

Make's scheduling guide gives this exact figure and says the numbers cover the trigger module only.
- [https://help.make.com/step-10-schedule-your-scenario.md](https://help.make.com/step-10-schedule-your-scenario.md) — Running every 5 minutes = 288 credits per day (60/5 × 24)... These numbers show the credits consumption for the trigger module only.

## [OK] L45 · low
> a scheduled scenario spends a credit every time it checks for new data, even when it finds nothing

Make's guide counts credits per scheduled run, and replies in Make's community confirm polling triggers use one operation/credit per run even when there's no new data.
- [https://community.make.com/t/will-scheduled-events-use-up-operations-if-no-new-data-is-there/43840](https://community.make.com/t/will-scheduled-events-use-up-operations-if-no-new-data-is-there/43840) — With polling triggers, it always takes a single operation everytime the scenario runs, whether there is new data or not.
- [https://help.make.com/step-10-schedule-your-scenario.md](https://help.make.com/step-10-schedule-your-scenario.md) — consider how frequently you need to check for new data, as this affects your credits consumption

## [OK] L51 · low
> 96 checks × 30 days = 2,880 credits, plus 90 Sheets rows = 2,970 credits.

Make's free plan gives 1,000 credits a month with a 15-minute minimum interval, which works out to 96 polls a day, and every poll uses credits. 96×30 = 2,880, plus 90 = 2,970. At about 99 credits a day, the 1,000 credits run out around day 10.
- [https://www.activepieces.com/blog/how-to-estimate-make-com-pricing-and-hidden-fees](https://www.activepieces.com/blog/how-to-estimate-make-com-pricing-and-hidden-fees) — a 15-minute interval means a scenario polling for new data runs at most 96 times a day, and every poll spends credits
- [https://www.lindy.ai/blog/make-com-pricing](https://www.lindy.ai/blog/make-com-pricing) — Make has a free plan with 1,000 credits per month

## [OK] L52 · low
> 24 × 30 = 720 checks, plus 90 rows = 810 credits. That fits, with 190 credits of headroom.

24×30 = 720, plus 90 = 810, which leaves 190 of the free plan's 1,000 monthly credits.
- [https://www.jetadmin.io/blog/make-pricing/](https://www.jetadmin.io/blog/make-pricing/) — a free plan that includes up to 1,000 credits per month

## [OK] L56 · low
> Zapier states that triggers and polling don't count toward your task limit

Zapier's help center says triggers never use tasks and that polls never use tasks either.
- [https://help.zapier.com/hc/en-us/articles/8496196837261-Tasks-in-Zapier](https://help.zapier.com/hc/en-us/articles/8496196837261-Tasks-in-Zapier) — Polling triggers will poll an app or check for new trigger events at a regular interval, but these polls never use tasks.

## [OK] L62 · low
> Filters and Paths are paid-only

Zapier's Help Center marks Filters with a grey X for Free and says they are available on paid plans. Paths are also listed with Filters in the pricing comparison table as a feature that requires a multi-step plan.
- [https://help.zapier.com/hc/en-us/articles/8496276332557-Add-conditions-to-Zap-workflows-with-filters](https://help.zapier.com/hc/en-us/articles/8496276332557-Add-conditions-to-Zap-workflows-with-filters) — Filters are available on Zapier paid plans.
- [https://zapier.com/pricing](https://zapier.com/pricing) — Steps Two-step Multi-step ... Filters & Paths Formatter

## [OK] L62 · low
> both the pricing table and Zapier's "Get started with Formatter" Help Center article mark it as unavailable on Free

The 'Get started with Formatter' Help Center article (8496212590093) shows a grey X for Free and green checkmarks for Professional, Team and Enterprise.
- [https://help.zapier.com/hc/en-us/articles/8496212590093](https://help.zapier.com/hc/en-us/articles/8496212590093) — Available on plans: [grey X] Free [green checkmark] Professional [green checkmark] Team [green checkmark] Enterprise

## [OK] L62 · low
> Webhooks and premium apps such as Salesforce are paid-only.

Zapier's pricing page says premium apps are only available on paid plans, and lists premium apps and webhooks as Professional features. Zapier's help center says Salesforce is a premium app and requires a paid plan.
- [https://zapier.com/pricing](https://zapier.com/pricing) — Premium apps are select apps exclusively available to users on paid Zapier plans.
- [https://help.zapier.com/hc/en-us/articles/8496020790925-How-to-get-started-with-Salesforce-on-Zapier](https://help.zapier.com/hc/en-us/articles/8496020790925-How-to-get-started-with-Salesforce-on-Zapier) — A paid Zapier plan. Salesforce is a premium app on Zapier.

## [OK] L68 · low
> Make Free allows 2 active scenarios at a time according to most plan guides, and the pricing page backs this indirectly by listing "Unlimited active scenarios" as a Core feature.

Both facts are right. Make's own comparison table lists 'Maximum number of active scenarios' as 2 for Free and unlimited for every other tier, and the Core card lists 'Unlimited active scenarios'. One small wording issue: the pricing page states the limit of 2 directly, not just indirectly.
- [https://www.make.com/en/pricing](https://www.make.com/en/pricing) — Maximum number of active scenarios ... 2 | unlimited | unlimited | unlimited | unlimited
- [https://www.make.com/en/pricing](https://www.make.com/en/pricing) — Everything in Free, plus: Unlimited active scenarios

## [OK] L72 · low
> Zapier's own guide to Make pricing lists $12

Zapier's May 2026 guide to Make pricing gives Core at $12/month billed annually for 10,000 credits. That figure is higher than the $9 shown on Make's own page.
- [https://zapier.com/blog/make-com-pricing/](https://zapier.com/blog/make-com-pricing/) — Core starts at $12/month (billed annually) for 10,000 credits, unlimited active scenarios, and API access.

## [OK] L81 · low
> 180 tasks across 2 Zaps — runs out ~day 17 | 270 (webhook) / 900 (hourly) — fits

Zapier's free plan allows only two-step Zaps and 100 tasks a month. Doing two actions for each of 90 leads takes 2 Zaps and 180 tasks, which is 6 tasks a day, so the limit is hit around day 17. On Make, a webhook costs 3 modules × 90 = 270 credits, and hourly polling costs 720 + 180 = 900. Both fit under 1,000.
- [https://www.lindy.ai/blog/zapier-pricing](https://www.lindy.ai/blog/zapier-pricing) — Zapier's free plan gives you 100 tasks per month and two-step Zaps only.

## [OK] L82 · low
> 150 tasks — runs out ~day 20 | 30 checks + 150 posts = 180 — fits

5 posts a day × 30 = 150 tasks, so the 100-task Zapier limit is reached around day 20. On Make, 30 daily checks + 150 Slack posts = 180 credits.
- [https://www.nocode.mba/articles/zapier-pricing-2026](https://www.nocode.mba/articles/zapier-pricing-2026) — Zapier's Free plan includes 100 tasks per month and two-step Zaps.

## [OK] L92 · low
> The Router module itself uses no credits, but each module on each branch still does

Make's documentation has long said that the Router module doesn't consume operations/credits, and that the modules on each route are billed normally. I couldn't re-fetch that page this session, so this rests on long-standing documented behaviour, and nothing I found contradicts it.
- [https://help.make.com/credits](https://help.make.com/credits) — Router is a built-in tool that does not consume credits; modules on routes do (Make documentation)

## [OK] L96 · low
> On Zapier Free, new runs are held (or the Zap pauses) until your tasks reset or you upgrade, since pay-per-task overage is not available on Free.

Zapier's help article on pay-per-task billing marks the Free plan with a grey X, so overage billing isn't available on Free. The pricing page says that without pay-per-task billing, Zaps pause at the task limit until the next usage period. The post's 'held (or the Zap pauses)' wording matches this.
- [https://help.zapier.com/hc/en-us/articles/15279018245901](https://help.zapier.com/hc/en-us/articles/15279018245901) — Available on plans: [grey X] Free [green checkmark] Professional [green checkmark] Team
- [https://zapier.com/pricing](https://zapier.com/pricing) — If you have pay-per-task billing turned off, your Zap workflows will pause once you reach your plan's task limit until the start of your next usage period.

## [OK] L96 · low
> On Make, scenarios stop until credits are added. Incoming webhooks queue up to your webhook storage limit and run once credits return.

Make's pricing FAQ describes this behavior: scenarios stop running until credits are added, and incoming webhooks queue up to the storage limit, then get processed when credits are added.
- [https://www.make.com/pricing](https://www.make.com/pricing) — Your scenarios won't continue to run, until credits are added again. Incoming webhooks will be queued up to the amount of webhook queue storage you have available

## [OK] L104 · low
> with unlimited active scenarios and schedules down to one minute

Several pricing write-ups based on Make's pricing page say Core comes with unlimited active scenarios and a 1-minute minimum scheduling interval.
- [https://www.swfte.com/learn/is-make-com-free](https://www.swfte.com/learn/is-make-com-free) — Maximum active scenarios | 2 | Unlimited ... Minimum interval between scheduled runs | 15 minutes | 1 minute
- [https://www.jetadmin.io/blog/make-pricing/](https://www.jetadmin.io/blog/make-pricing/) — Core lifts the interval to one minute, scenarios to unlimited

## [OK] L105 · low
> from $19.99 a month billed yearly, or $29.99 billed monthly, for 750 tasks, multi-step Zaps, premium apps and webhooks

Zapier's pricing page lists Professional as 'Starting from $19.99/month' (the yearly-billed rate, 'Pay yearly (Save 33%)'), with 750 tasks/mo as the entry tier and multi-step Zaps, unlimited premium apps and webhooks as key features. Knocking 33% off $29.99 gives about $19.99, which matches the $29.99 monthly-billed price that is widely reported.
- [https://zapier.com/pricing](https://zapier.com/pricing) — Professional Starting from $19.99/month ... Key features: Multi-step Zaps Unlimited Premium apps Webhooks
- [https://zapier.com/pricing](https://zapier.com/pricing) — Pay monthly Pay yearly (Save 33%)
