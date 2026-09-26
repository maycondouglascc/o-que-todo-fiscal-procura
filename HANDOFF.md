# Handoff operacional — Tributos em Foco

## Objetivo

Landing page editorial do guia digital O Que Todo Fiscal Procura, de Ivan Gonçalves. O projeto é uma página estática em português, com checkout externo HeroSpark, Meta Pixel e assets locais.

## Estado de produção

- Worker: guia-nfe
- Conta Cloudflare: conta do cliente autenticada pelo Wrangler
- Domínios Custom Domain:
  - tributosemfoco.com.br
  - www.tributosemfoco.com.br
- URL principal: https://tributosemfoco.com.br/guia-nfe
- URL alternativa: https://www.tributosemfoco.com.br/guia-nfe
- Raiz dos domínios: redireciona para /guia-nfe
- Hospedagem: Cloudflare Workers com Static Assets, não Cloudflare Pages
- Checkout: HeroSpark, link externo definido nos CTAs da oferta
- Instagram: https://www.instagram.com/tributos.em.foco

O projeto não depende de GitHub pessoal. O deploy é feito diretamente na conta Cloudflare do cliente pelo Wrangler.

## Arquitetura do projeto

- index.html: estrutura, copy, Meta Pixel e links para checkout.
- styles.css: tokens, layout e responsividade principal.
- styles-hero.css: ajustes do hero e do mockup.
- styles-feedback.css: refinamentos visuais das seções finais.
- app.js: variantes de copy, atribuição UTM e eventos de conversão.
- assets/: capas, mockup, previews e imagens editoriais.
- autor-ivan-goncalves.png: foto atual da bio.
- _redirects: raiz para /guia-nfe e proxy da landing nessa rota.
- wrangler.jsonc: configuração declarativa do Worker, domínios e assets.
- .assetsignore: arquivos de desenvolvimento que não devem ser publicados.
- .githooks/pre-commit: preflight de HTML, imagens, JavaScript e Growth Council.
- growth-council/: sistema de avaliação da oferta, copy e CRO.

## Roteamento

O _redirects atual é deliberadamente:

~~~text
/ /guia-nfe 301
/guia-nfe/ /guia-nfe 301
/guia-nfe / 200
~~~

O proxy para / é importante. Redirecionar /guia-nfe para /index.html causa loop porque o roteamento de assets normaliza index.html de volta para /.

## Rastreamento

O Meta Pixel 1387221636851693 está instalado no index.html.

Eventos implementados:

- PageView: carregamento da página.
- ViewContent: visualização do conteúdo.
- InitiateCheckout: clique nos CTAs que levam ao HeroSpark, com valor de referência de R$ 47 e moeda BRL.
- CTA_Click e CheckoutOutbound: eventos locais enviados para dataLayer e para o evento customizado guia:analytics.
- Purchase: somente após confirmação real do pagamento, por meio do hook window.growthCouncil.recordApprovedPurchase ou da ponte de retorno com gc_purchase=approved e transaction_id.

UTMs, fbclid, gclid e _gl são preservados e anexados aos links do checkout.

O token da API de Conversões não está no frontend. Não adicionar esse token ao repositório. Para uma implementação server-side, usar o Worker, um webhook autorizado do checkout e um secret do Cloudflare.

## Fluxo recomendado para agentes

### 1. Antes de editar

~~~bash
git status --short
rg -n "data-cta|fbq|_redirects|tributosemfoco|HeroSpark" index.html app.js _redirects wrangler.jsonc
~~~

Preserve alterações existentes e assets já aprovados. Não recrie mockups ou capas sem necessidade.

### 2. Validar localmente

~~~bash
git diff --check
node --check app.js
python3 growth-council/run_council.py verdict
npx --yes wrangler@latest dev --config wrangler.jsonc
~~~

Se a alteração afetar o layout, conferir desktop e mobile no navegador. Se afetar assets, verificar caminho, extensão e MIME type.

### 3. Commit

O repositório usa:

~~~bash
git config core.hooksPath .githooks
~~~

O pre-commit adiciona o working tree, verifica HTML, imagens, JavaScript e Growth Council. Faça commits pequenos e descritivos. O hook é a última barreira antes da publicação.

### 4. Deploy autorizado

Use o script canônico:

~~~bash
./scripts/deploy-cloudflare.sh "descrição curta da alteração"
~~~

Ou, diretamente:

~~~bash
npx --yes wrangler@latest deploy \
  --config wrangler.jsonc \
  --keep-vars \
  --message "descrição curta da alteração"
~~~

O --keep-vars preserva variáveis configuradas no dashboard. Antes do primeiro deploy em uma máquina nova:

~~~bash
npx --yes wrangler@latest login
npx --yes wrangler@latest whoami
npx --yes wrangler@latest versions list --name guia-nfe --json
~~~

Confirme que o login é da conta do cliente. Nunca peça para o usuário colar token no chat.

### 5. Verificar produção

~~~bash
curl -sS -L --max-redirs 5 \
  -o /dev/null \
  -w 'status=%{http_code} final=%{url_effective}\n' \
  https://tributosemfoco.com.br/guia-nfe

curl -sS -L --max-redirs 5 \
  -o /dev/null \
  -w 'status=%{http_code} final=%{url_effective}\n' \
  https://www.tributosemfoco.com.br/guia-nfe
~~~

O critério de sucesso é 200 nas duas URLs, com a URL final preservando /guia-nfe. Também conferir a nova versão:

~~~bash
npx --yes wrangler@latest versions list --name guia-nfe --json
~~~

## Segurança e limites

- Manter tokens, senhas e secrets fora do Git.
- Não mover o Pixel para outro ID sem autorização do cliente.
- Não disparar Purchase em clique, seleção de Pix ou abertura do checkout.
- Não alterar os Custom Domains sem declarar os dois: apex e www.
- Não usar wrangler pages deploy: este projeto é um Worker com Static Assets.
- Não publicar growth-council/, relatórios, hooks ou documentação como assets públicos.
- Se uma plataforma alternativa for usada, preservar a rota /guia-nfe, os caminhos relativos de assets/, o _redirects equivalente e o checkout externo.

## Migração para outra plataforma

Se o cliente trocar Cloudflare por outra hospedagem estática:

1. Publicar index.html, CSS, JS e os assets referenciados mantendo a estrutura relativa.
2. Criar uma regra equivalente a GET /guia-nfe → conteúdo da raiz, sem redirecionar para /index.html.
3. Redirecionar / para /guia-nfe somente se essa continuar sendo a URL pública escolhida.
4. Revalidar o Meta Pixel e os links HeroSpark no domínio novo.
5. Fazer um teste de produção com os dois hostnames antes de mudar anúncios.

## Prompt inicial para outro agente

> Leia AGENTS.md e HANDOFF.md antes de agir. Este é um Worker Cloudflare chamado guia-nfe, com Static Assets e Custom Domains tributosemfoco.com.br e www.tributosemfoco.com.br. Preserve o rastreamento, o checkout HeroSpark, a rota /guia-nfe e os assets locais. Faça a alteração mínima, valide o projeto e só publique com Wrangler após autorização explícita.
