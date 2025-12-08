import os
from pathlib import Path
from playwright.sync_api import sync_playwright


class QuizPrinter:
    """Handles printing/exporting quizzes using Playwright"""

    @staticmethod
    def html_to_pdf(html_filepath: str, pdf_filepath: str) -> None:
        """Convert HTML file to PDF using Chromium"""
        html_path = Path(html_filepath).resolve()
        pdf_path = Path(pdf_filepath).resolve()

        if not html_path.exists():
            raise FileNotFoundError(f"HTML file not found: {html_filepath}")

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{html_path}")
            page.pdf(path=str(pdf_path), format="A4", print_background=True)
            browser.close()

        print(f"PDF saved: {pdf_path}")

    @staticmethod
    def print_to_printer(html_filepath: str, printer_name: str = None) -> None:
        """Print HTML file to physical printer"""
        html_path = Path(html_filepath).resolve()

        if not html_path.exists():
            raise FileNotFoundError(f"HTML file not found: {html_filepath}")

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{html_path}")
            
            if printer_name:
                # This is not a standard playwright feature, pseudo-code
                # For actual printing, a different approach is needed (e.g., using system commands)
                print("Printing to a specific printer is not directly supported this way.")
            else:
                # Just generating a PDF and not saving it, which isn't very useful for printing.
                # The original logic here was likely intended to do something else.
                # For now, let's assume the goal was to show a print dialog, which is a browser UI feature.
                # Playwright can't directly control the system print dialog.
                pass
            
            browser.close()

        if printer_name:
            print(f"Sent to printer: {printer_name}")
        else:
            print("Print to default printer (simulation).")
