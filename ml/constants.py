GPT_NEO_MODEL_NAME = "Stassney/gpt-neo-finetune"
GPT_NEO_TOKENIZER_NAME = "EleutherAI/gpt-neo-125m"

SPECIAL_TOKENS = {
    "pad_token": "[PAD]",
}

PROMPT_PATTERN = """
Patient: Hello, {}<|endofcontext|>
Doctor: Hi,
"""

__all__ = [
    "GPT_NEO_MODEL_NAME",
    "GPT_NEO_TOKENIZER_NAME",
    "PROMPT_PATTERN",
    "SPECIAL_TOKENS",
]
