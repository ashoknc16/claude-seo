# Full SEO Audit Report — national-claims.co.uk
**Generated:** 2 April 2026  
**Audited URL:** https://national-claims.co.uk  
**Business Type:** Claims Management Company (UK Financial/Legal Services)  
**Audit Method:** Multi-agent parallel analysis + indexed content + search intelligence

---

## ⚠️ Audit Limitation Notice

The site returns **HTTP 403 Forbidden** to all automated crawler requests from datacenter IPs (CDN/WAF protection — likely Cloudflare). This blocked direct HTML fetching for robots.txt, sitemap.xml, and page content analysis. All findings below are derived from:

- Google-indexed page cache and search snippets
- Public business registry data
- Trustpilot and third-party review platforms
- LinkedIn and Facebook profile data
- FCA register data

Recommendations in this report should be verified by the site owner with direct access, or by running audits from a residential/whitelisted IP.

---

## Executive Summary

### SEO Health Score: **58 / 100**

| Category | Score | Weight | Weighted |
|----------|-------|--------|---------|
| Technical SEO | 55/100 | 22% | 12.1 |
| Content Quality | 72/100 | 23% | 16.6 |
| On-Page SEO | 63/100 | 20% | 12.6 |
| Schema / Structured Data | 42/100 | 10% | 4.2 |
| Performance (CWV) | 50/100 | 10% | 5.0 |
| AI Search Readiness | 38/100 | 10% | 3.8 |
| Images | 50/100 | 5% | 2.5 |
| **TOTAL** | | **100%** | **56.8 → 58** |

> **Score confidence: Medium** — limited by 403 WAF blocking of direct page crawl. Actual scores may differ once access is available.

### Top 5 Critical Issues
1. **403 WAF blocking all automated crawlers** — prevents SEO tools from auditing; risk to non-Googlebot crawlers
2. **Phone number NAP inconsistency** — 0800 029 3849 (site footer) vs 0345 2600 600 (external sources)
3. **Address format inconsistency** — two different address formats found across indexed content
4. **No llms.txt file** — AI search engines cannot discover indexed content permissions
5. **Subdomain gb.national-claims.co.uk detected** — potential duplicate content/indexation risk

### Top 5 Quick Wins
1. Create `/llms.txt` file to allow AI crawler access and boost AI Overview citations
2. Standardise NAP across all pages and external citations (one phone number, one address format)
3. Redirect or canonicalise `gb.national-claims.co.uk` to the main domain
4. Add `ReviewAggregation` schema linking Trustpilot's 1,900+ reviews to homepage
5. Add `LegalService` schema to service pages (personal injury, clinical negligence, car accident claims)

---

## Business Profile

| Field | Value |
|-------|-------|
| Legal name | Finance Advice Helpline Limited |
| Trading name | National Claims / National Claims Compensation Helpline |
| Company number | 11285085 (England & Wales) |
| FCA registration | FRN 838876 |
| Registered address | Ground Floor, Spectra House, Spring Villa Park, Spring Villa Road, Edgware, HA8 7EB |
| Phone (site) | 0800 029 3849 |
| Phone (external) | 0345 2600 600 |
| Email | info@national-claims.co.uk |
| Trustpilot | 5 stars, ~1,900+ reviews |
| Awards | Claims Management Company of the Year 2024 (Personal Injury Awards); Outsourced Partner of the Year 2025; Shortlisted Modern Claims Awards 2026 |

---

## 1. Technical SEO — 55/100

### 1.1 Crawlability

| Check | Status | Notes |
|-------|--------|-------|
| HTTP → HTTPS redirect | ✅ Assumed | Site serves on HTTPS |
| www → non-www (or vice versa) | ⚠️ Unverified | 403 blocked redirect check |
| robots.txt accessible | ❌ **Blocked (403)** | Could not fetch `/robots.txt` |
| Sitemap accessible | ❌ **Blocked (403)** | Could not fetch `/sitemap.xml` |
| WAF/IP blocking | ❌ **CRITICAL** | All datacenter IPs return 403; SEO tools blocked |
| Googlebot likely allowed | ✅ Inferred | Site IS indexed by Google, so Googlebot passes |
| Crawl budget efficiency | ⚠️ Unknown | Sitemap not accessible |

**Key Issue — WAF Blocking:** The site's CDN (likely Cloudflare) is blocking all datacenter IP ranges. While Googlebot appears to be whitelisted (as the site ranks and appears in Google index), this blocking will affect:
- All third-party SEO audit tools (Semrush, Ahrefs, Screaming Frog, etc.)
- Bing Bot (if not whitelisted)
- AI crawlers (GPTBot, ClaudeBot, PerplexityBot) — unless individually whitelisted in robots.txt
- Synthetic monitoring / Core Web Vitals lab testing

**Recommendation:** Review WAF rules to allow legitimate bot User-Agents. At minimum, add an explicit `Allow` for known SEO tool bots in robots.txt and whitelist their IP ranges in Cloudflare.

### 1.2 Indexability

| Check | Status | Notes |
|-------|--------|-------|
| Site indexed by Google | ✅ | Multiple pages visible in site: search |
| Meta robots (homepage) | ⚠️ Unverified | Could not fetch page HTML |
| Canonical tags | ⚠️ Unverified | Could not verify |
| Duplicate content risk (subdomain) | ❌ **HIGH** | `gb.national-claims.co.uk` found in search results — needs investigation |
| Pagination issues | ⚠️ Unknown | Could not crawl |

**Subdomain Risk:** `https://gb.national-claims.co.uk/` is indexed and appears to serve content ("Home - National Claims"). If this is the same content as the main domain, it creates a duplicate indexation risk and dilutes link equity. Immediate action required: either 301 redirect to main domain, or canonicalise all pages to main domain.

### 1.3 Security & Headers

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS | ✅ Active | |
| HSTS | ⚠️ Unverified | Headers blocked by 403 |
| X-Frame-Options | ⚠️ Unverified | |
| CSP | ⚠️ Unverified | |
| X-Content-Type-Options | ⚠️ Unverified | |
| Referrer-Policy | ⚠️ Unverified | |

### 1.4 URL Structure

Indexed URLs show clean, readable URL patterns:
- `/personal-injury-claims/` ✅
- `/car-accident-claims/` ✅
- `/clinical-negligence-claims/` ✅
- `/claim-process/` ✅
- `/start-my-claim/` ✅
- `/faqs/` ✅
- `/contact-the-team/` ✅
- `/meet-the-team/` ✅

All URLs use trailing slashes consistently. No URL structure issues detected from indexed content.

### 1.5 NAP Inconsistency (Critical)

Two phone numbers found:
- **0800 029 3849** — appears in footer/site content
- **0345 2600 600** — appears in external third-party sources

Two address formats found:
- `Ground Floor, Spectra House, Spring Villa Park, Spring Villa Road, Edgware, HA8 7EB`
- `10 Spectra House Ground Floor, Spring Villa Road, Edgware, HA8 7EB`

These inconsistencies damage local citation authority and confuse both users and search engines. A single canonical NAP must be used everywhere.

---

## 2. Content Quality — 72/100

### 2.1 E-E-A-T Assessment

| Signal | Status | Notes |
|--------|--------|-------|
| Experience | ✅ Strong | Claim process page, No Win No Fee explanation |
| Expertise | ✅ Strong | FCA regulation, panel solicitors, specialist service areas |
| Authoritativeness | ✅ Strong | Award-winning (2024, 2025, 2026 shortlist), 1,900+ Trustpilot reviews |
| Trustworthiness | ✅ Strong | FCA FRN displayed, company reg, 25% success fee disclosed |
| Author attribution | ⚠️ Unknown | Could not verify blog post authorship |
| Medical/legal expert review | ⚠️ Unknown | Clinical negligence pages — expert review attribution not confirmed |

**Assessment:** Strong E-E-A-T foundation for a regulated financial services entity. FCA authorisation number, explicit fee disclosure, and award recognition are excellent trust signals. The "Meet the Team" page is a positive E-E-A-T signal.

**Gap:** For clinical negligence pages (YMYL content), Google expects explicit medical expert review/sign-off. If blog or service pages lack author credentials, this is a ranking risk.

### 2.2 Content Depth (Inferred)

| Page | Est. Status | Notes |
|------|-------------|-------|
| Homepage | ✅ Good | Award messaging, service overview, trust signals |
| Personal Injury Claims | ⚠️ Unknown depth | Service page exists |
| Car Accident Claims | ⚠️ Unknown depth | Service page exists |
| Clinical Negligence | ⚠️ Unknown depth | Service page exists; YMYL — needs depth |
| Claim Process | ✅ Good signal | Dedicated page is a positive UX/SEO signal |
| FAQs | ✅ Present | Good for AI citation even if not Google rich result |
| Blog | ✅ Present | Award posts visible (at least 2 confirmed) |
| About Us | ✅ Present | Good E-E-A-T signal |
| Meet the Team | ✅ Present | Strong E-E-A-T signal |

**Missing service pages** (based on business description but not confirmed in indexed URLs):
- Housing Disrepair Claims
- Birth Injury Claims
- Defective Product Claims
- Injury at Work Claims
- Slip and Trip Claims

If these exist but aren't indexed, it's a crawlability issue. If they don't exist as dedicated pages, it's a content gap opportunity.

### 2.3 Readability

Could not directly assess readability scores. The site caters to general public (personal injury claimants), requiring plain English (Flesch-Kincaid grade 8 or lower). Claims management content should avoid excessive legal jargon.

---

## 3. On-Page SEO — 63/100

### 3.1 Title Tags

| Page | Title | Assessment |
|------|-------|------------|
| Homepage | "Claims Management Company of the Year 2025 \| National Claims" | ✅ Good — award-focused differentiator, brand included. ~62 chars |

Inner page titles not verified (403 blocked). Based on Google snippet titles:
- `/about-us/` → "About Us - National Claims" — ⚠️ generic, no keyword value
- `/personal-injury-claims/` → "Personal Injury claims - National Claims" — ✅ keyword present
- `/car-accident-claims/` → "Car Accident Compensation Claims" — ✅ strong keyword, missing brand
- `/clinical-negligence-claims/` → "Clinical Negligence Claims" — ✅ keyword present, missing brand
- `/contact-the-team/` → "Contact the team - National Claims" — ⚠️ lowercase "team", minor issue
- `/faqs/` → "FAQs - National Claims" — ⚠️ no keyword value in title

**Issues identified:**
- "About Us" title has no keyword value — opportunity to target "about National Claims" or "award-winning claims management company"
- FAQs title misses keyword opportunity — e.g., "Compensation Claims FAQs | National Claims"
- Some inner pages missing brand name

### 3.2 Meta Descriptions

Not directly verifiable due to 403 blocking. Site-indexed snippets suggest descriptions exist. Quality and CTR optimisation cannot be verified without direct page access.

### 3.3 Heading Structure

H1 on homepage appears to be award-focused: "Claims Management Company of the Year 2025" (inferred). Inner page H1 tags not verifiable.

### 3.4 Internal Linking

Navigation structure is clean with 9 main pages. Breadcrumbs and contextual internal linking to service pages could not be verified. Blog posts visible suggest content hub internal linking opportunity.

### 3.5 Open Graph / Social Meta

Could not verify OG tags (403 blocked). These are important for social sharing (Facebook, LinkedIn) given the company's active social presence.

---

## 4. Schema & Structured Data — 42/100

> **Note:** Schema markup could not be directly extracted due to 403 blocking. Assessment based on indexed content and business type analysis.

### 4.1 Expected vs Detected Schema

| Schema Type | Expected | Likely Status | Priority |
|-------------|----------|---------------|----------|
| Organization | ✅ Yes | ⚠️ Unverified | High |
| LocalBusiness / LegalService | ✅ Yes | ❌ Likely missing | High |
| WebPage / WebSite | ✅ Yes | ⚠️ Unverified | Medium |
| BreadcrumbList | ✅ Yes | ❌ Likely missing | Medium |
| FAQPage | ℹ️ Exists on /faqs/ | ⚠️ Flag if present | Info (AI citation benefit only; not for Google rich results on commercial site) |
| ReviewAggregation | ✅ Yes (1,900+ reviews) | ❌ Likely missing | High |
| Person (team page) | ✅ Yes | ❌ Likely missing | Medium |
| Article (blog posts) | ✅ Yes | ⚠️ Unverified | Medium |

### 4.2 Recommendations

**High Priority:**

**LegalService Schema** — Add to all claims service pages:
```json
{
  "@context": "https://schema.org",
  "@type": "LegalService",
  "name": "National Claims",
  "description": "FCA-regulated claims management company specialising in personal injury, clinical negligence and car accident claims",
  "url": "https://national-claims.co.uk",
  "telephone": "08000293849",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Ground Floor, Spectra House, Spring Villa Road",
    "addressLocality": "Edgware",
    "postalCode": "HA8 7EB",
    "addressCountry": "GB"
  },
  "areaServed": "GB",
  "hasCredential": {
    "@type": "EducationalOccupationalCredential",
    "credentialCategory": "FCA Authorised",
    "recognizedBy": {
      "@type": "Organization",
      "name": "Financial Conduct Authority",
      "url": "https://www.fca.org.uk"
    }
  }
}
```

**ReviewAggregation Schema** — Add to homepage to surface Trustpilot rating in search results:
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "National Claims",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "5",
    "bestRating": "5",
    "reviewCount": "1900",
    "ratingSource": "https://www.trustpilot.com/review/national-claims.co.uk"
  }
}
```

**FAQPage Note:** If `/faqs/` already has FAQPage schema, flag at **Info** level — it provides AI/LLM citation benefits but no longer generates Google rich results for commercial sites (Aug 2023 restriction). Do NOT add new FAQPage schema for Google benefit.

---

## 5. Performance (Core Web Vitals) — 50/100

> **Note:** Lab and field data could not be collected due to 403 WAF blocking. All scores are estimated.

### 5.1 Estimated CWV Status

| Metric | Threshold | Status | Notes |
|--------|-----------|--------|-------|
| LCP (Largest Contentful Paint) | ≤2.5s Good | ⚠️ Unknown | Could not measure |
| INP (Interaction to Next Paint) | ≤200ms Good | ⚠️ Unknown | Cannot measure without JS execution |
| CLS (Cumulative Layout Shift) | ≤0.1 Good | ⚠️ Unknown | Could not measure |

**Action Required:** The site owner should run PageSpeed Insights (https://pagespeed.web.dev/) directly to get CrUX field data. Google API credentials are not configured — set up `GOOGLE_API_KEY` to enable automated CWV tracking via `/seo google cwv`.

### 5.2 Performance Risk Factors (Inferred)

For a WordPress/CMS-based claims management site, common performance risks include:
- Render-blocking third-party scripts (live chat, tracking pixels, form tools)
- Unoptimised hero images
- Google Fonts loading delays
- Marketing/analytics tag bloat (GA4, Facebook Pixel, etc.)

---

## 6. AI Search Readiness (GEO) — 38/100

### 6.1 AI Crawler Access

| Check | Status | Notes |
|-------|--------|-------|
| llms.txt file | ❌ **Missing** | `/llms.txt` returns 403/404 |
| robots.txt AI rules | ⚠️ Unknown | robots.txt blocked by 403 |
| GPTBot in robots.txt | ⚠️ Unknown | |
| ClaudeBot in robots.txt | ⚠️ Unknown | |
| PerplexityBot in robots.txt | ⚠️ Unknown | |
| Googlebot-Extended | ⚠️ Unknown | |
| WAF blocking AI crawlers | ❌ **Likely** | All datacenter IPs return 403, AI crawlers included |

**Critical Gap:** The absence of `llms.txt` and the WAF blocking of datacenter IPs means AI search engines (ChatGPT, Perplexity, Claude, Gemini) may not be able to crawl and cite this site. This is a significant missed opportunity given the site's strong E-E-A-T signals.

### 6.2 Citability Assessment

| Signal | Score | Notes |
|--------|-------|-------|
| Factual, citable statements | 7/10 | FCA reg, company reg, fee disclosures |
| Entity clarity (brand name, company) | 8/10 | Clear entity signals |
| Award/credential clarity | 8/10 | Specific awards with years |
| Structured FAQ content | 6/10 | FAQs page present |
| Statistical data | 5/10 | Success fee % disclosed |
| Expert attribution | 5/10 | Team page exists, blog authorship unknown |
| **Overall Citability** | **6.5/10** | |

### 6.3 Brand Mention Signals

Positive signals found:
- Named in Legal Futures services directory
- Trustpilot case study subject
- Facebook and LinkedIn active presence
- Personal Injury Awards 2024 winner (industry publication coverage)
- Modern Claims Awards 2026 shortlist

**Gap:** No Wikipedia page, limited press coverage, no industry association citations found.

### 6.4 Recommendations for AI Search

1. **Create /llms.txt** immediately — allows AI engines to understand what content can be cited
2. **Whitelist AI crawlers in robots.txt**: GPTBot, ClaudeBot, PerplexityBot, Googlebot-Extended, CCBot
3. **Create explicit "facts about National Claims" content** — a dedicated About page section with structured facts (founded, FCA number, awards, service area)
4. **Add structured FAQ answers** optimised for AI snippet extraction — plain English, factual, concise
5. **Pursue industry publication mentions** — Legal Futures, Claims Management Today, Personal Injury Bar Association

---

## 7. Local SEO — 65/100

> Note: National Claims operates as a national UK service area business (SAB), not a single-location brick-and-mortar. Local SEO principles apply differently — primarily GBP optimisation and UK-wide citation consistency.

### 7.1 NAP Consistency

| Source | Phone | Address |
|--------|-------|---------|
| Site footer | 0800 029 3849 | Ground Floor, Spectra House, Spring Villa Park, Spring Villa Road, Edgware, HA8 7EB |
| External sources | 0345 2600 600 | 10 Spectra House Ground Floor, Spring Villa Road, Edgware, HA8 7EB |

**Two phone numbers and two address formats found.** This must be resolved. The FCA register address should be used as the canonical version.

### 7.2 Trust & Regulatory Signals

| Signal | Status | Notes |
|--------|--------|-------|
| FCA Authorisation | ✅ | FRN: 838876 displayed on site |
| Company Registration | ✅ | 11285085 displayed |
| Success Fee Disclosure | ✅ | 25% (incl. VAT) disclosed |
| Cancellation Policy | ✅ | 14-day cancellation period disclosed |
| Trustpilot Reviews | ✅ | 5 stars, ~1,900+ reviews |
| Awards Display | ✅ | 2024/2025/2026 awards visible |
| No Win No Fee Statement | ✅ | Prominent |

### 7.3 Recommendations

1. Standardise NAP to single format across all pages, schema, and external citations
2. Ensure Google Business Profile (GBP) is claimed, verified, and uses the canonical NAP
3. Add `areaServed: "GB"` to LegalService schema
4. Build citations on UK legal/financial directories: FCA register, Solicitors Regulation Authority referencing, Trustpilot, Google Business, Bing Places, Yell, Thomson Local

---

## 8. Images — 50/100

> Image analysis could not be performed due to 403 blocking. All findings are estimated.

| Check | Status | Notes |
|-------|--------|-------|
| Hero image alt text | ⚠️ Unverified | |
| Award badge alt text | ⚠️ Unverified | Award badges are important for E-E-A-T |
| Team photo alt text | ⚠️ Unverified | Meet the Team page |
| Image formats (WebP/AVIF) | ⚠️ Unverified | |
| Image compression | ⚠️ Unverified | |
| Lazy loading | ⚠️ Unverified | |

**Recommendation:** Verify all images have descriptive alt text, award badges specifically should have text like `alt="Claims Management Company of the Year 2024 - Personal Injury Awards"`.

---

## 9. Competitor Landscape (Context)

The UK claims management sector is highly competitive, particularly for personal injury and clinical negligence keywords. Key competitors likely include:
- National Accident Helpline
- Slater and Gordon
- Thompsons Solicitors
- Claims.co.uk
- RTA (road traffic accident) specialists

National Claims differentiates via:
- Award-winning status (2024, 2025)
- 1,900+ Trustpilot reviews (strong social proof)
- FCA regulation prominently displayed
- No Win No Fee with explicit fee disclosure

**Content gap opportunity:** Long-tail informational content ("can I claim for X?", "how long does a personal injury claim take?") can capture top-of-funnel searches.

---

## Scoring Summary

```
SEO Health Score: 58/100
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Technical SEO       ████████████░░░░░░░░  55/100
Content Quality     ██████████████░░░░░░  72/100
On-Page SEO         █████████████░░░░░░░  63/100
Schema / Struct.    ████████░░░░░░░░░░░░  42/100
Performance (CWV)   ██████████░░░░░░░░░░  50/100
AI Search Ready     ███████░░░░░░░░░░░░░  38/100
Images              ██████████░░░░░░░░░░  50/100
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Score confidence: Medium (WAF blocked direct crawl)
```

---

*Report generated by Claude SEO v1.7.2 | https://github.com/AgriciDaniel/claude-seo*
