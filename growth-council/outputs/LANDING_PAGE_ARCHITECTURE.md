# Landing Page Architecture

Status: READY
Run ID: `RUN-20260912-124721`
Owner: UX
Evidence Used: E-005, E-006, E-007, E-008
Assumptions: A-001, A-002, A-003, A-004
Confidence Score: 74/100

## Section-by-section plan

| # | Section | Purpose | Primary Question Answered | Copy | Visual | CTA | Objection | Proof | Mobile Behavior |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | Hero | Orientar e qualificar | É para mim e o que ganho? | Promise específica + 3 bullets | Mockup fiel + amostra real | Acessar guia e bônus | Não entendi o produto | Página real | CTA full-width; amostra visível sem scroll excessivo |
| 2 | Problema | Criar identificação | Que dúvida isso resolve? | 3 perguntas atuais | Cards simples | Nenhum | Minha dúvida é específica | Linguagem de cliente a validar | Stack vertical |
| 3 | Mecanismo | Tornar o método compreensível | Como organizo a revisão? | Fluxo em cinco pontos | Linha de etapas | Nenhum | Parece abstrato? | Baseado nos entregáveis declarados | Grid 2 colunas |
| 4 | Prova do material | Reduzir risco | Posso ver antes? | Sumário, 2 páginas e checklist quando disponíveis | Recortes legíveis | CTA secundário opcional | É conteúdo superficial? | Produto real | Carousel/stack com zoom acessível |
| 5 | O que recebe | Tornar escopo concreto | O que está incluso? | Core + cada bônus + uso | Mockups fiéis | Acessar oferta | O bônus é enfeite? | Entregáveis reais | Um item por bloco |
| 6 | Para quem é/não é | Filtrar público | Serve para meu caso? | MEI/prestador primário; limites | Tags e aviso | Nenhum | Município/contador | FAQ/escopo | Texto curto e escaneável |
| 7 | Autor | Identificar responsável | Quem assina? | Bio factual + retrato | Fotos fornecidas | Nenhum | Posso confiar? | Autorização do asset | Imagem em largura confortável |
| 8 | Oferta e garantia | Fechar decisão | Quanto custa e qual risco? | Preço confirmado + política | Card limpo | CTA principal | Pagamento/garantia | Checkout/política | CTA e preço antes do fold da seção |
| 9 | FAQ | Remover fricção | O que acontece depois? | Acesso, formato, município, garantia | `details` atual | CTA após FAQ | Operação incerta | Informação operacional | Uma pergunta por linha |
| 10 | Fechamento | Reforçar ação | Qual é o próximo passo? | Promise + entrega | Fundo contrastante | CTA claro | Hesitação final | Microcopy de checkout | Sticky só quando CTA não estiver visível |

## Structural decision

Mover a prova real para antes de autor/oferta e remover a seção de slots vazios enquanto os arquivos não forem fornecidos. A sequência atual é coerente, mas a prova chega tarde e é explicitamente incompleta (`E-007`, `E-008`).

## Recommendation metadata

| Recommendation | Priority | Impact | Confidence | Effort | Evidence | Owner |
|---|---:|---:|---:|---:|---|---|
| Substituir slots por prova real ou remover bloco | P0 | 5 | 5 | 2 | RESEARCH | UX |
| Fazer o CTA explicar o destino/entrega | P1 | 4 | 4 | 1 | INFERENCE | UX |

## Post-input update — 2026-09-12

A etapa de prova foi atualizada para uma seção real de amostras antes da oferta: capa + página interna dos três PDFs, com destaque para o checklist mensal. O bloco de slots vazios não existe mais na página publicada.
