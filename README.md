# Intelligent Code Reviewer & Explainer

## Project Overview

This project is an AI-powered code review utility developed as part of
the Generative AI Project 4 mastery phase.

The application reads a source-code file and sends the code to a local
Llama 3.2 model running through Ollama. The AI analyzes the code,
identifies bugs and problems, and generates improved refactored code.

## Objectives

- Read Python, JavaScript, or Java source code as input.
- Use the source code as AI context.
- Analyze code for bugs and logical problems.
- Generate optimized and corrected code.
- Enforce structured AI output.
- Validate the AI response.
- Display the result using Markdown formatting.

## Technologies Used

- Python
- Ollama
- Llama 3.2
- Requests
- Rich
- VS Code

## Project Workflow

Source Code File
        ↓
File Ingestion
        ↓
AI Prompt
        ↓
Ollama / Llama 3.2
        ↓
Code Analysis
        ↓
Bug Report
        ↓
Refactored Code
        ↓
Response Validation
        ↓
Markdown Rendering

## Files

### app.py

Main application that:
- Reads the source code.
- Sends the code to Ollama.
- Receives the AI review.
- Validates the response.
- Displays the result.

### test_code.py

Sample source-code file used for testing the reviewer.

## Output Format

The AI produces two sections:

## BUG_REPORT

Contains identified bugs and code-quality issues.

## REFACTORED_CODE

Contains the improved version of the source code.

## Error Handling

The application handles:

- FileNotFoundError
- PermissionError
- UnicodeDecodeError
- Ollama connection errors
- API/request errors

## Conclusion

The project demonstrates code-as-context management, prompt engineering,
structured outputs, response validation, and AI-powered code analysis.