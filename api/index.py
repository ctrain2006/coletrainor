"""coletrainor.com — personal site, served by Flask on Vercel."""

from flask import Flask, render_template_string

app = Flask(__name__)

NAME = "Cole Trainor"
TAGLINE = "CS + Economics @ John Carroll University"

PARAGRAPHS = [
    (
        "Hi! I’m a freshman at John Carroll University double-majoring in "
        "Computer Science and Economics, with a growing interest in business "
        "development, artificial intelligence, startups, and entrepreneurship "
        "as a whole."
    ),
    (
        "Right now, I’m focused on building my technical foundation in "
        "full-stack programming and AI while actively learning from "
        "entrepreneurs, investors, researchers, and professionals working in "
        "the field. I enjoy taking on projects, solving problems, and putting "
        "myself in environments where I can learn from people with more "
        "experience than me."
    ),
    (
        "I’m always interested in connecting with people working in AI, "
        "technology, startups, venture capital, and related fields."
    ),
]

LINKS = [
    ("Email", "mailto:ctrainor30@jcu.edu"),
    ("LinkedIn", "https://www.linkedin.com/in/cole-trainor-2a0236395/"),
    ("GitHub", "https://github.com/ctrain2006"),
]

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{ name }}</title>
<meta name="description" content="{{ name }} — {{ tagline }}">
<style>
  :root {
    --bg: #fbfaf8;
    --text: #1c1b1a;
    --muted: #6d6a66;
    --accent: #2456d6;
    --rule: #e6e3de;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #14151a;
      --text: #e8e6e3;
      --muted: #9a978f;
      --accent: #7da2ff;
      --rule: #2a2c33;
    }
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    background: var(--bg);
    color: var(--text);
    font: 17px/1.65 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
      Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
  }
  main {
    max-width: 620px;
    margin: 0 auto;
    padding: 88px 20px 64px;
  }
  h1 {
    font-size: 32px;
    line-height: 1.2;
    margin: 0 0 6px;
    letter-spacing: -0.02em;
  }
  .tagline {
    color: var(--muted);
    margin: 0 0 36px;
  }
  p { margin: 0 0 20px; }
  .links {
    margin-top: 36px;
    padding-top: 24px;
    border-top: 1px solid var(--rule);
    display: flex;
    gap: 24px;
    flex-wrap: wrap;
  }
  .links a {
    color: var(--accent);
    text-decoration: none;
    font-weight: 500;
  }
  .links a:hover { text-decoration: underline; }
</style>
</head>
<body>
<main>
  <h1>{{ name }}</h1>
  <p class="tagline">{{ tagline }}</p>
  {% for paragraph in paragraphs %}
  <p>{{ paragraph }}</p>
  {% endfor %}
  <nav class="links">
    {% for label, url in links %}
    <a href="{{ url }}">{{ label }}</a>
    {% endfor %}
  </nav>
</main>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(
        TEMPLATE, name=NAME, tagline=TAGLINE, paragraphs=PARAGRAPHS, links=LINKS
    )
