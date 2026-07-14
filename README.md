# jobseeker-youtube

Um template de "assistente de busca de emprego" para rodar com [Claude](https://claude.ai) / [Cowork](https://claude.ai)
ou [Claude Code](https://claude.com/product/claude-code). Este repositório mostra, de forma genérica e sem
dados pessoais, o sistema usado no vídeo: um agente de IA que busca vagas, prepara candidaturas, gera CV em PDF
e mantém um tracker de candidaturas atualizado.

`[LINK DO VÍDEO NO YOUTUBE AQUI]`

## O que tem aqui

- **`AGENTS.md` / `CLAUDE.md`** — o "cérebro" do sistema. Um arquivo de instruções que qualquer agente de IA lê
  antes de agir: quem você é, como quer ser descrito, quais regras seguir, onde registrar o que foi feito. É a
  peça mais importante do repositório — vale a pena ler antes de tudo.
- **`scripts/build_cv.py`** — gera um CV em PDF (EN e PT) a partir de um dicionário Python simples. O layout
  fica separado do conteúdo, então você troca o texto sem mexer no design.
- **`tracker/`** — um template de planilha de candidaturas (CSV), com instruções para usar local ou importado
  para o Google Sheets.
- **`.claude/settings.local.json.example`** — exemplo de permissões para liberar comandos sem precisar aprovar
  toda hora (ex: automação de navegador).

Este repositório é intencionalmente **sem dados pessoais reais**: nome, e-mail, telefone, histórico de carreira
e CVs de exemplo são todos fictícios/placeholder. Antes de usar, preencha com os seus dados (veja "Como usar").

## Como funciona

1. Você preenche `AGENTS.md` com o seu perfil: título profissional, narrativa de carreira, métricas-chave,
   idiomas, disponibilidade, prioridades de vaga. Esse arquivo vira a única fonte de verdade sobre como a IA
   deve falar de você — evita que ela invente números ou conte sua trajetória de um jeito diferente a cada CV.
2. Você conversa com Claude/Cowork/Claude Code dentro desta pasta e pede coisas como "busca vagas de X no
   LinkedIn das últimas 24h" ou "prepara uma candidatura pra essa vaga".
3. Para interagir com sites (LinkedIn, Indeed, portais de ATS, o próprio Google Sheets), o agente usa **um
   navegador**. Duas opções, escolha a que você já tem disponível:
   - **[Claude in Chrome](https://claude.com)**: a extensão oficial, controla uma aba do seu Chrome já logado.
   - **Uma skill de automação de navegador própria** (no vídeo, chamada de `ego-lite`): qualquer alternativa
     leve baseada em Node.js/Playwright que você já use para automatizar navegador. O repositório não depende
     de uma implementação específica — só ajuste `.claude/settings.local.json` para liberar o comando dela.
4. Cada candidatura feita é registrada no tracker (`tracker/`), e o CV é gerado/atualizado com
   `python scripts/build_cv.py` sempre que o posicionamento mudar.

## Como usar

```bash
git clone <o-seu-fork-deste-repo>
cd jobseeker-youtube

# 1. Preencha os seus dados
#    - Edite AGENTS.md (e CLAUDE.md, é um espelho) com seu perfil.
#    - Edite scripts/build_cv.py, no dicionário CONTENT, com o conteúdo do seu CV.
#    - Copie tracker/job_tracker_template.csv (ou importe pro Google Sheets) e aponte o link em AGENTS.md.

# 2. Instale a dependência do gerador de CV
pip install reportlab

# 3. Gere o CV de exemplo pra conferir o layout
python scripts/build_cv.py
# gera output/cv_example_en.pdf e output/cv_example_pt.pdf

# 4. Abra a pasta no Claude Code / Cowork e comece a pedir para o agente buscar e aplicar em vagas
```

## Privacidade

- `output/`, `tmp/` e qualquer `*.pdf` já estão no `.gitignore` — seus CVs gerados com dados reais nunca são
  versionados por engano.
- `.claude/settings.local.json` (com suas permissões específicas) também está no `.gitignore`; use o
  `.example` como base.
- Se for publicar seu próprio fork, revise o histórico de commits antes de tornar o repo público — dados
  pessoais colados num commit antigo continuam no histórico do Git mesmo depois de apagados do arquivo atual.

## Licença

MIT — veja `LICENSE`. Use, adapte e compartilhe à vontade.
