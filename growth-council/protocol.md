# Growth Council Protocol

## State machine

```text
INTAKE
  ↓
DIAGNOSIS (parallel, independent)
  ↓
SPECIALIST_OUTPUTS (dependency order)
  ↓
DEBATE (conflicts extracted by Chair)
  ↓
CROSS_EXAMINATION (direct response)
  ↓
VERDICT (decision, minority, or experiment)
```

`RED_TEAM` and `CRITIQUE` são modos de revisão que podem ser executados após qualquer estado com material suficiente. Uma mudança de evidência deve gerar novo `Run ID`; não se reescreve uma decisão histórica.

## Intake

O executor lê todos os arquivos de `inputs/` e cria `PROJECT_CONTEXT.md`, `EVIDENCE_LEDGER.md` e `ASSUMPTIONS.md`. Arquivos vazios ou claims sem fonte permanecem unknown/assumption. Ausência não é zero.

## Diagnóstico independente

Cada especialista responde as sete perguntas do round 1 sem consultar a conclusão de outro agente. O objetivo é detectar divergência antes do efeito de grupo.

## Dependências

Market → Offer → Funnel → Copy → Creative → UX/CRO → Persuasion → Experimentation → Chair. Um downstream pode emitir `CHALLENGE`, nunca alterar upstream sem log.

## Debate e cross-examination

O Chair seleciona conflitos que afetam posicionamento, oferta, economia, promessa, prova, risco ou fricção. Cada posição deve citar evidência e declarar assumptions. A resolução pode ser:

- `DECISION`: evidência suficiente;
- `MAJORITY DECISION + MINORITY POSITION`: decisão com dissenso explícito;
- `HYPOTHESIS`: explicação ainda não demonstrada;
- `EXPERIMENT`: duas alternativas razoáveis e decisão reversível;
- `NEEDS_INPUT`: risco alto e ausência de informação essencial.

## Claim taxonomy

`FACT` = fornecido e verificável; `DATA` = medição observada; `CUSTOMER EVIDENCE` = fala/comportamento de cliente; `RESEARCH` = fonte externa registrada; `INFERENCE` = conclusão derivada; `ASSUMPTION` = premissa não verificada; `OPINION` = preferência; `HYPOTHESIS` = previsão falsificável.

## Severidade

P0 bloqueia confiança, legalidade, medição ou funcionamento. P1 tem alto impacto e deve preceder polish. P2 é melhoria média. P3 é refinamento. Impacto, confiança e esforço usam escala 1–5.

## Reexecução

Quando chegam novos dados, atualize inputs, rode `analyze`, compare o novo ledger com `DECISION_LOG.md` e só reabra decisões afetadas pela evidência nova.
