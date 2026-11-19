# TruthLens – Multimodal Digital Forensics & Deepfake Detection System

> **Innovedge Hackathon 2026 | Official Problem Statement 04**  
> **Domain:** Digital Forensics & Cybersecurity  
> **Challenge Area:** Multimodal Media Authenticity Analysis  
> **Expected Outcome:** Explainable forensic report with cross-modal correlation, calibrated uncertainty, and chain-of-custody preservation.  
> **Live Web Application:** [https://shreyajr271.github.io/truthLENS/](https://shreyajr271.github.io/truthLENS/)

---

## 01 | Executive Overview

Modern editing tools and generative AI architectures (diffusion models, neural vocoders, facial reenactment, generative text) produce hyper-realistic media that bypass single-modality detectors. Traditional forensic approaches often fail when:
- Subtle inconsistencies are spread across different formats (e.g., an authentic-looking video paired with a cloned voice and fabricated social text).
- Compression artifacts from messaging platforms mimic tampering.
- Automated systems output binary black-box verdicts ("Real" vs. "Fake") without evidentiary traceability or explainable confidence intervals.

**TruthLens** is an explainable multimodal digital forensics platform engineered for cyber-investigators, fact-checkers, and digital forensics laboratories. Rather than asserting unfounded certainty, TruthLens treats model predictions as calibrated forensic indicators, reveals spatial and temporal coordinates of anomalies, compares cross-modal signals, and produces a structured, courtroom-ready evidentiary dossier.

---

## 02 | Web Audit & Score Optimization (>95% Across All Metrics)

To resolve all 27 audit issues (1 Critical, 5 High, 11 Medium, 10 Low) identified by SEOWebChecker / Google Lighthouse and boost the overall score from **86/100** to **>95/100**:

| Category | Previous | Target | Fixes Implemented |
| :--- | :---: | :---: | :--- |
| **Security** | 63/100 | **98/100** | Content-Security-Policy (CSP) meta tag, Strict Referrer Policy, `X-Content-Type-Options: nosniff`, `Permissions-Policy`, sanitized inputs, and hardened external links (`rel="noopener noreferrer"`). |
| **UX & Interaction** | 77/100 | **98/100** | Interactive Methodology & Problem Statement 04 guide modal, floating Toast notifications, "Copy Case Brief" action, keyboard shortcuts (`ESC` to close, arrow key video scrubbing), and sticky footer with Back-to-Top navigation. |
| **SEO** | 80/100 | **98/100** | Canonical URL tag, search engine directives (`robots.txt`), XML Sitemap (`sitemap.xml`), clean 156-character meta description, semantic `<h1>`–`<h4>` heading hierarchy, and UTF-8 entity sanitization. |
| **Schema Markup** | 80/100 | **100/100** | Comprehensive JSON-LD structured data graph including `WebApplication`, `FAQPage` (4 rich forensic Q&As), and `BreadcrumbList`. |
| **Social / Open Graph** | 85/100 | **100/100** | Complete Open Graph (`og:title`, `og:description`, `og:image`, `og:url`, `og:type`) and Twitter Card (`summary_large_image`) tags with dedicated high-res vector icon `favicon.svg`. |
| **Mobile & PWA** | 89/100 | **98/100** | Responsive touch targets (>= 44px min-height), progressive web app `manifest.json`, theme-color meta, and viewport scaling configuration (`user-scalable=yes, maximum-scale=5.0`). |
| **Accessibility (a11y)** | 90/100 | **98/100** | Screen reader skip link (`.skip-link`), ARIA live announcer (`#aria-announcer`), `prefers-reduced-motion` CSS query, WCAG AAA compliant badge contrast, and full keyboard focus rings. |

---

## 03 | Core Forensic Capabilities

| Capability | Technical Forensic Mechanism | Explainability Feature |
| :--- | :--- | :--- |
| **Image Authenticity** | Real-time Error Level Analysis (ELA) with adjustable DCT compression amplification (10x–60x), Photo-Response Non-Uniformity (PRNU) sensor noise gradient extraction, and EXIF/Quantization table inspection. | Visual heatmap overlay, localized bounding box coordinates `[x, y, w, h]`, and quantization anomaly flags. |
| **Video Forensics** | Temporal frame-by-frame scrubbing, physiological eye blink frequency tracking (baseline 12–18 blinks/min), lip-sync viseme-phoneme phase drift, and boundary warping optical flow detection. | Temporal anomaly heat-strip, synchronized playhead, and keyframe warp tags. |
| **Audio & Voice Forensics** | Web Audio API real-time FFT spectrum analysis, neural vocoder spectral cutoff detection (e.g. sharp drop at 7.8 kHz or 16 kHz), pitch roboticism stability, and ambient noise floor silence profiling. | Interactive frequency spectrogram, live acoustic oscilloscope, and bandwidth cutoff markers. |
| **Text & Context Forensics** | Natural Language entity extraction (temporal claims, geolocation, meteorological claims, speaker attribution) cross-checked against media sensor realities. | Highlighted claim-conflict tokens and ground-truth contradiction table. |
| **Cross-Modal Correlation** | 5-axis Inter-Modal Congruence Matrix measuring corroboration vs. conflict across Audio-Visual, Video-Text, Audio-Text, Image-Text, and Metadata-Physics. | Interactive 5-point radar polygon and prioritized inconsistency alert feed. |
| **Calibrated Confidence** | Calibrated score with explicit margin of error (e.g. `91% ± 6%`), accompanied by benign alternative explanations (e.g. codec transcode, low-bitrate compression). | "Honest Uncertainty" disclosures and 5-point human verification checklist. |
| **Chain of Custody (ISO 27037)** | SHA-256 cryptographic digest calculation per asset immediately upon ingestion, byte-level tracking, and tamper audit ledger. | Complete evidentiary table and single-click JSON export. |
| **Forensic Dossier** | Formal printable investigative report formatted with official seals, investigator sign-off blocks, and high-contrast courtroom styling. | Dedicated `@media print` CSS layout for PDF/paper exports. |

---

## 04 | 5-Stage Analysis Workflow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  01 INGEST  │ ──> │ 02 ANALYZE  │ ──> │03 CORRELATE │ ──> │  04 REVIEW  │ ──> │  05 REPORT  │
│ Multi-Modal │     │ ELA, Audio, │     │ Inter-Modal │     │ Calibrated  │     │ Printable   │
│ Drag & Drop │     │ Video, Text │     │ Radar Feed  │     │ Uncertainty │     │ Dossier/JSON│
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

1. **Ingest:** Upload target media (Image, Video, Audio, Context Text) or choose from preloaded high-profile forensic cases. Real-time SHA-256 hash calculated in-browser via Web Crypto API.
2. **Analyze:** Inspect individual modality viewers (toggle between Original, ELA, and Sensor PRNU; play audio stream with live spectrogram; scrub video frames).
3. **Correlate:** Review the Cross-Modal Radar and inconsistency feed to identify conflicts between visual scene, acoustic environment, and textual claims.
4. **Review:** Examine calibrated confidence intervals, review benign alternative explanations, and complete the human investigator verification checklist.
5. **Report:** Generate the official TruthLens Forensic Dossier for presentation or export JSON data into Digital Evidence Management Systems (DEMS).

---

## 05 | Preloaded Forensic Case Studies

TruthLens includes 4 preloaded forensic cases:

1. **Case TL-2026-081: "Diplomatic Summit Fabricated Address"**
   - *Threat Level:* Critical Disinformation
   - *Modalities:* Deepfake Video, Neural Cloned Audio, Telegram Transcript, Spliced Image
   - *Key Anomaly:* Visual speech visemes desynchronized from audio (+195 ms); transcript claims "heavy downpours" while visual frames exhibit overhead direct sunlight and dry pavement.
2. **Case TL-2026-094: "CEO Treasury Wire Authorization Fraud"**
   - *Threat Level:* High Financial Fraud
   - *Modalities:* WhatsApp Voice Note, Spliced Wire Invoice PDF/PNG, Mobile Context
   - *Key Anomaly:* Audio lacks airport tarmac ambiance (anechoic TTS output); invoice ELA demonstrates digital bank seal was spliced in Photoshop on a desktop workstation.
3. **Case TL-2026-112: "Wildfire Catastrophe Photo Manipulation"**
   - *Threat Level:* Moderate Social Panic Propaganda
   - *Modalities:* Diffusion Composite Image, News Tweet
   - *Key Anomaly:* AI-generated smoke fractal vortex artifacts; vertical smoke plume contradicts claimed 65 mph gale force winds.
4. **Case TL-2026-042: "Verified Official Press Briefing"**
   - *Threat Level:* Clean (High Authenticity Corroboration)
   - *Modalities:* DSLR Canon RAW, Studio Microphone, Wire Transcript
   - *Key Anomaly:* Zero manipulation indicators; uniform sensor PRNU noise, natural vocal cord jitter, and hardware C2PA authenticity provenance credentials.

---

## 06 | How to Push to GitHub Pages

To deploy these updates to your live site at `https://shreyajr271.github.io/truthLENS/`:

```powershell
# In your truthLess repository directory:
git add .
git commit -m "Optimize website for >95% score: Security headers, JSON-LD Schema, PWA manifest, UX toast notifications, accessibility, and problem statement alignment"
git push origin main
```

Within 1–2 minutes, GitHub Pages will deploy the updated bundle. Re-running the audit on **SEOWebChecker.com** will register the upgraded score (>95%).

---

## 07 | Forensic Trust Statement

> *"A detection score is an indicator, not a final verdict."*  
> TruthLens preserves evidence context, calculates cryptographic checksums, highlights anomaly locations, and presents honest limitations to empower human investigators in reaching sound evidentiary conclusions.
