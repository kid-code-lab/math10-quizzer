from typing import List
from jinja2 import Template
from .problems import Problem


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bài Tập Toán - Math 10</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: "Roboto", sans-serif;
            font-optical-sizing: auto;
            font-weight: 400;
            font-style: normal;
            font-variation-settings: "wdth" 100;
            background: white url('../../paper.jpg') repeat;
            padding: 0;
            min-height: 100vh;
            font-size: 14px;
            line-height: 20px;
        }

        .container {
            max-width: 210mm;
            height: 297mm;
            margin: 0 auto;
            overflow: hidden;
            page-break-after: always;
        }

        .content {
            padding: 20px;
            height: 100%;
            overflow: hidden;
        }

        .problems {
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-template-rows: auto;
            gap: 20px;
            margin-bottom: 0;
        }

        .problem {
            padding: 4px 6px;
            border: none;
            border-radius: 0;            
            font-size: 13px;
            font-weight: 600;
            transition: none;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            min-height: auto;
            text-align: left;
            line-height: 1.4;
        }

        .num, .op, .blank {
            display: inline-block;
            width: 28px;
            text-align: center;
        }

        .blank {
            border: 1px solid #333;
            height: 18px;
            margin: 0 3px;
            vertical-align: middle;
            position: relative;
        }

        @media print {
            body {
                padding: 0;
                margin: 0;
            }

            .container {
                box-shadow: none;
                border-radius: 0;
                margin: 0;
                page-break-after: always;
            }

            .problem {
                page-break-inside: avoid;
                border: none;
            }

            .problem:hover {
                box-shadow: none;
                border-color: transparent;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="content">
            <div class="problems">
                {% for problem in problems %}
                <div class="problem" data-number="{{ loop.index }}">
                    {{ problem.problem_html | safe }}
                </div>
                {% endfor %}
            </div>
        </div>
    </div>
</body>
</html>"""


class QuizRenderer:
    """Renders quiz HTML from problems"""

    @staticmethod
    def render_html(problems: List[Problem], title: str = "Bài Tập Toán") -> str:
        """Render problems to HTML string"""
        template = Template(HTML_TEMPLATE)
        
        html_content = template.render(
            problems=problems,
            title=title
        )
        
        return html_content

    @staticmethod
    def save_html(problems: List[Problem], filepath: str, title: str = "Bài Tập Toán") -> None:
        """Save quiz as HTML file"""
        html_content = QuizRenderer.render_html(problems, title)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
