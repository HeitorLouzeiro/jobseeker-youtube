# CLAUDE.md

> Este arquivo é um espelho de `AGENTS.md` (mesmo conteúdo), mantido separado porque o Claude Code lê
> `CLAUDE.md` automaticamente. Edite os dois juntos para não ficarem dessincronizados.

Instruções para qualquer IA (Claude, Cowork, Claude Code, etc.) que trabalhe nesta pasta de busca de emprego.

Este arquivo é o "cérebro" do sistema: é ele que garante que a IA fale sempre a mesma língua sobre você,
não invente números, não varie a sua história de carreira de candidatura para candidatura, e saiba exatamente
onde e como registrar o que foi feito. Preencha os campos entre `[colchetes]` com os seus dados antes de usar.

> Por que um arquivo assim importa: sem regras explícitas, um agente de IA tende a "flutuar" — hoje diz que
> você reduziu retrabalho em 60%, amanhã em 70%; hoje conta sua carreira de um jeito, amanhã de outro. Isso é
> péssimo numa busca de emprego, onde CVs, LinkedIn, formulários e respostas de entrevista precisam bater. Este
> arquivo existe para ser a única fonte de verdade sobre como falar de você.

## Objetivo

Apoiar a sua busca de emprego: encontrar vagas, candidatar-se e manter um tracker atualizado. A planilha/tracker
(ver seção "Como atualizar o tracker") é a fonte de verdade sobre candidaturas — este arquivo é a fonte de
verdade sobre como se apresentar.

- Tracker: `[link da sua planilha Google Sheets, ou aponte para tracker/job_tracker_template.csv se preferir local]`
- Aba/coluna "Applications": todas as candidaturas.
- Aba/coluna "Summary": contagens por status.

## Perfil do candidato (preencha com os seus dados)

- **Título profissional único:** `[ex: "AI Integration Engineer"]`. Escolha UM título e use sempre o mesmo —
  não deixe a IA variar entre "Engenheiro de Automação", "Especialista em IA" etc. em materiais diferentes.
- **Narrativa de carreira (defina UMA versão e repita sempre):** descreva aqui, em poucas frases, como quer que
  sua trajetória seja contada. Se teve mais de um papel na mesma empresa, diga explicitamente que é "uma história
  de crescimento contínuo", e não "empregos separados". Se teve um projeto paralelo/freelance, deixe claro que é
  part-time e simultâneo, não dois empregos full-time ao mesmo tempo.
- **Métrica(s) chave:** se você tem um número que usa para se vender (ex: "reduzi X em Y%"), escreva-o aqui UMA
  vez e diga "usar sempre este número, nunca outro". Isso evita que a IA arredonde ou invente variações.
- **Localização / permissão de trabalho:** `[cidade, país; nacionalidade; situação de visto/permissão]`.
- **Idiomas:** `[liste idioma e nível, na forma exata que quer que apareça — ex: evite abreviações como "B2" se preferir "proficiência profissional"]`.
- **Disponibilidade:** `[full-time / part-time, remoto / híbrido / presencial, a partir de quando]`.
- **CV em uso:** `[nome do arquivo, ex: cv_seu_nome_en.pdf]` — gerado por `scripts/build_cv.py` (veja abaixo).
- **Portfolio / LinkedIn / e-mail de contato:** `[links e e-mail que a IA deve usar nas candidaturas]`.
- **Prioridade de vagas:** `[liste os tipos de vaga/empresa em ordem de prioridade]`.
- **Buscas de nicho prioritárias:** `[palavras-chave que a IA deve priorizar ao buscar vagas]`.

## Regras ao escrever em seu nome (ajuste ao seu estilo)

- Defina aqui maneirismos de escrita que a IA deve seguir ou evitar (ex: "nunca usar travessão", "sempre em
  primeira pessoa", "tom direto, sem jargão").
- Responder perguntas de elegibilidade e localização com honestidade.
- **Não criar contas, não digitar senhas, não resolver CAPTCHA.** A IA deve pular essas etapas e te avisar.
- Defina se a IA **pode auto-submeter candidaturas** ou só preparar rascunhos para sua revisão. Se puder
  auto-submeter, diga em quais condições (ex: só em Easy Apply, só se o fit for claro).
- Diga explicitamente o que a IA **nunca deve inventar** por conta própria: pretensão salarial, anos exatos de
  experiência num nicho específico, respostas dissertativas técnicas detalhadas. Nesses casos, ela deve salvar
  um rascunho e te perguntar.

## Como atualizar o tracker

- Cada candidatura vira uma linha com as colunas: `Date, Company, Role, Location, Mode, Source / ATS, Status, Notes`.
- Valores de Status sugeridos: `Applied`, `Interview done`, `Action needed`, `Aguardando resposta`, `Closed`.
- Antes de aplicar, a IA deve conferir se a empresa e a vaga já estão na lista, para não duplicar candidatura.
- Depois de qualquer alteração, a IA deve reler o tracker e confirmar visualmente que a linha foi salva
  (planilhas online às vezes "perdem" a digitação silenciosamente se o clique for no lugar errado).

## Onde buscar vagas

LinkedIn (Easy Apply), Indeed, relocate.me, sites das empresas.
ATS comuns: Greenhouse, Ashby, Lever, Recruitee, Teamtailor, SuccessFactors, Workable, Oracle ORC.

## Acesso técnico (como a IA interage com o navegador)

Este workflow foi desenhado para funcionar com qualquer uma das duas opções abaixo — escolha uma:

1. **Claude in Chrome** (extensão oficial): a IA controla uma aba do seu navegador Chrome já logado, útil para
   preencher formulários de candidatura e editar planilhas online diretamente.
2. **Uma skill de automação de navegador tipo "ego-lite"**: se você usa uma skill/ferramenta própria de browser
   automation (ex: um driver Node.js), ajuste as permissões em `.claude/settings.local.json.example` para o
   comando correspondente e documente aqui como invocá-la.

Se sua planilha for um Google Sheet nativo sem conector de API disponível, a IA deve editar diretamente pelo
navegador: clicar na caixa de nome (Name Box), digitar a referência da célula (ex: `A61`), Enter, digitar o
valor. Sempre releia depois para confirmar que salvou.
