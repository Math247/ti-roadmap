# Professor de IA em Produção — Trilha de sextas

Material: documentação da Anthropic, cursos do repositório
anthropics/courses, documentação do Amazon Bedrock e do pgvector.
Critérios de passagem: seção "Trilha paralela: IA em produção" do ROADMAP.md.
Cada bloco fecha com o projeto funcionando no repositório e a avaliação do
agente com nota mínima de 80%. A trilha nunca trava a principal.

Blocos:
- A (Fases 1 a 3): fundamentos de LLM: tokens, contexto, prompts,
  chamadas de API. Projeto: CLI em Python que resume logs de servidor.
- B (Fases 4 e 5): RAG com embeddings e busca vetorial no pgvector.
  Projeto: busca semântica sobre documentação técnica.
- C (Fases 6 e 7): agentes, tool use e MCP. Projeto: agente que consulta a
  AWS via boto3 e responde perguntas sobre a infra.
- D (Fases 8 e 9): deploy de IA com Lambda, Bedrock, filas e limites de
  taxa. Projeto: serviço RAG serverless criado com IaC e pipeline.
- E (Fases 10 e 11): evals, observabilidade e custo de LLM, guardrails.
  Projeto: painel de qualidade e custo por requisição do serviço do bloco D.

Exercícios típicos:
- Medir tokens e custo de uma chamada e reduzir sem perder qualidade
- Montar um conjunto pequeno de evals e comparar duas versões de prompt
- Tratar limite de taxa, timeout e erro da API com retry e backoff

Em produção:
- Concilie, onde procurar: agentes do concilie-workspace e funcionalidades
  com IA.
- Dia a dia: custo de tokens subindo sem explicação; avaliar a qualidade
  das respostas antes de trocar de modelo.

Para praticar: SDK da Anthropic em Python, contagem de tokens, pgvector no
PostgreSQL local, boto3 com Bedrock.
