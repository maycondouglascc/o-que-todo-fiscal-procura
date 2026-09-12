# Evidence Ledger

| ID | Type | Source | Claim | Reliability (1-5) | Used by |
|---|---|---|---|---:|---|
| E-001 | ANALYTICS | inputs/ANALYTICS.md | No traffic, CVR, purchases, revenue, CAC or refund data supplied. Blank is UNKNOWN, not zero. | 5 | Funnel, Experimentation, Chair |
| E-002 | ASSUMPTION | inputs/BUSINESS_CONTEXT.md | Cost structure, goals, sources and operating policies are not supplied. | 5 | Funnel, Chair |
| E-003 | CUSTOMER_INTERVIEW | inputs/CUSTOMER_RESEARCH.md | No interviews, reviews or customer language are supplied. | 5 | Market, Copy, Chair |
| E-004 | COMPETITOR | inputs/COMPETITORS.md | No competitor/alternative research is supplied. | 4 | Market, Offer |
| E-005 | RESEARCH | inputs/EXISTING_LANDING_PAGE.md → index.html | Page currently presents eBook + two bonuses, prices, FAQ, author claims and four CTA positions. | 4 | All agents |
| E-006 | RESEARCH | app.js | Attribution is retained in a local dataLayer; CTA clicks are emitted, but no verified analytics ID or purchase confirmation is configured. | 5 | Funnel, UX, Experimentation |
| E-007 | RESEARCH | index.html, colecao-960.webp | The page labels the main image as an illustrative mockup and reserves three slots for real content samples. | 5 | Creative, Persuasion, UX, Chair |
| E-008 | RESEARCH | index.html | Visible `[A CONFIRMAR]` markers remain in delivery, guarantee, author and content details; the page also uses `noindex,nofollow`. | 5 | UX, Persuasion, Chair |
| E-009 | EXPERT_HEURISTIC | RELATORIO-MELHORIAS-LANDING-PAGE.md | Existing audit identifies the same proof, placeholder, ICP, CTA and measurement gaps; treated as secondary expert heuristic. | 3 | Chair |
| E-010 | RESEARCH | user attachment `image-1.jpeg` | Portrait asset supplied for the author section and used as `autor-ivan-goncalves.jpeg`. | 4 | Creative, UX, Chair |
| E-011 | RESEARCH | user attachment `image-2.png` | Detail portrait asset supplied for the author summary and used as `autor-ivan-goncalves-detalhe.png`. | 4 | Creative, UX, Chair |
| E-012 | RESEARCH | user-supplied PDF `O-Que-Todo-Fiscal-Procura-Guia-Pratico-de-Notas-Fiscais-para-Nao-Levar-Multa.pdf` | Product PDF supplied; 23 pages. Cover, internal pages and the “Checklist de Conformidade Mensal” page are rendered under `assets/previews/`. | 5 | Offer, Creative, UX, Persuasion, Chair |
| E-013 | RESEARCH | user-supplied PDF `Bonus-Guia-de-Erros-Mais-Comuns-ao-Emitir-a-NFS-e-Nacional.pdf` | Bonus PDF supplied; 11 pages. Cover and internal consultation page are rendered under `assets/previews/`. | 5 | Offer, Creative, UX, Persuasion, Chair |
| E-014 | RESEARCH | user-supplied PDF `Bonus-Como-Correlacionar-o-Item-de-Servico-com-o-IBS-e-a-CBS.pdf` | Bonus PDF supplied; 13 pages. Cover and internal consultation page are rendered under `assets/previews/`. | 5 | Offer, Creative, UX, Persuasion, Chair |
| E-015 | ASSUMPTION | user message | User authorized use of the supplied PDFs and portrait assets for this landing implementation; retain formal publication record for public launch. | 4 | Creative, UX, Chair |
