# UX/CRO Audit

Status: READY
Run ID: `RUN-20260912-124721`
Owner: UX
Evidence Used: E-005, E-006, E-007, E-008, E-010, E-011
Assumptions: A-003, A-004, A-007
Confidence Score: 80/100

## Summary

A página tem boa base de estrutura, responsividade e acessibilidade, mas a experiência de decisão é interrompida por pendências internas e falta de demonstração do produto. Não há baseline para afirmar impacto de CVR (`E-001`).

| Finding | Area | Priority | Impact | Confidence | Effort | Evidence | Recommendation |
|---|---|---:|---:|---:|---:|---|---|
| Placeholders e slots vazios expostos | Credibility/friction | P0 — RESOLVED | 5 | 5 | 2 | E-007,E-008 | Removidos da publicação; manter gate para não reintroduzir |
| Hero usa “mais segurança”, pouco observável | Hero clarity | P1 | 5 | 4 | 1 | E-005 | Testar promessa “Saiba o que conferir...” |
| Cinco públicos no mesmo percurso | Relevance/message match | P1 | 5 | 3 | 2 | E-005 | ICP primário MEI/prestador; variante para contador |
| CTA longo não explicita destino/entrega | CTA/friction | P1 | 4 | 4 | 1 | E-005 | “Acessar o guia e os 2 bônus” + microcopy checkout |
| Prova vem como reserva antes de decisão | Information hierarchy | P0 | 5 | 5 | 3 | E-007 | Slots removidos; inserir páginas reais quando fornecidas |
| `noindex,nofollow` pode bloquear descoberta | Launch/SEO | P1 — RESOLVED | 3 | 5 | 1 | E-008 | Meta alterada para `index,follow` |
| Evento local sem compra aprovada | Measurement | P0 — PARTIAL | 5 | 5 | 3 | E-006 | Hook `recordApprovedPurchase` criado; conectar ao checkout |
| FAQ é abrangente, mas tem respostas UNKNOWN | Friction | P0 — MITIGATED | 4 | 5 | 1 | E-008 | Placeholders removidos; confirmar texto operacional no checkout |
| Autorização dos retratos não registrada | Credibility/legal | P1 | 3 | 4 | 1 | E-010,E-011 | Confirmar autorização do titular |
| Base técnica é boa: skip link, focus, details, srcset | Accessibility/technical | P2 | 4 | 4 | 2 | E-005,E-006 | Preservar e fazer QA teclado/mobile |

## What works

Estrutura progressiva, linguagem humana nas dúvidas, CTA repetido, responsividade, `srcset`, foco visível e ressalvas de escopo (`E-005`, `E-006`).

## What does not work yet

Confiança do produto melhorou com retratos e remoção de pendências visíveis; prova de conteúdo e conexão de compra aprovada ainda dependem de assets/checkout. O ganho esperado continua hipótese até medir.

## Checkout transition

O checkout HeroSpark é identificado, mas a página deve dizer exatamente destino, entrega e prazo após confirmação. Registrar `CTA_Click`, início de checkout e compra aprovada em eventos separados; nunca equacionar clique com venda.

## Recommendation metadata

| Recommendation | Priority | Impact | Confidence | Effort | Evidence | Owner |
|---|---:|---:|---:|---:|---|---|
| Fazer QA de publicação: zero placeholders visíveis | P0 | 5 | 5 | 1 | RESEARCH | UX |
| Definir baseline e evento de compra aprovada | P0 | 5 | 5 | 3 | RESEARCH | UX |

## Post-input update — 2026-09-12

Prova visual real implementada em `index.html` na seção “Veja por dentro”, com três PDFs e nove imagens locais verificadas. O gate de conteúdo está resolvido; permanecem o baseline de métricas e a validação do evento de compra no checkout (`E-001`, `E-006`, `E-012`–`E-014`).
