# Gera CVs em PDF (EN e PT) a partir de um dicionário de conteúdo simples.
# Design: uma coluna, tipografia sóbria, sem cores berrantes.
#
# COMO USAR: edite o dicionário CONTENT abaixo com os seus dados (ou copie este arquivo e crie o seu próprio
# CONTENT). Depois rode: python scripts/build_cv.py
#
# Este arquivo é o "motor" de geração de PDF. Ele é genérico de propósito: toda a lógica de layout está nas
# funções abaixo, e todo o conteúdo pessoal fica isolado no dicionário CONTENT, para você poder trocar o
# conteúdo sem tocar no layout (e vice-versa).

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]

FONT_CANDIDATES = {
    "Sans": [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ],
    "Sans-Bold": [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ],
    "Sans-Italic": [
        "/System/Library/Fonts/Supplemental/Arial Italic.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf",
    ],
}

INK = colors.HexColor("#1A1A1A")
MUTED = colors.HexColor("#5A5F66")
ACCENT = colors.HexColor("#0F3557")
RULE = colors.HexColor("#C9CED4")


def register_fonts():
    for name, paths in FONT_CANDIDATES.items():
        for p in paths:
            if Path(p).exists():
                pdfmetrics.registerFont(TTFont(name, p))
                break
        else:
            raise FileNotFoundError(f"Nenhuma fonte encontrada para {name}")


def wrap(text, font, size, width):
    words = text.split()
    lines, cur = [], ""
    for wd in words:
        trial = (cur + " " + wd).strip()
        if pdfmetrics.stringWidth(trial, font, size) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


class Doc:
    def __init__(self, out):
        self.c = canvas.Canvas(str(out), pagesize=A4)
        self.w, self.h = A4
        self.margin = 16 * mm
        self.x = self.margin
        self.cw = self.w - 2 * self.margin
        self.y = self.h - 16 * mm

    def text(self, s, font="Sans", size=9, leading=None, color=INK, x=None, width=None, space=0):
        leading = leading or size * 1.22
        x = x if x is not None else self.x
        width = width or (self.w - x - self.margin)
        self.c.setFont(font, size)
        self.c.setFillColor(color)
        for line in wrap(s, font, size, width):
            self.c.drawString(x, self.y, line)
            self.y -= leading
        self.y -= space

    def section(self, title):
        self.y -= 4
        self.c.setFillColor(ACCENT)
        self.c.setFont("Sans-Bold", 9.6)
        self.c.drawString(self.x, self.y, " ".join(title.upper()))
        self.y -= 3.4
        self.c.setStrokeColor(RULE)
        self.c.setLineWidth(0.7)
        self.c.line(self.x, self.y, self.x + self.cw, self.y)
        self.y -= 11

    def role(self, left, right, size=9.6):
        self.c.setFillColor(INK)
        self.c.setFont("Sans-Bold", size)
        self.c.drawString(self.x, self.y, left)
        self.c.setFont("Sans", 8.4)
        self.c.setFillColor(MUTED)
        self.c.drawRightString(self.x + self.cw, self.y, right)
        self.y -= size * 1.3

    def bullet(self, s, size=8.8, leading=None):
        leading = leading or size * 1.2
        self.c.setFillColor(INK)
        self.c.circle(self.x + 2.0, self.y + 2.4, 1.0, fill=1, stroke=0)
        self.c.setFont("Sans", size)
        bx = self.x + 8
        for line in wrap(s, "Sans", size, self.cw - 8):
            self.c.drawString(bx, self.y, line)
            self.y -= leading
        self.y -= 1.2

    def kv(self, key, value, size=8.8):
        self.c.setFont("Sans-Bold", size)
        self.c.setFillColor(INK)
        self.c.drawString(self.x, self.y, key + ":")
        kw = pdfmetrics.stringWidth(key + ": ", "Sans-Bold", size)
        self.c.setFont("Sans", size)
        for line in wrap(value, "Sans", size, self.cw - kw):
            self.c.drawString(self.x + kw, self.y, line)
            self.y -= size * 1.25
        self.y -= 1.6


# ---------------------------------------------------------------------------
# CONTEÚDO DE EXEMPLO — troque tudo abaixo pelos seus dados reais.
# Mantenha a mesma estrutura de chaves; só o texto precisa mudar.
# ---------------------------------------------------------------------------
CONTENT = {
    "en": {
        "out": "cv_example_en.pdf",
        "pdf_title": "Jane Doe - CV EN",
        "name": "Jane Doe",
        "title": "Your Professional Title",
        "tagline": "Key skill  ·  Key skill  ·  Key skill",
        "contact": "City, Country  ·  you@example.com  ·  +00 000 000 000",
        "contact2": "yourportfolio.com  ·  linkedin.com/in/yourprofile  ·  github.com/yourhandle",
        "s_summary": "Summary",
        "summary": (
            "One consistent paragraph describing who you are professionally, your years of experience, the "
            "kind of problems you solve, and the single metric you always want to lead with. Keep this exact "
            "wording across every CV version so your story never contradicts itself."
        ),
        "s_exp": "Work Experience",
        "chatguru_h": "Company Name, what they do",
        "chatguru_m": "Month Year to Month Year  ·  Remote/Hybrid/On-site",
        "chatguru_note": "One line framing the whole tenure, e.g. a continuous growth story across roles.",
        "roles": [
            (
                "Most Recent Title",
                "Month Year to Month Year",
                [
                    "Result-oriented bullet describing scope and impact.",
                    "Another bullet with a concrete, consistent metric.",
                ],
            ),
            (
                "Previous Title",
                "Month Year to Month Year",
                [
                    "Bullet describing what you built or owned in this role.",
                ],
            ),
        ],
        "ninja_h": "Side Project / Consultancy Name",
        "ninja_m": "Month Year to Month Year",
        "ninja_note": "One line clarifying this was part-time and ran alongside your main role, if applicable.",
        "ninja_bullets": [
            "Bullet describing the scope of this side project or consultancy.",
        ],
        "s_projects": "Selected Projects",
        "projects": [
            "Project name: one line describing what it does and the stack used.",
        ],
        "s_skills": "Skills",
        "skills": [
            ("Category", "Skill, skill, skill"),
            ("Category", "Skill, skill, skill"),
        ],
        "s_lang": "Languages & Education",
        "languages": "Language (level)  ·  Language (level)",
        "education": "Degree / certification / what you are currently studying",
        "s_refs": "References",
        "refs": [
            '"A short quote from a former manager or client." Name, Title, Company',
        ],
    },
    "pt": {
        "out": "cv_example_pt.pdf",
        "pdf_title": "Jane Doe - CV PT",
        "name": "Jane Doe",
        "title": "Seu Título Profissional",
        "tagline": "Skill chave  ·  Skill chave  ·  Skill chave",
        "contact": "Cidade, País  ·  voce@example.com  ·  +00 000 000 000",
        "contact2": "seuportfolio.com  ·  linkedin.com/in/seuperfil  ·  github.com/seuusuario",
        "s_summary": "Resumo",
        "summary": (
            "Um parágrafo consistente descrevendo quem você é profissionalmente, seus anos de experiência, o "
            "tipo de problema que resolve, e a métrica única que você sempre quer destacar. Use exatamente o "
            "mesmo texto em todas as versões do CV para a história nunca se contradizer."
        ),
        "s_exp": "Experiência Profissional",
        "chatguru_h": "Nome da Empresa, o que ela faz",
        "chatguru_m": "mês ano a mês ano  ·  Remoto/Híbrido/Presencial",
        "chatguru_note": "Uma linha explicando a trajetória, ex: uma história de crescimento contínuo entre cargos.",
        "roles": [
            (
                "Cargo mais recente",
                "mês ano a mês ano",
                [
                    "Bullet orientado a resultado descrevendo escopo e impacto.",
                    "Outro bullet com uma métrica concreta e consistente.",
                ],
            ),
            (
                "Cargo anterior",
                "mês ano a mês ano",
                [
                    "Bullet descrevendo o que você construiu ou liderou nesse cargo.",
                ],
            ),
        ],
        "ninja_h": "Nome do projeto paralelo / consultoria",
        "ninja_m": "mês ano a mês ano",
        "ninja_note": "Uma linha deixando claro que era part-time e simultâneo ao cargo principal, se for o caso.",
        "ninja_bullets": [
            "Bullet descrevendo o escopo desse projeto paralelo ou consultoria.",
        ],
        "s_projects": "Projetos Selecionados",
        "projects": [
            "Nome do projeto: uma linha descrevendo o que faz e o stack usado.",
        ],
        "s_skills": "Skills",
        "skills": [
            ("Categoria", "Skill, skill, skill"),
            ("Categoria", "Skill, skill, skill"),
        ],
        "s_lang": "Idiomas & Educação",
        "languages": "Idioma (nível)  ·  Idioma (nível)",
        "education": "Formação / certificação / o que está estudando atualmente",
        "s_refs": "Referências",
        "refs": [
            '"Uma citação curta de um ex-gestor ou cliente." Nome, Cargo, Empresa',
        ],
    },
}


def build(lang):
    data = CONTENT[lang]
    out = ROOT / "output" / data["out"]
    out.parent.mkdir(parents=True, exist_ok=True)
    d = Doc(out)
    c = d.c

    # Header
    c.setFillColor(INK)
    c.setFont("Sans-Bold", 21)
    c.drawString(d.x, d.y, data["name"])
    c.setFont("Sans-Bold", 11.5)
    c.setFillColor(ACCENT)
    c.drawRightString(d.x + d.cw, d.y, data["title"])
    d.y -= 14
    c.setFont("Sans", 8.6)
    c.setFillColor(MUTED)
    c.drawRightString(d.x + d.cw, d.y, data["tagline"])
    d.y -= 13
    c.setFont("Sans", 8.4)
    c.setFillColor(MUTED)
    c.drawString(d.x, d.y, data["contact"])
    d.y -= 10.5
    c.drawString(d.x, d.y, data["contact2"])
    d.y -= 8

    # Summary
    d.section(data["s_summary"])
    d.text(data["summary"], size=9, leading=11.4, space=2)

    # Experience
    d.section(data["s_exp"])
    d.role(data["chatguru_h"], data["chatguru_m"], size=10)
    c.setFont("Sans-Italic", 8.4)
    c.setFillColor(MUTED)
    c.drawString(d.x, d.y, data["chatguru_note"])
    d.y -= 12
    for role_name, dates, bullets in data["roles"]:
        d.role(role_name, dates, size=9.2)
        for b in bullets:
            d.bullet(b)
        d.y -= 2.5
    d.y -= 1
    d.role(data["ninja_h"], data["ninja_m"], size=10)
    c.setFont("Sans-Italic", 8.4)
    c.setFillColor(MUTED)
    c.drawString(d.x, d.y, data["ninja_note"])
    d.y -= 12
    for b in data["ninja_bullets"]:
        d.bullet(b)

    # Projects
    d.section(data["s_projects"])
    for p in data["projects"]:
        d.bullet(p, size=8.6)

    # Skills
    d.section(data["s_skills"])
    for k, v in data["skills"]:
        d.kv(k, v)

    # Languages & Education
    d.section(data["s_lang"])
    d.text(data["languages"], size=8.8, space=1)
    d.text(data["education"], size=8.8, space=0)

    # References
    d.section(data["s_refs"])
    for r in data["refs"]:
        d.text(r, font="Sans-Italic", size=7.9, leading=9.6, color=MUTED, space=1)

    c.setTitle(data["pdf_title"])
    c.setAuthor(data["name"])
    c.save()
    print(f"OK {out}  (y final: {d.y:.0f})")


if __name__ == "__main__":
    register_fonts()
    for lang in ("en", "pt"):
        build(lang)
