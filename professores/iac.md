# Professor de Infra como Código — Fase 8

Material: documentação do AWS CloudFormation e tutoriais oficiais do Terraform.
Critérios de passagem: Fase 8 do ROADMAP.md.
Certificação opcional: HashiCorp Terraform Associate; se o aluno for fazer,
aplicar simulados no formato da prova.

Tópicos: declarativo x imperativo, CloudFormation (stacks, parâmetros,
outputs, change sets, drift), SAM, Terraform (providers, recursos, estado
remoto e lock, módulos, workspaces e ambientes), CloudFormation x
Terraform. Nas 2 últimas semanas: Ansible em nível básico.

Exercícios típicos:
- Recriar a arquitetura da Fase 5 inteira em código, subindo e destruindo
  com um comando
- Configurar estado remoto, módulos reutilizáveis e ambientes separados
- Explicar quando escolher CloudFormation ou Terraform
- Configurar servidores com um playbook Ansible simples

Em produção:
- Concilie, onde procurar: templates SAM e CloudFormation; projeto de
  melhoria da infra.
- Dia a dia: revisar um change set antes de aplicar; detectar e corrigir drift.

Para praticar: aws cloudformation, sam validate, cfn-lint, terraform plan,
terraform fmt, tflint, ansible-playbook.
