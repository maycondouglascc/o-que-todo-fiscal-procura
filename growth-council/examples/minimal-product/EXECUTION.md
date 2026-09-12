# Exemplo de execução mínima

Input fornecido: um eBook de R$27 sobre erros comuns em NFS-e, sem pesquisa de cliente, métricas, prova ou custos.

```text
$ python3 ../../run_council.py analyze --root .
Analysis scaffold ready: RUN-YYYYMMDD-HHMMSS (analyze)
Next: fill council/round-1 and outputs using the generated specialist packets, then run verdict.

$ python3 ../../run_council.py verdict --root .
NOT READY — outputs remain incomplete or invalid.
```

Esse resultado é correto: a arquitetura já distribuiu os nove contratos e separou as dependências, mas não transforma um produto sem evidência em estratégia “pronta”. Depois que os workers preencherem os briefs, cada saída deve receber `Status: READY`, IDs de evidência/assumption e confiança; então `verdict` pode passar.
