import random
from typing import List, Dict, Literal
from dataclasses import dataclass


@dataclass
class Problem:
    """Base class for math problems"""
    type: str
    problem_html: str
    answer: any


class ProblemGenerator:
    """Generates different types of math problems"""

    def __init__(self, seed: int = None):
        if seed is not None:
            random.seed(seed)

    def generate_addition_subtraction(self, max_num: int = 10) -> Problem:
        """Generate addition/subtraction problem within max_num limit"""
        operation = random.choice(["+", "-"])

        if operation == "+":
            a = random.randint(0, max_num)
            b = random.randint(0, max_num - a)
            answer = a + b
        else:
            a = random.randint(0, max_num)
            b = random.randint(0, max_num)
            if a < b:
                a, b = b, a
            answer = a - b

        problem_html = f'<span class="num">{a}</span> <span class="op">{operation}</span> <span class="num">{b}</span> <span class="op">=</span> <span class="blank"></span>'
        
        return Problem(
            type="addition_subtraction",
            problem_html=problem_html,
            answer=answer
        )

    def generate_comparison(self) -> Problem:
        """Generate comparison operator problem (>, <, =)"""
        a = random.randint(0, 10)
        b = random.randint(0, 10)

        if a > b:
            answer = ">"
        elif a < b:
            answer = "<"
        else:
            answer = "="

        problem_html = f'<span class="num">{a}</span> <span class="blank"></span> <span class="num">{b}</span>'
        
        return Problem(
            type="comparison",
            problem_html=problem_html,
            answer=answer
        )

    def generate_operator_fill(self, max_num: int = 10) -> Problem:
        """Generate problem where student fills in +/- operator"""
        operation = random.choice(["+", "-"])

        if operation == "+":
            a = random.randint(0, max_num)
            b = random.randint(0, max_num - a)
            result = a + b
        else:
            a = random.randint(0, max_num)
            b = random.randint(0, max_num)
            if a < b:
                a, b = b, a
            result = a - b

        problem_html = f'<span class="num">{a}</span> <span class="blank"></span> <span class="num">{b}</span> <span class="op">=</span> <span class="num">{result}</span>'
        
        return Problem(
            type="operator_fill",
            problem_html=problem_html,
            answer=operation
        )

    def generate_number_fill(self, max_num: int = 10) -> Problem:
        """Generate problem where student fills in missing number in calculation"""
        operation = random.choice(["+", "-"])

        if operation == "+":
            a = random.randint(0, max_num)
            b = random.randint(0, max_num - a)
            result = a + b
            blank_position = random.choice(["a", "b"])
        else:
            a = random.randint(0, max_num)
            b = random.randint(0, max_num)
            if a < b:
                a, b = b, a
            result = a - b
            blank_position = random.choice(["a", "b"])

        if blank_position == "a":
            answer = a
            problem_html = f'<span class="blank"></span> <span class="op">{operation}</span> <span class="num">{b}</span> <span class="op">=</span> <span class="num">{result}</span>'
        else:
            answer = b
            problem_html = f'<span class="num">{a}</span> <span class="op">{operation}</span> <span class="blank"></span> <span class="op">=</span> <span class="num">{result}</span>'
        
        return Problem(
            type="number_fill",
            problem_html=problem_html,
            answer=answer
        )

    def generate_quiz(self, num_problems: int = 10, problem_types: List[str] = None) -> List[Problem]:
        """Generate a quiz with specified number of problems and types"""
        if problem_types is None:
            problem_types = ["addition_subtraction", "comparison", "operator_fill", "number_fill"]

        problems = []
        for _ in range(num_problems):
            problem_type = random.choice(problem_types)
            
            if problem_type == "addition_subtraction":
                problems.append(self.generate_addition_subtraction())
            elif problem_type == "comparison":
                problems.append(self.generate_comparison())
            elif problem_type == "operator_fill":
                problems.append(self.generate_operator_fill())
            elif problem_type == "number_fill":
                problems.append(self.generate_number_fill())

        return problems
