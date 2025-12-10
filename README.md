# Math 10 Quiz Generator

This tool generates math quizzes for 1st graders, including solutions, and saves them as PDF files.

## Features

- Generate random math problems suitable for 1st graders.
- Automatically create a solution sheet.
- Save quizzes and solutions in PDF format.
- Customize the number and types of problems.

## Problem Types

You can generate quizzes with a mix of the following problem types:

- `addition_subtraction`: Basic addition and subtraction problems.
- `comparison`: Compare two numbers using `<`, `>`, or `=`.
- `operator_fill`: Fill in the correct operator (`+` or `-`) to complete the equation.
- `number_fill`: Fill in the missing number to complete the equation.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/math10-quizzer.git
    cd math10-quizzer
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Install Google Chrome:**
    This tool uses `playwright` to convert HTML to PDF, which requires Google Chrome to be installed.

## Usage

### Generate a Quiz (PDF)

To generate a quiz with 10 random problems and save it as a PDF:

```bash
python main.py generate
```

The output will be saved in the `output/YYYY-MM-DD/` directory.

**Customization Options:**

-   `--num-problems`: Specify the number of problems.
    ```bash
    python main.py generate --num-problems 20
    ```

-   `--types`: Choose specific problem types.
    ```bash
    python main.py generate --types addition_subtraction --types comparison --types operator_fill --types number_fill --num-problems 50
    ```

-   `--output`: Set a custom output path.
    ```bash
    python main.py generate --output my_quiz.pdf
    ```

-   `--seed`: Use a seed for reproducible quizzes.
    ```bash
    python main.py generate --seed 42
    ```

### Generate an HTML Quiz

If you prefer an HTML file, use the `generate-html` command:

```bash
python main.py generate-html
```

### Convert HTML to PDF

To convert an existing HTML quiz to PDF:

```bash
python main.py to-pdf your_quiz.html
```

## Development

To set up the development environment, install the required dependencies:

```bash
pip install -r requirements.txt
playwright install
```
