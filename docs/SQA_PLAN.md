# Software Quality Assurance Plan — Danish Shakil Portfolio

> **Document ID:** SQA-DS-001  
> **Version:** 1.0.0  
> **Standard:** IEEE 730-2014 (Software Quality Assurance Plans)  
> **Supplementary:** ISO/IEC 25010:2023, WCAG 2.1 AA, ISO 9241-110:2020  
> **Last Updated:** 2026-09-23

---

## 1. Purpose

This SQA Plan establishes the quality assurance activities, standards, and acceptance criteria for the Danish Shakil Portfolio Website project. It ensures the delivered product meets functional, performance, accessibility, security, and maintainability requirements as defined in the Architecture Document (ARCH-DS-001) and Design System (DS-DS-001).

---

## 2. Scope

### 2.1 In Scope
- Single-page portfolio website (`index.html`)
- CSS design system (`css/style.css`, `css/animations.css`)
- JavaScript interactions (`js/main.js`, `js/animations.js`, `js/form.js`)
- Static assets (images, documents, favicon)
- GitHub Actions deployment pipeline
- SEO metadata and structured data

### 2.2 Out of Scope
- Backend services (none exist)
- User authentication (none required)
- Database operations (none exist)
- Third-party API internals (Web3Forms, Google Fonts)

---

## 3. Referenced Standards

| Standard | Title | Application |
|----------|-------|-------------|
| **IEEE 730-2014** | Software Quality Assurance Plans | This document structure |
| **ISO/IEC 25010:2023** | Systems & Software Quality Requirements (SQuaRE) | Quality attribute framework |
| **ISO 9241-110:2020** | Ergonomics — Interaction Principles | Usability evaluation |
| **WCAG 2.1 Level AA** | Web Content Accessibility Guidelines | Accessibility requirements |
| **ISO/IEC 25023** | Measurement of Quality Properties | Metrics definition |
| **W3C HTML5 Spec** | HTML Living Standard | Markup validation |
| **W3C CSS Level 3** | CSS Specifications | Stylesheet validation |

---

## 4. Quality Objectives

| ID | Objective | Target | Measurement Method |
|----|-----------|--------|-------------------|
| QO-01 | **Zero HTML validation errors** | 0 errors, 0 warnings | W3C Markup Validator |
| QO-02 | **Zero CSS validation errors** | 0 errors | W3C CSS Validator |
| QO-03 | **Lighthouse Performance ≥ 95** | Score ≥ 95 | Lighthouse CI |
| QO-04 | **Lighthouse Accessibility ≥ 95** | Score ≥ 95 | Lighthouse CI |
| QO-05 | **Lighthouse SEO ≥ 95** | Score ≥ 95 | Lighthouse CI |
| QO-06 | **Lighthouse Best Practices ≥ 95** | Score ≥ 95 | Lighthouse CI |
| QO-07 | **First Contentful Paint < 1.5s** | < 1500ms | Lighthouse/WebPageTest |
| QO-08 | **Largest Contentful Paint < 2.5s** | < 2500ms | Lighthouse/WebPageTest |
| QO-09 | **Cumulative Layout Shift < 0.1** | < 0.10 | Lighthouse/WebPageTest |
| QO-10 | **Total page weight < 1.5MB** | < 1536KB | Network DevTools |
| QO-11 | **Cross-browser consistency** | Pixel-consistent | Visual comparison |
| QO-12 | **WCAG 2.1 AA compliance** | 0 violations | axe DevTools |
| QO-13 | **Contact form functional** | 100% delivery | Manual test |
| QO-14 | **Responsive 320px–2560px** | No overflow/broken | Chrome DevTools |
| QO-15 | **All links functional** | 0 broken links | Dead link checker |

---

## 5. Quality Assurance Activities

### 5.1 Activity Matrix

| Phase | Activity | Owner | Deliverable |
|-------|----------|-------|-------------|
| **Pre-Development** | Requirements review | Architect (Claude) | Approved Implementation Plan |
| **Pre-Development** | Design system review | Architect (Claude) | Approved Design System Doc |
| **Development** | Code review per section | Developer (Gemini) | Clean, semantic code |
| **Development** | Progressive testing | Developer (Gemini) | Test results per section |
| **Post-Development** | Validation suite | Developer (Gemini) | Validation report |
| **Post-Development** | Cross-browser testing | Developer (Gemini) | Browser compatibility report |
| **Post-Development** | Performance audit | Developer (Gemini) | Lighthouse report |
| **Post-Development** | Accessibility audit | Developer (Gemini) | axe DevTools report |
| **Deployment** | Smoke test | User (Danish) | Deployment verification |

### 5.2 Testing Types

#### A. Static Analysis (Automated)

| Test | Tool | Command | Pass Criteria |
|------|------|---------|---------------|
| HTML Validation | W3C Validator | `npx html-validate index.html` | 0 errors |
| CSS Validation | W3C CSS Validator | Online validator | 0 errors |
| JS Lint | ESLint (browser rules) | `npx eslint js/` | 0 errors, 0 warnings |
| Accessibility | axe-core | Browser extension or `npx @axe-core/cli` | 0 critical/serious |
| Link Check | broken-link-checker | `npx broken-link-checker` | 0 broken links |

#### B. Performance Testing

| Metric | Tool | Target | Measurement |
|--------|------|--------|-------------|
| Performance Score | Lighthouse | ≥ 95 | Automated CI |
| FCP | Lighthouse | < 1.5s | Automated |
| LCP | Lighthouse | < 2.5s | Automated |
| CLS | Lighthouse | < 0.1 | Automated |
| TBT | Lighthouse | < 200ms | Automated |
| Speed Index | Lighthouse | < 3.4s | Automated |
| Page Weight | DevTools Network | < 1.5MB | Manual check |
| Image Optimization | Lighthouse | All WebP, lazy loaded | Automated |

#### C. Cross-Browser Testing

| Browser | Version | Platform | Priority | Test Method |
|---------|---------|----------|----------|-------------|
| Chrome | Latest 2 | Windows/macOS | P0 | Manual + Visual |
| Firefox | Latest 2 | Windows/macOS | P0 | Manual + Visual |
| Safari | Latest 2 | macOS/iOS | P1 | Manual + Visual |
| Edge | Latest 2 | Windows | P1 | Manual + Visual |
| Chrome Mobile | Latest | Android | P0 | DevTools Emulation |
| Safari Mobile | Latest | iOS | P0 | DevTools Emulation |

**Test Points per Browser:**
1. Page loads correctly (no console errors)
2. Navigation smooth scroll works
3. Mobile menu opens/closes
4. Animations play correctly
5. Cards hover effect works
6. Contact form submits
7. Images load (including lazy-loaded)
8. Fonts render correctly
9. Grid overlay displays
10. Stats counter animates

#### D. Responsive Design Testing

| Viewport | Width | Device Emulation | Key Checks |
|----------|-------|-------------------|------------|
| Mobile S | 320px | iPhone SE | No text overflow, readable fonts |
| Mobile M | 375px | iPhone 12 | Proper stacking, touch targets ≥ 44px |
| Mobile L | 428px | iPhone 14 Pro Max | Image scaling, form usability |
| Tablet P | 768px | iPad | 2-column layouts, spacing |
| Tablet L | 1024px | iPad Pro Landscape | Desktop nav visible, grid switch |
| Laptop | 1280px | — | Full desktop layout |
| Desktop | 1536px | — | Max-width container activates |
| Ultrawide | 2560px | — | Content centered, no stretching |

#### E. Accessibility Testing (WCAG 2.1 AA)

| Criterion | WCAG ID | Test Method | Pass Criteria |
|-----------|---------|-------------|---------------|
| Non-text content | 1.1.1 | Manual | All `<img>` have descriptive `alt` |
| Info and relationships | 1.3.1 | axe | Semantic HTML, proper headings |
| Meaningful sequence | 1.3.2 | Manual | DOM order matches visual order |
| Color contrast | 1.4.3 | axe | ≥ 4.5:1 normal, ≥ 3:1 large |
| Resize text | 1.4.4 | Manual | Page usable at 200% zoom |
| Keyboard | 2.1.1 | Manual | All interactive elements focusable |
| No keyboard trap | 2.1.2 | Manual | Modal escapable via Escape key |
| Page titled | 2.4.2 | axe | `<title>` is descriptive |
| Focus order | 2.4.3 | Manual | Tab order is logical |
| Link purpose | 2.4.4 | axe | Links have clear text or aria-label |
| Headings and labels | 2.4.6 | axe | Headings are descriptive |
| Focus visible | 2.4.7 | Manual | Focus ring visible on all elements |
| Language of page | 3.1.1 | axe | `lang="en"` on `<html>` |
| On focus | 3.2.1 | Manual | No unexpected context changes |
| Error identification | 3.3.1 | Manual | Form errors identified clearly |
| Labels | 3.3.2 | axe | All inputs have labels |
| Parsing | 4.1.1 | W3C Validator | Valid HTML |
| Name, role, value | 4.1.2 | axe | ARIA attributes correct |

#### F. Functional Testing

| Feature | Test Case | Expected Result |
|---------|-----------|-----------------|
| **Navigation** | Click each nav link | Smooth scroll to correct section |
| **Navigation** | Click logo/name | Scroll to top |
| **Mobile Menu** | Click hamburger | Drawer opens from right |
| **Mobile Menu** | Click X or outside | Drawer closes |
| **Mobile Menu** | Click nav link | Scroll to section + close drawer |
| **Hero Typing** | Wait 10 seconds | Text cycles through 4 phrases |
| **Stats Counter** | Scroll to stats section | Numbers animate from 0 to target |
| **Project Cards** | Hover over card | Card lifts, border highlights |
| **Project Cards** | Click "View Details" | Modal opens with full details |
| **Project Modal** | Click X or overlay | Modal closes |
| **Project Modal** | Press Escape | Modal closes |
| **Timeline** | Scroll through timeline | Cards fade in on scroll |
| **Skills Marquee** | Observe marquee | Logos scroll continuously |
| **Contact Form** | Submit with valid data | Success toast, form resets |
| **Contact Form** | Submit empty form | Validation errors shown |
| **Contact Form** | Submit invalid email | Email validation error |
| **Resume Download** | Click "Resume" button | PDF downloads |
| **Back to Top** | Scroll down, click arrow | Smooth scroll to top |
| **Social Links** | Click GitHub/LinkedIn | Opens in new tab |
| **Reduced Motion** | Enable prefers-reduced-motion | All animations disabled |

#### G. Security Testing

| Test | Method | Pass Criteria |
|------|--------|---------------|
| XSS injection in form | Manual: enter `<script>` in inputs | Form input is sent to API, not rendered on page |
| CSP header | Browser DevTools console | No CSP violations |
| HTTPS enforcement | Navigate to HTTP URL | Redirected to HTTPS |
| External links | Manual check | All external links have `rel="noopener noreferrer"` |
| Mixed content | Lighthouse | No mixed content warnings |
| Console errors | DevTools Console | 0 errors in production |

---

## 6. Defect Classification

### 6.1 Severity Levels

| Level | Name | Definition | Resolution |
|-------|------|------------|------------|
| **S1** | Critical | Site crashes, blank page, form doesn't submit | Must fix before deploy |
| **S2** | Major | Broken layout on a primary viewport, accessibility barrier | Must fix before deploy |
| **S3** | Minor | Visual inconsistency, animation glitch, minor spacing | Fix in next iteration |
| **S4** | Cosmetic | Pixel-level alignment, font rendering difference | Nice-to-have |

### 6.2 Priority Levels

| Priority | Name | Response Time |
|----------|------|---------------|
| **P0** | Blocker | Fix immediately |
| **P1** | High | Fix before deployment |
| **P2** | Medium | Fix in next sprint |
| **P3** | Low | Backlog |

---

## 7. Acceptance Criteria

### 7.1 Minimum Viable Quality Gate (Must Pass Before Deployment)

- [ ] HTML validates with 0 errors (W3C Validator)
- [ ] CSS validates with 0 errors (W3C CSS Validator)
- [ ] Lighthouse Performance ≥ 90 (target: 95)
- [ ] Lighthouse Accessibility ≥ 90 (target: 95)
- [ ] Lighthouse SEO ≥ 90 (target: 95)
- [ ] Lighthouse Best Practices ≥ 90 (target: 95)
- [ ] 0 critical/serious axe accessibility violations
- [ ] All 8 sections render correctly on Chrome (desktop + mobile)
- [ ] Contact form submits successfully to email
- [ ] Resume PDF downloads correctly
- [ ] No JavaScript console errors
- [ ] All images load (no broken images)
- [ ] Mobile hamburger menu works
- [ ] All navigation links scroll to correct sections

### 7.2 Enhanced Quality Gate (Nice-to-Have Before Deployment)

- [ ] Cross-browser tested on Firefox + Safari
- [ ] Tested on physical mobile device
- [ ] Lighthouse all scores ≥ 95
- [ ] 0 axe violations of any severity
- [ ] Print stylesheet clean
- [ ] `prefers-reduced-motion` verified
- [ ] OG image displays correctly on social platforms
- [ ] JSON-LD structured data validates (Google Rich Results Test)

---

## 8. Quality Metrics & Reporting

### 8.1 Key Quality Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| **Defect Density** | Total defects / Total components | < 0.5 per component |
| **First-Pass Yield** | Components passing on first test / Total components | > 80% |
| **Lighthouse Average** | (Perf + A11y + SEO + BP) / 4 | > 95 |
| **Validation Compliance** | Valid pages / Total pages | 100% |
| **Accessibility Compliance** | WCAG criteria met / Total criteria | 100% (AA level) |

### 8.2 Test Execution Report Template

```markdown
## Test Execution Report — [DATE]

### Summary
| Category | Total | Passed | Failed | Blocked |
|----------|-------|--------|--------|---------|
| Functional | 20 | X | X | 0 |
| Visual | 8 | X | X | 0 |
| Performance | 6 | X | X | 0 |
| Accessibility | 18 | X | X | 0 |
| Cross-Browser | 6 | X | X | 0 |

### Lighthouse Scores
| Metric | Score | Target | Status |
|--------|-------|--------|--------|
| Performance | XX | ≥ 95 | ✅/❌ |
| Accessibility | XX | ≥ 95 | ✅/❌ |
| Best Practices | XX | ≥ 95 | ✅/❌ |
| SEO | XX | ≥ 95 | ✅/❌ |

### Defects Found
| ID | Severity | Description | Status |
|----|----------|-------------|--------|
| DEF-001 | S2 | ... | Open/Fixed |

### Recommendation
[ ] PASS — Ready for deployment
[ ] CONDITIONAL PASS — Deploy after fixing S1/S2 defects
[ ] FAIL — Major rework required
```

---

## 9. Tools & Infrastructure

| Tool | Purpose | Version | License |
|------|---------|---------|---------|
| W3C Markup Validator | HTML validation | Online | Free |
| W3C CSS Validator | CSS validation | Online | Free |
| Lighthouse | Performance, A11y, SEO | Chrome built-in | Free |
| axe DevTools | Accessibility testing | Browser extension | Free |
| Chrome DevTools | Responsive testing, debugging | Chrome built-in | Free |
| broken-link-checker | Link integrity | npm package | MIT |
| html-validate | HTML best practices | npm package | MIT |
| Google Rich Results Test | Structured data validation | Online | Free |
| WebPageTest | Performance (multi-location) | Online | Free |

---

## 10. Roles & Responsibilities

| Role | Responsibility | Assigned To |
|------|---------------|-------------|
| **Quality Architect** | Define standards, create SQA plan, review architecture | Claude Opus (this session) |
| **Developer** | Implement code, run unit tests, fix defects | Gemini 3.1 Pro (next session) |
| **Quality Tester** | Execute test plan, report defects | Gemini 3.1 Pro (post-build) |
| **Product Owner** | Accept/reject deliverables, final sign-off | Danish Shakil (user) |

---

## 11. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-09-23 | Claude Opus (Architect) | Initial SQA Plan |
