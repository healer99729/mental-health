import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
device = "cuda:0" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-125m", torch_dtype=torch.float16)
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-125m")

prompt = "Tell me about the tensorflow"
sample_prompts = [
    "A: From now, translate the sentenceses I give you into germany",
    "B: Yes!",
    "A: Hello, how are you?",
]

model_inputs = tokenizer([prompt], return_tensors="pt").to(device)
model.to(device)

generated_ids = model.generate(**model_inputs, max_new_tokens=500, do_sample=True)
print(tokenizer.batch_decode(generated_ids)[0])

print(tokenizer.model_max_length)
