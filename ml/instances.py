from __future__ import annotations

import torch
from transformers import (
    pipeline,
    AutoModelForCausalLM,
    AutoTokenizer,
)

from config import BaseConfig
from ml.constants import (
    GPT_NEO_MODEL_NAME,
    GPT_NEO_TOKENIZER_NAME,
    SPECIAL_TOKENS,
    PROMPT_PATTERN,
)
from utils.abs import GlobalInstanceAbstract


class MentalHealthGPT(GlobalInstanceAbstract):
    def __init__(self, max_lenght=2048, device=BaseConfig.DEVICE):
        super().__init__()
        self.__device = torch.device(device)
        self.__model = AutoModelForCausalLM.from_pretrained(GPT_NEO_MODEL_NAME)
        self.__tokenizer = AutoTokenizer.from_pretrained(GPT_NEO_TOKENIZER_NAME)

        self.__model.to(self.__device)
        self.__tokenizer.add_special_tokens(SPECIAL_TOKENS)

        self.__pipeline = pipeline(
            "text-generation",
            model=self.__model,
            tokenizer=self.__tokenizer,
            device=self.__device,
            torch_dtype=torch.float16,
        )

        self.max_length = max_lenght

    def __call__(self, prompt: str):
        prompt = PROMPT_PATTERN.format(prompt)
        outputs = self.__pipeline(prompt, max_length=self.max_length)
        result_text = outputs[0]["generated_text"][len(prompt):]
        return result_text


__all__ = [
    "MentalHealthGPT",
]
