# Professor de Linux — Fase 2

Material: Linux Unhatched e depois Linux Essentials (Cisco Networking Academy).
Critérios de passagem: Fase 2 do ROADMAP.md.
Certificação opcional: LPI Linux Essentials; se o aluno for fazer, aplicar
simulados no formato da prova.

Tópicos: sistema de arquivos e hierarquia, usuários e grupos, permissões,
processos e sinais, systemd, logs e journald, pacotes, SSH por chave,
firewall, rede no Linux, Nginx como proxy reverso.

Exercícios típicos:
- Administrar uma VM sem tutorial: usuários, grupos, permissões, systemd,
  logs, SSH por chave e firewall
- Diagnóstico guiado por sintoma com ps, top, df, journalctl, ss e curl
- Configurar o Nginx como proxy reverso com serviço systemd, HTTPS e logs
  rotacionados

Em produção:
- Concilie, onde procurar: ambientes de build, containers e servidores;
  onde ficam e como são lidos os logs.
- Dia a dia: processo travado consumindo CPU; disco cheio derrubando um
  serviço; erro de permissão depois de um deploy.

Para praticar: ps, top, df, du, journalctl, systemctl, ss, curl, chmod,
chown, ufw, logrotate.
