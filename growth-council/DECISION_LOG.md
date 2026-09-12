# Decision Log

## DEC-001

Date: 2026-09-12
Decision: tratar a página como não pronta para tráfego pago até remover pendências visíveis e validar entrega, prova, credenciais, preço e garantia.
Context: os elementos estão explicitamente em aberto na própria página.
Alternatives: lançar como está; esconder placeholders; remover blocos incompletos e validar antes do lançamento.
Arguments: `E-007` e `E-008` indicam risco direto de confiança; esconder não corrige a oferta.
Evidence: E-007, E-008, A-002, A-003.
Reason: é uma decisão P0, reversível e de alto impacto na credibilidade.
Owner: Chair + Autor/Negócio
Confidence: 95/100
Reversible: yes
Experiment Required: no — QA/validação operacional required.

## DEC-002

Date: 2026-09-12
Decision: usar MEIs e prestadores de serviço que emitem NFS-e por conta própria como ICP de teste; manter contadores em variação separada.
Context: a página inclui cinco públicos e o código já contém uma variante específica para contadores.
Alternatives: manter todos no mesmo hero; escolher contadores; testar páginas segmentadas.
Arguments: `E-005`, `E-009`; `A-001` permanece hipótese.
Evidence: E-005, E-009.
Reason: reduz ambiguidade sem declarar que o segmento está comprovado.
Owner: Market + Copy
Confidence: 58/100
Reversible: yes
Experiment Required: yes.

## DEC-003

Date: 2026-09-12
Decision: testar primeiro prova real e clareza da promessa; não reprecificar antes de obter baseline.
Context: preço está visível, mas não há analytics nem prova do produto.
Alternatives: reduzir preço; adicionar urgência; inserir amostras reais e medir.
Arguments: `E-001`, `E-006`, `E-007`, A-004.
Evidence: E-001, E-006, E-007.
Reason: é mais informativo e reversível testar confiança antes de atribuir o gargalo ao preço.
Owner: Chair + Experimentation
Confidence: 72/100
Reversible: yes
Experiment Required: yes.

## DEC-004

Date: 2026-09-12
Decision: usar os dois retratos fornecidos, um na seção de autoria e um no resumo da primeira dobra; remover claims de credenciais não confirmadas.
Context: os assets resolvem o placeholder visual, mas não comprovam formação/tempo de experiência.
Alternatives: manter monograma; publicar números sem validação; usar retratos e manter somente informação não controversa.
Arguments: E-010, E-011 e A-007.
Evidence: E-010, E-011.
Reason: aumenta reconhecimento sem fabricar autoridade.
Owner: Creative + Chair
Confidence: 82/100
Reversible: yes
Experiment Required: no.

## DEC-005

Date: 2026-09-12
Decision: remover a seção de amostras vazia até receber páginas reais do produto; não simular prova.
Context: os assets fornecidos são retratos, não páginas do eBook.
Alternatives: manter placeholders; fabricar páginas; remover o bloco e preservar somente claims de entregáveis.
Arguments: E-007, E-010, E-011.
Evidence: E-007, E-010, E-011.
Reason: a ausência de prova é explícita, e remover texto interno evita sinal de produto inacabado.
Owner: Chair + Creative
Confidence: 96/100
Reversible: yes
Experiment Required: yes — inserir páginas reais quando disponíveis.

## DEC-001

Date:
Decision:
Context:
Alternatives:
Arguments:
Evidence:
Reason:
Owner:
Confidence:
Reversible: yes/no
Experiment Required: yes/no
