from datashader.datashape import promote


class LLM_Tiny_Llama:
    def __init__(self):
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM

        MODEL_PATH = "/data/models--TinyLlama--TinyLlama-1.1B-Chat-v1.0/snapshots/fe8a4ea1ffedaf415f4da2f062534de366a451e6"

        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
        self.model = AutoModelForCausalLM.from_pretrained( MODEL_PATH)

    def prompt(self, prompt):

        messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": f"{prompt}"}]

        prompt = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = self.tokenizer(prompt, return_tensors="pt")

        outputs = self.model.generate(**inputs,max_new_tokens=100)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)



if __name__ == "__main__":

    first_model = LLM_Tiny_Llama()

    print(first_model.prompt("Hello, is this the Tiny LLama model?, who designed you ?"))