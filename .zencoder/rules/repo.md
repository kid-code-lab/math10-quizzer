---
description: Repository Information Overview
alwaysApply: true
---

# Math 10 Quiz Generator

## Summary

A Python-based tool that generates randomized math quizzes for 1st graders with multiple problem types, auto-generates solution sheets, and exports quizzes as PDF or HTML files. The application uses CLI commands to customize quiz generation, including number of problems, problem types, and reproducible seeds.

## Structure

- **main.py**: Application entry point
- **app/**: Core application module
  - **cli.py**: Click-based CLI with three commands (generate, generate-html, to-pdf)
  - **problems.py**: ProblemGenerator class with methods for 4 problem types
  - **renderer.py**: QuizRenderer class using Jinja2 templates to generate HTML
  - **printer.py**: QuizPrinter class for HTML-to-PDF conversion via Playwright
  - **__init__.py**: Module initialization
- **output/**: Generated quiz output directory (organized by date)
- **requirements.txt**: Python dependencies
- **README.md**: Project documentation

## Language & Runtime

**Language**: Python 3  
**Package Manager**: pip  
**Key Framework**: Click (CLI framework)

## Dependencies

**Main Dependencies**:
- **click** (8.1.7): Command-line interface creation
- **playwright** (1.40.0): Browser automation for PDF export (requires Google Chrome installation)
- **jinja2** (3.1.2): HTML template rendering

## Build & Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install
```

Google Chrome must be installed on the system (required by Playwright for PDF conversion).

## Main Entry Points & Commands

**Primary Command** (`main.py`): Launches Click CLI group

**Available Commands**:

1. **generate**: Generate quiz and save as PDF
   ```bash
   python main.py generate [--num-problems N] [--output PATH] [--types TYPE] [--seed SEED]
   ```

2. **generate-html**: Generate quiz as HTML file
   ```bash
   python main.py generate-html [--num-problems N] [--output PATH] [--types TYPE] [--seed SEED]
   ```

3. **to-pdf**: Convert existing HTML to PDF
   ```bash
   python main.py to-pdf HTML_FILE [--output PATH]
   ```

**Default Output**: `output/YYYY-MM-DD/quiz-TIMESTAMP.{pdf|html}`

## Problem Types

The application supports 4 problem types selected randomly or by user preference:

- **addition_subtraction**: Basic addition/subtraction within limit (0-10)
- **comparison**: Compare two numbers with <, >, = operators
- **operator_fill**: Fill missing operator (+/-) in equation
- **number_fill**: Fill missing number in calculation

## Project Architecture

**ProblemGenerator** (`app/problems.py`):
- Generates random math problems based on specified types
- Returns `Problem` dataclass with type, HTML markup, and answer
- Supports reproducible generation via seed parameter

**QuizRenderer** (`app/renderer.py`):
- Uses Jinja2 templates to convert problems to HTML
- Includes embedded CSS for A4 page layout (210mm × 297mm)
- Generates 2-column grid layout suitable for printing

**QuizPrinter** (`app/printer.py`):
- Uses Playwright's sync API to launch Chromium browser
- Converts HTML files to A4 PDF format with print background

**CLI** (`app/cli.py`):
- Click decorator-based command structure
- Date-based output directory creation
- Error handling and user feedback
