# BhramGuard

BhramGuard is a phishing and social engineering detection project focused on identifying suspicious messages and explaining the warning signs behind each risk score.

The planned system uses a hybrid approach: NLP feature extraction, URL/domain spoofing checks, and LLM-assisted scoring. It is designed to support a browser extension, a dashboard, a backend API, scan history, risk explanations, and user feedback for future model improvement.

## Repository Layout

```text
BhramGuard-/
|-- About Project.md          # Detailed project description and Phase 1 scope
|-- README.md                 # Repository overview and setup notes
|-- backend/                  # Planned backend API
|-- docs/                     # Planned project documentation
|-- dashboard/                # Next.js dashboard app
`-- bhramguard-extension/     # Plasmo browser extension
```

## Current Status

- Dashboard: Next.js starter app in `dashboard/`
- Browser extension: Plasmo starter extension in `bhramguard-extension/`
- Backend: folder created for the planned API
- Docs: folder created for future technical documentation

For the detailed product scope, see [About Project.md](About%20Project.md).

## Getting Started

### Dashboard

```bash
cd dashboard
npm install
npm run dev
```

Open `http://localhost:3000` in your browser.

### Browser Extension

```bash
cd bhramguard-extension
npm install
npm run dev
```

Load the generated development extension from:

```text
bhramguard-extension/build/chrome-mv3-dev
```

## Planned Phase 1 Features

- User authentication with JWT
- Message scanning through an API
- Browser extension one-click scanning
- Hybrid risk analysis engine
- Risk tier classification
- Explainable warning signals
- Scan history dashboard
- False positive and false negative feedback
- Testing and validation against phishing datasets

## Development Notes

- Do not commit `node_modules`, generated builds, local environment files, or caches.
- Keep implementation-specific setup inside each subproject directory.
- Keep project planning and architecture notes in `docs/` as the system grows.
