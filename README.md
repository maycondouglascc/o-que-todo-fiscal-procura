# o-que-todo-fiscal-procura
Landing page do guia O Que Todo Fiscal Procura, de Ivan Gonçalves.

## Handoff e operação

Para alterar a landing com outro agente, leia primeiro AGENTS.md e HANDOFF.md. O handoff reúne a arquitetura, o rastreamento, o checkout, os domínios e o fluxo de validação e deploy.

O deploy de produção é feito diretamente no Worker Cloudflare guia-nfe:

~~~bash
./scripts/deploy-cloudflare.sh "descrição da alteração"
~~~

## Growth Council

O sistema multiagente de estratégia, oferta, funil, copy, CRO e experimentação está em growth-council/. Comece com:

~~~bash
python3 growth-council/run_council.py init
python3 growth-council/run_council.py analyze
~~~

## Git pre-commit hook

O projeto usa .githooks/pre-commit para adicionar todos os arquivos e validar HTML, imagens, JavaScript e o contrato do Growth Council antes de cada commit. Ative-o uma vez:

~~~bash
git config core.hooksPath .githooks
~~~

## Meta Pixel e checkout

O Pixel 1387221636851693 está instalado na landing page e registra PageView e InitiateCheckout nos CTAs que levam ao checkout HeroSpark. O token da API de Conversão não é colocado no HTML ou no JavaScript público: como o checkout é externo, o evento Purchase deve ser configurado no provedor ou em um endpoint server-side com o token mantido como segredo.
