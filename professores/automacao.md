# Professor de Automação — Fase 3

Material: livro Pro Git (em português) e documentação do boto3.
Critérios de passagem: Fase 3 do ROADMAP.md.

Tópicos: modelo interno do Git, branches e merge, rebase interativo,
resolução de conflitos, reflog, Bash (variáveis, condicionais, laços,
códigos de saída, set -euo pipefail), cron, Python com boto3 (clientes,
paginação, tratamento de erro).

Exercícios típicos:
- Resolver conflitos, fazer rebase interativo e recuperar commits perdidos
  com reflog
- Script Bash de backup com rotação, tratamento de erro e agendamento no cron
- Script Python com boto3 que lista recursos AWS sem tag de dono e gera
  relatório

Em produção:
- Concilie, onde procurar: estratégia de branches entre homolog e
  desenvolvimento; scripts de deploy.
- Dia a dia: rebase de uma branch atrasada antes do merge; automatizar uma
  tarefa repetitiva com boto3.

Para praticar: git log --graph, git rebase -i, git reflog, git bisect,
bash -x, shellcheck, crontab, boto3 com paginators.
