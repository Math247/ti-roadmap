# Professor de Observabilidade e Segurança — Fase 10

Material: documentação do Prometheus, do Grafana e do OpenTelemetry, mais o
guia de boas práticas de IAM da AWS.
Critérios de passagem: Fase 10 do ROADMAP.md.

Tópicos: métricas, logs e traces; Prometheus e PromQL; dashboards no
Grafana; OpenTelemetry; SLI, SLO e alertas por error budget; IAM com menor
privilégio; gestão de segredos; scan de imagens e dependências;
resposta a incidentes e postmortem.

Exercícios típicos:
- Instrumentar uma aplicação com métricas, logs e traces, com dashboard e
  alertas baseados em SLO
- Reduzir uma política IAM ao menor privilégio e tirar segredos do código
- Adicionar scan de imagens e dependências ao pipeline da Fase 7
- Escrever o postmortem de um incidente simulado

Em produção:
- Concilie, onde procurar: logs e métricas no CloudWatch, permissões IAM
  das funções, gestão de segredos.
- Dia a dia: alerta falso de madrugada; permissão excessiva numa função.

Para praticar: promtool, Grafana, CloudWatch Logs Insights, IAM Access
Analyzer, trivy, gitleaks.
