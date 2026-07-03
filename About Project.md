# BhramGuard

BhramGuard is a phishing and social engineering defense project designed to detect, score, and explain suspicious messages before users interact with them. The project combines classical NLP signals, URL/domain analysis, and LLM-assisted reasoning to identify AI-generated phishing attempts, impersonation, urgency tactics, and manipulation patterns.

## Project Vision

Modern phishing messages are increasingly realistic, personalized, and AI-generated. BhramGuard aims to help users understand not only whether a message is risky, but also why it was flagged. The system is planned as a complete workflow across a backend API, browser extension, user dashboard, and feedback loop for future model improvement.

## Core Objective

Detect and explain phishing or social engineering attempts in real time using a hybrid analysis pipeline:

- Classical NLP feature extraction
- URL and domain spoofing checks
- LLM-based manipulation and intent scoring
- Weighted risk scoring from 0 to 100
- Human-readable explanations and highlighted warning signals

## Current Repository Structure

```text
BhramGuard-/
|-- About Project.md
|-- README.md
|-- backend/
|-- docs/
|-- dashboard/
|   |-- app/
|   |   |-- globals.css
|   |   |-- layout.tsx
|   |   `-- page.tsx
|   |-- public/
|   |-- package.json
|   |-- package-lock.json
|   |-- next.config.ts
|   |-- tsconfig.json
|   `-- README.md
`-- bhramguard-extension/
    |-- assets/
    |   `-- icon.png
    |-- popup.tsx
    |-- package.json
    |-- package-lock.json
    |-- tsconfig.json
    `-- README.md
```

## Planned Architecture

```text
Browser Extension / Dashboard
        |
        v
Backend API
        |
        v
Risk Analysis Engine
        |
        |-- NLP feature extraction
        |-- URL and domain checks
        |-- LLM scoring
        `-- Weighted risk classification
        |
        v
Scan result, explanation, highlights, and history
```

## Phase 1 Feature Scope

### Authentication

- User registration with email and password
- Login with JWT issuance
- Current user endpoint
- Password hashing with bcrypt
- Protected routes using JWT validation
- Client-side logout and token removal

### Message Scanning

- Text scanning through an API endpoint
- Browser extension scan trigger for visible page or email text
- CSV-based bulk scanning for dataset testing
- User-specific scan history

### Risk Analysis Engine

- Urgency language detection
- Authority impersonation detection
- Reward and threat framing detection
- Grammar and wording anomaly checks
- URL and domain spoofing detection
- Typosquatting and lookalike domain checks
- Redirect chain inspection
- LLM-assisted manipulation intent classification
- Weighted risk score from 0 to 100
- Risk tiers: Low, Medium, High, and Critical

### Explainability

- Clear explanation of triggered risk signals
- Highlighted suspicious phrases in the original message
- Dashboard view for flagged message sections

### Dashboard

- Login-gated dashboard access
- Scan history list and detail views
- Risk badge visualization
- Basic analytics for scan count and risk distribution

### Browser Extension

- Manifest V3-compatible browser extension
- Content extraction from emails and webpages
- Popup scan action
- Inline risk result display
- Local scan history cache
- JWT-based authentication against the local API

### Feedback Loop

- Mark scans as false positive or false negative
- Store feedback for future model retraining and validation

### Testing And Validation

- Unit tests for authentication
- Unit tests for scanning
- Unit tests for the risk engine
- Precision and recall evaluation against labeled phishing datasets
- Manual validation against real-world sample messages
- Target precision above 85% before Phase 1 is considered complete

## Technology Stack

| Area | Planned / Current Technology |
| --- | --- |
| Dashboard | Next.js, React, TypeScript, Tailwind CSS |
| Browser extension | Plasmo, React, TypeScript, Manifest V3 |
| Backend | Python API planned |
| Authentication | JWT, bcrypt planned |
| Risk scoring | Hybrid NLP, domain analysis, and LLM scoring planned |
| Testing | Unit and validation tests planned |

## Current Implementation Status

- `dashboard/` contains a Next.js starter application.
- `bhramguard-extension/` contains a Plasmo browser extension starter.
- `backend/` and `docs/` directories are present for future backend and documentation work.
- The Phase 1 feature list above describes the intended build scope and does not change existing application behavior.
