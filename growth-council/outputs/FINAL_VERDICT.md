# Growth Council Verdict

Status: READY
Run ID: `RUN-20260912-124721`
Chair: Growth Council Chair
Evidence Used: E-001–E-015
Assumptions: A-001–A-007
Confidence Score: 84/100

## Executive Summary

1. A base visual e a arquitetura permanecem boas, e os dois retratos fornecidos foram integrados.
2. Placeholders visíveis, claims de credenciais não confirmados e `noindex` foram removidos/corrigidos.
3. A prova verificável do conteúdo foi inserida; o gargalo restante é a conexão real da compra aprovada.
4. O ICP inicial deve ser MEI/prestador que emite NFS-e por conta própria; contador fica em variante.
5. A promessa deve sair de “mais segurança” para uma tarefa observável de conferência.
6. Não reprecificar antes de baseline e custos reais.
7. Instrumentar compra aprovada, não apenas clique.
8. Não usar urgência, escassez ou prova social sem evidência.
9. O próximo release é de validação operacional e medição; a prova do conteúdo já está no release atual.

## Primary Problem

A landing page clara e visualmente comprovável, porém ainda dependente de validação operacional do checkout e de dados reais para decidir escala.

## Root Cause

A mensagem e o design avançaram mais rápido que o fechamento da operação e da mensuração; os três PDFs agora fecham a principal lacuna de prova (`E-012`–`E-014`), mas checkout e economia continuam sem evidência (`E-001`, `E-006`).

## Strategic Decision

Não levar tráfego pago significativo até validar o pacote final, inserir páginas reais do conteúdo ou aceitar formalmente operar sem essa prova, confirmar checkout/garantia e conectar o evento de compra aprovada. Depois testar promessa, CTA e ICP sem reprecificar simultaneamente.

## Implementation Status

| Item | Status | Evidence |
|---|---|---|
| Retratos do autor | RESOLVED | `autor-ivan-goncalves.jpeg`, `autor-ivan-goncalves-detalhe.png`, uso autorizado nesta implementação (`E-010`, `E-011`, `E-015`) |
| Placeholders e seção vazia | RESOLVED | `index.html` sem `[A CONFIRMAR]`/slots de amostra |
| Headline e CTA específicos | RESOLVED | hero e CTAs atualizados; `app.js` mantém variante segura |
| `noindex,nofollow` | RESOLVED | `meta robots=index,follow` |
| Credenciais não comprovadas | MITIGATED | claims numéricos/formacionais removidos; os PDFs têm referências divergentes de experiência e não foram usados como credencial única |
| Prova real do conteúdo | RESOLVED | três PDFs fornecidos, com capas/páginas internas renderizadas; checklist real do guia principal exibido (`E-012`–`E-014`) |
| Compra aprovada | PARTIAL | hook local + bridge de retorno existem; configuração/validação do checkout externo ainda não existe |
| Custos, CAC, CVR, LTV | OPEN | `inputs/ANALYTICS.md` e `BUSINESS_CONTEXT.md` sem dados |

## Positioning

Uma referência prática para quem emite NFS-e por conta própria e quer saber o que conferir antes de enviar a nota, com limites claros para variações municipais e análise profissional.

## ICP

Hipótese primária: MEIs e prestadores de serviço que emitem NFS-e por conta própria. Segmento secundário: contadores, em landing/creative separados.

## Core Desire

Emitir com clareza sobre os pontos que foram conferidos.

## Core Problem

Dúvidas dispersas sobre código, cadastro, retenções e pendências.

## Core Promise

**Saiba o que conferir na sua NFS-e antes de enviá-la.**

## Unique Mechanism

Checklist por etapas: cadastro → serviço/classificação → retenções → pendências → revisão mensal. Confirmado no guia principal fornecido (`E-012`).

## Offer

### Core Product

eBook “O Que Todo Fiscal Procura”.

### Deliverables

eBook + Guia de Correlação NBS, IBS e CBS + Guia de Erros da NFS-e Nacional + checklist, glossário e orientação inicial, se confirmado no pacote final.

### Bonuses

Dois guias bônus. Cada um mostra a dúvida que resolve, e capas/páginas internas dos três PDFs estão na prova visual (`E-012`–`E-014`).

### Guarantee

7 dias com instrução para solicitar pelo canal indicado no checkout; a política exibida no checkout deve prevalecer e ser conferida antes do tráfego.

### Price

Manter R$47 Pix / R$49,90 cartão / até 5× R$11 como controle, se o checkout confirmar.

### Anchor

Nenhuma âncora até existir referência real.

### Urgency

Nenhuma; não criar urgência artificial.

### Scarcity

Nenhuma; não criar escassez artificial.

## Funnel

Traffic → Landing Page → Core Offer → checkout HeroSpark → entrega digital → eventual bump/upsell/backend após validação.

## Unit Economics

Price: R$47 core, page claim.
AOV: R$53,55 apenas no cenário ilustrativo com bump/upsell hipotéticos.
Target CVR: UNKNOWN; 1,5% é cenário Base, não benchmark.
Target CAC: abaixo da contribuição real por compra; modelo ilustrativo R$48,20.
Break-even CAC: R$48,20 no modelo ilustrativo, sujeito a custos reais.
Target ROAS: não definido sem margem; cenário ilustrativo Base 0,80.

## Messaging

### Big Idea

Trocar a dúvida antes da emissão por uma rotina de conferência visível.

### Headline

Saiba o que conferir na sua NFS-e antes de enviá-la.

### Subheadline

Um guia prático para revisar cadastro, código do serviço, retenções e pendências — com checklist mensal para transformar a conferência em rotina.

### CTA

Acessar o guia e os 2 bônus.

### Key Benefits

Revisar pontos essenciais; entender dúvidas de MEI/Simples; consultar checklist; reconhecer quando buscar ajuda.

### Key Objections

Município, atualização, formato, entrega, credenciais, garantia, pagamento e substituição do contador.

## Landing Page Structure

1. **Hero:** promessa específica, ICP primário, mockup ilustrativo + retrato do autor, CTA de acesso; responde “é para mim e o que recebo?”.
2. **Problema:** manter as três perguntas atuais; responde “qual dúvida resolve?”.
3. **Mecanismo:** fluxo em cinco pontos baseado nos entregáveis declarados; responde “como organizo a revisão?”.
4. **Prova real:** capas, páginas internas e checklist do guia principal exibidos na seção “Veja por dentro”; não exibir amostras que não pertençam à edição comercial.
5. **O que recebe:** core e bônus com finalidade; responde “o que está incluso?”.
6. **Para quem é/não é:** MEI/prestador em primeiro plano e limites municipais; responde “serve para meu caso?”.
7. **Autor:** retratos fornecidos e bio factual, sem credenciais não validadas; responde “quem assina o material?”.
8. **Oferta/garantia:** preço e operação confirmados; responde “quanto custa e qual o risco?”.
9. **FAQ:** acesso, formato, atualização, município, garantia e pagamento sem placeholders.
10. **Fechamento:** mesma promessa + CTA “Acessar o guia e os 2 bônus”.

## Creative Direction

Conceito “Da dúvida à conferência”. Os retratos fornecidos foram aplicados na autoria e no resumo da dobra inicial (`E-010`, `E-011`, `E-015`). Capas, páginas internas e checklist reais dos PDFs agora funcionam como prova visual (`E-012`–`E-014`); mockup continua rotulado como ilustrativo.

## Design Direction

Manter responsividade, `srcset`, skip link, foco visível, FAQ nativa e sticky mobile. Reduzir repetição de “clareza/rotina/segurança”; slots vazios foram removidos; `noindex,nofollow` foi substituído por `index,follow`.

## Persuasion Strategy

Usar reciprocidade via amostra real e autoridade somente verificável. Clareza e demonstração antes de escassez. Não usar fake testimonials, fake countdown, âncora enganosa ou claim de evitar multa sem fonte.

## Proof Requirements

Capas e páginas internas dos três PDFs; checklist; versão/data de revisão; formato e entrega; política de garantia; autorização dos retratos; preço conferido com checkout; eventual depoimento identificável e autorizado. A prova de conteúdo está resolvida pelos arquivos fornecidos; operação, política e prova social continuam externas.

## What We Will NOT Do

Não esconder placeholders, inventar depoimentos/dados/benchmarks, adicionar urgência/escassez falsa, declarar compra por clique, reprecificar sem baseline ou prometer ausência de multa.

## Risks

Claim regulatório de “não levar multa”; variação municipal; conteúdo desatualizado; credenciais pendentes; checkout divergente; falta de purchase tracking; tráfego pago com margem insuficiente.

## Unknowns

CVR, CAC, AOV, LTV, refunds, margem, custos, origem, ICP vencedor, customer language, concorrentes, atualização, entrega e garantia operacional.

## Assumptions

A-001 ICP; A-002 conteúdo; A-003 operação/claims; A-004 gargalo de confiança; A-005 bump/upsell; A-006 staging/SEO; A-007 autorização dos retratos.

## Experiments

### P0

EXP-001 prova real; EXP-006 conexão de compra aprovada. Remoção de placeholders e correção de `noindex` já executadas.

### P1

EXP-002 headline; EXP-003 CTA; EXP-004 segmentação.

### P2

EXP-005 preço após baseline.

### P3

Refinamentos visuais e SEO depois dos gates de confiança e medição.

## Implementation Plan

### Phase 1 — Foundation

Fechar versão comercial, entrega, garantia, checkout e escopo municipal. Conteúdo e retratos foram integrados; registrar a autorização formal antes da publicação pública.

### Phase 2 — Offer

Confirmar stack; não adicionar bump/upsell antes do core offer.

### Phase 3 — Copy

Adotada promessa/CTA específicos e removido claim de multa sem evidência da descrição principal.

### Phase 4 — Design

Retratos integrados, slots vazios removidos, hierarquia ajustada e amostras reais dos três PDFs inseridas.

### Phase 5 — Build

Removidos placeholders visíveis, meta alterada para `index,follow` e eventos `CheckoutOutbound`/hook `recordApprovedPurchase`/bridge de retorno implementados.

### Phase 6 — Launch

QA mobile/teclado/checkout; confirmar autorização dos retratos e conexão de compra antes do tráfego.

### Phase 7 — Optimize

Executar EXP-001/006, depois hero/CTA/ICP; decidir por compra aprovada e guardrails.

## Council Confidence Score

78/100. A página está mais publicável e sem pendências internas visíveis, mas faltam customer research, analytics de produção, custos, páginas reais do produto, autorização formal dos retratos e confirmação externa do checkout/política.

## Recommendation metadata

| Recommendation | Priority | Impact | Confidence | Effort | Evidence | Owner |
|---|---:|---:|---:|---:|---|---|
| Fechar operação e remover placeholders | P0 | 5 | 5 | 2 | RESEARCH | Chair |
| Inserir prova real do conteúdo | P0 | 5 | 5 | 3 | RESEARCH | Creative |
| Instrumentar compra aprovada | P0 | 5 | 5 | 3 | RESEARCH | Funnel |
| Testar ICP, hero e CTA | P1 | 5 | 3 | 2 | HYPOTHESIS | Market/Copy |
| Testar preço apenas após baseline | P2 | 4 | 2 | 3 | HYPOTHESIS | Offer/Funnel |
