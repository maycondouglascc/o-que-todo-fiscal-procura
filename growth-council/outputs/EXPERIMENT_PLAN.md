# Experiment Backlog

Status: READY
Run ID: `RUN-20260912-124721`
Owner: Experimentation
Evidence Used: E-001, E-005, E-006, E-007, E-008
Assumptions: A-001, A-004, A-005
Confidence Score: 64/100

## Method

Score = `Impact × Confidence ÷ Effort`, cada dimensão 1–5. A métrica primária é compra aprovada por sessão qualificada. Clique e início de checkout são métricas antecedentes; usar guardrails de refund, erro de checkout e qualidade da entrega.

## Experiment EXP-001 — Prova real

Hypothesis: amostras reais aumentam confiança e compra aprovada porque tornam o mecanismo verificável.
Evidence: E-007; ausência atual de amostras. Os retratos E-010/E-011 resolvem identificação do autor, não prova do conteúdo.
Control: página atual com slots/sem conteúdo real.
Variant: sumário + duas páginas + checklist legíveis.
Primary Metric: compra aprovada por sessão.
Secondary Metric: início de checkout.
Guardrail Metric: taxa de refund/erro de entrega.
Expected Impact: alto; Confidence: 4/5; Effort: 3/5; Priority: P0.
Decision Rule: vencer somente com janela/amostra definidas antes e sem piora de guardrail.

## Experiment EXP-002 — Promessa do hero

Hypothesis: promessa observável supera “mais segurança” em entendimento e compra.
Evidence: E-005; sem CVR (`E-001`).
Control: “Emita notas fiscais com mais segurança.”
Variant: “Saiba o que conferir na sua NFS-e antes de enviá-la.”
Primary Metric: compra aprovada por sessão.
Secondary Metric: CTA e checkout iniciado.
Guardrail Metric: bounce/tempo de leitura.
Expected Impact: alto; Confidence: 4/5; Effort: 2/5; Priority: P1.
Decision Rule: usar holdout e não declarar vitória por CTR isolado.

## Experiment EXP-003 — CTA

Hypothesis: nomear entrega reduz hesitação.
Evidence: E-005.
Control: “Quero revisar minhas notas com mais segurança”.
Variant: “Acessar o guia e os 2 bônus”.
Primary Metric: compra aprovada por sessão.
Secondary Metric: checkout iniciado.
Guardrail Metric: refund e suporte pré-compra.
Expected Impact: médio/alto; Confidence: 4/5; Effort: 1/5; Priority: P1.
Decision Rule: medir por posição e origem.

## Experiment EXP-004 — Segmentação

Hypothesis: uma página para MEI/prestador supera a página ampla; contadores respondem melhor a outra promessa.
Evidence: E-005, A-001.
Control: público misto.
Variant: hero e exemplos para MEI/prestador.
Primary Metric: compra aprovada por sessão qualificada.
Secondary Metric: conversão por origem.
Guardrail Metric: custo por compra e refunds.
Expected Impact: alto; Confidence: 3/5; Effort: 2/5; Priority: P1.
Decision Rule: manter páginas separadas apenas com volume mínimo pré-definido.

## Experiment EXP-005 — Preço

Hypothesis: o gargalo é confiança, não preço; alterar preço antes da prova gera aprendizado fraco.
Evidence: E-001, E-007, A-004.
Control: preço atual confirmado no checkout.
Variant: preço alternativo só depois do baseline.
Primary Metric: contribuição por sessão, não somente CVR.
Secondary Metric: AOV e checkout iniciado.
Guardrail Metric: refund e margem.
Expected Impact: alto; Confidence: 2/5; Effort: 3/5; Priority: P2.
Decision Rule: não testar até custo/margem e checkout estarem confirmados.

## Experiment EXP-006 — Instrumentação

Hypothesis: eventos de compra aprovada revelam gargalo diferente do clique.
Evidence: E-006. Hook local `recordApprovedPurchase` now exists, but provider-side confirmation is not connected.
Control: dataLayer local.
Variant: eventos reconciliados com checkout e UTMs.
Primary Metric: completude/qualidade dos dados.
Secondary Metric: funil por dispositivo/origem.
Guardrail Metric: duplicação e consentimento.
Expected Impact: crítico; Confidence: 5/5; Effort: 3/5; Priority: P0.
Decision Rule: não escalar tráfego enquanto purchase não for reconciliável.

## Backlog prioritário

| Priority | Experiment | Score orientativo | Owner |
|---|---|---:|---|
| P0 | Prova real + instrumentação | 20/15 e 25/15 | Creative/Funnel |
| P1 | Hero + CTA + segmentação | 10, 16 e 7,5 | Copy/Market |
| P2 | Preço | 10/3 | Offer/Funnel |
| P3 | Refinamentos visuais | após baseline | UX/Creative |

## Post-input update — 2026-09-12

EXP-001 (prova real) foi implementado como baseline visual: três cards com capas e páginas internas reais, sem alterar preço. Medir cliques no CTA e compra aprovada depois que o checkout fornecer integração; sem tráfego ou números atuais, ainda não há resultado de teste.
