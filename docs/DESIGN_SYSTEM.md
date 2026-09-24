# Design System Specification — Danish Shakil Portfolio

> **Document ID:** DS-DS-001  
> **Version:** 1.0.0  
> **Standard:** ISO 9241-110:2020 (Interaction Principles)  
> **Reference:** turabacademy.com  
> **Last Updated:** 2026-09-23

---

## 1. Design Philosophy

### 1.1 Core Principles

| Principle | Description | Implementation |
|-----------|-------------|----------------|
| **Dark-First** | Navy/dark backgrounds feel premium, technical, and engineering-focused | `--navy-deep: #0B1E3D` as primary background |
| **Precision Aesthetic** | Grid overlays and monospace labels evoke engineering precision | 56px CSS grid overlay at low opacity |
| **Glow Accents** | Cyan radial glows suggest technology and innovation | `radial-gradient` blobs behind key sections |
| **Micro-Motion** | Subtle animations show care and polish without distraction | 200ms transitions, fade-in-up reveals |
| **Glassmorphism** | Semi-transparent cards with backdrop blur create depth | `backdrop-filter: blur(12px)` on timeline cards |

### 1.2 Design Inspiration from turabacademy.com

**What we adopt:**
- Navy deep background with cyan accent system
- Grid overlay pattern on hero section
- Card hover effects (lift + border highlight)
- Marquee scrolling for logos/badges
- Stats counter strip between sections
- Space Grotesk + DM Sans font pairing
- Monospace labels for section eyebrows
- Copper accent for decorative divider lines

**What we adapt:**
- Replace image carousel with profile photo + floating badges
- Replace event cards with project cards (same shape, different content)
- Replace programs grid with experience timeline
- Replace "Verify certificate" CTA with "Download Resume" CTA
- Replace multi-page navigation with single-page scroll navigation

---

## 2. Color System

### 2.1 Primary Palette

```
┌─────────────────────────────────────────────────────────┐
│  TOKEN              │  HEX      │  HSL                   │
├─────────────────────┼───────────┼────────────────────────┤
│  --navy-deep        │  #0B1E3D  │  216° 72% 14%         │
│  --navy             │  #102A56  │  216° 69% 20%         │
│  --cyan             │  #00A8E8  │  197° 100% 45%        │
│  --cyan-hover       │  #25BAF3  │  198° 89% 55%         │
│  --copper           │  #B84E24  │  17° 67% 43%          │
│  --cloud            │  #F5F8FC  │  213° 54% 97%         │
│  --charcoal         │  #182230  │  216° 33% 14%         │
│  --white            │  #FFFFFF  │  0° 0% 100%           │
└─────────────────────┴───────────┴────────────────────────┘
```

### 2.2 Semantic Color Mapping

```css
/* ── Background ──────────────────────────── */
--bg-primary:      var(--navy-deep);       /* Main page background */
--bg-secondary:    var(--navy);            /* Header, cards on dark */
--bg-light:        var(--cloud);           /* Stats strip, about section */
--bg-card:         var(--white);           /* Project cards on light bg */

/* ── Text ────────────────────────────────── */
--text-primary:    var(--white);           /* Headings on dark bg */
--text-secondary:  rgba(245,248,252,0.85); /* Body text on dark bg */
--text-muted:      rgba(245,248,252,0.70); /* Hints, captions on dark */
--text-dark:       var(--charcoal);        /* Text on light bg */
--text-dark-muted: rgba(24,34,48,0.75);   /* Muted text on light bg */

/* ── Accent ──────────────────────────────── */
--accent:          var(--cyan);            /* Links, active states, icons */
--accent-hover:    var(--cyan-hover);      /* Hover state for accents */
--accent-subtle:   rgba(0,168,232,0.15);   /* Badge backgrounds */
--accent-glow:     rgba(0,168,232,0.30);   /* Glow effects */

/* ── Border ──────────────────────────────── */
--border-subtle:   rgba(0,168,232,0.20);   /* Header bottom border */
--border-card:     rgba(16,42,86,0.12);    /* Card borders on light bg */
--border-input:    rgba(255,255,255,0.25); /* Form input borders */
--border-hover:    var(--cyan);            /* Hover state borders */

/* ── Decorative ──────────────────────────── */
--copper-line:     var(--copper);          /* Section eyebrow divider */
```

### 2.3 Color Contrast Verification (WCAG 2.1 AA)

| Foreground | Background | Contrast Ratio | Result |
|------------|------------|----------------|--------|
| `#FFFFFF` | `#0B1E3D` | 15.2:1 | ✅ AAA |
| `#F5F8FC` @ 85% | `#0B1E3D` | 11.8:1 | ✅ AAA |
| `#F5F8FC` @ 70% | `#0B1E3D` | 8.5:1 | ✅ AAA |
| `#00A8E8` | `#0B1E3D` | 5.9:1 | ✅ AA Large / AA |
| `#182230` | `#F5F8FC` | 13.8:1 | ✅ AAA |
| `#182230` @ 75% | `#F5F8FC` | 8.1:1 | ✅ AAA |
| `#00A8E8` | `#FFFFFF` | 2.8:1 | ⚠️ Large text only |

---

## 3. Typography System

### 3.1 Font Stack

```css
--font-display: 'Space Grotesk', system-ui, -apple-system, sans-serif;
--font-body:    'DM Sans', system-ui, -apple-system, sans-serif;
--font-mono:    'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace;
```

### 3.2 Google Fonts Import

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet" />
```

### 3.3 Type Scale (Major Third — 1.25 Ratio)

```
USAGE                  TOKEN       SIZE      WEIGHT  FONT         LINE-HEIGHT
──────────────────────────────────────────────────────────────────────────────
Hero Heading           --text-5xl   3.4rem    700     Display      1.12
Section Heading        --text-3xl   2rem      700     Display      1.2
Card Title             --text-lg    1.125rem  700     Display      1.35
Body Text              --text-base  1rem      400     Body         1.6
Body Emphasis          --text-base  1rem      600     Body         1.6
Small Text             --text-sm    0.875rem  400     Body         1.5
Caption / Label        --text-xs    0.6875rem 600     Mono         1.4
Badge Text             --text-xs    0.6875rem 700     Mono         1.0
Section Eyebrow        --text-xs    0.75rem   600     Mono         1.4
   └── UPPERCASE, letter-spacing: 0.2em, --copper line prefix
```

### 3.4 Typography CSS Classes

```css
/* Display headings — Space Grotesk */
.heading-hero   { font: 700 var(--text-5xl)/1.12 var(--font-display); }
.heading-section{ font: 700 var(--text-3xl)/1.2  var(--font-display); }
.heading-card   { font: 700 var(--text-lg)/1.35  var(--font-display); }
.heading-small  { font: 600 var(--text-base)/1.4 var(--font-display); }

/* Body text — DM Sans */
.body           { font: 400 var(--text-base)/1.6 var(--font-body); }
.body-emphasis  { font: 600 var(--text-base)/1.6 var(--font-body); }
.body-small     { font: 400 var(--text-sm)/1.5   var(--font-body); }
.body-large     { font: 400 var(--text-lg)/1.6   var(--font-body); }

/* Mono labels — JetBrains Mono */
.label          { font: 600 var(--text-xs)/1.4 var(--font-mono); 
                  text-transform: uppercase; letter-spacing: 0.2em; }
.badge          { font: 700 var(--text-xs)/1.0 var(--font-mono); 
                  text-transform: uppercase; letter-spacing: 0.04em; }
```

---

## 4. Spacing System

### 4.1 Base Unit: 8px

```
TOKEN        VALUE       PIXELS    TYPICAL USE
───────────────────────────────────────────────────────────
--space-1    0.25rem     4px       Tight gaps (icon-text)
--space-2    0.5rem      8px       Inline spacing
--space-3    0.75rem     12px      Badge padding
--space-4    1rem        16px      Card inner padding (mobile)
--space-5    1.25rem     20px      Card inner padding (desktop)
--space-6    1.5rem      24px      Element gaps
--space-8    2rem        32px      Sub-section gaps
--space-10   2.5rem      40px      Section title → content gap
--space-12   3rem        48px      Inter-section spacing
--space-16   4rem        64px      Section vertical padding
--space-20   5rem        80px      Large section vertical padding
```

### 4.2 Container System

```css
.container {
  width: 100%;
  max-width: var(--max-width);  /* 1760px */
  margin-inline: auto;
  padding-inline: var(--space-8);  /* 32px */
}

@media (min-width: 640px) {
  .container { padding-inline: 3.5rem; }  /* 56px */
}

@media (min-width: 1024px) {
  .container { padding-inline: 5rem; }    /* 80px */
}
```

---

## 5. Border Radius System

```
TOKEN           VALUE       USE
────────────────────────────────────────────
--radius-sm     0.375rem    Input fields, small badges
--radius-md     0.5rem      Buttons, nav items
--radius-lg     0.75rem     CTA buttons, timeline cards
--radius-xl     1rem        Medium cards, modals
--radius-2xl    1.25rem     Project cards, major containers
--radius-full   9999px      Pills, avatar circles, round buttons
```

---

## 6. Shadow System

```css
--shadow-sm:    0 1px 2px rgba(0,0,0,0.12);
--shadow-md:    0 4px 12px rgba(0,0,0,0.15);
--shadow-lg:    0 8px 30px rgba(0,0,0,0.20);
--shadow-glow:  0 0 20px rgba(0,168,232,0.30);
--shadow-card:  0 1px 3px rgba(0,0,0,0.10), 0 1px 2px rgba(0,0,0,0.06);
```

---

## 7. Transition System

```css
--transition-fast:  150ms ease-out;   /* Hover color changes */
--transition-base:  200ms ease-out;   /* Card hover, button states */
--transition-slow:  300ms ease-out;   /* Menu open/close */
--transition-image: 700ms ease-out;   /* Image scale on hover */

/* Transition shorthand — match turabacademy.com pattern */
.interactive {
  transition: color var(--transition-base),
              background-color var(--transition-base),
              border-color var(--transition-base),
              box-shadow var(--transition-base),
              transform var(--transition-base);
}
```

---

## 8. Grid Overlay Effect

The signature grid overlay from turabacademy.com, adapted for the portfolio:

```css
.grid-overlay {
  position: absolute;
  inset: -4%;
  z-index: -1;
  pointer-events: none;
  opacity: 0.22;
  background-image: 
    linear-gradient(rgba(0,168,232,0.18) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,168,232,0.18) 1px, transparent 1px);
  background-size: 56px 56px;
}
```

---

## 9. Glow Effects

### 9.1 Radial Glow Blobs

```css
.glow-blob {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
  z-index: -1;
  filter: blur(60px);
}

.glow-blob--cyan {
  background: radial-gradient(circle, rgba(0,168,232,0.28) 0%, rgba(0,168,232,0) 65%);
  width: 38rem;
  height: 38rem;
}

.glow-blob--copper {
  background: radial-gradient(circle, rgba(184,78,36,0.15) 0%, rgba(184,78,36,0) 65%);
  width: 20rem;
  height: 20rem;
}
```

### 9.2 CTA Button Glow

```css
.cta-glow {
  position: relative;
}

.cta-glow::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
  background: var(--cyan);
  opacity: 0;
  filter: blur(12px);
  z-index: -1;
  transition: opacity var(--transition-base);
}

.cta-glow:hover::after {
  opacity: 0.4;
}
```

---

## 10. Component Design Specifications

### 10.1 Navigation Header

```
┌───────────────────────────────────────────────────────────────────────┐
│  ┌─────────┐  Home  Projects  Experience  Skills  About  Contact    │
│  │  DS     │                                           ┌────────────┐│
│  │  Logo   │                                           │ Resume ↓  ││
│  └─────────┘                                           └────────────┘│
├───────────────────────────────────────────────────────────────────────┤
│  border-bottom: 1px solid color-mix(in oklab, cyan 20%, transparent) │
└───────────────────────────────────────────────────────────────────────┘

SPECS:
- position: fixed; top: 0; inset-x: 0; z-index: 50
- height: 4.5rem (72px)
- background: var(--navy) → on scroll: adds shadow-md
- Logo: "DS" monogram or name "Danish Shakil" in Space Grotesk 600
- Nav links: DM Sans 500, 0.95rem, --cloud/85 → hover: --white
- Active link: --cyan color
- CTA: "Resume ↓" pill button, bg: cyan/15, text: cyan, ring: cyan/30
- Mobile (< 1024px): hamburger icon, slide-in drawer from right
```

### 10.2 Hero Section

```
┌──────────────────────────────────────────────────────────────────┐
│  ── Mechanical Engineer                                          │
│                                                                  │
│  ┌─── 5 col ──────────────┐  ┌─── 7 col ────────────────────┐  │
│  │ EMERGING TECH ENGINEER   │  │                              │  │
│  │                          │  │   ┌──────────────────┐       │  │
│  │ I design                 │  │   │                  │       │  │
│  │ combat robots▎           │  │   │   Profile Photo  │       │  │
│  │                          │  │   │   (Glassmorphic  │       │  │
│  │ Professional summary     │  │   │    frame)        │       │  │
│  │ text goes here with      │  │   │                  │       │  │
│  │ a brief description.     │  │   └──────────────────┘       │  │
│  │                          │  │                              │  │
│  │ ┌──────────┐ ┌────────┐  │  │  [SolidWorks] [ANSYS]       │  │
│  │ │View Work │ │Contact │  │  │       [MATLAB]  [ROS2]      │  │
│  │ └──────────┘ └────────┘  │  │    (floating badges)        │  │
│  │                          │  │                              │  │
│  │ 5+ Projects · CSWA Cert  │  │                              │  │
│  └──────────────────────────┘  └──────────────────────────────┘  │
│                                                                  │
│  [grid overlay] [glow blob top-left] [glow blob bottom-right]   │
└──────────────────────────────────────────────────────────────────┘

SPECS:
- padding-top: calc(header-height + 2.5rem)
- padding-bottom: 3rem
- background: var(--navy-deep)
- Grid: 12-column, 5 col left / 7 col right
- Title: Space Grotesk 700, 3.4rem (desktop), 1.75rem (mobile)
- Typing animation: 2s per word, 0.5s pause, infinite loop
  Words: ["combat robots", "precision brackets", "trailer enclosures", "autonomous systems"]
- CTA Primary: rounded-full, bg-cyan, text-navy, hover:bg-cyan-hover
- CTA Secondary: rounded-lg, border white/25, text-white, hover:border-cyan
- Floating badges: absolute positioned, CSS float animation (3s ease-in-out infinite alternate)
```

### 10.3 Stats Strip

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│   5+             3.29           3              2                 │
│   Projects       CGPA           Certifications  Clients         │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘

SPECS:
- background: var(--cloud), border-y 1px solid navy/15
- 4-column grid (2×2 on mobile)
- Number: Space Grotesk 700, 2rem, --navy color
- Label: DM Sans 500, 0.875rem, --charcoal/75
- Counter animation: triggered by IntersectionObserver
  - Easing: easeOutExpo
  - Duration: 2s
  - Count from 0 to target
```

### 10.4 Project Card

```
┌──────────────────────────────────────┐
│  ┌──────────────────────────────┐    │
│  │                              │    │
│  │   Project Image (16:9)       │    │
│  │   aspect-ratio: 16/9         │    │
│  │                              │    │
│  └──────────────────────────────┘    │
│                                      │
│  ┌─────────────┐ ┌──────────────┐   │
│  │ Professional│ │ Jun-Jul 2026 │   │
│  └─────────────┘ └──────────────┘   │
│                                      │
│  ┌────────┐ ┌──────────────────┐    │
│  │ Client │ │ SolidWorks       │    │
│  └────────┘ └──────────────────┘    │
│                                      │
│  Automated Tobacco Reclaimer         │
│  System                              │
│                                      │
│  Designed and mapped an automated    │
│  tobacco reclaimer system...         │
│                                      │
│  ┌────────────────────────────────┐  │
│  │         View Details           │  │
│  └────────────────────────────────┘  │
└──────────────────────────────────────┘

SPECS:
- width: 100% of column (3-col grid)
- border-radius: var(--radius-2xl)
- border: 1px solid navy/12 → hover: cyan
- background: white
- shadow: var(--shadow-sm) → hover: var(--shadow-lg)
- hover: transform translateY(-4px)
- transition: all 200ms ease-out
- Image: object-fit: cover, hover: scale(1.02)
- Status badge: rounded-full, emerald bg for "Professional", cyan for "Competition"
- Date badge: rounded-full, navy bg, white text, JetBrains Mono 700
- Tech pills: rounded-full, bg: cloud, text: charcoal, 0.6875rem
- Title: Space Grotesk 700, 1.125rem, navy
- Description: line-clamp: 2, DM Sans 400, 0.875rem, charcoal/75
- CTA: full-width, bg: cyan, text: navy, rounded-lg, 0.875rem 600
```

### 10.5 Experience Timeline

```
         ┌────────────────────────┐
         │  BAT — Design Intern   │
         │  Jun–Jul 2026          │
   ──────┼──●─────────────────────┘
         │
         │  ┌─────────────────────────┐
         │  │  Bigfoot Trailers — CAD │
         │  │  Contractor, Aug 2025   │
         └──┼──●──────────────────────┘
            │
   ┌────────┼──●
   │ RoboCup│
   │ SSL    │
   │ Robot  │
   └────────┘

SPECS:
- Timeline line: 2px width, gradient from cyan (top) to copper (bottom)
- Timeline nodes: 12px circles, bg: cyan, border: 3px solid navy-deep
- Node animation: pulse (scale 1→1.3→1, opacity 1→0.5→1), 2s, triggered on scroll
- Cards: glassmorphic (backdrop-blur: 12px, bg: white/5, border: white/10)
- Desktop: alternating left/right
- Mobile: all cards on right side, line on left
- Card date: JetBrains Mono 600, 0.6875rem, copper color
- Card title: Space Grotesk 700, 1.125rem, white
- Card body: DM Sans 400, 0.875rem, cloud/85
```

### 10.6 Skills Marquee

```
┌──────────────────────────────────────────────────────────────────┐
│  →  [SolidWorks] [ANSYS] [COMSOL] [MATLAB] [Blender] [ROS2] →  │
│  ←  [Arduino] [Python] [Simulink] [Proteus] [3D Print]     ←   │
└──────────────────────────────────────────────────────────────────┘

SPECS:
- Two rows, opposite scroll direction
- Row 1: animation: marquee 30s linear infinite
- Row 2: animation: marquee-reverse 35s linear infinite
- Items: 48px height logos, grayscale → hover: full color
- Gap between items: 3rem
- Duplicated items for seamless loop
- prefers-reduced-motion: pause animation
```

### 10.7 Contact Form

```
┌──────────────────────────────────────────────────────────────────┐
│  ┌─── Info ────────────┐  ┌─── Form ──────────────────────────┐ │
│  │                     │  │                                    │ │
│  │ 📧 danish...@gmail  │  │  Name     ┌──────────────────────┐│ │
│  │ 📞 +92 314 974...   │  │           │                      ││ │
│  │ 📍 Nowshera, KP     │  │           └──────────────────────┘│ │
│  │                     │  │  Email    ┌──────────────────────┐│ │
│  │ ┌────┐ ┌────┐       │  │           │                      ││ │
│  │ │ GH │ │ LI │       │  │           └──────────────────────┘│ │
│  │ └────┘ └────┘       │  │  Subject  ┌──────────────────────┐│ │
│  │                     │  │           │                      ││ │
│  └─────────────────────┘  │           └──────────────────────┘│ │
│                           │  Message  ┌──────────────────────┐│ │
│                           │           │                      ││ │
│                           │           │                      ││ │
│                           │           └──────────────────────┘│ │
│                           │  ┌────────────────────────────────┐│ │
│                           │  │         Send Message           ││ │
│                           │  └────────────────────────────────┘│ │
│                           └────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘

SPECS:
- Background: var(--navy-deep) with grid overlay
- Layout: 2-column (5/7 split), stacked on mobile
- Inputs: bg: transparent, border: white/25, rounded-lg
  - Focus: border-cyan, ring-2 ring-cyan/50
  - Placeholder: cloud/50
  - Text: white
- Submit button: bg: cyan, text: navy, rounded-lg, full-width
  - Loading state: spinner SVG + "Sending..." text
  - Disabled opacity: 0.6
- Success toast: bg: emerald-600, text: white, slide in from top
- Error toast: bg: red-600, text: white, slide in from top
- Honeypot: hidden input for bot detection
```

---

## 11. Animation Keyframes

### 11.1 Section Reveal

```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(24px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.reveal {
  opacity: 0;
  transform: translateY(24px);
}

.reveal.visible {
  animation: fadeInUp 0.6s ease-out forwards;
}
```

### 11.2 Hero Typing Effect

```css
@keyframes typing {
  from { width: 0; }
  to { width: 100%; }
}

@keyframes blink {
  50% { border-color: transparent; }
}

.typing-text {
  overflow: hidden;
  white-space: nowrap;
  border-right: 3px solid var(--cyan);
  animation: typing 2s steps(20, end), blink 0.75s step-end infinite;
}
```

### 11.3 Floating Badges (Hero)

```css
@keyframes float {
  0%   { transform: translateY(0px) rotate(0deg); }
  50%  { transform: translateY(-10px) rotate(2deg); }
  100% { transform: translateY(0px) rotate(0deg); }
}

.floating-badge {
  animation: float 3s ease-in-out infinite;
}
.floating-badge:nth-child(2) { animation-delay: 0.5s; }
.floating-badge:nth-child(3) { animation-delay: 1.0s; }
.floating-badge:nth-child(4) { animation-delay: 1.5s; }
```

### 11.4 Skills Marquee

```css
@keyframes marquee {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); }
}

@keyframes marquee-reverse {
  from { transform: translateX(-50%); }
  to   { transform: translateX(0); }
}

.marquee-track       { animation: marquee 30s linear infinite; }
.marquee-track--rev  { animation: marquee-reverse 35s linear infinite; }
```

### 11.5 Timeline Node Pulse

```css
@keyframes pulse {
  0%   { box-shadow: 0 0 0 0 rgba(0,168,232,0.6); }
  70%  { box-shadow: 0 0 0 10px rgba(0,168,232,0); }
  100% { box-shadow: 0 0 0 0 rgba(0,168,232,0); }
}

.timeline-node.visible {
  animation: pulse 2s ease-out;
}
```

### 11.6 Reduced Motion Override

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
  
  .marquee-track,
  .marquee-track--rev {
    animation-play-state: paused;
  }
}
```

---

## 12. Responsive Breakpoints

```css
/* Mobile First — Base styles for < 640px */

/* Small tablets and up */
@media (min-width: 640px) {
  /* 2-column layouts, larger text, expanded padding */
}

/* Landscape tablets / small laptops */
@media (min-width: 1024px) {
  /* Full desktop layout, 12-col grid, side-by-side sections */
  /* Navigation links visible (hamburger hidden) */
}

/* Large desktops */
@media (min-width: 1536px) {
  /* Max-width container kicks in */
}
```

### 12.1 Key Responsive Changes

| Component | Mobile (< 640) | Tablet (640–1023) | Desktop (1024+) |
|-----------|----------------|-------------------|-----------------|
| **Header** | Hamburger menu | Hamburger menu | Full nav links |
| **Hero** | Stacked, text only | Stacked, photo below | 5/7 grid columns |
| **Stats** | 2×2 grid | 4-column | 4-column |
| **Projects** | 1 column | 2 columns | 3 columns |
| **Timeline** | Left line, right cards | Left line, right cards | Alternating L/R |
| **Contact** | Stacked (info → form) | Stacked | 5/7 grid columns |
| **Hero title** | 1.75rem | 3rem | 3.4rem |

---

## 13. Icon System

Using **Lucide Icons** (open-source, MIT license):

```html
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
<script>lucide.createIcons();</script>
```

### Icons Used

| Icon | Lucide Name | Context |
|------|-------------|---------|
| 📧 | `mail` | Contact info |
| 📞 | `phone` | Contact info |
| 📍 | `map-pin` | Location |
| 📅 | `calendar-days` | Timeline dates |
| 🔗 | `external-link` | Project links |
| 👤 | `user` | About section |
| 🎓 | `graduation-cap` | Education |
| 🔧 | `wrench` | Skills |
| 📄 | `file-text` | Resume download |
| ↑ | `arrow-up` | Back to top |
| ☰ | `menu` | Mobile hamburger |
| ✕ | `x` | Close mobile menu |
| → | `chevron-right` | Card links |
| GitHub | `github` | Social link |
| LinkedIn | `linkedin` | Social link |

---

## 14. Asset Specifications

### 14.1 Image Requirements

| Asset | Dimensions | Format | Max Size | Notes |
|-------|-----------|--------|----------|-------|
| **Profile Photo** | 600×600px | WebP | 80KB | Square, center-cropped face |
| **Project Card Image** | 800×450px | WebP | 60KB each | 16:9 ratio, card thumbnail |
| **Project Modal Image** | 1200×675px | WebP | 120KB each | 16:9 ratio, detailed view |
| **Tool Logo** | 48×48px | SVG | 5KB each | Monochrome, consistent style |
| **OG Image** | 1200×630px | WebP | 100KB | Social preview card |
| **Favicon** | 32×32, 16×16 | PNG + ICO | < 5KB | Brand monogram "DS" |

### 14.2 Tool Logos Needed

```
SolidWorks · ANSYS · COMSOL Multiphysics · MATLAB · Simulink
Blender · Arduino · ROS 2 · Python · Proteus · 3D Printing
```
