# System Architecture Document — Danish Shakil Portfolio

> **Document ID:** ARCH-DS-001  
> **Version:** 1.0.0  
> **Standard:** ISO/IEC 25010:2023 (SQuaRE — Software Quality Requirements & Evaluation)  
> **Last Updated:** 2026-09-23

---

## 1. System Context

### 1.1 Purpose
A premium single-page portfolio website for Danish Shakil, a Mechanical Engineering student at GIK Institute. The site showcases professional CAD work, competition robotics projects, and academic research — deployed on GitHub Pages as a fully static site with zero runtime dependencies.

### 1.2 Stakeholders

| Stakeholder | Role | Concerns |
|-------------|------|----------|
| Danish Shakil | Owner / Subject | Content accuracy, visual appeal, recruitability |
| Recruiters / Hiring Managers | Primary audience | Fast load, clear project showcase, resume download |
| Academic contacts | Secondary audience | Research detail, certification verification |
| GitHub Pages | Hosting platform | Static files only, 100MB repo limit, no server-side code |

### 1.3 Constraints

| Constraint | Description |
|------------|-------------|
| **No Backend** | GitHub Pages serves static files only. No server-side processing, databases, or authentication. |
| **No Build Step** | Pure HTML/CSS/JS — no Node.js, no Webpack, no framework. Files served as-is. |
| **Repo Size** | GitHub Pages repositories limited to ~1GB; assets must be optimized. |
| **Bandwidth** | GitHub Pages soft limit of 100GB/month; images must be compressed. |
| **Custom Domain** | Supported via CNAME file, but DNS must be configured externally. |
| **HTTPS** | GitHub Pages provides free HTTPS via Let's Encrypt. Enforced by default. |

---

## 2. Architecture Overview

### 2.1 Deployment Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                        INTERNET                               │
├──────────┬──────────┬────────────┬───────────────────────────┤
│          │          │            │                             │
│  Browser │  Google  │ Web3Forms  │  Lucide Icons               │
│  (User)  │  Fonts   │ API        │  CDN                       │
│          │  CDN     │            │                             │
│    ▼     │    ▼     │     ▼      │      ▼                     │
│  ┌───────┴──────────┴────────────┴───────────────────────┐   │
│  │              GitHub Pages CDN (Fastly)                  │   │
│  │         https://username.github.io                      │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │  index.html ─┬── css/style.css                          │   │
│  │              ├── css/animations.css                      │   │
│  │              ├── js/main.js                              │   │
│  │              ├── js/animations.js                        │   │
│  │              ├── js/form.js                              │   │
│  │              ├── assets/images/**                        │   │
│  │              ├── assets/documents/Resume.pdf             │   │
│  │              └── assets/favicon/**                       │   │
│  └─────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────┘
```

### 2.2 Component Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        index.html                                │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │ <head>                                                     │   │
│  │ ├── Meta tags (SEO, OG, Twitter)                           │   │
│  │ ├── Google Fonts preconnect + stylesheet                    │   │
│  │ ├── css/style.css (design system + components)              │   │
│  │ ├── css/animations.css (keyframes)                          │   │
│  │ ├── Lucide Icons CDN                                        │   │
│  │ └── JSON-LD structured data                                 │   │
│  └───────────────────────────────────────────────────────────┘   │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │ <body>                                                     │   │
│  │ ├── Skip Link (accessibility)                               │   │
│  │ ├── <header> Navigation                                     │   │
│  │ │   ├── Logo / Name                                         │   │
│  │ │   ├── Nav Links (smooth scroll)                           │   │
│  │ │   ├── Resume CTA Button                                   │   │
│  │ │   └── Mobile Hamburger                                    │   │
│  │ ├── <main id="main-content">                                │   │
│  │ │   ├── <section id="hero">                                 │   │
│  │ │   │   ├── Title + Typing Animation                        │   │
│  │ │   │   ├── Profile Photo + Floating Badges                 │   │
│  │ │   │   └── CTA Buttons                                     │   │
│  │ │   ├── <section id="stats">                                │   │
│  │ │   │   └── Counter Strip (4 metrics)                       │   │
│  │ │   ├── <section id="projects">                             │   │
│  │ │   │   ├── Section Header                                   │   │
│  │ │   │   ├── Project Card Grid (3-col)                        │   │
│  │ │   │   └── Project Detail Modal (overlay)                   │   │
│  │ │   ├── <section id="experience">                           │   │
│  │ │   │   └── Vertical Timeline (alternating cards)            │   │
│  │ │   ├── <section id="skills">                               │   │
│  │ │   │   └── Marquee (dual-row, opposite direction)           │   │
│  │ │   ├── <section id="about">                                │   │
│  │ │   │   ├── Bio Text                                         │   │
│  │ │   │   ├── Education Card                                   │   │
│  │ │   │   └── Certifications Row                               │   │
│  │ │   └── <section id="contact">                              │   │
│  │ │       ├── Contact Info (email, phone, location)            │   │
│  │ │       └── Form (Web3Forms)                                 │   │
│  │ └── <footer>                                                 │   │
│  │     ├── Social Links                                         │   │
│  │     ├── Copyright                                            │   │
│  │     └── Back-to-top Button                                   │   │
│  └───────────────────────────────────────────────────────────┘   │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │ Scripts (deferred)                                         │   │
│  │ ├── js/main.js         (navigation, scroll, mobile menu)   │   │
│  │ ├── js/animations.js   (IntersectionObserver triggers)      │   │
│  │ └── js/form.js         (Web3Forms POST handler)             │   │
│  └───────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. Data Flow

### 3.1 Page Load Sequence

```
Browser Request
     │
     ▼
GitHub Pages CDN (Fastly)
     │ ─── Serves index.html (gzipped, ~15KB)
     │
     ├── Parallel CSS Loads ──► css/style.css (~12KB)
     │                         css/animations.css (~3KB)
     │
     ├── Preconnect ──► fonts.googleapis.com
     │                  fonts.gstatic.com
     │
     ├── Font Load ──► Space Grotesk (woff2, ~18KB)
     │                 DM Sans (woff2, ~20KB)
     │                 JetBrains Mono (woff2, ~15KB)
     │
     ├── Deferred JS ──► js/main.js (~8KB)
     │                   js/animations.js (~4KB)
     │                   js/form.js (~3KB)
     │
     ├── Lazy Images ──► Profile photo (above fold, eager)
     │                   Project renders (lazy, IntersectionObserver)
     │                   Tool logos (lazy, marquee section)
     │
     └── First Paint ──► Target: < 1.5s FCP
                          Target: < 2.5s LCP
```

### 3.2 Contact Form Data Flow

```
User fills form
     │
     ▼
Client-side validation (js/form.js)
     │ ─── Check: required fields, email regex, honeypot empty
     │
     ├── Validation Fail ──► Show inline error messages
     │                        Focus first invalid field
     │
     ├── Validation Pass ──► Show loading spinner on button
     │
     ▼
POST to Web3Forms API
     │ ─── https://api.web3forms.com/submit
     │ ─── Headers: Content-Type: application/json
     │ ─── Body: { access_key, name, email, subject, message, botcheck: "" }
     │
     ├── HTTP 200 ──► Show success toast
     │                 Reset form fields
     │                 Re-enable submit button
     │
     └── HTTP 4xx/5xx ──► Show error toast
                           Preserve form data
                           Offer mailto: fallback link
```

---

## 4. External Dependencies

| Dependency | Type | URL | Fallback | Risk |
|------------|------|-----|----------|------|
| **Google Fonts** | CDN | `fonts.googleapis.com` | System fonts via `font-display: swap` | Low — Google Fonts has 99.99% uptime |
| **Web3Forms** | API | `api.web3forms.com` | `mailto:` link displayed on failure | Low — free tier, no rate limit for personal use |
| **Lucide Icons** | CDN | `unpkg.com/lucide` | Inline SVG fallback in HTML | Low — static assets on unpkg CDN |
| **GitHub Pages** | Hosting | `github.io` | None (primary host) | Very Low — SLA backed by GitHub |

---

## 5. Security Considerations

| Threat | Mitigation |
|--------|------------|
| **XSS (Cross-Site Scripting)** | No user-generated content rendered. All content is hardcoded HTML. Form inputs are sent to Web3Forms, not displayed. |
| **CSRF** | Web3Forms handles CSRF protection via access key. No server-side state. |
| **Spam (Contact Form)** | Honeypot field (`botcheck`) + Web3Forms' built-in spam filtering. |
| **Email Harvesting** | Email displayed as text (not mailto: link directly). Can be obfuscated with JS if needed. |
| **Content Injection** | Static site — no dynamic content injection vectors. |
| **HTTPS** | Enforced by GitHub Pages with auto-renewing Let's Encrypt certificate. |
| **Content Security Policy** | Recommended `<meta>` CSP header allowing only required CDN origins. |

### 5.1 Recommended Content Security Policy

```html
<meta http-equiv="Content-Security-Policy" 
  content="
    default-src 'self';
    style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
    font-src 'self' https://fonts.gstatic.com;
    script-src 'self' https://unpkg.com;
    img-src 'self' data:;
    connect-src 'self' https://api.web3forms.com;
    frame-src 'none';
  " />
```

---

## 6. Performance Budget

| Asset Category | Budget | Strategy |
|----------------|--------|----------|
| **HTML** | < 20KB | Semantic, minimal markup |
| **CSS** (total) | < 15KB | CSS custom properties, no framework |
| **JS** (total) | < 15KB | Vanilla JS, no libraries |
| **Fonts** (total) | < 60KB | WOFF2 only, subset if possible |
| **Images** (total, above fold) | < 100KB | WebP, responsive `srcset`, lazy loading |
| **Images** (total, full page) | < 1MB | WebP, lazy loaded, max 800px card / 1200px modal |
| **TOTAL (above fold)** | < 200KB | Critical path optimized |
| **TOTAL (full page)** | < 1.5MB | All assets inclusive |

---

## 7. Hosting & Deployment

### 7.1 GitHub Pages Configuration

| Setting | Value |
|---------|-------|
| **Repository** | `username/username.github.io` |
| **Branch** | `main` |
| **Source** | GitHub Actions (deploy.yml) |
| **HTTPS** | Enforced |
| **Custom Domain** | TBD (optional via CNAME) |
| **Jekyll** | Disabled via `.nojekyll` |

### 7.2 GitHub Actions Workflow

```yaml
name: Deploy to GitHub Pages
on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      
      - name: Setup Pages
        uses: actions/configure-pages@v4
      
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: '.'
      
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

---

## 8. Maintainability (ISO/IEC 25010 — Maintainability)

### 8.1 File Organization Rationale

| Directory | Purpose | Change Frequency |
|-----------|---------|-----------------|
| `css/` | Design system + animations | Low (after initial build) |
| `js/` | Interaction logic | Low (after initial build) |
| `assets/images/projects/` | Project renders | Medium (as new projects added) |
| `assets/documents/` | Downloadable resume | Medium (updated per semester) |
| `docs/` | Architecture & design docs | Low (reference only) |

### 8.2 Content Update Guide

To add a new project:
1. Add WebP image to `assets/images/projects/`
2. Copy an existing `<article class="project-card">` block in `index.html`
3. Update text content, image `src`, and tech stack badges
4. No build step needed — push to `main` and GitHub Actions deploys

---

## 9. Compatibility Matrix

| Environment | Support Level | Notes |
|-------------|---------------|-------|
| Chrome 100+ | Full | Primary development browser |
| Firefox 100+ | Full | Tested |
| Safari 16+ | Full | Tested on macOS/iOS |
| Edge 100+ | Full | Chromium-based, mirrors Chrome |
| Mobile Chrome (Android) | Full | Responsive layouts |
| Mobile Safari (iOS) | Full | Responsive layouts |
| IE 11 | None | Not supported, no polyfills |
| Opera | Partial | Not tested, likely works (Chromium) |

---

## 10. ISO/IEC 25010 Quality Attributes Mapping

| Quality Attribute | Sub-characteristic | Implementation |
|-------------------|-------------------|----------------|
| **Functional Suitability** | Completeness | All sections (hero, projects, experience, skills, education, contact) |
| **Performance Efficiency** | Time behavior | FCP < 1.5s, LCP < 2.5s |
| **Performance Efficiency** | Resource utilization | < 1.5MB total page weight |
| **Compatibility** | Co-existence | No conflicts with GitHub Pages infrastructure |
| **Compatibility** | Interoperability | Cross-browser (Chrome/Firefox/Safari/Edge) |
| **Usability** | Appropriateness recognizability | Clear section headers, intuitive navigation |
| **Usability** | Learnability | Single-page, no complex interactions |
| **Usability** | Accessibility | WCAG 2.1 AA compliant |
| **Reliability** | Availability | 99.9%+ (GitHub Pages SLA) |
| **Reliability** | Fault tolerance | Graceful fallbacks for fonts, icons, form |
| **Security** | Confidentiality | No user data stored; form sent to Web3Forms |
| **Security** | Integrity | Static content, no injection vectors |
| **Maintainability** | Modularity | Separated CSS/JS concerns |
| **Maintainability** | Modifiability | CSS custom properties for easy theme changes |
| **Portability** | Adaptability | Responsive design, 320px–2560px |
