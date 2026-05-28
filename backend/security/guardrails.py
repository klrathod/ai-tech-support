BLOCKED_TERMS = ["hack", "malware"]


def validate_prompt(prompt: str):
    for term in BLOCKED_TERMS:
        if term in prompt:
            raise Exception("Blocked prompt")
