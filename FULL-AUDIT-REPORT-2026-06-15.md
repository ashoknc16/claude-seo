# Full SEO Audit Report — national-claims.co.uk
**Generated:** 15 June 2026 (fresh full re-audit)
**Audited URL:** https://national-claims.co.uk
**Business Type:** UK Claims Management Company (FCA-regulated, financial/legal YMYL)
**Audit Method:** Indexed-content + search-intelligence reconstruction (direct crawl blocked)
**Supersedes:** FULL-AUDIT-REPORT.md (2 April 2026) — kept for history

---

## ⚠️ Audit Limitation Notice

The site returns **HTTP 403 Forbidden** to automated requests (CDN/WAF, likely Cloudflare), and this audit environment's network policy does not allowlist the host. Direct fetching of HTML, `robots.txt`, `sitemap.xml`, headers, schema, and Core Web Vitals was therefore not possible. All findings are reconstructed from:

- Google-indexed page titles, URLs, and snippets (June 2026)
- Trustpilot, Companies House, FCA register, and social profiles
- Industry award coverage (Personal Injury Awards, Modern Claims Awards)

**Anything marked ⚠️ Unverified must be confirmed by the site owner** with direct access, or by re-running this audit from a whitelisted/residential IP. Scores carry **Medium confidence**.

---

## Executive Summary

### SEO Health Score: **60 / 100**

| Category | Score | Weight | Weighted |
|----------|-------|--------|----------|
| Technical SEO | 55/100 | 22% | 12.1 |
| Content Quality | 76/100 | 23% | 17.5 |
| On-Page SEO | 62/100 | 20% | 12.4 |
| Schema / Structured Data | 42/100 | 10% | 4.2 |
| Performance (CWV) | 50/100 | 10% | 5.0 |
| AI Search Readiness | 42/100 | 10% | 4.2 |
| Images | 50/100 | 5% | 2.5 |
| **TOTAL** | | **100%** | **57.9 → 60** |

> Up from 58 (April). The lift is driven by **Content Quality** — active, timely publishing across five service lines plus a large mis-sold car finance cluster. Technical and Schema scores are unchanged because the same blockers (WAF, unresolved subdomain, unverified markup) persist.

### Top 6 Critical / High Issues
1. **WAF returns 403 to all non-Googlebot crawlers** — blocks SEO tools, Bing, and (likely) AI crawlers; cannot verify robots/sitemap/headers/schema.
2. **`gb.national-claims.co.uk` subdomain STILL indexed** — serves "Home - National Claims"; unresolved duplicate-content / link-equity dilution from April.
3. **Housing-disrepair page cannibalization** — at least 3 overlapping indexed pages (`/housing-disrepair-claims/`, `/housing-disrepair-claims-and-costs/`, `/housing-disrepair-and-housing-association-negligence/`) competing for the same intent.
4. **Mis-sold car finance cluster has no canonical pillar page** — large blog cluster, scattered authority; money-YMYL content needs FCA-compliant disclaimers and sourced figures.
5. **NAP / phone inconsistency** — 0800 029 3849 (site) vs 0345 2600 600 (some external sources); two address formats.
6. **Brand-entity ambiguity** — a *separate* "National Claims Limited" (Companies No. **09882820**) appears in results alongside the operator **Finance Advice Helpline Limited** (No. 11285085, FRN 838876). Entity signals must disambiguate clearly.

### Top 5 Quick Wins
1. 301-redirect or canonicalise `gb.national-claims.co.uk` → main domain.
2. Consolidate the housing-disrepair pages into one canonical page (301 the rest).
3. Create `/llms.txt` covering all five service lines + car finance.
4. Build a mis-sold car finance pillar page and internally link the blog cluster to it.
5. Add `aggregateRating` (Trustpilot ~1,908 reviews) + `LegalService`/`FinancialService` schema.

---

## Business Profile

| Field | Value |
|-------|-------|
| Operating legal entity | Finance Advice Helpline Limited |
| Trading name | National Claims |
| Company number | 11285085 (England & Wales) |
| FCA registration | FRN 838876 |
| ⚠️ Entity note | A separate **National Claims Limited (09882820)** also appears in search — not the same entity; disambiguate. |
| Address (site) | Ground Floor, Spectra House, Spring Villa Park, Spring Villa Road, Edgware, HA8 7EB |
| Phone (site) | 0800 029 3849 |
| Phone (some external) | 0345 2600 600 |
| Email | info@national-claims.co.uk |
| Hours | 7 days a week |
| Trustpilot | 5 stars, ~1,908 reviews (96 review pages) |
| Awards | Claims Management Company of the Year 2024 & 2025; Outsourced Partner of the Year 2025; Modern Claims Awards 2026 shortlist (Best Customer Service <100 Employees; Innovation of the Year — ceremony 26 Feb 2026) |
| Model | Claims management company (not solicitors); panel of regulated solicitors; No Win No Fee, up to 25% incl. VAT |

---

## 1. Technical SEO — 55/100

### 1.1 Crawlability & Indexability
| Check | Status | Notes |
|-------|--------|-------|
| HTTPS | ✅ | Serves on HTTPS |
| Googlebot access | ✅ Inferred | Site is indexed and ranks |
| Non-Googlebot crawlers (Bing, SEO tools, AI bots) | ❌ 403 | WAF blocks datacenter IPs |
| robots.txt / sitemap.xml | ⚠️ Unverified | Blocked by 403 |
| `gb.` subdomain duplicate | ❌ **Unresolved** | `gb.national-claims.co.uk` still indexed as "Home - National Claims" |
| Canonical tags | ⚠️ Unverified | |

**Subdomain (still open from April):** Either 301 all `gb.` URLs to the main domain, or `rel=canonical` them to the equivalent main-domain URL, then request removal in Search Console. This is the single highest-leverage unresolved technical issue.

### 1.2 URL Structure & Duplication
Indexed service URLs are clean and readable:
`/personal-injury-claims/`, `/car-accident-claims/`, `/medical-negligence-claims/`, `/housing-disrepair-claims/`, `/claim-process/`, `/start-my-claim/`, `/faqs/`, `/about-us/`, `/meet-the-team/`, `/contact-the-team/`, `/complaints-procedure/`, `/privacy-policy/`.

⚠️ **New duplication risk — housing disrepair.** Multiple indexed pages target overlapping intent:
- `/housing-disrepair-claims/`
- `/housing-disrepair-claims-and-costs/`
- `/housing-disrepair-and-housing-association-negligence/`
- plus several housing-disrepair blog posts

Pick **one** canonical money page, fold the others' unique content into it (or make them clearly informational/blog), and 301 the redundant ones. Otherwise they split rankings and internal link equity.

⚠️ **Note:** April referenced `/clinical-negligence-claims/`; June indexes `/medical-negligence-claims/`. Confirm there is one canonical medical/clinical negligence URL, not two competing ones.

### 1.3 Security & Headers
HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy — all ⚠️ Unverified (403). Verify directly.

---

## 2. Content Quality — 76/100  *(up from 72)*

### 2.1 E-E-A-T
| Signal | Status | Notes |
|--------|--------|-------|
| Experience | ✅ Strong | Detailed claim-process, real Trustpilot case study |
| Expertise | ✅ Strong | FCA-regulated, panel solicitors, multiple service areas |
| Authoritativeness | ✅ Strong | CMC of the Year 2024 & 2025; Modern Claims 2026 shortlist; ~1,908 reviews |
| Trustworthiness | ✅ Strong | FCA FRN, company reg, 25% fee disclosure, complaints procedure published |
| Author attribution on blog | ⚠️ Likely missing | Not verified; **critical** for money/health YMYL |
| Medical/financial expert review | ⚠️ Unknown | Clinical negligence + car finance are YMYL |

### 2.2 Breadth & Activity
National Claims is publishing actively across five service lines:
- **Personal injury / road traffic accident** — core, mature pages
- **Medical (clinical) negligence** — service + guide content
- **Housing disrepair** — multiple pages + guides (needs consolidation, see §1.2)
- **Mis-sold car / vehicle finance** — large, timely blog cluster around the 2026 FCA redress scheme (PCP/HP 2007–2024; FCA final decisions Feb–Mar 2026; complaint-handling pause to 31 May 2026)

This breadth and freshness is the main reason Content scores well. The weaknesses are structural (no pillar pages, cannibalization) and compliance (YMYL), not volume.

### 2.3 Compliance Caveat (money/health YMYL)
Car-finance posts cite payout figures ("most claims under £950", "~£700 per agreement"). For an FCA-authorised CMC these must be **sourced to FCA/FOS/court rulings, dated, and accompanied by fee + no-guarantee disclaimers** consistent with CMC financial-promotion rules. The motor-finance CMC sector is under active FCA scrutiny in 2026 (the FCA has opened investigations into other motor-finance CMCs) — no evidence implicates National Claims, but accuracy and substantiation are now reputationally and regulatorily material.

---

## 3. On-Page SEO — 62/100

### 3.1 Titles (from indexed snippets)
| Page | Indexed Title | Assessment |
|------|---------------|------------|
| Homepage | "Claims Management Company of the Year 2025 \| National Claims" | ✅ Strong differentiator, brand present. Consider refreshing the year/award messaging. |
| /about-us/ | "About Us - National Claims" | ⚠️ No keyword value |
| /personal-injury-claims/ | "Personal Injury claims - National Claims" | ✅ Keyword present (capitalise "Claims") |
| /car-accident-claims/ | "Car Accident Compensation Claims" | ✅ Strong keyword; **add brand** |
| /medical-negligence-claims/ | "Medical Negligence Claims" | ✅ Keyword; **add brand** |
| /housing-disrepair-claims/ | "Housing Disrepair Claims - National Claims" | ✅ |
| /faqs/ | "FAQs - National Claims" | ⚠️ No keyword value |
| /contact-the-team/ | "Contact the team - National Claims" | ⚠️ lowercase "team" |

**Fixes:** add brand to service titles missing it; give About/FAQs keyword value; standardise capitalisation. Template: `[Primary Keyword] | National Claims`.

### 3.2 Meta Descriptions / OG / Headings
⚠️ Unverified (403). Verify uniqueness, length (140–160 chars), CTAs; verify single H1 per page; verify `og:image` (1200×630) given active Facebook/LinkedIn presence.

### 3.3 Internal Linking
Clean primary nav across service + trust pages. Gaps: no pillar→cluster linking for car finance; housing-disrepair pages link-compete. Build hub-and-spoke linking per service line.

---

## 4. Schema & Structured Data — 42/100

⚠️ Markup not directly verifiable (403). Based on type, the following are **expected and likely missing/partial**:

| Schema | Priority | Action |
|--------|----------|--------|
| Organization + `aggregateRating` (Trustpilot ~1,908) | High | Surface star rating; keep count current |
| LegalService (PI / RTA / clinical negligence) | High | Per service page, with `areaServed: GB`, FCA credential |
| FinancialService / Service (car finance) | High | Distinct from LegalService |
| BreadcrumbList | Medium | All inner pages (HTML + schema) |
| Person (Meet the Team) | Medium | Entity recognition / E-E-A-T |
| Article + `author` + `dateModified` (blog) | Medium | Freshness + YMYL authorship |
| FAQPage (/faqs/) | Info only | AI-citation benefit; no Google rich result for commercial since 2023 |

```json
{
  "@context": "https://schema.org",
  "@type": "LegalService",
  "name": "National Claims",
  "url": "https://national-claims.co.uk/personal-injury-claims/",
  "telephone": "+448000293849",
  "areaServed": { "@type": "Country", "name": "United Kingdom" },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Ground Floor, Spectra House, Spring Villa Road",
    "addressLocality": "Edgware", "postalCode": "HA8 7EB", "addressCountry": "GB"
  },
  "hasCredential": {
    "@type": "EducationalOccupationalCredential",
    "credentialCategory": "FCA Authorised (FRN 838876)",
    "recognizedBy": { "@type": "Organization", "name": "Financial Conduct Authority" }
  }
}
```

---

## 5. Performance (Core Web Vitals) — 50/100

⚠️ Estimated only — no lab/field data (403). Owner should run PageSpeed Insights / CrUX directly on the homepage + top service pages. Typical CMS/claims-site risks: render-blocking chat & tracking scripts, unoptimised hero images, font load delay, tag bloat (GA4/Meta Pixel). Targets: LCP ≤2.5s, INP ≤200ms, CLS ≤0.1.

---

## 6. AI Search Readiness (GEO) — 42/100

| Check | Status |
|-------|--------|
| /llms.txt | ❌ Missing / unverifiable |
| AI crawler access (GPTBot, ClaudeBot, PerplexityBot, Googlebot-Extended, CCBot) | ❌ Likely blocked by WAF |
| Citability of content | ✅ Good — FCA reg, company reg, awards, fee disclosure, dated guides |

Strong citable facts and a topical, timely car-finance cluster make this site a good AI-citation candidate — **if** AI crawlers are unblocked. Create `/llms.txt`, explicitly allow AI user-agents in robots.txt, and ensure the WAF doesn't 403 them.

```
# National Claims — llms.txt
> Finance Advice Helpline Limited, trading as National Claims — FCA-authorised (FRN 838876)
> UK claims management company. No Win No Fee (up to 25% incl. VAT). Trustpilot 5★ (~1,908 reviews).
## Key Pages
- [Home](https://national-claims.co.uk/)
- [Personal Injury Claims](https://national-claims.co.uk/personal-injury-claims/)
- [Car Accident Claims](https://national-claims.co.uk/car-accident-claims/)
- [Medical Negligence Claims](https://national-claims.co.uk/medical-negligence-claims/)
- [Housing Disrepair Claims](https://national-claims.co.uk/housing-disrepair-claims/)
- [Mis-Sold Car Finance Claims](https://national-claims.co.uk/mis-sold-car-finance-claims/)  ← create pillar
- [How Claims Work](https://national-claims.co.uk/claim-process/)
- [FAQs](https://national-claims.co.uk/faqs/)
```

---

## 7. Local / Entity SEO — 62/100

National Claims is a UK-wide service-area business (not a single-location retailer). Priorities are GBP optimisation, NAP consistency, and **entity disambiguation**.

| Issue | Status | Action |
|-------|--------|--------|
| Phone inconsistency | ❌ | 0800 029 3849 vs 0345 2600 600 — pick one canonical |
| Address format inconsistency | ❌ | Standardise to FCA-register format everywhere |
| Brand-entity ambiguity | ❌ **New** | Disambiguate from "National Claims Limited" (09882820); use full operating entity (Finance Advice Helpline Ltd, FRN 838876) in schema + About |
| Trust/regulatory signals | ✅ | FCA FRN, company reg, fee + cancellation disclosure, complaints procedure |
| Citations | ⚠️ | Standardise across GBP, Bing Places, Trustpilot, Yell, Companies House, Legal Futures |

---

## 8. Images — 50/100
⚠️ Unverified (403). Confirm descriptive alt text everywhere; award badges should carry specific alt (e.g. `alt="Claims Management Company of the Year 2025 – Personal Injury Awards"`); modern formats (WebP/AVIF), compression, lazy-loading, and a preloaded LCP hero image.

---

## 9. Competitor Context
Crowded UK CMC/PI market: National Accident Helpline, National Accident Law, claims.co.uk, Slater and Gordon, Thompsons. National Claims differentiates on awards, ~1,908 Trustpilot reviews, FCA regulation, and a fast-moving content engine — especially the timely mis-sold car finance cluster, where first-mover topical depth is a real advantage if consolidated into a pillar and kept compliant.

---

## Scoring Summary
```
SEO Health Score: 60/100  (April baseline: 58)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Technical SEO       ███████████░░░░░░░░░  55/100
Content Quality     ███████████████░░░░░  76/100
On-Page SEO         ████████████░░░░░░░░  62/100
Schema / Struct.    ████████░░░░░░░░░░░░  42/100
Performance (CWV)   ██████████░░░░░░░░░░  50/100
AI Search Ready     ████████░░░░░░░░░░░░  42/100
Images              ██████████░░░░░░░░░░  50/100
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Confidence: Medium (WAF + network policy blocked direct crawl)
```

## Priority Roadmap (this audit)
1. **Now:** resolve `gb.` subdomain; consolidate housing-disrepair pages; confirm single medical-negligence URL.
2. **Week 1:** `/llms.txt` + unblock AI/SEO crawlers in WAF; standardise NAP; disambiguate brand entity.
3. **Week 2:** car-finance pillar page + cluster internal linking; LegalService/FinancialService + `aggregateRating` schema; FCA-compliant disclaimers & sourced figures; fix weak titles.
4. **Month 1+:** blog author attribution + `dateModified`; BreadcrumbList & Person schema; meta descriptions; measure & fix CWV.

> Detailed task breakdowns (effort, code samples) are in **ACTION-PLAN.md** (items C1–C3, H1–H7, M1–M8, L1–L6).

---
*Fresh re-audit — 15 June 2026. Scores are Medium-confidence pending direct-access verification.*
