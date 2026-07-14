# Tracker de candidaturas

Este CSV (`job_tracker_template.csv`) é um ponto de partida. Você tem duas opções de uso:

1. **Local (mais simples):** deixe a IA ler e editar este CSV diretamente pelo Claude/Cowork, sem depender de
   navegador. Basta apontar para ele em `AGENTS.md`, na seção "Tracker".
2. **Google Sheets (como no vídeo):** importe este CSV para uma planilha Google Sheets nova. Deixe as colunas
   exatamente como estão (`Date, Company, Role, Location, Mode, Source / ATS, Status, Notes`). Aponte o link da
   planilha em `AGENTS.md`. Se você não tiver um conector de API do Google Sheets disponível, a IA precisa editar
   pelo navegador (Claude in Chrome ou a skill de automação que você estiver usando) — clicando na caixa de nome
   (Name Box) e digitando a referência da célula.

## Colunas

- `Date`: data da candidatura (YYYY-MM-DD).
- `Company`: nome da empresa.
- `Role`: título da vaga.
- `Location`: localização da vaga.
- `Mode`: Remote / Hybrid / On-site.
- `Source / ATS`: onde a vaga foi encontrada ou por qual ATS foi aplicada (LinkedIn, Greenhouse, Lever, etc.).
- `Status`: sugestão de valores: `Applied`, `Interview done`, `Action needed`, `Aguardando resposta`, `Closed`.
- `Notes`: qualquer contexto relevante (próximos passos, quem indicou, o que falta).

## Dica

Peça para a IA sempre conferir se a empresa + vaga já existem no tracker antes de aplicar de novo, e para
reler o tracker depois de cada atualização para confirmar que salvou.
