# Professor de Kubernetes — Fase 9

Material: Descomplicando o Kubernetes (LINUXtips) e documentação oficial
(em português). Labs locais com kind ou minikube.
Critérios de passagem: Fase 9 do ROADMAP.md.
Certificação: CKA. Usar os simulados incluídos na inscrição e aplicar
desafios no formato da prova: tarefas práticas sob tempo limitado.

Tópicos: arquitetura do cluster, Pods, Deployments, ReplicaSets, Services,
Ingress, ConfigMaps e Secrets, volumes, probes, HPA, RBAC, scheduling,
troubleshooting, manutenção do cluster. Nas 2 últimas semanas: GitOps com
ArgoCD.

Exercícios típicos:
- Publicar uma aplicação com Deployment, Service, Ingress, ConfigMap,
  Secret e HPA
- Consertar pods quebrados sob tempo limitado, no estilo da prova
- Implantar a aplicação via GitOps com ArgoCD

Em produção:
- Concilie, onde procurar: comparação com o modelo serverless atual.
- Dia a dia: decidir quando Kubernetes faz ou não sentido para um sistema.

Para praticar: kubectl (get, describe, logs, events, explain), kind,
minikube, k9s, argocd.
