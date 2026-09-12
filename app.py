import requests
from rich.console import Console
from rich.markdown import Markdown
console = Console()

SYSTEM_PROMPT = """
You are a Senior Code Quality Assurance Engineer.

Your task is to review the provided source code carefully and accurately.

Analyze ONLY the code that is actually provided.
Do not invent bugs, variables, values, or code that does not exist.

Your response MUST contain exactly these two sections:

## BUG_REPORT

List actual bugs, logical errors, security issues, input-validation
problems, and meaningful performance issues.

Each issue must be a concise bullet point.

Only report a problem if it is supported by the source code.

## REFACTORED_CODE

Provide an improved and corrected version of the original code.

Preserve the original functionality unless a change is necessary
to fix a problem.

Put the complete refactored code inside exactly ONE Markdown
code block.

Use the correct language identifier, such as ```python for Python code.

Do not use ```markdown.
Do not include greetings.
Do not include unnecessary explanations.
"""

print("AI Code Reviewer started!")

file_path = "test_code.py"

# Read the source code
try:
    with open(file_path, "r", encoding="utf-8") as file:
        code = file.read()

    print("\nCode loaded successfully!")
    print("\n--- CODE ---")
    print(code)

except FileNotFoundError:
    print("Error: Code file not found.")
    exit()

except PermissionError:
    print("Error: Permission denied.")
    exit()

except UnicodeDecodeError:
    print("Error: Unable to decode the file.")
    exit()


# Send the code to Ollama
try:
    prompt = SYSTEM_PROMPT + "\n\nSOURCE CODE:\n\n" + code

    response = requests.post(
        "http://127.0.0.1:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()

    result = response.json()["response"]

    print("\n--- AI REVIEW ---")
    console.print(Markdown(result))

    # Validate the AI response
    if "## BUG_REPORT" not in result:
        print("\nWarning: BUG_REPORT section is missing.")

    if "## REFACTORED_CODE" not in result:
        print("\nWarning: REFACTORED_CODE section is missing.")

    if "```" not in result:
        print("\nWarning: Markdown code block is missing.")

    if (
        "## BUG_REPORT" in result
        and "## REFACTORED_CODE" in result
        and "```" in result
    ):
        print("\nResponse validation: PASSED")
    else:
        print("\nResponse validation: FAILED")

except requests.exceptions.ConnectionError:
    print("\nCould not connect to Ollama.")
    print("Make sure Ollama is running.")

except Exception as e:
    print("\nAI request failed:")
    print(e)