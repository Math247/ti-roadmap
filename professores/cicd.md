# Professor de CI/CD — Fase 7

Material: documentação do GitHub Actions (em português).
Critérios de passagem: Fase 7 do ROADMAP.md.

Tópicos: workflows, jobs, steps e runners, gatilhos, cache e artefatos,
matrizes, segredos, OIDC com a AWS, ambientes com aprovação manual,
registros de artefatos (ECR ou GitHub Packages), estratégias de deploy e
rollback.

Exercícios típicos:
- Pipeline com lint, testes, build, push da imagem e deploy na AWS
- Autenticar na AWS via OIDC, sem chaves de acesso guardadas
- Ambiente de produção com aprovação manual e imagens versionadas num
  registro de artefatos

Em produção:
- Concilie, onde procurar: pipeline de deploy para homolog.
- Dia a dia: pipeline quebrado sem mudança aparente no código; deploy
  seguro com plano de rollback.

Para praticar: act (rodar workflows localmente), gh run, gh workflow,
actionlint.
