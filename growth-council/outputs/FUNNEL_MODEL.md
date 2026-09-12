# Funnel Model

Status: READY
Run ID: `RUN-20260912-124721`
Owner: Funnel
Evidence Used: E-001, E-002, E-005, E-006
Assumptions: A-003, A-005
Confidence Score: 32/100

## Model inputs and formulas

Modelo de sensibilidade, não previsão. Assumptions: 1.000 visitantes; preço core R$47; bump candidato R$17 com 10% take rate; upsell candidato R$97 com 5% take rate; custo variável total 10%; mídia R$1.000 por cenário. Não há dados de margem, impostos ou checkout (`E-001`, `E-002`).

`AOV = 47 + (17 × 10%) + (97 × 5%) = R$53,55`.

`Contribution/order = AOV × (1 - 10%) = R$48,20`.

`Break-even CAC = contribution/order`; recalcular com custos reais.

## Traffic Source

UNKNOWN. Não comprar mídia até escolher fonte, eventos e baseline.

## Front-End Offer

Price: R$47 Pix / R$49,90 cartão (page claim).
Expected CVR: UNKNOWN; 1,5% é cenário Base, não benchmark.

## Order Bump

Product: candidato a checklist/planilha complementar — não confirmado.
Price: R$17 ASSUMPTION.
Expected Take Rate: 10% ASSUMPTION.

## Upsell

Product: candidato a orientação/pack avançado — não inventar como deliverable.
Price: R$97 ASSUMPTION.
Expected Take Rate: 5% ASSUMPTION.

## Downsell

Nenhum definido. Só criar após observar rejeição do upsell.

## Backend Offer

UNKNOWN. Possíveis serviços ou atualização precisam de validação de capacidade, margem e compliance.

## Expected AOV

R$53,55 no cenário ilustrativo. Core-only AOV observado ainda UNKNOWN.

## Target CAC

No modelo ilustrativo, abaixo de R$48,20 por compra; não é target financeiro aprovado.

## Break-Even CAC

R$48,20 no modelo ilustrativo; incluir taxa HeroSpark, impostos, reembolsos, suporte e custos reais.

## Expected LTV

UNKNOWN. Não há recompra, backend, cancelamento ou coorte.

## Funnel Economics

Landing Page → Core Offer → checkout HeroSpark. Bump, upsell e backend são hipóteses futuras. `app.js` mede clique local, mas não compra aprovada (`E-006`).

## Sensitivity Analysis

| Scenario | Visitors | CVR | Purchases | Revenue | AOV | CAC (R$1.000 spend) | Ad spend | Contribution margin after media | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Conservative | 1.000 | 0,8% | 8 | R$428,40 | R$53,55 | R$125,00 | R$1.000 | -R$614,40 | 0,43 |
| Base | 1.000 | 1,5% | 15 | R$803,25 | R$53,55 | R$66,67 | R$1.000 | -R$277,00 | 0,80 |
| Aggressive | 1.000 | 2,2% | 22 | R$1.178,10 | R$53,55 | R$45,45 | R$1.000 | R$60,40 | 1,18 |

Fórmulas: `revenue = purchases × AOV`; `contribution after media = purchases × R$48,20 - ad spend`; `ROAS = revenue ÷ ad spend`. Todos os números são `ASSUMPTION`.

## Recommendation metadata

| Recommendation | Priority | Impact | Confidence | Effort | Evidence | Owner |
|---|---:|---:|---:|---:|---|---|
| Instrumentar compra aprovada e custos reais antes de escalar | P0 | 5 | 5 | 3 | DATA | Funnel |
| Validar core offer antes de bump/upsell | P1 | 4 | 4 | 2 | INFERENCE | Funnel |
