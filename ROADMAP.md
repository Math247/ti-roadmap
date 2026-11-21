# Roadmap DevOps → Sênior (com IA em produção)

Nov 20, 2026 · @Matheus Carregal Habib

## Como funciona

Você estuda de segunda a sexta, 1 hora por dia, cerca de 5 horas por semana. Fins de semana são livres. Todo o material é gratuito; só as provas de certificação são pagas.

| Dia | Foco | Tempo |
| --- | --- | --- |
| Segunda a quinta | Trilha principal (fase atual) | 1h |
| Sexta | Trilha paralela de IA em produção | 1h |

Cada sessão de 1h segue o mesmo formato:

1. 10 min: revisão do dia anterior, de cabeça, sem olhar anotações.
2. 30 min: conteúdo novo com prática (lab, comando, código), mais 10 min vendo o conceito em produção, na Concilie e no dia a dia de DevOps. Você tenta primeiro e só depois consulta.
3. 10 min: anotações e commit no repositório `ti-roadmap`.

Folga programada: 2 semanas por ano (fim de ano e uma no meio), já contadas nas estimativas.

### Regra para passar de fase

Você só avança quando passar pelos 3 portões:

1. **Conteúdo**: material da fase concluído e anotado no repositório.
2. **Projeto prático**: o projeto da fase funcionando, versionado e revisado pelo agente professor.
3. **Avaliação do agente**: nota mínima de 80%, com perguntas teóricas e um desafio prático cronometrado. Em fases com certificação, também 2 simulados seguidos acima de 80% antes de agendar a prova.

Se reprovar, faça 1 a 2 semanas de revisão focada nos pontos fracos e refaça. Se a fase passar de 50% do tempo previsto, revise o plano com o agente em vez de só estender.

### Acelerar (opcional, só se você quiser)

Nada aqui é obrigatório; o plano padrão continua sendo 1h por dia.

- **Adiantar fase:** você pode pedir a prova antes do prazo. Passou nos 3 portões, avança. As Fases 3 e 4 são as candidatas naturais, porque você já usa Git, Python e AWS no trabalho.
- **Trabalho como prática:** o que você fizer no projeto de melhoria da infra e conseguir explicar ao professor conta como prática da Fase 8.
- **Ritmo maior após a formatura:** se quiser, suba para 1h30 por dia. Nesse ritmo, o término estimado cai para meados de 2028.

Pós-graduação fica fora por enquanto; reavaliar ao terminar a Fase 5. Use o roadmap.sh/devops como checklist de cobertura: marque os tópicos lá conforme avança.

## Visão geral

São 11 fases e cerca de 111 semanas de estudo, terminando por volta de abril de 2029 se começar em 23 de novembro de 2026. As datas são estimativas e incluem as folgas.

| Fase | Tema | Duração | Término estimado | Certificação |
| --- | --- | --- | --- | --- |
| 1 | Redes | 8 semanas | fev/2027 | — |
| 2 | Linux | 10 semanas | abr/2027 | LPI Linux Essentials (opcional) |
| 3 | Git, Bash e Python para automação | 6 semanas | mai/2027 | — |
| 4 | AWS fundamentos | 6 semanas | jul/2027 | AWS Cloud Practitioner |
| 5 | AWS Solutions Architect | 14 semanas | out/2027 | AWS Solutions Architect Associate |
| 6 | Docker | 6 semanas | jan/2028 | — |
| 7 | CI/CD com GitHub Actions | 5 semanas | fev/2028 | — |
| 8 | Infra como Código | 12 semanas | jun/2028 | HashiCorp Terraform Associate (opcional) |
| 9 | Kubernetes | 18 semanas | out/2028 | CKA |
| 10 | Observabilidade e Segurança | 10 semanas | dez/2028 | — |
| 11 | Arquitetura e nível sênior | 16 semanas | abr/2029 | AWS DevOps Engineer Professional |

Preços de prova mudam; confira no site oficial ao agendar. A AWS costuma dar voucher de desconto para a próxima prova após cada certificação dela.

## Fases 1 a 4: a base

### Fase 1 — Redes (8 semanas)

Material: Networking Basics e Subnetting no [Cisco Networking Academy](https://www.netacad.com).

Para passar:

- [ ] Calcular sub-redes de /16 a /30 sem calculadora, em menos de 2 minutos cada
- [ ] Explicar o caminho de uma requisição HTTPS: DNS, TCP, TLS, roteamento, NAT
- [ ] Projeto: desenhar o plano de endereçamento de uma VPC com sub-redes públicas e privadas em 2 zonas
- [ ] Nota mínima de 80% no exame final do curso e na avaliação do agente

### Fase 2 — Linux (10 semanas)

Material: Linux Unhatched e depois Linux Essentials, no [Cisco Networking Academy](https://www.netacad.com).

Para passar:

- [ ] Administrar uma VM sem tutorial: usuários, grupos, permissões, systemd, logs, SSH por chave, firewall
- [ ] Diagnosticar problemas com `ps`, `top`, `df`, `journalctl`, `ss` e `curl`
- [ ] Projeto: configurar o Nginx numa VM como proxy reverso de uma aplicação, com serviço systemd, HTTPS e logs rotacionados
- [ ] Nota mínima de 80% no exame do curso e na avaliação do agente

### Fase 3 — Git, Bash e Python para automação (6 semanas)

Material: livro [Pro Git](https://git-scm.com/book/pt-br/v2) em português e documentação do [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html). Como você já domina Python, o foco é automação de infraestrutura.

Para passar:

- [ ] Resolver conflitos, fazer rebase interativo e recuperar commits perdidos com reflog
- [ ] Projeto 1: script Bash de backup com rotação, tratamento de erro e agendamento no cron
- [ ] Projeto 2: script Python com boto3 que lista recursos AWS sem tag de dono e gera um relatório

### Fase 4 — AWS fundamentos (6 semanas)

Material: [AWS Cloud Practitioner Essentials](https://aws.amazon.com/pt/training/course-descriptions/cloud-practitioner-essentials/) no AWS Skill Builder, com o conjunto oficial gratuito de questões de prática.

Crie a conta AWS pessoal só no início desta fase: o plano gratuito dura 6 meses ou até acabarem os créditos, e assim cobre as Fases 4 e 5. Depois disso, use o plano pago com alerta de orçamento e destrua tudo ao fim de cada lab.

Para passar:

- [ ] 2 simulados seguidos acima de 80%
- [ ] Explicar modelo de responsabilidade compartilhada, preços e os serviços principais
- [ ] Certificação: AWS Cloud Practitioner

## Fases 5 a 8: cloud e automação

### Fase 5 — AWS Solutions Architect (14 semanas)

Material: cursos gratuitos de preparação no AWS Skill Builder, documentação oficial e labs no Free Tier. Configure alerta de orçamento na conta antes de qualquer lab.

Para passar:

- [ ] Projeto: arquitetura de 3 camadas com VPC, ALB, Auto Scaling, RDS Multi-AZ e S3, montada no console e documentada
- [ ] Explicar trade-offs entre opções de computação, armazenamento e banco de dados
- [ ] 2 simulados seguidos acima de 80%
- [ ] Certificação: AWS Solutions Architect Associate

### Fase 6 — Docker (6 semanas)

Material: [Descomplicando o Docker](https://github.com/badtuxx/DescomplicandoDocker), do LINUXtips.

Para passar:

- [ ] Projeto: containerizar uma aplicação com build multi-stage, usuário não-root e imagem enxuta
- [ ] Orquestrar app, banco e cache com Docker Compose, com volumes e healthchecks
- [ ] Explicar camadas de imagem, redes do Docker e diferença entre container e VM

### Fase 7 — CI/CD com GitHub Actions (5 semanas)

Material: [documentação do GitHub Actions](https://docs.github.com/pt/actions) em português.

Para passar:

- [ ] Projeto: pipeline com lint, testes, build, push da imagem e deploy na AWS
- [ ] Autenticar na AWS via OIDC, sem chaves de acesso guardadas
- [ ] Usar ambientes com aprovação manual para produção e versionar imagens num registro de artefatos (ECR ou GitHub Packages)

### Fase 8 — Infra como Código (12 semanas)

Material: documentação do [AWS CloudFormation](https://docs.aws.amazon.com/pt_br/AWSCloudFormation/latest/UserGuide/Welcome.html) e tutoriais oficiais do [Terraform](https://developer.hashicorp.com/terraform/tutorials). Esta fase conversa direto com o projeto de melhoria da infra no trabalho.

Para passar:

- [ ] Projeto: recriar a arquitetura da Fase 5 inteira em código, subindo e destruindo com um comando
- [ ] Usar estado remoto, módulos reutilizáveis e ambientes separados
- [ ] Explicar quando escolher CloudFormation ou Terraform e, nas 2 últimas semanas, configurar servidores com Ansible em nível básico
- [ ] Certificação opcional: HashiCorp Terraform Associate

## Fases 9 a 11: nível sênior

### Fase 9 — Kubernetes (18 semanas)

Material: [Descomplicando o Kubernetes](https://github.com/badtuxx/DescomplicandoKubernetes), do LINUXtips, e a [documentação oficial](https://kubernetes.io/pt-br/docs/home/) em português. Labs locais com kind ou minikube, sem custo.

Para passar:

- [ ] Projeto: publicar uma aplicação com Deployment, Service, Ingress, ConfigMap, Secret e HPA
- [ ] Resolver problemas de pods quebrados sob tempo limitado, no estilo da prova, e nas 2 últimas semanas implantar a aplicação via GitOps com ArgoCD
- [ ] Passar nos simulados que vêm incluídos com a inscrição da CKA
- [ ] Certificação: CKA

### Fase 10 — Observabilidade e Segurança (10 semanas)

Material: documentação do [Prometheus](https://prometheus.io/docs/introduction/overview/), do [Grafana](https://grafana.com/docs/grafana/latest/) e do [OpenTelemetry](https://opentelemetry.io/docs/), mais o guia de boas práticas de IAM da AWS.

Para passar:

- [ ] Projeto: métricas, logs e traces de uma aplicação, com dashboard e alertas baseados em SLO
- [ ] Aplicar menor privilégio no IAM e gerenciar segredos sem nada em código
- [ ] Escanear imagens e dependências no pipeline da Fase 7
- [ ] Escrever um postmortem de um incidente simulado

### Fase 11 — Arquitetura e nível sênior (16 semanas)

Material: [AWS Well-Architected Framework](https://docs.aws.amazon.com/pt_br/wellarchitected/latest/framework/welcome.html) em português e preparação gratuita no AWS Skill Builder.

Para passar:

- [ ] Fazer uma revisão Well-Architected completa de um sistema real, com riscos e plano de ação
- [ ] Projeto final: plataforma completa juntando IaC, CI/CD, Kubernetes ou serverless, observabilidade e um serviço com IA
- [ ] Defender as decisões de arquitetura para o agente, como numa entrevista sênior, incluindo quando um service mesh se justifica
- [ ] 2 simulados seguidos acima de 80%
- [ ] Certificação: AWS DevOps Engineer Professional

## Trilha paralela: IA em produção (sextas)

Toda sexta, 1 hora vai para IA aplicada. Cada bloco termina num projeto de portfólio e acompanha o que a trilha principal já ensinou.

| Bloco | Período | Tema | Projeto de saída |
| --- | --- | --- | --- |
| A | Fases 1 a 3 | Fundamentos de LLM: tokens, contexto, prompts, chamadas de API | CLI em Python que resume logs de servidor com um LLM |
| B | Fases 4 e 5 | RAG: embeddings e busca vetorial com pgvector no PostgreSQL | Busca semântica sobre documentação técnica |
| C | Fases 6 e 7 | Agentes, tool use e MCP | Agente que consulta a AWS via boto3 e responde perguntas sobre a infra |
| D | Fases 8 e 9 | Deploy de IA: Lambda, Bedrock, filas, limites de taxa | Serviço RAG serverless criado com IaC e pipeline |
| E | Fases 10 e 11 | Evals, observabilidade e custo de LLM, guardrails | Painel de qualidade e custo por requisição do serviço do bloco D |

Material gratuito: [documentação da Anthropic](https://docs.claude.com), cursos do repositório [anthropics/courses](https://github.com/anthropics/courses), documentação do [Amazon Bedrock](https://docs.aws.amazon.com/pt_br/bedrock/) e do [pgvector](https://github.com/pgvector/pgvector).

Para fechar um bloco: projeto funcionando no repositório e avaliação do agente de IA com nota mínima de 80%. A trilha de IA nunca trava a principal; se atrasar, segue no seu ritmo.

## Agentes e repositório

Esta seção traz tudo pronto para montar o sistema no repositório ti-roadmap: estrutura, CLAUDE.md, STATUS.md, o orquestrador e o modelo dos professores.

O orquestrador é um comando (/ativar-estudos) e os professores são arquivos de instrução que ele carrega na conversa. Subagentes do Claude Code trabalham sozinhos e devolvem só o resultado, sem conversar com você no meio; um professor precisa de vai e volta, por isso roda na sessão principal.

### Como montar

1. Crie ou abra o repositório ti-roadmap.
2. Exporte este documento em Markdown e salve como ROADMAP.md.
3. Crie os arquivos dos blocos abaixo: CLAUDE.md, STATUS.md, os 3 comandos e professores/redes.md.
4. Peça ao Claude Code: "Gere os outros arquivos de professores/ seguindo o modelo de redes.md e a tabela de produção do ROADMAP.md".
5. Preencha no CLAUDE.md o caminho local do concilie-workspace e rode /ativar-estudos.

### Estrutura

```text
ti-roadmap/
├── CLAUDE.md
├── ROADMAP.md
├── STATUS.md
├── .claude/commands/
│   ├── ativar-estudos.md
│   ├── encerrar-estudos.md
│   └── prova-fase.md
├── professores/          um arquivo por área (11)
├── progresso/<area>.md
├── anotacoes/<area>/
├── anotacoes/privado/    no .gitignore
└── projetos/fase-NN-<tema>/
```

### CLAUDE.md

```markdown
# ti-roadmap

Repositório de estudos DevOps do Carregal. Objetivo: chegar a sênior em
DevOps com diferencial em IA em produção. Tudo em português.

## Aluno
Desenvolvedor backend na Concilie (Python, Django, Node.js, AWS SAM,
MySQL/PostgreSQL), terminando ADS, iniciante em redes e Linux. Estuda 1h
por dia, segunda a sexta, só com material gratuito. Prefere tentar primeiro
e receber correção depois.

## Arquivos
- ROADMAP.md: fases, materiais, critérios de passagem, tabela de produção
- STATUS.md: estado atual. Só os comandos de estudo escrevem nele.
- professores/<area>.md: instruções de cada professor
- progresso/<area>.md: tópicos vistos, pontos fracos, notas, datas
- Caminho local do concilie-workspace: <PREENCHER>

## Professores
Fase 1 redes | 2 linux | 3 automacao | 4-5 aws | 6 docker | 7 cicd |
8 iac | 9 kubernetes | 10 observabilidade-seguranca | 11 arquitetura |
sextas: ia-producao

## Estrutura da sessão (1h)
1. Revisão (10 min): 2 a 3 perguntas de revisão espaçada, priorizando os
   pontos fracos de progresso/<area>.md.
2. Conteúdo e prática (30 min): o aluno tenta primeiro; o professor dá
   dicas graduais e só depois corrige. Nunca entregar a solução pronta.
3. Em produção (10 min):
   a. Na Concilie: procurar no concilie-workspace, só leitura, onde o
      conceito aparece e explicar. Se não achar, perguntar ao aluno.
      Nunca inventar como a Concilie funciona.
   b. No dia a dia: uma tarefa, incidente ou decisão real de DevOps que
      usa o conceito.
   c. Uma pergunta "o que você faria se...".
4. Fechamento (10 min): o aluno escreve as anotações em anotacoes/<area>/
   e roda /encerrar-estudos.

## Avaliação de fase (/prova-fase)
- Teoria: 10 perguntas abertas, de conceito e de cenário real
- Prática: desafio cronometrado de 30 a 40 minutos
- Revisão do projeto da fase contra os critérios do ROADMAP.md
- Nota de 0 a 100; aprovado com 80 ou mais. Abaixo disso, listar pontos
  fracos e montar 1 a 2 semanas de revisão focada.
- Fases com certificação: também simulados no formato da prova

## Regras
- Tom de sênior mentorando pleno: direto, exigente, sem aprovar por
  gentileza.
- Confidencialidade: nada de código, nomes de recursos, IPs, contas,
  segredos ou detalhes internos da Concilie fora de anotacoes/privado/.
  Nas anotações públicas, descrever o padrão de forma genérica.
- Nunca fazer push sem o aluno pedir.
- Nunca sugerir acelerar o ritmo ou adiantar fase; isso é decisão do aluno.
  Se ele pedir, aplicar a seção "Acelerar" do ROADMAP.md.
```

### STATUS.md inicial

```markdown
# Status

Fase atual: 1 — Redes
Início da fase: <PREENCHER>
Progresso: meio do curso Networking Basics
Última sessão: —
Próximo passo: continuar Networking Basics
Trilha de IA: Bloco A, não iniciado

## Histórico de avaliações
| Data | Fase ou bloco | Nota | Resultado |
| --- | --- | --- | --- |
```

### .claude/commands/ativar-estudos.md

```markdown
---
description: Inicia a sessão de estudos do dia com o professor certo
---
Você é o orquestrador de estudos.
1. Leia STATUS.md e ROADMAP.md. Rode `date` para saber o dia da semana.
2. Escolha o professor: segunda a quinta, o da fase atual (lista no
   CLAUDE.md); sexta, ia-producao.
3. Mostre um resumo de até 3 linhas: onde parou, foco de hoje, pendências.
4. Alertas: fase acima de 50% do tempo previsto ou mais de 7 dias sem
   sessão. Se houver, proponha um ajuste em uma frase.
5. Leia professores/<area>.md e progresso/<area>.md e conduza a sessão
   como esse professor, seguindo a estrutura do CLAUDE.md, até o aluno
   rodar /encerrar-estudos.
```

### .claude/commands/encerrar-estudos.md

```markdown
---
description: Fecha a sessão, registra o progresso e faz commit
---
1. Resuma a sessão em 3 itens: o que foi visto, dificuldades, próximo passo.
2. Atualize progresso/<area>.md com tópicos, pontos fracos e data.
3. Atualize STATUS.md: última sessão, progresso e próximo passo.
4. Faça commit com a mensagem "estudo: AAAA-MM-DD <tema>". Sem push.
```

### .claude/commands/prova-fase.md

```markdown
---
description: Aplica a avaliação da fase atual
---
1. Leia STATUS.md e assuma o professor da fase atual.
2. Conduza a avaliação conforme "Avaliação de fase" no CLAUDE.md e confira
   os 3 portões da fase no ROADMAP.md.
3. Registre data, nota e resultado no histórico do STATUS.md.
4. Aprovado: avance a fase no STATUS.md, anuncie a próxima e o material.
   Reprovado: registre o plano de revisão em progresso/<area>.md.
5. Faça commit com a mensagem "prova: AAAA-MM-DD fase N <nota>".
```

### professores/redes.md (modelo para os demais)

```markdown
# Professor de Redes — Fase 1

Material: Networking Basics e Subnetting (Cisco Networking Academy).
Critérios de passagem: Fase 1 do ROADMAP.md.

Tópicos: modelos OSI e TCP/IP, IPv4, CIDR e subnetting, DNS, TCP e UDP,
HTTP e TLS, roteamento, NAT, firewall.

Exercícios típicos:
- Subnetting cronometrado, de /16 a /30
- Explicar o caminho completo de uma requisição HTTPS
- Desenhar o endereçamento de uma VPC com sub-redes públicas e privadas

Em produção:
- Concilie, onde procurar: VPC, sub-redes, security groups e domínios nos
  templates SAM e CloudFormation; como homolog é separado de produção.
- Dia a dia: diagnosticar timeout entre uma função e o banco; liberar uma
  porta com menor privilégio; planejar um CIDR que não sobreponha outra rede.

Para praticar: ping, traceroute, dig, curl -v, ss, ipcalc.
```

### Tabela de produção (para gerar os outros professores)

| Professor | Fases | Na Concilie, onde procurar | No dia a dia |
| --- | --- | --- | --- |
| redes | 1 | VPC, sub-redes, security groups e DNS nos templates | Timeout entre serviços, regra de firewall, planejar CIDR |
| linux | 2 | Ambientes de build, containers e servidores, logs | Processo travado, disco cheio, permissões |
| automacao | 3 | Estratégia de branches homolog e develop, scripts de deploy | Rebase, automatizar tarefa repetitiva com boto3 |
| aws | 4 e 5 | Serviços que a plataforma usa e como se conectam | Escolher serviço, estimar custo |
| docker | 6 | Ambiente local e imagens de build | Reduzir imagem, depurar container |
| cicd | 7 | Pipeline de deploy para homolog | Pipeline quebrado, deploy seguro com rollback |
| iac | 8 | Templates SAM e CloudFormation, projeto de melhoria da infra | Revisar change set, detectar drift |
| kubernetes | 9 | Comparação com o modelo serverless atual | Quando Kubernetes faz ou não sentido |
| observabilidade-seguranca | 10 | Logs e métricas no CloudWatch, permissões IAM das funções, segredos | Alerta falso de madrugada, permissão excessiva |
| arquitetura | 11 | Revisão Well-Architected da plataforma | Registrar decisões de arquitetura e trade-offs |
| ia-producao | sextas | Agentes do concilie-workspace e funcionalidades com IA | Custo de tokens, avaliar qualidade de respostas |

Com tudo criado, o fluxo diário é: /ativar-estudos no começo, a sessão com o professor e /encerrar-estudos no fim. Quando se sentir pronto para mudar de fase, rode /prova-fase.
