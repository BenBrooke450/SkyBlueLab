


from transformers import AutoTokenizer, AutoModelForMaskedLM

# Load from local paths
tokenizer = AutoTokenizer.from_pretrained("./ModernBERT-tokenizer")
model = AutoModelForMaskedLM.from_pretrained("./ModernBERT-model")

# Test it
inputs = tokenizer("The patient was given [MASK].", return_tensors="pt")
outputs = model(**inputs)

print(outputs.logits.shape)



def run_ocean():
    pass

