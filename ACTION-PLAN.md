# SEO Action Plan — national-claims.co.uk
**Generated:** 2 April 2026  
**Overall Health Score: 58/100**  
**Business Type:** UK Claims Management Company (FCA Regulated)

---

## Priority Legend
- 🔴 **Critical** — Blocks indexing or causes penalties. Fix immediately.
- 🟠 **High** — Significantly impacts rankings. Fix within 1 week.
- 🟡 **Medium** — Optimisation opportunity. Fix within 1 month.
- 🟢 **Low** — Nice to have. Backlog.

---

## 🔴 Critical Issues (Fix Immediately)

### C1 — Resolve WAF/Cloudflare Blocking of Legitimate Crawlers
**Category:** Technical SEO  
**Impact:** All SEO audit tools blocked; AI search crawlers likely blocked; risk to non-Googlebot bots

**Actions:**
1. Review Cloudflare (or WAF provider) bot management rules
2. Whitelist the following User-Agents:
   - `GPTBot` (OpenAI/ChatGPT)
   - `ClaudeBot` / `anthropic-ai` (Anthropic)
   - `PerplexityBot` (Perplexity)
   - `Googlebot-Extended` (Google AI Overviews)
   - `CCBot` (Common Crawl)
   - `Bingbot` (Bing)
   - `AhrefsBot`, `SemrushBot`, `Screaming Frog` (optional)
3. Add corresponding `Allow` directives in robots.txt for these User-Agents
4. Test with `curl -A "Googlebot"` and SEO tool user-agents to confirm access

**Effort:** 2 hours (DevOps/hosting)

---

### C2 — Fix NAP Inconsistency (Phone Number + Address)
**Category:** Local SEO / Technical  
**Impact:** Confuses Google's entity understanding; damages local citation authority; potential compliance issue for FCA-regulated firm

**Actions:**
1. Decide canonical phone number (0800 029 3849 OR 0345 2600 600 — confirm with business)
2. Decide canonical address format — use exactly as shown on FCA register
3. Update **all on-site instances**: footer, contact page, schema markup, About page
4. Update **all off-site citations**: Google Business Profile, Bing Places, Trustpilot, Yell, Companies House listing, Legal Futures directory, LinkedIn, Facebook
5. Set up monthly NAP consistency monitoring (Moz Local, BrightLocal, or manual)

**Effort:** 3–4 hours (admin + outreach)

---

### C3 — Investigate and Resolve gb.national-claims.co.uk Subdomain
**Category:** Technical SEO  
**Impact:** Potential duplicate content index, diluted link equity, confused brand signals

**Actions:**
1. Check what content `gb.national-claims.co.uk` serves — is it identical to main domain?
2. If duplicate/same content: implement **301 redirect** from all `gb.` URLs to `national-claims.co.uk` equivalents
3. If different content (geo-targeting): add `rel="canonical"` pointing to main domain + hreflang if needed
4. Submit disavow or request removal of indexed `gb.` URLs from Google Search Console after redirect

**Effort:** 2–3 hours (DevOps + GSC)

---

## 🟠 High Priority (Fix Within 1 Week)

### H1 — Create /llms.txt for AI Search Engines
**Category:** AI Search Readiness  
**Impact:** Without llms.txt, AI engines (ChatGPT, Perplexity, Claude) cannot understand which pages to index and cite

**Actions:**
1. Create `https://national-claims.co.uk/llms.txt` with the following structure:
```
# National Claims — llms.txt
# FCA-regulated claims management company

> National Claims (Finance Advice Helpline Limited) is an FCA-authorised claims management company (FRN: 838876) helping UK residents make personal injury, clinical negligence and car accident compensation claims on a No Win No Fee basis.

## Key Pages

- [Homepage](https://national-claims.co.uk/)
- [Personal Injury Claims](https://national-claims.co.uk/personal-injury-claims/)
- [Car Accident Claims](https://national-claims.co.uk/car-accident-claims/)
- [Clinical Negligence Claims](https://national-claims.co.uk/clinical-negligence-claims/)
- [How Claims Work](https://national-claims.co.uk/claim-process/)
- [About National Claims](https://national-claims.co.uk/about-us/)
- [FAQs](https://national-claims.co.uk/faqs/)

## About
National Claims is authorised and regulated by the Financial Conduct Authority (FRN: 838876). 
Winner: Claims Management Company of the Year 2024 (Personal Injury Awards).
5-star Trustpilot rating with 1,900+ verified reviews.
No Win No Fee — customers pay up to 25% (incl. VAT) of recovered amount.
```
2. Ensure AI crawlers can fetch this file (not blocked by WAF)
3. Reference in robots.txt: `# llms.txt: https://national-claims.co.uk/llms.txt`

**Effort:** 1 hour

---

### H2 — Add LegalService Schema to Service Pages
**Category:** Schema / Structured Data  
**Impact:** Rich results eligibility; improved Google entity understanding; better AI citation

**Actions:**
1. Add `LegalService` schema to each service page (personal injury, car accident, clinical negligence):
```json
{
  "@context": "https://schema.org",
  "@type": "LegalService",
  "name": "National Claims",
  "description": "[Page-specific description]",
  "url": "[Page URL]",
  "telephone": "08000293849",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Ground Floor, Spectra House, Spring Villa Road",
    "addressLocality": "Edgware",
    "postalCode": "HA8 7EB",
    "addressCountry": "GB"
  },
  "areaServed": {
    "@type": "Country",
    "name": "United Kingdom"
  },
  "serviceType": "[e.g. Personal Injury Claims]",
  "hasCredential": {
    "@type": "EducationalOccupationalCredential",
    "name": "FCA Authorisation",
    "recognizedBy": {
      "@type": "Organization",
      "name": "Financial Conduct Authority"
    }
  }
}
```
2. Validate with Google's Rich Results Test after implementation
3. Add `offers` property with "No Win No Fee" details if schema validation passes

**Effort:** 3–4 hours (developer)

---

### H3 — Add ReviewAggregation Schema (Trustpilot)
**Category:** Schema / Structured Data  
**Impact:** May enable star ratings in SERP snippets; boosts click-through rate

**Actions:**
1. Add `aggregateRating` to Organization/LegalService schema on homepage:
```json
"aggregateRating": {
  "@type": "AggregateRating",
  "ratingValue": "5.0",
  "bestRating": "5",
  "worstRating": "1",
  "reviewCount": "1900",
  "url": "https://www.trustpilot.com/review/national-claims.co.uk"
}
```
2. Keep review count updated (script or manual quarterly update)
3. Note: Google's policy requires reviews to be genuine customer reviews — Trustpilot qualifies

**Effort:** 1–2 hours

---

### H4 — Fix Weak Title Tags on Inner Pages
**Category:** On-Page SEO  
**Impact:** Higher click-through rates from search results

**Pages to fix:**
| Current Title | Recommended Title |
|---------------|-------------------|
| About Us - National Claims | Award-Winning Claims Management Company \| About National Claims |
| FAQs - National Claims | Personal Injury Claims FAQs \| National Claims |
| Contact the team - National Claims | Contact National Claims \| Free Advice: 0800 029 3849 |

**General template:** `[Primary Keyword] \| National Claims — Claims Management Company of the Year`

**Effort:** 1 hour (CMS/content team)

---

### H5 — Verify and Fix robots.txt and Sitemap
**Category:** Technical SEO  
**Impact:** Ensure proper crawl management and sitemap submission

**Actions:**
1. Verify robots.txt is publicly accessible (fix if WAF is blocking)
2. Ensure robots.txt declares sitemap: `Sitemap: https://national-claims.co.uk/sitemap.xml`
3. Verify sitemap.xml is accessible and includes all key pages
4. Submit sitemap to Google Search Console and Bing Webmaster Tools
5. Ensure sitemap includes all service pages, blog posts, and key landing pages
6. Exclude: thank-you pages, admin pages, duplicate/paginated URLs

**Effort:** 2 hours

---

### H6 — Build a Mis-Sold Car Finance Pillar/Service Page (Added 15 Jun 2026)
**Category:** Content Quality / On-Page SEO  
**Impact:** Consolidates the existing car-finance blog cluster into a single authoritative hub; captures surging 2026 motor-finance redress search demand; concentrates internal link equity

**Context:** National Claims has published a large blog cluster on mis-sold car/vehicle finance but appears to lack a canonical service/pillar page. Blog-only coverage scatters authority and competes against itself.

**Actions:**
1. Create `/mis-sold-car-finance-claims/` (or similar) as the canonical pillar page
2. Target primary keywords: "mis-sold car finance claim", "car finance compensation", "PCP/HP commission claim"
3. Internally link every car-finance blog post up to this pillar, and from the pillar down to key posts (hub-and-spoke)
4. Add `Service` or `FinancialService` schema (separate from the personal-injury `LegalService`)
5. Include: eligibility (PCP/HP 2007–2024), FCA redress-scheme timeline, No Win No Fee fee disclosure, "Start My Claim" CTA
6. Set canonical to the pillar; ensure blog posts canonical to themselves but link clearly to the hub

**Effort:** 1 day (content + developer)

---

### H7 — FCA-Compliant Disclaimers + Sourced Figures on Car-Finance Content (Added 15 Jun 2026)
**Category:** Content Quality / E-E-A-T / Compliance  
**Impact:** Mis-sold car finance is money-YMYL content for an FCA-authorised CMC — accuracy and compliance are ranking-critical AND regulatory-critical. The motor-finance CMC sector is under active FCA scrutiny in 2026.

**Actions:**
1. Source every payout/eligibility figure to a citable authority (FCA, FOS, court rulings) — no unsubstantiated "£X payout" claims
2. Add visible "Last updated: [date]" to every time-sensitive post and `dateModified` to Article schema
3. Add a clear fee disclosure (up to 25% incl. VAT) and risk/no-guarantee disclaimer on car-finance pages, consistent with CMC financial-promotion rules
4. Add author attribution with relevant credentials (ties to M2) — essential for financial YMYL
5. Establish a quarterly review cadence to refresh decayed timelines and figures

**Effort:** 4–6 hours initial + ongoing quarterly review

---

## 🟡 Medium Priority (Fix Within 1 Month)

### M1 — Add Missing Service Pages
**Category:** Content Quality  
**Impact:** Capture long-tail organic traffic for additional claim types

**Update (15 Jun 2026):** Housing disrepair and mis-sold vehicle finance are now confirmed live offerings (currently covered mainly via blog content). Prioritise dedicated service/pillar pages over blog-only coverage — see H6 for the car-finance pillar.

**Missing pages to create (based on services offered):**
- `/housing-disrepair-claims/` ← now an active service line; prioritise
- `/injury-at-work-claims/`
- `/slip-trip-fall-claims/`
- `/birth-injury-claims/`
- `/defective-product-claims/`

**Each page needs:**
- Minimum 800 words of original content
- Unique H1 targeting primary keyword
- Process explanation (How to claim, time limits, evidence needed)
- E-E-A-T signals (FCA reg, panel solicitors, success stats)
- FAQ section (for AI citation, not Google rich results)
- Clear CTA to "Start My Claim"
- Internal links to Claim Process page and related services

**Effort:** 2–3 hours per page (content writer)

---

### M2 — Add Author Attribution to Blog Posts
**Category:** Content Quality / E-E-A-T  
**Impact:** Critical for YMYL content (legal/financial/medical). Google's QRG explicitly requires author credentials on health/legal/financial content.

**Actions:**
1. Add author bio box to all blog posts with: name, role/title, credentials/qualifications
2. Link author name to author page (e.g., `/author/john-smith/`)
3. Add `Article` or `BlogPosting` schema with `author` property to each post:
```json
"author": {
  "@type": "Person",
  "name": "Author Name",
  "jobTitle": "Claims Specialist",
  "url": "https://national-claims.co.uk/author/author-name/"
}
```
4. For clinical negligence content specifically — add medical expert review attribution

**Effort:** 2 hours (developer + content team)

---

### M3 — Improve Meta Descriptions
**Category:** On-Page SEO  
**Impact:** Higher CTR from SERPs; not a direct ranking factor but influences traffic

**Guidelines:**
- Length: 140–160 characters
- Include primary keyword
- Include a CTA ("Start your claim today", "Free advice available")
- Mention key USP (No Win No Fee, FCA regulated, award-winning)
- Unique for every page

**Example for homepage:**
> "National Claims — FCA-regulated, award-winning claims management company. Personal injury, car accidents, clinical negligence. No Win No Fee. Call 0800 029 3849."

**Effort:** 2 hours (content team)

---

### M4 — Add BreadcrumbList Schema
**Category:** Schema / Structured Data  
**Impact:** Breadcrumb display in search results, improved crawl path understanding

**Actions:**
1. Implement `BreadcrumbList` schema on all inner pages:
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://national-claims.co.uk/"},
    {"@type": "ListItem", "position": 2, "name": "Personal Injury Claims", "item": "https://national-claims.co.uk/personal-injury-claims/"}
  ]
}
```
2. Ensure breadcrumb navigation is also present in HTML (not just schema)

**Effort:** 2–3 hours (developer)

---

### M5 — Add Person Schema to Meet the Team Page
**Category:** Schema / E-E-A-T  
**Impact:** Entity recognition for team members; E-E-A-T signal for Google

**Actions:**
1. Add `Person` schema for each named team member:
```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Team Member Name",
  "jobTitle": "Role Title",
  "worksFor": {"@type": "Organization", "name": "National Claims"},
  "url": "https://national-claims.co.uk/meet-the-team/"
}
```

**Effort:** 1–2 hours

---

### M6 — Create Informational Blog Content Strategy
**Category:** Content Quality  
**Impact:** Top-of-funnel organic traffic; AI citation opportunities; E-E-A-T signals

**Recommended content topics:**
1. "How long do personal injury claims take in the UK?"
2. "What evidence do I need for a car accident claim?"
3. "Clinical negligence vs medical error: what's the difference?"
4. "UK personal injury compensation calculator: what am I entitled to?"
5. "Time limits for making a personal injury claim in the UK"
6. "Housing disrepair: your rights as a tenant in 2026"

**Each post should:**
- Target a specific keyword with search intent
- Be 1,000+ words with factual, citable content
- Include an expert review byline
- Link to relevant service pages (internal linking)

**Effort:** 3–4 hours per article

---

### M7 — Verify and Optimise Open Graph Tags
**Category:** On-Page SEO / Social  
**Impact:** Better social sharing appearance on LinkedIn/Facebook (company is active on both)

**Actions:**
1. Verify all key pages have: `og:title`, `og:description`, `og:image` (1200×630px), `og:type`
2. Ensure award badge or professional image is set as OG image for homepage
3. Add `twitter:card`, `twitter:title`, `twitter:description` tags
4. Test with Facebook Debugger and LinkedIn Post Inspector

**Effort:** 2 hours

---

### M8 — Measure and Optimise Core Web Vitals
**Category:** Performance  
**Impact:** Google CWV is a page experience ranking signal

**Actions:**
1. Run PageSpeed Insights on homepage and 3 service pages
2. Target: LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1
3. Common fixes for claims/legal sites:
   - Defer non-critical JS (chat widgets, analytics)
   - Optimise hero image (WebP format, preload LCP image)
   - Lazy load below-fold images
   - Minimise CSS blocking render
4. Configure Google API key for automated CWV tracking: set `GOOGLE_API_KEY` env variable

**Effort:** 4–8 hours (developer)

---

## 🟢 Low Priority (Backlog)

### L1 — Add Award Schema (ItemList / Achievement)
Add schema markup for each award to reinforce brand authority signals.

### L2 — Create Wikipedia / Wikidata Entry
Build entity presence for the brand. Requires notability criteria — existing press coverage from Personal Injury Awards, Legal Futures, Modern Claims Awards should qualify.

### L3 — Pursue Industry Publication Mentions
Target: Claims Management Today, Legal Futures, Personal Injury Bar Association, FCA Insight, Trustpilot blog (they are already a case study).

### L4 — Implement Hreflang (If Expanding)
Currently UK-only. If expanding to Ireland or international, implement hreflang. Note: `gb.national-claims.co.uk` subdomain may indicate existing geo-targeting — investigate.

### L5 — Video Content for YouTube / Schema
How-to claim videos can target visual search and YouTube SEO. Add `VideoObject` schema if implemented.

### L6 — Image Alt Text Audit
Once WAF allows crawl access, run full image alt text audit to ensure all images have descriptive alt attributes.

---

## Implementation Roadmap

### Week 1 (Critical + Quick Wins)
- [ ] Fix WAF rules to allow legitimate crawlers (C1)
- [ ] Standardise NAP — choose canonical phone + address (C2)
- [ ] Create /llms.txt file (H1)
- [ ] Investigate and redirect gb.national-claims.co.uk (C3)

### Week 2 (High Priority Schema + Technical)
- [ ] Add LegalService schema to all service pages (H2)
- [ ] Add ReviewAggregation schema (H3) — update reviewCount to ~1,908
- [ ] Fix weak title tags (H4)
- [ ] Verify robots.txt + sitemap accessibility (H5)
- [ ] Build mis-sold car finance pillar/service page + internal linking (H6)
- [ ] Add FCA-compliant disclaimers + sourced figures to car-finance content (H7)

### Weeks 3–4 (Content + On-Page)
- [ ] Fix meta descriptions across all pages (M3)
- [ ] Add author attribution to blog posts (M2)
- [ ] Add BreadcrumbList schema (M4)
- [ ] Verify/fix Open Graph tags (M7)
- [ ] Run PageSpeed Insights and address CWV issues (M8)

### Month 2 (Content Expansion)
- [ ] Create 2–3 missing service pages (M1)
- [ ] Publish 3 informational blog posts (M6)
- [ ] Add Person schema to team page (M5)

### Quarter 2 (Authority Building)
- [ ] Industry publication outreach (L3)
- [ ] Wikipedia/Wikidata entity creation (L2)
- [ ] YouTube video content (L5)

---

## Expected Score Impact After Full Implementation

| Category | Current | Target |
|----------|---------|--------|
| Technical SEO | 55 | 80 |
| Content Quality | 72 | 82 |
| On-Page SEO | 63 | 80 |
| Schema / Structured Data | 42 | 78 |
| Performance (CWV) | 50 | 72 |
| AI Search Readiness | 38 | 75 |
| Images | 50 | 70 |
| **Overall** | **58** | **79** |

---

*Action Plan generated by Claude SEO v1.7.2 | https://github.com/AgriciDaniel/claude-seo*
