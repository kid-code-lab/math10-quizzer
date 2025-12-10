from typing import List, Dict
from jinja2 import Template
from .problems import Problem


TYPE_LABELS = {
    "addition_subtraction": "Cộng & Trừ",
    "comparison": "So Sánh",
    "operator_fill": "Điền Toán Tử",
    "number_fill": "Điền Số"
}


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
            margin: 0;
            font-size: 28px;
            line-height: 40px;
        }

        .content {
            display: flex;
            flex-direction: column;
            width: 100%;
            max-width: 210mm;
            margin: 0 auto;
            padding: 20px;
        }

        .problems {
            display: block;
        }

        .problem-group {
            margin-bottom: 20px;
        }

        .group-title {
            font-size: 20px;
            font-weight: 700;
            color: #333;
            margin-bottom: 12px;
            padding-bottom: 8px;
            border-bottom: 2px solid #333;
        }

        .group-items {
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-template-rows: auto;
            gap: 20px;
        }

        .problem {
            padding: 8px 12px;
            border: none;
            border-radius: 0;            
            font-size: 26px;
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
            width: 56px;
            text-align: center;
        }

        .blank {
            border: 1px solid #333;
            height: 36px;
            margin: 0 6px;
            vertical-align: middle;
            position: relative;
        }


    </style>
</head>
<body>
    <div class="content">
        <div class="problems">
            {% for group_type, group_problems in problem_groups.items() %}
            {% if group_problems %}
            <div class="problem-group">
                <div class="group-title">{{ group_labels[group_type] }}</div>
                <div class="group-items">
                    {% for problem in group_problems %}
                    <div class="problem" data-type="{{ problem.type }}">
                        {{ problem.problem_html | safe }}
                    </div>
                    {% endfor %}
                </div>
            </div>
            {% endif %}
            {% endfor %}
        </div>
    </div>
</body>
</html>"""


class QuizRenderer:
    """Renders quiz HTML from problems"""

    @staticmethod
    def _group_problems_by_type(problems: List[Problem]) -> Dict[str, List[Problem]]:
        """Group problems by their type"""
        grouped = {}
        type_order = ["addition_subtraction", "comparison", "operator_fill", "number_fill"]
        
        for problem_type in type_order:
            grouped[problem_type] = [p for p in problems if p.type == problem_type]
        
        return grouped

    @staticmethod
    def render_html(problems: List[Problem], title: str = "Bài Tập Toán") -> str:
        """Render problems to HTML string"""
        template = Template(HTML_TEMPLATE)
        
        problem_groups = QuizRenderer._group_problems_by_type(problems)
        
        html_content = template.render(
            problem_groups=problem_groups,
            group_labels=TYPE_LABELS,
            title=title
        )
        
        return html_content

    @staticmethod
    def save_html(problems: List[Problem], filepath: str, title: str = "Bài Tập Toán") -> None:
        """Save quiz as HTML file"""
        html_content = QuizRenderer.render_html(problems, title)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
