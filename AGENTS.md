# AGENTS.md

Instruções para qualquer IA (Claude, Cowork, Claude Code, etc.) que trabalhe nesta pasta de busca de emprego.

Este arquivo é o "cérebro" do sistema: garante que a IA fale sempre a mesma língua sobre o Heitor, não invente
números, não varie a história de carreira de candidatura para candidatura, e saiba onde e como registrar o que
foi feito. Fonte do perfil: `Curriculo_-_Heitor_Garcez_Martins_Louzeiro.pdf` (não versionado).

## Objetivo

Apoiar a busca de emprego: encontrar vagas, preparar candidaturas e manter o tracker atualizado. O tracker é a
fonte de verdade sobre candidaturas; este arquivo é a fonte de verdade sobre como se apresentar.

- Tracker: `tracker/candidaturas.csv` (local).
- Vagas encontradas e ainda não aplicadas: `vagas/` (um arquivo por rodada de busca, `AAAA-MM-DD_linkedin.md`).

## Perfil do candidato

- **Nome:** Heitor Garcez Martins Louzeiro.
- **Título profissional único:** "Desenvolvedor Backend Python" (em inglês: "Backend Python Developer"). Usar
  sempre este título, em todo material. Não variar para "Engenheiro de Software", "Full Stack" etc.
- **Narrativa de carreira (versão única):** Desenvolvedor backend com 3 anos de experiência em Python. Hoje é
  Desenvolvedor Backend e DevOps na Prefeitura Municipal de Corrente (desde jun/2025), onde resolveu um incidente
  grave de segurança. Antes disso, fez trabalhos freelance/por projeto (abr/2023 a jun/2024): automação para a
  SEDUC, PoC para a OKEAN Yachts e o sistema de eventos da Agrosul Piauí, este último desenvolvido durante a
  graduação no IFPI. Os freelances são projetos curtos e pontuais, não empregos full-time simultâneos.
- **Métricas chave (usar sempre estes números, nunca outros, nunca arredondar para cima):**
  - Parou um ataque ao servidor em **menos de 15 minutos** e colocou **cerca de 25 sistemas** de volta no ar.
  - Reforçou a segurança de **24 aplicações em Docker** (firewall, limites de recursos, atualização do servidor).
  - Relatório do incidente (causa, impacto, solução) entregue em **24 horas**.
  - Na Prefeitura, coordena uma **equipe de 4 pessoas** no desenvolvimento dos sistemas: define o que deve
    ser feito, como fazer e os prazos. Descrever como coordenação técnica, não como cargo de gestor/tech lead.
  - Sistema de eventos Agrosul Piauí: **+50 artigos** submetidos, **+100 listas de presença**, **+900 certificados**.
  - Automação SEDUC: **+1.000 alunos** cadastrados, tempo de processamento reduzido em **80%**.
  - PoC OKEAN Yachts: atuou como **desenvolvedor frontend** (não backend) numa equipe de **4 pessoas** (2 devs,
    1 tech lead, 1 scrum master); criou **4 páginas** (Home, Login, Signup, Chat de atendimento integrado ao ChatGPT).
- **Stack (só o que está no CV, não acrescentar):** Python, Django, PostgreSQL, Docker, Linux (servidor,
  firewall), Heroku, Git, Selenium, OpenAI API, HTML, CSS, Bootstrap.
- **Localização / permissão de trabalho:** São Paulo, Brasil. Brasileiro, pode trabalhar no Brasil sem visto.
- **Idiomas:** Português (nativo). Inglês básico (entende bem, mas tem dificuldade em falar e escrever).
  Nunca declarar inglês intermediário/avançado/fluente.
- **Disponibilidade:** **somente vagas 100% remotas** (no Brasil). Descartar vagas híbridas e presenciais, mesmo
  em São Paulo. Aceita **CLT e PJ** (não descartar vaga pelo regime).
  Data de início: **imediata** (pode começar assim que for aprovado).
- **Formação:** Análise e Desenvolvimento de Sistemas, IFPI (Instituto Federal do Piauí). Curso de Django Web
  Framework (Udemy).
- **CV em uso:** `output/cv_heitor_louzeiro_pt.pdf` e `output/cv_heitor_louzeiro_en.pdf`, gerados por
  `python scripts/build_cv.py`.
- **Contato:** heitorlouzeiro2019@gmail.com · (89) 99905-4536 · https://www.linkedin.com/in/heitor-louzeiro/
- **Níveis-alvo (foco obrigatório):** somente vagas de **Estágio, Júnior ou Pleno**. Descartar Sênior,
  Especialista, Tech Lead, Staff e Principal, mesmo que o stack bata.
- **Prioridade de vagas (em ordem):**
  1. Desenvolvedor Backend Python (Júnior / Pleno), Django, remoto.
  2. Desenvolvedor Python Júnior / Pleno (qualquer framework), remoto.
  3. Estágio remoto em desenvolvimento backend / Python (conferir se exige matrícula ativa na faculdade).
  4. DevOps / SRE Júnior remoto com Python, Docker e Linux.
  5. Automação / RPA remoto com Python (Selenium).
  **Foco no Brasil:** só vagas de empresas/contratação no Brasil (remotas dentro do Brasil). Descartar vagas
  internacionais ("remote worldwide", pagamento em dólar/euro, cliente estrangeiro), vagas fora do Brasil e vagas
  que exigem inglês avançado/fluente.
- **Buscas de nicho prioritárias (LinkedIn):** "Desenvolvedor Python", "Desenvolvedor Backend Python",
  "Python Django", "Desenvolvedor Django", "Python Júnior", "DevOps Júnior", "Automação Python",
  "Desenvolvedor Python Pleno", "Backend Pleno", "Estágio Python",
  "Estágio Desenvolvimento Back End".

## Regras ao escrever em nome do Heitor

- Sempre em primeira pessoa, tom direto, frases curtas, sem jargão de marketing.
- Escrever em português por padrão. Em inglês, só se a vaga exigir, e sem exagerar o nível de inglês.
- Responder perguntas de elegibilidade e localização com honestidade.
- **Não criar contas, não digitar senhas, não resolver CAPTCHA.** Pular essas etapas e avisar.
- **Não auto-submeter candidaturas.** Preparar a candidatura (respostas, carta, CV certo) e deixar para o Heitor
  revisar e enviar, salvo autorização explícita para uma vaga específica.
- **Nunca inventar:** pretensão salarial, anos de experiência em tecnologias além das listadas, tecnologias que
  não estão no CV (ex: FastAPI, AWS, Kubernetes, React), nível de inglês, ou respostas técnicas dissertativas
  detalhadas. Nesses casos, salvar rascunho e perguntar.
- Se a vaga pedir algo que o Heitor não tem, dizer isso no resumo da vaga (ex: "pede AWS, que não está no CV")
  em vez de esconder.

## Como atualizar o tracker

- Cada candidatura vira uma linha em `tracker/candidaturas.csv` com as colunas:
  `Date, Company, Role, Location, Mode, Source / ATS, Status, Notes`.
- Valores de Status: `Para avaliar`, `Applied`, `Interview done`, `Action needed`, `Aguardando resposta`, `Closed`.
- Antes de aplicar, conferir se a empresa e a vaga já estão na lista, para não duplicar candidatura.
- Depois de qualquer alteração, reler o tracker e confirmar que a linha foi salva.

## Como buscar vagas no LinkedIn

- Usar as buscas prontas em `vagas/README.md` (filtros: Brasil, somente remoto, últimas 24h/semana, nível Estágio/Júnior/Pleno).
- Para cada vaga relevante, registrar no arquivo da rodada em `vagas/`: empresa, cargo, local/modelo, link, e
  uma linha de fit (o que bate com o CV e o que falta).
- Conferir se a vaga ainda está aberta e se é mesmo 100% remota antes de preparar candidatura (vagas antigas
  somem ou expiram; algumas marcadas como remotas pedem ida ao escritório).

## Onde buscar vagas

LinkedIn (Easy Apply), Indeed, Gupy, Programathor, sites das empresas.
ATS comuns: Gupy, Greenhouse, Ashby, Lever, Recruitee, Teamtailor, SuccessFactors, Workable, Oracle ORC.

## Acesso técnico (como a IA interage com o navegador)

1. **Claude in Chrome** (extensão oficial): controla uma aba do Chrome já logado no LinkedIn. É a forma
   recomendada para buscar vagas com filtros e usar o Easy Apply.
2. **Uma skill de automação de navegador tipo "ego-lite"**: ajuste as permissões em
   `.claude/settings.local.json.example` para o comando correspondente.

Observação: sessões na nuvem do Claude Code podem ter o linkedin.com bloqueado pela política de rede. Nesse caso,
a busca é feita por pesquisa web e os links precisam ser conferidos no navegador.
