import click
from pathlib import Path
from datetime import datetime
from .problems import ProblemGenerator
from .renderer import QuizRenderer
from .printer import QuizPrinter


def get_output_dir():
    """Get output directory with date structure"""
    date_folder = datetime.now().strftime('%Y-%m-%d')
    output_dir = Path('output') / date_folder
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


@click.group()
def cli():
    """Math 10 Quiz Generator - Create quizzes automatically"""
    pass


@cli.command()
@click.option(
    '--num-problems',
    type=int,
    default=10,
    help='Number of problems to generate (default: 10)'
)
@click.option(
    '--output',
    type=click.Path(),
    default=None,
    help='Path to the output PDF file (default: output/yyyy-mm-dd/quiz-TIMESTAMP.pdf)'
)
@click.option(
    '--types',
    type=click.Choice(['all', 'addition_subtraction', 'comparison', 'operator_fill', 'number_fill']),
    multiple=True,
    help='Types of problems to generate (can specify multiple). Leave empty for all.'
)
@click.option(
    '--seed',
    type=int,
    default=None,
    help='Seed for the random number generator (for reproducible quizzes)'
)
def generate(num_problems, output, types, seed):
    """Generate a math quiz and save it as a PDF file."""

    if output is None:
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        output = str(get_output_dir() / f'quiz-{timestamp}.pdf')

    problem_types = None
    if types:
        types_list = list(types)
        if 'all' not in types_list:
            problem_types = types_list

    generator = ProblemGenerator(seed=seed)
    problems = generator.generate_quiz(num_problems=num_problems, problem_types=problem_types)

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    html_file = str(output_path.with_suffix('.html'))
    QuizRenderer.save_html(problems, html_file)

    try:
        QuizPrinter.html_to_pdf(html_file, output)
        click.echo(f"✓ Successfully created {num_problems} problems and saved as PDF!")
        click.echo(f"✓ File: {Path(output).resolve()}")
    except Exception as e:
        click.echo(f"✗ Error: {str(e)}", err=True)


@cli.command('generate-html')
@click.option(
    '--num-problems',
    type=int,
    default=10,
    help='Number of problems to generate (default: 10)'
)
@click.option(
    '--output',
    type=click.Path(),
    default=None,
    help='Path to the output HTML file (default: output/yyyy-mm-dd/quiz-TIMESTAMP.html)'
)
@click.option(
    '--types',
    type=click.Choice(['all', 'addition_subtraction', 'comparison', 'operator_fill', 'number_fill']),
    multiple=True,
    help='Types of problems to generate (can specify multiple). Leave empty for all.'
)
@click.option(
    '--seed',
    type=int,
    default=None,
    help='Seed for the random number generator (for reproducible quizzes)'
)
def generate_html(num_problems, output, types, seed):
    """Generate a math quiz and save it as an HTML file."""

    if output is None:
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        output = str(get_output_dir() / f'quiz-{timestamp}.html')

    problem_types = None
    if types:
        types_list = list(types)
        if 'all' not in types_list:
            problem_types = types_list

    generator = ProblemGenerator(seed=seed)
    problems = generator.generate_quiz(num_problems=num_problems, problem_types=problem_types)

    QuizRenderer.save_html(problems, output)
    click.echo(f"✓ Successfully created {num_problems} problems!")
    click.echo(f"✓ Saved to: {Path(output).resolve()}")


@cli.command('to-pdf')
@click.argument('html_file', type=click.Path(exists=True))
@click.option(
    '--output',
    type=click.Path(),
    default=None,
    help='Path to the output PDF file (default: same as input with .pdf extension)'
)
def to_pdf(html_file, output):
    """Convert an HTML file to PDF."""

    if output is None:
        output = str(get_output_dir() / (Path(html_file).stem + '.pdf'))

    try:
        QuizPrinter.html_to_pdf(html_file, output)
        click.echo(f"✓ Conversion successful!")
    except Exception as e:
        click.echo(f"✗ Error: {str(e)}", err=True)


if __name__ == '__main__':
    cli()
