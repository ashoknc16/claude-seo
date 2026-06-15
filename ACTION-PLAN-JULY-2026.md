# SEO Action Plan — July 2026
**Site:** national-claims.co.uk
**Current Health Score:** 60/100 → **July target: 68/100**
**Based on:** FULL-AUDIT-REPORT-2026-06-15.md
**Item IDs** reference ACTION-PLAN.md (C1–C3, H1–H7, M1–M8, L1–L6)

> July theme: **Unblock, de-duplicate, and consolidate.** Clear the structural debt (WAF, subdomain, cannibalization) first so everything downstream — schema, AI citation, the car-finance pillar — actually gets crawled and counted.

---

## Owners (assign before 1 July)
- **DEV** — web developer / hosting
- **OPS** — DevOps / Cloudflare admin
- **CON** — content / copywriter
- **MKT** — marketing / SEO lead (also owns GSC + reporting)
- **COMP** — compliance (FCA financial-promotion sign-off)

---

## Week 1 — 1–5 July · Unblock & Stop the Bleeding 🔴
Goal: remove the issues that suppress crawling and split equity.

| # | Task | Item | Owner | Effort | Done when |
|---|------|------|-------|--------|-----------|
| 1 | Audit Cloudflare/WAF bot rules; allow `Googlebot-Extended`, `Bingbot`, `GPTBot`, `ClaudeBot`, `PerplexityBot`, `CCBot` (+ optional Ahrefs/Semrush) | C1 | OPS | 2h | `curl -A "<bot>"` returns 200, not 403 |
| 2 | 301-redirect (or canonicalise) all `gb.national-claims.co.uk` URLs → main domain | C3 | OPS/DEV | 3h | `gb.` URLs 301 to main; removal requested in GSC |
| 3 | Decide canonical housing-disrepair money page; 301 the redundant ones; fold unique copy in | §1.2 | DEV/CON | 4h | One indexable HD money page; others 301 or clearly informational |
| 4 | Confirm single canonical medical/clinical-negligence URL (resolve `/medical-` vs `/clinical-`) | §1.2 | DEV | 1h | One URL; the other 301s |
| 5 | Standardise NAP (one phone, one address = FCA-register format) across site footer/contact/schema | C2 | MKT/DEV | 3h | Identical NAP everywhere on-site |
| 6 | Verify `robots.txt` + `sitemap.xml` are publicly reachable (post-WAF fix) and sitemap submitted | H5 | OPS/MKT | 2h | Both return 200; sitemap accepted in GSC + Bing |

**Exit check (5 Jul):** WAF passes named bots · `gb.` 301s live · one HD page · one negligence URL · NAP consistent · sitemap submitted.

---

## Week 2 — 6–12 July · Discoverability & AI 🟠
Goal: make the site legible to AI engines and disambiguate the brand entity.

| # | Task | Item | Owner | Effort | Done when |
|---|------|------|-------|--------|-----------|
| 7 | Publish `/llms.txt` (five service lines + car-finance pillar) | H1 | DEV | 1h | File live, 200 to AI bots |
| 8 | Add AI `Allow` directives + `Sitemap:` line to robots.txt | H1/H5 | OPS | 1h | Verified in robots.txt |
| 9 | Disambiguate brand entity — use full operating entity (Finance Advice Helpline Ltd, FRN 838876) in About + schema; distinguish from National Claims Ltd (09882820) | §7 | MKT/CON | 2h | About + schema name the correct entity + FRN |
| 10 | Off-site NAP citation cleanup (GBP, Bing Places, Trustpilot, Yell, Companies House, Legal Futures, LinkedIn, Facebook) | C2 | MKT | 4h | Top 8 citations match canonical NAP |
| 11 | Fix weak title tags (add brand to service pages; give About/FAQs keyword value; fix capitalisation) | H4 | CON | 2h | All target pages updated |

**Exit check (12 Jul):** llms.txt + robots AI rules live · brand entity consistent · top citations aligned · titles fixed.

---

## Week 3 — 13–19 July · Car-Finance Pillar & Schema 🟠
Goal: consolidate the highest-opportunity cluster and ship structured data.

| # | Task | Item | Owner | Effort | Done when |
|---|------|------|-------|--------|-----------|
| 12 | Build `/mis-sold-car-finance-claims/` pillar page (eligibility, FCA redress timeline, fee disclosure, CTA) | H6 | CON/DEV | 1d | Pillar live, indexable |
| 13 | Internally link every car-finance blog post → pillar, and pillar → key posts (hub-and-spoke) | H6 | CON | 3h | All cluster posts link up; pillar links down |
| 14 | FCA-compliant disclaimers + source every payout/eligibility figure (FCA/FOS/court) on car-finance content | H7 | COMP/CON | 5h | COMP sign-off recorded; no unsourced figures |
| 15 | Add `aggregateRating` (Trustpilot ~1,908) to Organization schema on homepage | H3 | DEV | 1.5h | Passes Rich Results Test |
| 16 | Add `LegalService` schema to PI / RTA / medical-negligence pages; `FinancialService`/`Service` to car finance | H2 | DEV | 4h | Each page validates |

**Exit check (19 Jul):** car-finance pillar live + linked · figures sourced & COMP-approved · aggregateRating + service schema validating.

---

## Week 4 — 20–26 July · On-Page Depth & E-E-A-T 🟡
| # | Task | Item | Owner | Effort | Done when |
|---|------|------|-------|--------|-----------|
| 17 | Add author attribution + bios to blog posts; `author` + `dateModified` in Article schema | M2 | DEV/CON | 5h | Bylines + schema on YMYL posts |
| 18 | Add visible "Last updated" dates + freshness cadence for time-sensitive car-finance posts | H7 | CON | 2h | Dates visible; review cadence documented |
| 19 | Rewrite meta descriptions (unique, 140–160 chars, CTA, USP) for all key pages | M3 | CON | 3h | Every key page unique |
| 20 | Add `BreadcrumbList` schema + HTML breadcrumbs on inner pages | M4 | DEV | 3h | Validates on inner pages |
| 21 | Add `Person` schema to Meet the Team | M5 | DEV | 1.5h | Validates |

**Exit check (26 Jul):** authorship + dates live · meta descriptions unique · breadcrumb + person schema validating.

---

## Week 5 — 27–31 July · Measure, Verify & Plan August 🟢
| # | Task | Item | Owner | Effort | Done when |
|---|------|------|-------|--------|-----------|
| 22 | Run PageSpeed Insights / CrUX on homepage + 4 top pages; log LCP/INP/CLS; ticket fixes | M8 | DEV/MKT | 4h | Baseline recorded; fix backlog created |
| 23 | Re-run a crawl now that WAF allows tools (Screaming Frog/Semrush) to verify everything previously ⚠️ Unverified | C1 | MKT | 3h | Verified report on schema/headers/meta |
| 24 | GSC review: index coverage of `gb.` removal, HD consolidation, new pillar; check for new duplicates | — | MKT | 2h | Coverage clean; pillar indexed |
| 25 | Draft August plan (image alt audit L6, OG tags M7, missing service pages M1, authority/L2–L3) | M1/M7/L | MKT | 2h | August plan ready |

**Exit check (31 Jul):** CWV baselined · tool-verified audit replaces estimates · GSC clean · August plan drafted.

---

## July Definition of Done
- [ ] WAF allows AI + SEO crawlers (no 403 for named bots)
- [ ] `gb.` subdomain no longer indexed as duplicate
- [ ] One canonical page each for housing disrepair & medical negligence
- [ ] NAP consistent on-site and across top 8 citations; brand entity disambiguated
- [ ] `/llms.txt` live; robots.txt updated
- [ ] Mis-sold car finance pillar live, internally linked, COMP-approved
- [ ] aggregateRating + LegalService/FinancialService + BreadcrumbList + Person schema validating
- [ ] Blog authorship + dateModified on YMYL content
- [ ] CWV baselined; tool-verified audit replaces ⚠️ Unverified items

## KPIs to watch (set baseline 1 July in GSC/GA4)
| Metric | Baseline (1 Jul) | 31 Jul target |
|--------|------------------|---------------|
| Health score | 60 | 68 |
| Indexed duplicate (`gb.`) URLs | >0 | 0 |
| Pages with valid schema | low | all service + home + pillar |
| Car-finance cluster: organic clicks | record | +20% |
| AI crawler hits (GPTBot/ClaudeBot/PerplexityBot in logs) | ~0 | >0 |
| Avg LCP (top 5 pages) | record | ≤2.5s on ≥3 |

## Carried to August (not in July scope)
M1 remaining service/pillar pages · M7 Open Graph audit · L6 image alt audit · L1 award schema · L2 Wikidata/Wikipedia · L3 industry-publication outreach.

---
*July 2026 plan · derived from the 15 Jun 2026 re-audit · all ⚠️ Unverified items assume WAF is unblocked in Week 1 so they can finally be confirmed.*
