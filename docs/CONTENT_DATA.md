# Content Data Reference — Danish Shakil Portfolio

> **Document ID:** CDR-DS-001  
> **Purpose:** Complete content inventory for the portfolio website.  
> **Source:** [Portfolio.pdf](file:///d:/Daniportfoli/portfolio/data/Portfolio.pdf) + [Resume.pdf](file:///d:/Daniportfoli/portfolio/data/Resume.pdf)  
> **Last Updated:** 2026-09-23

---

## 1. Personal Information

```yaml
name: "Danish Shakil"
location: "Nowshera, Khyber Pakhtunkhwa, Pakistan"
email: "danishshakil3264@gmail.com"
phone: "+92 314 9746879"
tagline: "Mechanical Design · CAD · Simulation"
linkedin: "https://www.linkedin.com/in/danish36"
github: "https://github.com/Danishshakil32"
```

---

## 2. Professional Summary

> Mechanical engineering student turning technical specifications into manufacturable CAD — from a client enclosure design for a US trailer maker to a titanium aerospace bracket optimized under FEA. Skilled in 3D modeling, mechanical simulation, and interpreting technical specifications to deliver client-facing design work, including a completed manufacturing-process project for British American Tobacco.

---

## 3. Education

```yaml
university: "Ghulam Ishaq Khan Institute of Engineering Sciences and Technology (GIKI)"
university_short: "GIK Institute"
location: "Topi, Khyber Pakhtunkhwa, Pakistan"
degree: "Bachelor of Science in Mechanical Engineering"
graduation: "Expected 2027"
cgpa: "3.29 / 4.00"
cgpa_percentage: 82.25  # For progress bar (3.29/4.00 × 100)
```

---

## 4. Technical Skills

### 4.1 CAD & Modeling
| Skill | Proficiency | Certification |
|-------|------------|---------------|
| SolidWorks | Expert | CSWA Certified |
| Blender | Intermediate | — |

### 4.2 Engineering & Analysis
| Skill | Proficiency |
|-------|------------|
| ANSYS | Advanced |
| COMSOL Multiphysics | Intermediate |
| MATLAB | Advanced |
| Simulink | Intermediate |
| Dynacam | Intermediate |
| Linkages | Intermediate |

### 4.3 Robotics & Embedded
| Skill | Proficiency |
|-------|------------|
| ROS 2 | Intermediate |
| RViz2 | Intermediate |
| Proteus | Intermediate |
| Arduino IDE | Advanced |

### 4.4 Core Competencies
- Machine Design (Shigley's standards)
- Technical Drawing Interpretation
- GD&T Fundamentals
- Topology Optimization
- Geometric Inverse Kinematics

### 4.5 Manufacturing
- 3D Printing
- Rapid Prototyping
- Additive Manufacturing

### 4.6 Skills for Marquee (Tool Logos Needed)
```
SolidWorks | ANSYS | COMSOL | MATLAB | Simulink | Blender | 
Arduino | ROS 2 | Python | Proteus | 3D Printing
```

---

## 5. Professional Experience

### 5.1 British American Tobacco (BAT)

```yaml
role: "Mechanical Design Intern"
company: "British American Tobacco (BAT)"
type: "Internship"
period: "Jun 2026 – Jul 2026"
project: "Automated Tobacco Reclaimer System"
bullets:
  - "Designed and mapped an automated tobacco reclaimer system as part of a manufacturing internship, aimed at optimizing primary production operations."
  - "Produced technical design reports and detailed cross-departmental process flow diagrams for engineering and operations stakeholders."
card_badge: "Professional"
card_badge_color: "emerald"
tech_stack: ["SolidWorks", "Technical Drawing"]
images:
  - "page1_img1.png"  # Process flow diagram
  - "page1_img2.png"  # Technical design report visualization
```

### 5.2 Bigfoot Trailers

```yaml
role: "CAD Design Contractor"
company: "Bigfoot Trailers"
company_note: "US-based client"
type: "Freelance / Contract"
period: "Aug 2025"
project: "Yeti 24 Product Enclosure Design"
bullets:
  - "Delivered the complete 3D CAD model for a Yeti-branded product enclosure for a US-based trailer manufacturer, working remotely to client specifications."
  - "Ensured designs strictly adhered to client requirements, optimizing structure for manufacturability and aesthetic appeal."
card_badge: "Professional"
card_badge_color: "emerald"
tech_stack: ["SolidWorks", "CAD Modeling"]
images:
  - "page2_img1.jpeg"  # Yeti 24 exterior CAD render
  - "page2_img2.jpeg"  # Detailed section view with mounting points
```

---

## 6. Academic & Competition Projects

### 6.1 RoboCup Small Size League Robot

```yaml
title: "RoboCup Small Size League Robot"
subtitle: "Autonomous Soccer Robot, Maxon-Motor Drivetrain"
type: "Competition"
period: "Dec 2025 – May 2026"
bullets:
  - "Developed 3D CAD assemblies for an autonomous soccer robot equipped with Maxon motors."
  - "Designed and modeled a specialized mechanical dribbler and kicker mechanism in SolidWorks, optimizing packaging constraints and internal clearances."
  - "Managed iterative design revisions for rapid prototyping and executed 3D printing of complex structural components."
card_badge: "Competition"
card_badge_color: "cyan"
tech_stack: ["SolidWorks", "3D Printing", "Rapid Prototyping"]
images:
  - "page3_img1.png"   # Overall CAD assembly
  - "page3_img2.jpeg"  # Dribbler/kicker mechanism detail
  - "page3_img3.jpeg"  # Additional robot view
  - "page3_img4.jpeg"  # Additional robot view
```

### 6.2 Heavyweight Combat Robot

```yaml
title: "Heavyweight Combat Robot"
subtitle: "60 kg Vertical Spinner"
type: "Competition"
period: "Jul 2024 – May 2025"
bullets:
  - "Executed structural calculations, material selection, and force analysis to ensure design integrity under heavy impact."
  - "Developed the full 3D CAD assembly, ensuring all internal mechanisms met dimensional and weight constraints."
  - "Transitioned CAD models into physical builds through hands-on fabrication, machining, and rapid prototyping."
card_badge: "Competition"
card_badge_color: "cyan"
tech_stack: ["SolidWorks", "FEA", "Fabrication", "Machining"]
images:
  - "page4_img1.png"   # Structural layout and weapon integration
  - "page4_img2.png"   # Top-down CAD view, chassis + internals
```

### 6.3 Aerospace Bracket Topology Optimization

```yaml
title: "Aerospace Bracket Topology Optimization"
subtitle: "Ti-6Al-4V Titanium Alloy Structural Bracket"
type: "Academic Research"
period: "Dec 2024 – May 2025"
bullets:
  - "Executed a topology optimization study using ANSYS to lightweight a standard Ti-6Al-4V aerospace bracket while preserving its load-bearing integrity."
  - "Defined the design space, non-design regions (mounting holes), and applied multi-axis loading conditions simulating in-flight forces (e.g., 10 kN static load, 5G vibrational load)."
  - "Iteratively refined the generated organic geometry to enforce additive manufacturing constraints (e.g., overhang angles, minimum feature sizes)."
  - "Achieved a 32% reduction in overall component mass while maintaining a structural Factor of Safety (FoS) > 1.5, verifying the final design via a secondary Von Mises stress analysis."
card_badge: "Academic"
card_badge_color: "copper"
tech_stack: ["ANSYS", "FEA", "Topology Optimization", "Additive Manufacturing"]
key_metric: "32% mass reduction, FoS > 1.5"
images:
  - "page3_img1.png"   # Von Mises stress baseline (may need separate extraction)
  - "page3_img2.jpeg"  # Topology-optimized stress contour
```

---

## 7. Certifications

```yaml
certifications:
  - name: "Certified SOLIDWORKS Associate (CSWA)"
    issuer: "Dassault Systèmes"
    icon: "solidworks"
  - name: "SOLIDWORKS Electrical Design"
    issuer: "Dassault Systèmes"
    icon: "solidworks-electrical"
  - name: "Additive Manufacturing"
    issuer: "[Issuer TBD]"
    icon: "3d-printer"
```

---

## 8. Stats Strip Data

```yaml
stats:
  - value: 5
    suffix: "+"
    label: "Projects"
  - value: 3.29
    suffix: ""
    label: "CGPA"
  - value: 3
    suffix: ""
    label: "Certifications"
  - value: 2
    suffix: ""
    label: "Clients"
```

---

## 9. Hero Typing Animation Words

```yaml
typing_words:
  - "combat robots"
  - "precision brackets"
  - "trailer enclosures"
  - "autonomous systems"
```

---

## 10. Navigation Links

```yaml
nav_links:
  - label: "Home"
    href: "#hero"
  - label: "Projects"
    href: "#projects"
  - label: "Experience"
    href: "#experience"
  - label: "Skills"
    href: "#skills"
  - label: "About"
    href: "#about"
  - label: "Contact"
    href: "#contact"
cta:
  label: "Resume ↓"
  href: "assets/documents/Danish_Shakil_Resume.pdf"
  download: true
```

---

## 11. Extracted Images Inventory

All images extracted from Portfolio.pdf to `data/extracted_images/`:

| Filename | Source Page | Description | Use In |
|----------|-----------|-------------|--------|
| `page1_img1.png` | Page 1 | BAT process flow diagram | Project Card: BAT |
| `page1_img2.png` | Page 1 | BAT technical design report | Project Modal: BAT |
| `page2_img1.jpeg` | Page 2 | Yeti 24 exterior CAD render | Project Card: Bigfoot |
| `page2_img2.jpeg` | Page 2 | Yeti 24 section view, mounting points | Project Modal: Bigfoot |
| `page3_img1.png` | Page 3 | RoboCup robot CAD assembly | Project Card: RoboCup |
| `page3_img2.jpeg` | Page 3 | Dribbler/kicker mechanism detail | Project Modal: RoboCup |
| `page3_img3.jpeg` | Page 3 | Additional robot view | Project Modal: RoboCup |
| `page3_img4.jpeg` | Page 3 | Additional robot view | Project Modal: RoboCup |
| `page4_img1.png` | Page 4 | Combat robot structural layout | Project Card: Combat Robot |
| `page4_img2.png` | Page 4 | Combat robot top-down chassis view | Project Modal: Combat Robot |

> **Note:** Aerospace bracket images may need to be re-extracted or generated. The Von Mises stress plots from the PDF may be low-resolution.

---

## 12. SEO Metadata

```yaml
seo:
  title: "Danish Shakil — Mechanical Engineer · CAD · Simulation"
  description: "Mechanical engineering portfolio of Danish Shakil. CAD design, FEA simulation, and robotics projects. CSWA certified. GIK Institute."
  og_title: "Danish Shakil — Mechanical Engineer"
  og_description: "CAD design, FEA simulation, and robotics projects by Danish Shakil. CSWA certified, GIK Institute."
  og_type: "website"
  twitter_card: "summary_large_image"
  author: "Danish Shakil"
  keywords: "mechanical engineer, CAD, SolidWorks, ANSYS, FEA, robotics, portfolio, CSWA, GIK Institute"
  
structured_data:
  type: "Person"
  name: "Danish Shakil"
  jobTitle: "Mechanical Engineering Student"
  alumniOf: "GIK Institute of Engineering Sciences and Technology"
  knowsAbout: ["CAD", "SolidWorks", "ANSYS", "FEA", "Robotics", "3D Printing"]
```

---

## 13. Contact Form Fields

```yaml
form:
  service: "Web3Forms"
  access_key: "[TO BE GENERATED at web3forms.com]"
  fields:
    - name: "name"
      label: "Full Name"
      type: "text"
      required: true
      placeholder: "John Doe"
    - name: "email"
      label: "Email Address"
      type: "email"
      required: true
      placeholder: "john@example.com"
    - name: "subject"
      label: "Subject"
      type: "text"
      required: true
      placeholder: "Project Inquiry"
    - name: "message"
      label: "Message"
      type: "textarea"
      required: true
      placeholder: "Tell me about your project..."
      rows: 5
  honeypot:
    name: "botcheck"
    type: "hidden"
  redirect: false  # Handle via JS
  success_message: "Message sent successfully! I'll get back to you soon."
  error_message: "Something went wrong. Please try again or email me directly."
```
