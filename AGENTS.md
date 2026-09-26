# Instruções para agentes

Antes de alterar a landing page, o rastreamento, os assets ou a publicação, leia HANDOFF.md. Ele é a fonte de contexto operacional do projeto.

Use o handoff especialmente quando a solicitação envolver:

- conteúdo, layout, imagens ou conversão da landing;
- Meta Pixel, eventos de checkout ou atribuição UTM;
- Cloudflare, Worker, domínio, DNS ou deploy;
- migração para outra plataforma de hospedagem.

Fluxo mínimo para uma alteração:

1. Inspecionar o estado atual e preservar mudanças existentes.
2. Fazer a alteração mínima necessária.
3. Executar git diff --check, node --check app.js e o Growth Council.
4. Confirmar as rotas públicas.
5. Publicar com ./scripts/deploy-cloudflare.sh "descrição da alteração" quando o usuário tiver autorizado o deploy.

Não coloque tokens, senhas ou credenciais de API no HTML, JavaScript, documentação pública ou commits.
