# Fact-check: zapier-pricing-how-many-tasks.md

- Checked: 2026-10-14T09:56:38 · model claude-opus-5-5 · 29 claims
- Verdicts: supported 29
- Blocking: 0  ·  estimated cost $1.985 (12 searches)

## [OK] L16 · low
> Zapier's pricing FAQ is explicit: "Each successful action in a Zap counts as a separate task."

The FAQ on Zapier's pricing page contains this sentence word for word.
- [https://zapier.com/pricing](https://zapier.com/pricing) — When Zapier performs an action successfully, it counts as a task. Each successful action in a Zap counts as a separate task.

## [OK] L24 · low
> defines it as "any successful action that runs in Zapier,"

The Help Center article with that title defines a task with this exact wording.
- [https://help.zapier.com/hc/en-us/articles/8496196837261-How-is-task-usage-measured-in-Zapier](https://help.zapier.com/hc/en-us/articles/8496196837261-How-is-task-usage-measured-in-Zapier) — A task is any successful action that runs in Zapier. Only successful actions count toward your task usage.

## [OK] L28 · low
> **Failed actions are free.** If an action errors or halts, it does not count against your limit.

The Help Center lists action steps that error or halt among the things that do not count as tasks.
- [https://help.zapier.com/hc/en-us/articles/8496196837261-How-is-task-usage-measured-in-Zapier](https://help.zapier.com/hc/en-us/articles/8496196837261-How-is-task-usage-measured-in-Zapier) — the following do not count as tasks: ... All action steps that error or halt.

## [OK] L29 · low
> AI by Zapier steps vary by model tier, Code by Zapier can use extra tasks if you extend runtime

Zapier's help article on task usage says AI by Zapier task usage depends on the model tier you pick. It also says Code by Zapier uses 1 task per run at standard runtime and can use more if you extend the runtime.
- [https://help.zapier.com/hc/en-us/articles/8496196837261-How-is-task-usage-measured-in-Zapier](https://help.zapier.com/hc/en-us/articles/8496196837261-How-is-task-usage-measured-in-Zapier) — In AI by Zapier, task usage depends on the model tier you select.
- [https://help.zapier.com/hc/en-us/articles/8496196837261-How-is-task-usage-measured-in-Zapier](https://help.zapier.com/hc/en-us/articles/8496196837261-How-is-task-usage-measured-in-Zapier) — steps use 1 task per run with standard runtime, and can use more tasks if you extend the runtime

## [OK] L29 · low
> one Zapier MCP tool call uses two tasks

Zapier's help article says each successful Zapier MCP tool call counts as 2 tasks. One small detail: tool calls that fail don't count toward task usage.
- [https://help.zapier.com/hc/en-us/articles/8496196837261-How-is-task-usage-measured-in-Zapier](https://help.zapier.com/hc/en-us/articles/8496196837261-How-is-task-usage-measured-in-Zapier) — In Zapier MCP, each successful tool call counts as 2 tasks. Failed tool calls do not count toward your task usage.

## [OK] L30 · low
> Replaying a whole Zap run re-bills the steps that had already succeeded.

The Help Center says previously successful steps count as tasks again when you replay an entire Zap run.
- [https://help.zapier.com/hc/en-us/articles/8496196837261-How-is-task-usage-measured-in-Zapier](https://help.zapier.com/hc/en-us/articles/8496196837261-How-is-task-usage-measured-in-Zapier) — Any previously successful steps that run again when you replay an entire Zap run.

## [OK] L32 · low
> Zapier's FAQ says it "never charges you a task to check for new data,"

The pricing FAQ uses this exact wording, and the Help Center confirms that polls never use tasks.
- [https://zapier.com/pricing](https://zapier.com/pricing) — Zapier never charges you a task to check for new data—only when a Zap successfully completes an action for you.

## [OK] L36 · low
> the following steps do not count as a task: Zapier Tables, Zapier Forms, Filter by Zapier, Formatter by Zapier, Path by Zapier, and Delay, Looping, Sub-Zap, Digest, Zapier Manager and Storage.

Zapier's pricing page FAQ currently lists exactly these built-in tools as steps that don't count as a task: Tables, Forms, Filter, Formatter, Paths, Delay, Looping, Sub-Zap, Digest, Zapier Manager and Storage.
- [https://zapier.com/pricing](https://zapier.com/pricing) — The following steps do not count as a task: Zapier Tables, Zapier Forms, Filter by Zapier, Formatter by Zapier, Path by Zapier, Delay, Looping, Sub-Zap, Digest, Zapier Manager, Storage

## [OK] L61 · low
> So 300 runs produce only 200 × 2 = 400 tasks.

Zapier's help center says triggers, Filter steps, and steps skipped by a filter don't count as tasks, so only the 200 runs that pass the filter, with 2 billed actions each, count: 200 × 2 = 400 tasks. The ratio also checks out: 2,130 ÷ 820 ≈ 2.60. The figures for the other two workflows come from the post's own hypothetical example and are consistent with these totals.
- [https://help.zapier.com/hc/en-us/articles/8496196837261-How-is-task-usage-measured-in-Zapier](https://help.zapier.com/hc/en-us/articles/8496196837261-How-is-task-usage-measured-in-Zapier) — In Zap workflows, the following do not count as tasks: All trigger steps. Any Filter or Paths step.
- [https://help.zapier.com/hc/en-us/articles/8496196837261-How-is-task-usage-measured-in-Zapier](https://help.zapier.com/hc/en-us/articles/8496196837261-How-is-task-usage-measured-in-Zapier) — All steps that do not run, either because of a previous filter or pat[h]

## [OK] L65 · low
> the 5,000 tier, which lists at $89 a month billed annually

Third-party pricing breakdowns list Professional at 5,000 tasks for $89/month billed yearly. Zapier's own page puts tier prices behind a slider, so I couldn't read them directly. A few blogs give rough figures that disagree, but those are ballpark numbers.
- [https://theexpertranking.com/tools/zapier/pricing/](https://theexpertranking.com/tools/zapier/pricing/) — 5,000 ($89 / $133.50), 10,000 ($129 / $193.50)

## [OK] L65 · low
> fits the 1,500 tier at $39 a month

Several sources agree the 1,500-task tier costs $39 billed annually or $58.50 billed monthly.
- [https://www.lindy.ai/blog/zapier-pricing](https://www.lindy.ai/blog/zapier-pricing) — 1,500 tasks/month | $58.50/month | $39/month
- [https://latenode.com/blog/zapier-pricing](https://latenode.com/blog/zapier-pricing) — 1,500 | $39 | $468

## [OK] L78 · low
> Zapier's pricing page lists Free at 100 tasks a month

Zapier's pricing page shows the Free plan at $0/month with 100 tasks per month.
- [https://zapier.com/pricing](https://zapier.com/pricing) — Zaps, Tables, and Forms included (100 tasks per month).

## [OK] L78 · low
> Professional starting at $19.99 a month billed annually ($29.99 monthly) for 750 tasks

Zapier's pricing page says Professional starts at $19.99/month and has a 750-task tier. Lindy confirms it's $29.99 on monthly billing.
- [https://zapier.com/pricing](https://zapier.com/pricing) — Professional Starting from $19.99/month
- [https://www.lindy.ai/blog/zapier-pricing](https://www.lindy.ai/blog/zapier-pricing) — 750 tasks/month | $29.99/month | $19.99/month

## [OK] L78 · low
> Team starting at $69 a month billed annually ($103.50 monthly) for 2,000 tasks

Zapier's official pricing page lists Team as "Starting from $69/month" on annual billing. Lindy's 2026 pricing guide agrees with the rest of the claim: $103.50/month when billed monthly, with 2,000 tasks.
- [https://zapier.com/pricing](https://zapier.com/pricing) — Team Starting from $69/month ... 25 users Shared Zaps and folders Shared app connections
- [https://www.lindy.ai/blog/zapier-pricing](https://www.lindy.ai/blog/zapier-pricing) — The Team plan starts at $69/month billed annually, or $103.50/month on monthly billing, with 2,000 tasks

## [OK] L78 · low
> Enterprise is quoted by sales.

Enterprise appears on the pricing page as 'Contact for pricing' with a Contact sales button.
- [https://zapier.com/pricing](https://zapier.com/pricing) — EnterpriseContact for pricing ... Contact sales

## [OK] L84 · low
> | 2,000 | $49 | $73.50 | $69 |

Several sources agree the 2,000-task tier costs $49 billed annually or $73.50 billed monthly, and Team starts at $69.
- [https://tinycommand.com/blogs/zapier-pricing-explained](https://tinycommand.com/blogs/zapier-pricing-explained) — the popular 2,000-task tier is $49 a month billed annually or $73.50 billed monthly

## [OK] L85 · low
> | 5,000 | $89 | $133.50 | $119 |

Sources list Professional at 5,000 tasks for $133.50 on monthly billing and Team at 5,000 tasks for $119 billed yearly. Lindy's 5,000-task tier also comes to $119 billed annually.
- [https://theexpertranking.com/tools/zapier/pricing/](https://theexpertranking.com/tools/zapier/pricing/) — Team - More tasks: 5,000 ($119 yearly
- [https://www.lindy.ai/blog/zapier-pricing](https://www.lindy.ai/blog/zapier-pricing) — Task tier: 5,000 tasks/month. Monthly billing: $178.50/month. Annual billing: $119/month.

## [OK] L86 · low
> | 10,000 | $129 | $193.50 | $169 |

Several current pricing breakdowns list the 10,000-task tier at $129 (Professional, yearly), $193.50 (Professional, monthly) and $169 (Team, yearly). Zapier's own page lists a 10K tier and Team starting at $69, which fits.
- [https://theexpertranking.com/tools/zapier/pricing/](https://theexpertranking.com/tools/zapier/pricing/) — 10,000 ($129 / $193.50) ... [Team] 10,000 ($169 / $253.50)
- [https://sodelia.ca/guides/zapier-integration-cost](https://sodelia.ca/guides/zapier-integration-cost) — 10,000 | $129 (CAD $184) | $193.50 (CAD $276) | $169 (CAD $241)
- [https://www.lindy.ai/blog/zapier-pricing](https://www.lindy.ai/blog/zapier-pricing) — the 10,000-task tier runs $253.50/month ($169/month annually)

## [OK] L92 · low
> roughly 2.7 cents at 750 tasks, 2.5 cents at 2,000 and 1.3 cents at 10,000

Using yearly Professional prices of $19.99 for 750 tasks, $49 for 2,000 and $129 for 10,000, the cost per task comes to about 2.67¢, 2.45¢ and 1.29¢. The post rounds these to 2.7¢, 2.5¢ and 1.3¢, which is correct.
- [https://theexpertranking.com/tools/zapier/pricing/](https://theexpertranking.com/tools/zapier/pricing/) — Professional starts at $19.99/month billed yearly for 750 tasks ... 2,000 ($49 / $73.50) ... 10,000 ($129 / $193.50)
- [https://www.saasswitcher.com/blog/zapier-pricing](https://www.saasswitcher.com/blog/zapier-pricing) — 10,000 | $129 | $193.50 | $169 | $253.50 | $0.0129

## [OK] L92 · low
> Team mainly adds collaboration (25 users, shared Zaps and shared app connections) and a 1-minute polling time versus 2 minutes on Professional

Zapier's official pricing page shows that Team includes 25 users, shared Zaps and folders, and shared app connections. Its comparison table lists polling times of 2 minutes on Professional and 1 minute on Team.
- [https://zapier.com/pricing](https://zapier.com/pricing) — Key features: 25 users Shared Zaps and folders Shared app connections SAML SSO Priority support
- [https://zapier.com/pricing](https://zapier.com/pricing) — Polling time 15 min 2 min 1 min 1 min (Free / Professional / Team / Enterprise)

## [OK] L96 · low
> bills the extra tasks "at a higher per-task rate than your base subscription tasks," according to the pricing FAQ. With it turned off, your Zaps pause until the next usage period.

The Zapier pricing FAQ says pay-per-task is charged at a higher per-task rate than base subscription tasks. It also says that with pay-per-task off, Zaps pause until the start of the next usage period.
- [https://zapier.com/pricing](https://zapier.com/pricing) — Pay-per-task billing is charged at a higher per-task rate than your base subscription tasks.
- [https://zapier.com/pricing](https://zapier.com/pricing) — If you have pay-per-task billing turned off, your Zap workflows will pause once you reach your plan's task limit until the start of your next usage period.

## [OK] L98 · low
> says the maximum "is set at 3 times your plan's task limit."

The Help Center article (updated August 15, 2026) uses this exact wording about the 3x cap.
- [https://help.zapier.com/hc/en-us/articles/15279018245901](https://help.zapier.com/hc/en-us/articles/15279018245901) — This is set at 3 times your plan's task limit, which includes your plan allocation and optional pay-per-task usage.

## [OK] L98 · low
> 750 plan tasks plus up to 1,500 pay-per-task tasks, for 2,250 in total

The Help Center article gives this exact Professional 750 example.
- [https://help.zapier.com/hc/en-us/articles/15279018245901](https://help.zapier.com/hc/en-us/articles/15279018245901) — 750 tasks (normal task limit) + 1500 tasks (pay-per-task limit) = 2250 tasks (maximum task limit)

## [OK] L100 · low
> Zapier's own blog puts the overage at 1.25x your normal per-task cost on annual plans and 2.5x on monthly plans

Zapier's blog post 'What is a task in Zapier?' gives these multipliers: 1.25x on annual plans and 2.5x on monthly plans.
- [https://zapier.com/blog/what-is-a-task-in-zapier/](https://zapier.com/blog/what-is-a-task-in-zapier/) — For annual plans, extra tasks are billed at 1.25x your plan's normal task cost. For monthly plans, the rate is 2.5x.

## [OK] L102 · low
> The free plan has no pay-per-task option, so free Zaps simply stop at 100 tasks.

The Help Center lists pay-per-task as unavailable on the Free plan, and the pricing page's lowest tier is 100 tasks per month. The 100-task limit is monthly, so free Zaps stop once 100 tasks are used in a month.
- [https://help.zapier.com/hc/en-us/articles/15279018245901](https://help.zapier.com/hc/en-us/articles/15279018245901) — This feature is only available on paid Zapier plans.
- [https://zapier.com/pricing](https://zapier.com/pricing) — 100 tasks /mo

## [OK] L102 · low
> On self-serve plans the task limit is monthly (tasks are listed "per month" even on annual billing), while Enterprise uses an annual task limit.

Self-serve task tiers are listed per month (e.g. '750 tasks /mo'), and that stays the same when you switch to yearly billing. 'Annual task limits' is listed as an Enterprise feature.
- [https://zapier.com/pricing](https://zapier.com/pricing) — Key features: Unlimited users Advanced admin permissions and app controls Advanced deployment options Annual task limits

## [OK] L121 · low
> The free plan allows two-step Zaps only, meaning one trigger and one action, and polls every 15 minutes.

Zapier's pricing page lists the Free plan with two-step Zaps and a 15-minute polling time.
- [https://zapier.com/pricing](https://zapier.com/pricing) — Steps: Two-step (Free) ... Polling time: 15 min (Free), 2 min (Professional)

## [OK] L123 · low
> If you need a Filter, a second action, or webhooks, you need Professional.

On the pricing page, Multi-step Zaps and Webhooks are listed as key features of Professional, and Free is limited to two-step Zaps. Filters & Paths appear as paid-tier features. Team and Enterprise also include these features, but Professional is the cheapest plan that does.
- [https://zapier.com/pricing](https://zapier.com/pricing) — Professional ... Key features: Multi-step Zaps, Unlimited Premium apps, Webhooks

## [OK] L123 · low
> Upgrades take effect right away and are prorated, per Zapier's FAQ.

The FAQ on Zapier's pricing page says upgrades happen immediately and are billed at a prorated amount.
- [https://zapier.com/pricing](https://zapier.com/pricing) — If you upgrade, the change happens immediately, and you'll only pay a prorated amount for the rest of the billing cycle.
