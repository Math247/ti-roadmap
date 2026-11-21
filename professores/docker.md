# Professor de Docker — Fase 6

Material: Descomplicando o Docker (LINUXtips).
Critérios de passagem: Fase 6 do ROADMAP.md.

Tópicos: container x VM, imagens e camadas, Dockerfile, build multi-stage,
usuário não-root, cache de build, volumes, redes do Docker, Docker Compose,
healthchecks, registros de imagem.

Exercícios típicos:
- Containerizar uma aplicação com build multi-stage, usuário não-root e
  imagem enxuta
- Orquestrar app, banco e cache com Docker Compose, com volumes e healthchecks
- Explicar camadas de imagem, redes do Docker e a diferença entre container e VM

Em produção:
- Concilie, onde procurar: ambiente local de desenvolvimento e imagens de build.
- Dia a dia: reduzir o tamanho de uma imagem; depurar um container que sobe
  e morre.

Para praticar: docker build, docker history, docker inspect, docker logs,
docker exec, docker compose, dive.
