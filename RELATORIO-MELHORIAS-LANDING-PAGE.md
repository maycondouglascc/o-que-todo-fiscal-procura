# Relatório de melhorias — “O Que Todo Fiscal Procura”

**Data da análise:** 12/09/2026  
**Escopo:** copy, proposta de valor, prova, oferta, conversão, mensuração, confiança e riscos de comunicação.  
**Base analisada:** landing page estática, `index.html`, `app.js`, `styles.css` e o mockup `colecao-960.webp`.

## Resumo executivo

A landing page tem uma base visual sólida e uma arquitetura de venda coerente: o visitante vê a promessa, os problemas, o conteúdo, o público, o autor, a oferta, a garantia e as dúvidas. O tom é sóbrio e adequado a um tema fiscal; a página também evita promessas absolutas em vários trechos e explicita que o material não substitui orientação individual.

Hoje, porém, ela parece mais uma página pronta para revisão do que uma página pronta para vender. O maior problema não é estética: é falta de evidência e de informação operacional confirmada. Há **11 ocorrências de `[A CONFIRMAR]`**, três espaços pedindo páginas reais do eBook, credenciais do autor ainda não verificadas e um mockup explicitamente apresentado como proposta. Isso reduz a confiança justamente nos pontos em que o comprador precisa decidir.

### Prioridades

1. **P0 — Remover todos os placeholders e validar a oferta:** acesso, formato, páginas, atualização, garantia, credenciais e política do checkout.
2. **P0 — Substituir a seção de amostras vazia por prova real:** sumário, páginas internas, checklist e, se existirem, referências/depoimentos verificáveis.
3. **P1 — Tornar a promessa mais específica e menos defensiva:** definir um público principal, um resultado principal e um mecanismo claro.
4. **P1 — Conectar a mensuração ao negócio:** hoje há apenas `dataLayer` local e eventos customizados; não há uma ferramenta/ID verificado nem confirmação de compra.
5. **P1 — Reduzir risco de claim:** “para não levar multa” e variações sobre fiscalização precisam ser sustentadas ou suavizadas.

## 1. Diagnóstico

### 1.1 Fatos observados

- A promessa principal atual é “Emita notas fiscais com mais segurança”, apoiada por três benefícios: identificar erros e pendências, conferir cadastro/regime e usar um checklist mensal (`index.html:20–25`).
- A página vende um eBook principal + dois bônus, com preço de R$ 47 no Pix, R$ 49,90 no cartão à vista ou 5× de R$ 11 (`index.html:24`, `index.html:38`, `index.html:54`, `index.html:57`).
- O checkout é externo, no HeroSpark, mas o texto não informa com precisão o canal de entrega nem o prazo de liberação (`index.html:38`, `index.html:41–44`).
- A seção “Veja antes de decidir” ainda contém três cartões de reserva e diz que as páginas reais precisam ser fornecidas (`index.html:35`).
- A imagem principal é descrita como “Mockup ilustrativo” e “capas propostas para o redesign” (`index.html:26`; `colecao-960.webp`).
- As credenciais — 18+ anos, 10+ anos de análise, formação e pós-graduação — estão marcadas como apresentadas no briefing e “A CONFIRMAR COM O CLIENTE” (`index.html:37`).
- A garantia de sete dias é anunciada, mas canal, procedimento e condições ainda estão em aberto (`index.html:25`, `index.html:39`, `index.html:50`).
- O documento está marcado com `noindex,nofollow` (`index.html:7`). Isso é adequado para staging, mas impede descoberta orgânica se for mantido na publicação.
- O `app.js` registra eventos em um `dataLayer` local e dispara um evento customizado no navegador; ele não conecta a uma plataforma de analytics e não registra confirmação de compra (`app.js:7–13`, `app.js:29–34`).
- Existem quatro posições de CTA — hero, oferta, fechamento e sticky mobile — com a mesma chamada longa (`index.html:24`, `index.html:38`, `index.html:54`, `index.html:57`).
- Há cuidado técnico positivo: responsividade, `srcset`, link de pular conteúdo, estados `focus-visible`, FAQ nativa com `details` e uma barra sticky condicionada ao mobile (`index.html:13`, `app.js:40–57`, `styles.css:1`).

### 1.2 Inferências estratégicas

- O visitante provavelmente está em estágio de consciência **problema/solução**: sabe que tem dúvidas sobre NFS-e, mas ainda não sabe exatamente quais erros revisar nem por que este guia merece confiança.
- A página tenta atender simultaneamente prestadores de serviço, MEIs, autônomos, pequenas empresas e contadores (`index.html:36`). Essa amplitude facilita a inclusão, mas enfraquece a identificação imediata e torna a promessa genérica.
- A página tem mais detalhes sobre o que o material pretende fazer do que evidência de que ele realmente faz isso. Para um produto educacional fiscal, a prova concreta deveria vir antes de uma longa explicação institucional.
- A linguagem visual transmite autoridade e cuidado, mas o mockup sofisticado pode criar uma expectativa de produto final que o texto ainda não confirma.

### 1.3 Lacunas que impedem uma recomendação definitiva

Precisam ser respondidas pelo autor/negócio antes do lançamento:

1. Quem é o comprador principal: MEI/prestador de serviço, pequena empresa ou contador que orienta clientes?
2. Qual é o formato final, número de páginas, data/versão e canal de acesso?
3. O que exatamente os bônus entregam e em que situação prática cada um é usado?
4. Quais credenciais podem ser comprovadas e quais documentos/fontes podem ser citados?
5. Qual é a política de atualização e a regra operacional da garantia?
6. Existe histórico de vendas, feedback, depoimentos ou exemplos de aplicação que possam ser usados com autorização?
7. O preço e o parcelamento exibidos na página correspondem exatamente ao checkout atual?

## 2. O que funciona

### Clareza e estrutura

- A primeira dobra informa categoria, benefício, preço, forma de pagamento, garantia e caminho para compra.
- A sequência de problemas (“Esse código está certo?”, “Meu cadastro está em dia?”, “E se houver uma pendência?”) traduz dúvidas reais em linguagem humana (`index.html:29`).
- A oferta é concreta: nome do produto, dois bônus, checklist, glossário e orientação inicial (`index.html:31–33`, `index.html:38`).
- A FAQ aborda objeções relevantes: município, MEI, contador, notificação, atualização, garantia e formas de pagamento (`index.html:41–52`).

### Confiança e responsabilidade

- O texto não promete que o guia substitui contador ou advogado e reconhece variações entre municípios (`index.html:36`, `index.html:56`).
- O checkout externo é identificado, e o acesso digital é distinguido de produto físico (`index.html:38`).
- O CTA não usa urgência artificial, contador regressivo ou falsa escassez.

### Base técnica

- A página tem boa intenção de acessibilidade e performance: HTML sem dependência de framework, imagem responsiva e foco visível (`index.html:13`, `index.html:26`, `styles.css:1`).
- O código já preserva parâmetros de atribuição e possui variantes de headline, público e autoridade (`app.js:14–27`, `app.js:29–34`). Isso permite testar, desde que a instrumentação seja concluída.

## 3. O que enfraquece a venda

### P0 — A página expõe pendências internas

O visitante encontra textos como “Canal de entrega e prazo de liberação: [A CONFIRMAR]”, “Foto profissional do autor: [A CONFIRMAR]” e “Adicionar página real do material” (`index.html:35`, `index.html:37–44`). Isso sinaliza produto inacabado, aumenta a ansiedade pós-compra e torna a garantia pouco crível.

**Correção:** antes de anunciar, substituir cada marcador por informação final ou retirar o bloco. Não esconder o problema com CSS: a página deve ser publicável apenas quando a oferta estiver operacionalmente definida.

### P0 — Falta prova do produto

O título e os bônus são plausíveis, mas o visitante não vê o conteúdo real, a profundidade, o método ou o nível de acabamento. A única peça visual é um mockup conceitual (`index.html:26`).

**Correção mínima:** incluir uma imagem real do sumário, duas páginas internas legíveis e um recorte real do checklist. Cada imagem deve ter legenda orientada ao benefício, por exemplo: “Exemplo de conferência de código do serviço”.

**Prova adicional, se existir:** um depoimento autorizado e identificável, com contexto do usuário e sem prometer resultado universal. Não inventar testemunhos, números, certificações ou endossos.

### P1 — Público amplo demais

“Prestadores de serviço”, “MEIs”, “autônomos”, “pequenas empresas” e “contadores” têm dúvidas e linguagem de compra diferentes (`index.html:36`). O `app.js` já prevê uma variante para contadores, o que confirma que há mais de um segmento em disputa (`app.js:20–24`).

**Recomendação:** escolher um público primário para a landing page de aquisição. Hipótese inicial a validar: **MEIs e prestadores de serviço que emitem NFS-e por conta própria**. Contadores podem receber uma versão específica, com promessa de apoio à orientação de clientes.

### P1 — Benefício principal genérico

“Mais segurança” é desejável, mas não é específico o bastante para diferenciar o guia. A variante “Identifique os erros que mais chamam atenção...” é mais concreta, porém longa e traz uma afirmação que precisa de evidência (`app.js:16–18`).

**Direção recomendada:** combinar tarefa, mecanismo e limite:

> **Saiba o que conferir na sua NFS-e antes de enviá-la.**  
> Um guia prático para revisar cadastro, código do serviço, retenções e pendências — com checklist mensal para transformar a conferência em rotina.

Essa redação promete uma ação observável, não a ausência garantida de multa.

### P1 — Claim de multa e fiscalização precisa de sustentação

“Guia prático de notas fiscais para não levar multa” aparece no produto e influencia a percepção da oferta (`index.html:31`). A frase pode ser lida como promessa de resultado jurídico/financeiro. “O que todo fiscal procura” também sugere uma universalidade difícil de provar.

**Recomendação:** se houver base técnica clara, explicitar a fonte, a jurisdição e a data de revisão. Se não houver, trocar por algo como “para revisar os pontos que costumam gerar dúvidas e pendências” e manter o aviso de que regras variam por município.

### P1 — CTA descreve intenção, não próximo passo

“Quero revisar minhas notas com mais segurança” é empático, mas não diz claramente o que acontece ao clicar. Também é repetido quatro vezes (`index.html:24`, `index.html:38`, `index.html:54`, `index.html:57`).

**Alternativas para teste:**

- **Acessar o guia e os 2 bônus** — hipótese: reduz ambiguidade sobre a entrega.
- **Quero conferir minha próxima NFS-e** — hipótese: aproxima o benefício da tarefa.

Adicionar microcopy abaixo do botão: “Você será levado ao checkout HeroSpark. Acesso digital após a confirmação do pagamento.”

### P1 — Ordem da prova está invertida

O visitante passa por uma seção vazia de amostras antes de chegar ao autor e à oferta. Enquanto os espaços não tiverem conteúdo real, a seção deve ser removida, condensada ou substituída por uma prova disponível.

**Ordem recomendada:** hero → prova do material → o que recebe → para quem é → autoridade do autor → oferta/garantia → FAQ → CTA final.

### P2 — Página longa sem hierarquia de decisão suficiente

A quantidade de seções é justificável para uma compra de informação, mas há repetição sem aumento proporcional de convicção: “mais clareza”, “rotina”, “consulta” e “segurança” aparecem em vários pontos. A copy deve avançar da promessa para a prova, da prova para a oferta e da oferta para a redução de risco.

**Não fazer agora:** adicionar mais slogans, mais ícones ou mais seções institucionais antes de preencher prova, operação e mensuração.

## 4. Posicionamento e brief recomendado

### Proposição única testável

**Para** MEIs e prestadores de serviço que emitem NFS-e sem uma rotina clara de conferência, **o guia entrega** um roteiro prático para revisar os pontos mais sujeitos a erro antes e depois da emissão, **porque** organiza cadastro, classificação, retenções, pendências e um checklist mensal em linguagem de consulta, **para que** a pessoa emita com mais clareza e saiba quando precisa buscar ajuda profissional.

### Hierarquia de mensagem

1. **Promessa:** saiba o que conferir na sua NFS-e antes de enviá-la.
2. **Razões para acreditar:** páginas reais, sumário, checklist, experiência verificável do autor, data de revisão e exemplos do conteúdo.
3. **Benefícios secundários:** entender MEI/Simples, reconhecer pendências e consultar NBS/IBS/CBS.
4. **Objeções:** município, formato, prazo de acesso, atualização, garantia e limites do material.
5. **Ação:** acessar o guia e os bônus no checkout.

### Copy sugerida para a primeira dobra

**Eyebrow:** PARA QUEM EMITE NFS-e POR CONTA PRÓPRIA  
**Título:** Saiba o que conferir na sua NFS-e antes de enviá-la.  
**Descrição:** Um guia prático para revisar cadastro, código do serviço, retenções e pendências — com checklist mensal para transformar a conferência em rotina.  
**Bullets:**

- Revise os pontos essenciais da emissão.
- Entenda dúvidas comuns de MEI e Simples Nacional.
- Consulte o checklist antes da próxima nota.

**CTA:** Acessar o guia e os 2 bônus  
**Microcopy:** Material digital · acesso após confirmação do pagamento · garantia de 7 dias, conforme condições da oferta.

## 5. Plano de execução priorizado

| Prioridade | Entrega | Responsável | Dependência | Critério de pronto |
|---|---|---|---|---|
| P0 | Fechar oferta operacional | Autor/negócio | Dados do checkout | Formato, páginas, acesso, prazo, atualização e garantia confirmados |
| P0 | Fechar credenciais e bio | Autor | Comprovação/autorização | Foto, cargo, formação, tempo de experiência e fonte revisados |
| P0 | Inserir prova real | Autor + design | eBook final | Sumário, 2 páginas e checklist reais, legíveis em mobile |
| P0 | Remover placeholders | Desenvolvimento | Entregas acima | Busca por `A CONFIRMAR`, “Adicionar página” e notas internas retorna zero |
| P1 | Reescrever hero e CTA | Copy + design | Público primário definido | Uma promessa, um público e um próximo passo compreensíveis em 5 segundos |
| P1 | Reorganizar blocos | Design + desenvolvimento | Prova real | Prova aparece antes da seção de autoridade/oferta; seção vazia removida |
| P1 | Instrumentar funil | Desenvolvimento/marketing | IDs e ferramenta definidos | PageView, ViewContent, CTA, checkout iniciado e compra mensuráveis |
| P2 | SEO e compartilhamento | Desenvolvimento | Decisão de publicação | `noindex` revisado; canonical, `og:image` e links sociais definidos |

### Sequência sugerida

**Dia 1:** fechar fatos da oferta e autorização de claims.  
**Dias 2–3:** produzir prova real, foto/bio e política de garantia.  
**Dias 4–5:** reescrever hero, CTA, títulos e FAQ; remover placeholders.  
**Dias 6–7:** instrumentar, revisar mobile/acessibilidade e fazer QA do checkout.  
**Depois do lançamento:** testar uma hipótese por vez e revisar por qualidade de checkout/compra, não por clique isolado.

## 6. Mensuração e testes

### Métrica primária

**Taxa de compra aprovada por sessão qualificada**, com janela definida pelo time e atribuição documentada. Se o checkout não permitir devolver compra aprovada para a landing page, usar o relatório do HeroSpark conciliado com UTMs e sessões/saídas.

### Indicadores antecedentes

- Visualização da seção de prova.
- Clique em CTA por posição: hero, oferta, fechamento e sticky.
- Início de checkout.
- Conversão do checkout para pagamento aprovado.
- Abandono por etapa e por forma de pagamento.
- Conversão por público, dispositivo e origem.

### Plano de testes

| Teste | Hipótese | Variação | Medida de decisão |
|---|---|---|---|
| Hero | Benefício observável supera “mais segurança” | “Saiba o que conferir...” vs. headline atual | Compra aprovada por sessão; CTR apenas como diagnóstico |
| CTA | Clareza do próximo passo reduz hesitação | “Acessar o guia e os 2 bônus” vs. CTA atual | Início de checkout e compra aprovada |
| Prova | Ver páginas reais aumenta confiança | Sem amostra vs. sumário + checklist + página interna | Checkout iniciado e compra aprovada |
| Segmentação | Mensagem específica converte melhor | Prestadores/MEI vs. contadores | Compra aprovada por audiência |

O `app.js` já cria variantes via URL, mas isso ainda não é um experimento confiável por si só: falta persistência de variante, ferramenta de coleta, atribuição e regra de amostra. Não declarar vencedor com base em poucos cliques.

## 7. Riscos e validações

- **Jurídico/regulatório:** validar “para não levar multa”, menções à fiscalização e qualquer frase que possa ser interpretada como garantia de resultado.
- **Atualização tributária:** NBS, IBS e CBS e a NFS-e Nacional podem mudar; exibir data de revisão, versão e política de atualização.
- **Variação municipal:** manter o limite de escopo, mas trazer exemplos de aplicação sem sugerir universalidade.
- **Credenciais:** publicar apenas informações comprovadas e autorizadas pelo autor.
- **Checkout:** confirmar preço, parcelamento, entrega, reembolso, suporte e eventual página de termos antes de levar tráfego.
- **Privacidade:** definir ferramenta de analytics, consentimento quando aplicável e política de uso de UTMs/identificadores.
- **Acessibilidade:** manter foco visível, contraste, alt text do mockup e revisar leitura mobile; marcar ícones decorativos como não informativos quando necessário.

## 8. Definição de pronto para lançamento

- Não existe texto interno ou placeholder visível.
- O produto exibido é o produto que será entregue; se o mockup continuar conceitual, isso fica claro sem ocupar o lugar da prova.
- O visitante sabe para quem é, o que recebe, em qual formato, quando recebe e como pedir garantia.
- O hero comunica uma promessa específica, um mecanismo e um CTA claro.
- Existe pelo menos uma prova real do conteúdo e uma prova verificável de autoridade.
- O checkout foi conferido manualmente em Pix e cartão.
- Os eventos do funil chegam a uma ferramenta ou relatório confiável.
- `noindex,nofollow` foi mantido apenas se a página ainda for privada/staging.
- O time definiu baseline, métrica primária, janela de análise e responsável pela otimização.

## Conclusão

A direção estratégica é promissora: transformar uma tarefa fiscal confusa em uma rotina de conferência simples. Para vender, a página precisa provar essa transformação com o próprio material, retirar todas as pendências visíveis e concentrar a mensagem em um comprador principal. A próxima melhoria de maior retorno não é “deixar mais bonita”; é tornar a oferta verificável, específica e mensurável.

