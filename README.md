# o-que-todo-fiscal-procura
Landing page do guia O Que Todo Fiscal Procura, de Ivan Gonçalves.

## Growth Council

O sistema multiagente de estratégia, oferta, funil, copy, CRO e experimentação está em [`growth-council/`](./growth-council/). Comece com:

```bash
python3 growth-council/run_council.py init
python3 growth-council/run_council.py analyze
```

## Git pre-commit hook

O projeto usa `.githooks/pre-commit` para adicionar todos os arquivos e validar HTML, imagens, JavaScript e o contrato do Growth Council antes de cada commit. Ative-o uma vez:

```bash
git config core.hooksPath .githooks
```
