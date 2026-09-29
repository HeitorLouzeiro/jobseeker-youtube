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
# CONTEÚDO: Heitor Garcez Martins Louzeiro.
# Fonte: Curriculo_-_Heitor_Garcez_Martins_Louzeiro.pdf. Números e datas devem bater com o AGENTS.md.
# ---------------------------------------------------------------------------
CONTENT = {
    "en": {
        "out": "cv_heitor_louzeiro_en.pdf",
        "pdf_title": "Heitor Garcez Martins Louzeiro - CV EN",
        "name": "Heitor Garcez Martins Louzeiro",
        "title": "Backend Python Developer",
        "tagline": "Python  ·  Django  ·  Docker  ·  PostgreSQL  ·  Linux",
        "contact": "São Paulo, Brazil  ·  heitorlouzeiro2019@gmail.com  ·  +55 (89) 99905-4536",
        "contact2": "linkedin.com/in/heitor-louzeiro",
        "s_summary": "Summary",
        "summary": (
            "Backend developer with 3 years of experience in Python. At the Corrente City Hall, I stopped a "
            "server attack in under 15 minutes, brought about 25 systems back online and hardened 24 Docker "
            "applications so the problem would not come back. I also coordinate a team of 4 people on systems "
            "development. During my studies I built an event management "
            "system for Agrosul Piauí that received 50+ scientific papers, generated 100+ attendance lists for "
            "workshops and issued 900+ certificates."
        ),
        "s_exp": "Work Experience",
        "chatguru_h": "Corrente City Hall (Prefeitura Municipal de Corrente)",
        "chatguru_m": "Jun 2025 to present",
        "chatguru_note": "Public sector, in charge of backend and infrastructure for the city's systems.",
        "roles": [
            (
                "Backend Developer and DevOps",
                "Jun 2025 to present",
                [
                    "Stopped an attack on the server in under 15 minutes and brought about 25 systems back online.",
                    "Hardened 24 Docker applications (firewall, resource limits, server updates) so the issue "
                    "would not happen again.",
                    "Wrote the incident report (root cause, impact and fix) within 24 hours.",
                    "Coordinated a team of 4 people on systems development: defined what had to be built, how "
                    "it should be done and the deadlines.",
                ],
            ),
        ],
        "ninja_h": "Freelance and Project Work",
        "ninja_m": "Apr 2023 to Jun 2024",
        "ninja_note": "Short, project-based engagements before the current role.",
        "ninja_bullets": [
            "Events system (Agrosul Piauí), Mar to Jun 2024: built with Django, Bootstrap, PostgreSQL and "
            "Heroku; 900+ certificates generated and 50+ papers submitted with automatic e-mail delivery.",
            "OKEAN Yachts PoC, Dec 2023 to Jan 2024: as frontend developer in a team of 4 (2 devs, 1 tech lead, 1 scrum master), "
            "built 4 pages (Home, Login, Signup, support Chat) integrated with ChatGPT using Django and OpenAI.",
            "Student registration automation (SEDUC), Apr 2023: Python and Selenium script that registered "
            "1,000+ students and cut processing time by 80%.",
        ],
        "s_projects": "Selected Projects",
        "projects": [
            "Event management system: paper submission, attendance lists and automatic certificates "
            "(Django, PostgreSQL, Heroku).",
        ],
        "s_skills": "Skills",
        "skills": [
            ("Backend", "Python, Django, PostgreSQL, OpenAI API"),
            ("Infra / DevOps", "Docker, Linux servers, firewall, Heroku, Git"),
            ("Automation", "Selenium, document processing"),
            ("Frontend", "HTML, CSS, Bootstrap"),
        ],
        "s_lang": "Languages & Education",
        "languages": "Portuguese (native)  ·  English (basic: good reading comprehension, limited speaking and writing)",
        "education": "Systems Analysis and Development, IFPI (Federal Institute of Piauí)  ·  Django Web Framework course, Udemy",
        "s_refs": "References",
        "refs": [],
    },
    "pt": {
        "out": "cv_heitor_louzeiro_pt.pdf",
        "pdf_title": "Heitor Garcez Martins Louzeiro - CV PT",
        "name": "Heitor Garcez Martins Louzeiro",
        "title": "Desenvolvedor Backend Python",
        "tagline": "Python  ·  Django  ·  Docker  ·  PostgreSQL  ·  Linux",
        "contact": "São Paulo, Brasil  ·  heitorlouzeiro2019@gmail.com  ·  (89) 99905-4536",
        "contact2": "linkedin.com/in/heitor-louzeiro",
        "s_summary": "Resumo",
        "summary": (
            "Desenvolvedor backend com 3 anos de experiência em Python. Na Prefeitura de Corrente, parei um "
            "ataque ao servidor em menos de 15 minutos, coloquei cerca de 25 sistemas de volta no ar e reforcei "
            "a segurança de 24 aplicações em Docker para o problema não voltar. Também coordeno uma equipe de 4 pessoas no "
            "desenvolvimento dos sistemas. Durante a graduação, desenvolvi "
            "um sistema de gerenciamento de eventos para a Agrosul Piauí que recebeu mais de 50 artigos "
            "científicos, gerou mais de 100 listas de presença para minicursos e oficinas e emitiu mais de 900 "
            "certificados."
        ),
        "s_exp": "Experiência Profissional",
        "chatguru_h": "Prefeitura Municipal de Corrente",
        "chatguru_m": "jun 2025 a atual",
        "chatguru_note": "Setor público, responsável pelo backend e pela infraestrutura dos sistemas do município.",
        "roles": [
            (
                "Desenvolvedor Backend e DevOps",
                "jun 2025 a atual",
                [
                    "Parei um ataque ao servidor em menos de 15 minutos e coloquei de volta no ar cerca de 25 "
                    "sistemas que estavam fora do ar.",
                    "Reforcei a segurança de 24 aplicações em Docker (firewall, limites de recursos e atualização "
                    "do servidor) para o problema não voltar.",
                    "Escrevi o relatório (causa, impacto e solução), do problema à correção, em 24 horas.",
                    "Coordenei uma equipe de 4 pessoas no desenvolvimento dos sistemas: definia o que precisava "
                    "ser feito, como fazer e os prazos.",
                ],
            ),
        ],
        "ninja_h": "Freelances e Projetos",
        "ninja_m": "abr 2023 a jun 2024",
        "ninja_note": "Trabalhos pontuais, por projeto, antes do cargo atual.",
        "ninja_bullets": [
            "Sistema de eventos (Agrosul Piauí), mar a jun 2024: Django, Bootstrap, PostgreSQL e Heroku; mais "
            "de 900 certificados gerados e mais de 50 artigos submetidos com envio automático por e-mail.",
            "PoC OKEAN Yachts, dez 2023 a jan 2024: como desenvolvedor frontend, em equipe de 4 pessoas (2 devs, 1 tech lead, 1 scrum "
            "master), criei 4 páginas (Home, Login, Signup e Chat de atendimento) integradas ao ChatGPT, com "
            "Django e OpenAI.",
            "Automação de cadastro de alunos (SEDUC), abr 2023: script em Python e Selenium que cadastrou mais "
            "de 1.000 alunos e reduziu o tempo de processamento em 80%.",
        ],
        "s_projects": "Projetos Selecionados",
        "projects": [
            "Sistema de gerenciamento de eventos: submissão de artigos, listas de presença e certificados "
            "automáticos (Django, PostgreSQL, Heroku).",
        ],
        "s_skills": "Skills",
        "skills": [
            ("Backend", "Python, Django, PostgreSQL, API da OpenAI"),
            ("Infra / DevOps", "Docker, servidores Linux, firewall, Heroku, Git"),
            ("Automação", "Selenium, processamento de documentos"),
            ("Frontend", "HTML, CSS, Bootstrap"),
        ],
        "s_lang": "Idiomas & Educação",
        "languages": "Português (nativo)  ·  Inglês (básico: entendo bem, mas tenho dificuldade em falar e escrever)",
        "education": "Análise e Desenvolvimento de Sistemas, IFPI (Instituto Federal do Piauí)  ·  Curso de Django Web Framework, Udemy",
        "s_refs": "Referências",
        "refs": [],
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

    # References (opcional: deixe a lista vazia para omitir a seção)
    if data["refs"]:
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
