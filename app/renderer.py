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
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: "Poppins", sans-serif;
            font-optical-sizing: auto;
            font-weight: 400;
            font-style: normal;
            background: linear-gradient(135deg, #FFF5F7 0%, #F0F4FF 50%, #F0FFF7 100%);
            padding: 0;
            margin: 0;
            font-size: 32px;
            line-height: 1.8;
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
            margin-bottom: 32px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.6);
            border-radius: 16px;
            backdrop-filter: blur(10px);
        }

        .group-title {
            font-size: 28px;
            font-weight: 700;
            color: #E74C3C;
            margin-bottom: 20px;
            padding: 16px 0;
            border-bottom: 4px solid #E74C3C;
            text-transform: uppercase;
            letter-spacing: 2px;
            text-shadow: 1px 1px 2px rgba(231, 76, 60, 0.1);
        }

        .group-items {
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-template-rows: auto;
            gap: 24px;
        }

        .problem {
            padding: 16px 20px;
            border: none;
            border-radius: 16px;            
            font-size: 32px;
            font-weight: 500;
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            position: relative;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            min-height: 68px;
            text-align: left;
            background: linear-gradient(135deg, #FFF9E6 0%, #FFFBF0 100%);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            border: 2px solid rgba(255, 200, 87, 0.3);
        }

        .problem:nth-child(2n) {
            background: linear-gradient(135deg, #F0F9FF 0%, #E6F7FF 100%);
            border-color: rgba(46, 134, 222, 0.3);
        }

        .problem:nth-child(3n) {
            background: linear-gradient(135deg, #F9F5FF 0%, #F0E6FF 100%);
            border-color: rgba(162, 155, 254, 0.3);
        }

        .problem:hover {
            transform: translateY(-4px) scale(1.02);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
        }

        .num {
            display: inline-block;
            color: #2E86DE;
            font-weight: 600;
            margin: 0 4px;
        }

        .op {
            display: inline-block;
            color: #A29BFE;
            font-weight: 600;
            margin: 0 4px;
        }

        .blank {
            border: 3px dashed #F39C12;
            border-radius: 12px;
            height: 56px;
            width: 72px;
            margin: 0 12px;
            vertical-align: middle;
            position: relative;
            background: linear-gradient(135deg, #FFFACD 0%, #FFFACD 100%);
            box-shadow: inset 0 2px 6px rgba(243, 156, 18, 0.1), 0 2px 4px rgba(243, 156, 18, 0.15);
            transition: all 0.3s ease;
        }

        .blank:hover {
            border-color: #FF6B6B;
            background: linear-gradient(135deg, #FFE6E6 0%, #FFE6E6 100%);
            box-shadow: inset 0 2px 6px rgba(255, 107, 107, 0.15), 0 4px 8px rgba(255, 107, 107, 0.2);
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
