
from transformers import AutoTokenizer, AutoModelForMaskedLM

model_id = "answerdotai/ModernBERT-base"


tokenizer = AutoTokenizer.from_pretrained(model_id)
tokenizer.save_pretrained("./ModernBERT-tokenizer")  # save locally


model = AutoModelForMaskedLM.from_pretrained(model_id)
model.save_pretrained("./ModernBERT-model")  # save weights and config locally

def run_ocean():

