# Development Handoff Brief — Danish Shakil Portfolio

> **To:** Gemini 3.1 Pro (Developer)  
> **From:** Claude Opus (Architect)  
> **Date:** 2026-09-23  
> **Project:** Portfolio Website for GitHub Pages

---

## 🎯 Mission

Build a **premium, single-page portfolio website** for Danish Shakil using **pure HTML + CSS + JS** (no framework, no build step). Deploy on GitHub Pages. The design must match the aesthetic quality of [turabacademy.com](https://turabacademy.com/) — adapted from an academy site to a personal mechanical engineering portfolio.

---

## 📦 Documentation Suite (READ THESE FIRST)

| Document | Path | What It Contains |
|----------|------|------------------|
| **Implementation Plan** | [implementation_plan.md](file:///C:/Users/Administrator/.gemini/antigravity-ide/brain/e8625cd9-35d8-47cb-8097-e76005baac8d/implementation_plan.md) | Full project spec, file structure, section descriptions, SEO, deployment |
| **Architecture** | [docs/ARCHITECTURE.md](file:///d:/Daniportfoli/portfolio/docs/ARCHITECTURE.md) | System architecture, data flow, security, performance budget, deployment config |
| **Design System** | [docs/DESIGN_SYSTEM.md](file:///d:/Daniportfoli/portfolio/docs/DESIGN_SYSTEM.md) | Every CSS token, component spec, animation keyframe, responsive breakpoint |
| **SQA Plan** | [docs/SQA_PLAN.md](file:///d:/Daniportfoli/portfolio/docs/SQA_PLAN.md) | Testing matrix, acceptance criteria, quality gates, defect classification |
| **Content Data** | [docs/CONTENT_DATA.md](file:///d:/Daniportfoli/portfolio/docs/CONTENT_DATA.md) | All personal data, project descriptions, skills, images, SEO metadata |

---

## 🏗️ Build Order (Recommended Sequence)

### Phase 1: Foundation
1. **Create `index.html`** — Full HTML structure with all sections, semantic elements, meta tags, JSON-LD
2. **Create `css/style.css`** — CSS reset, custom properties (all tokens from Design System doc), container system, grid
3. **Create `css/animations.css`** — All keyframe animations, reduced motion overrides

### Phase 2: Sections (Top to Bottom)
4. **Header/Navigation** — Fixed header, nav links with smooth scroll, mobile hamburger menu
5. **Hero Section** — 5/7 grid, title, typing animation placeholder, CTA buttons, grid overlay, glow blobs
6. **Stats Strip** — 4-metric counter strip
7. **Projects Section** — 3-column card grid with all 5 projects
8. **Experience Timeline** — Vertical timeline with glassmorphic cards
9. **Skills Marquee** — Dual-row infinite scroll with tool names/logos
10. **About & Education** — Bio + university card + certifications row
11. **Contact Section** — 2-column layout with form
12. **Footer** — Social links, copyright, back-to-top

### Phase 3: Interactions
13. **`js/main.js`** — Navigation scroll tracking, mobile menu, header scroll behavior, typing animation, back-to-top
14. **`js/animations.js`** — IntersectionObserver for section reveals, stats counter, timeline nodes
15. **`js/form.js`** — Web3Forms integration, validation, toast notifications

### Phase 4: Assets & Config
16. **Process images** — Convert extracted images from `data/extracted_images/` to WebP, move to `assets/images/projects/`
17. **Create favicon** — Generate "DS" monogram favicon set
18. **Create OG image** — Social preview image (1200×630)
19. **`robots.txt`**, **`sitemap.xml`**, **`.nojekyll`**, **`.github/workflows/deploy.yml`**

### Phase 5: QA
20. **Run validation** — HTML, CSS, Lighthouse, accessibility checks
21. **Cross-browser test** — Chrome, Firefox, Edge
22. **Responsive test** — 320px to 2560px

---

## ⚡ Critical Implementation Notes

### DO:
- ✅ Use **vanilla CSS custom properties** for all tokens (copy from Design System doc)
- ✅ Use **semantic HTML5** (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`)
- ✅ Use **`defer`** attribute on all `<script>` tags
- ✅ Use **`loading="lazy"`** on all images except the hero profile photo
- ✅ Use **`<picture>` with WebP** format for project images
- ✅ Add **`aria-label`** to all interactive elements
- ✅ Include **skip-to-content** link as first element in body
- ✅ Add **`rel="noopener noreferrer"`** to all external links
- ✅ Use **`prefers-reduced-motion`** media query to disable animations
- ✅ Use **`font-display: swap`** for Google Fonts
- ✅ Match the **exact color palette** from the Design System (navy-deep, navy, cyan, copper, cloud)
- ✅ Make the site feel **premium and polished** — this is the #1 priority

### DON'T:
- ❌ Do NOT use any framework (React, Vue, Tailwind, Bootstrap)
- ❌ Do NOT use jQuery or any JS library
- ❌ Do NOT add a build step (Webpack, Vite, etc.)
- ❌ Do NOT use inline styles (use CSS classes)
- ❌ Do NOT skip animations — they're critical to the premium feel
- ❌ Do NOT use placeholder images — use the extracted images from `data/extracted_images/`
- ❌ Do NOT hardcode the Web3Forms access key (use a placeholder comment `<!-- REPLACE WITH YOUR WEB3FORMS KEY -->`)

---

## 📐 Key Design Decisions (Already Made)

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Framework | None (pure HTML/CSS/JS) | GitHub Pages compatibility, zero build step |
| CSS approach | Vanilla CSS with custom properties | Maximum control, no external dependencies |
| Font loading | Google Fonts CDN | Industry standard, fast CDN, WOFF2 |
| Icons | Lucide Icons CDN | Lightweight, tree-shakeable SVGs |
| Contact form | Web3Forms | Free, no-signup serverless form handler |
| Image format | WebP | Best compression, wide browser support |
| Deployment | GitHub Actions → Pages | Automatic on push to main |
| Theme | Dark-first (no toggle) | Matches engineering/technical aesthetic |

---

## 🖼️ Project Images Available

Extracted from Portfolio.pdf → `data/extracted_images/`:

```
data/extracted_images/
├── page1_img1.png    → BAT: Process flow diagram
├── page1_img2.png    → BAT: Technical report visualization
├── page2_img1.jpeg   → Bigfoot: Yeti 24 exterior render
├── page2_img2.jpeg   → Bigfoot: Section view, mounting points
├── page3_img1.png    → RoboCup: Full robot CAD assembly
├── page3_img2.jpeg   → RoboCup: Dribbler/kicker mechanism
├── page3_img3.jpeg   → RoboCup: Additional view
├── page3_img4.jpeg   → RoboCup: Additional view
├── page4_img1.png    → Combat Robot: Structural layout
└── page4_img2.png    → Combat Robot: Top-down chassis view
```

**Action needed:** Convert these to WebP, resize to max 800px width for cards / 1200px for modals, and place in `assets/images/projects/`.

> **Note:** The Aerospace Bracket project may not have separate images — the FEA stress plots may be part of other page images. If no clear standalone image exists, generate an AI placeholder or use a generic FEA visualization.

---

## 🎨 Reference Screenshots

The reference website (turabacademy.com) has been captured via browser. Key design patterns to replicate:

1. **Dark navy background** with subtle cyan grid overlay (56px grid)
2. **Radial glow blobs** — large cyan/blue gradient spheres behind sections
3. **Cards with hover lift** — `translateY(-4px)`, border turns cyan, shadow grows
4. **Monospace eyebrow labels** — uppercase, letter-spacing 0.2em, copper line prefix
5. **Space Grotesk headings** — bold, tight leading
6. **DM Sans body text** — clean, readable, slightly transparent on dark bg
7. **Stats strip** — light background band between dark sections
8. **Marquee scrolling** — continuous horizontal scroll of logos

---

## ✅ Acceptance Checklist (Run After Build)

```bash
# 1. HTML Validation
npx html-validate index.html

# 2. Lighthouse
# Open Chrome DevTools → Lighthouse → Run on index.html

# 3. Accessibility
# Install axe DevTools extension → Scan page

# 4. Broken Links
npx broken-link-checker http://localhost:PORT --recursive

# 5. Responsive
# Chrome DevTools → Toggle device toolbar → Test: 320, 375, 768, 1024, 1536, 2560
```

---

## 📞 Questions?

If anything is ambiguous during development, refer to the documents in this order:
1. **CONTENT_DATA.md** — for text content and data values
2. **DESIGN_SYSTEM.md** — for visual specifications
3. **ARCHITECTURE.md** — for structural decisions
4. **SQA_PLAN.md** — for testing requirements

The user (Danish Shakil) is available for questions about content accuracy or design preferences.
