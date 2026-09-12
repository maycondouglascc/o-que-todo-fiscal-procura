# Growth Council

Sistema multiagente para transformar informação bruta de um produto low-ticket em uma recomendação estratégica auditável. O sistema usa arquivos Markdown como memória compartilhada e um protocolo de fases como máquina de estados. Os agentes são especialistas em frameworks; não representam nem imitam pessoas reais.

## Princípios operacionais

- Evidência antes de opinião; fato, dado, inferência, hipótese e suposição nunca são misturados.
- Estratégia antes de execução; oferta antes de acabamento visual; clareza antes de criatividade.
- Dependências explícitas: downstream pode contestar upstream, mas não altera decisões silenciosamente.
- Discordância é dado. O Chair registra maioria, minoria ou experimento quando a evidência não resolve.
- Nenhuma escassez, urgência, prova social, autoridade, depoimento ou benchmark pode ser inventado.
- Toda recomendação recebe prioridade, impacto, confiança, esforço, evidência e owner.

## Estrutura

```text
growth-council/
├── agents/                  # contratos de comportamento de cada especialista
├── inputs/                  # PRODUCT.md e pesquisa fornecidos pelo usuário
├── context/                 # contexto normalizado, ledger e hipóteses
├── council/
│   ├── round-1/             # diagnósticos independentes
│   ├── debates/             # conflitos e arbitragem
│   └── cross-examination/   # respostas diretas entre agentes
├── outputs/                 # briefs e veredito final
├── templates/               # contratos de documentos
├── examples/minimal-product/ # exemplo executável e seu resultado
├── run_council.py           # CLI/orquestrador
└── council.yml              # ordem, owners e comandos
```

## Execução

Na raiz do repositório:

```bash
python3 --version  # Python 3.10+
python3 growth-council/run_council.py init
python3 growth-council/run_council.py analyze
python3 growth-council/run_council.py status
python3 growth-council/run_council.py audit
python3 growth-council/run_council.py debate "preço versus aquisição"
python3 growth-council/run_council.py experiment "uma promessa mais específica aumenta CVR"
python3 growth-council/run_council.py red-team
python3 growth-council/run_council.py critique
python3 growth-council/run_council.py verdict
```

`init` cria apenas arquivos ausentes. `analyze` normaliza os inputs, cria o manifesto da execução, gera um pacote independente para cada agente e valida que as dependências estão disponíveis. O CLI não inventa análises: um executor humano, LLM ou worker lê os pacotes e grava os documentos usando os templates. Use `--root /caminho` para executar contra outro diretório de projeto.

Para auditar a página existente neste repositório, preencha/ajuste `inputs/EXISTING_LANDING_PAGE.md`; por padrão ele aponta para `../index.html`.

Depois de aplicar correções, use [`inputs/IMPLEMENTATION_INPUTS.md`](/home/maycon/Documents/code/o-que-todo-fiscal-procura/growth-council/inputs/IMPLEMENTATION_INPUTS.md) para fechar as dependências de conteúdo, checkout, métricas, economia e autorização. O contrato do evento de compra está em [`integrations/checkout-bridge.md`](/home/maycon/Documents/code/o-que-todo-fiscal-procura/growth-council/integrations/checkout-bridge.md).

Para um exemplo autocontido:

```bash
python3 growth-council/run_council.py analyze --root growth-council/examples/minimal-product
```

## Contrato de cada saída

Cada documento de agente deve começar com `Status`, `Run ID`, `Owner`, `Evidence Used`, `Assumptions` e `Confidence Score`. Afirmações relevantes usam a forma:

```text
[CLAIM C-001 | INFERENCE | E-001,E-002 | confidence 3/5]
Mensagem específica deve ser testada contra a promessa genérica.
```

Quando houver conflito, adicionar um bloco `CHALLENGE` com agente, decisão contestada, razão, evidência, alternativa e impacto esperado. O `FINAL_VERDICT.md` só deve ser considerado pronto quando as validações do CLI passarem.

## Limitações atuais

O repositório não possui credenciais nem um provedor de LLM. O orquestrador entrega contexto, prompts/contratos, estado e validação, mas não finge executar raciocínio especializado. A conexão com qualquer worker pode escrever os arquivos no mesmo layout sem mudar a lógica de negócio.
