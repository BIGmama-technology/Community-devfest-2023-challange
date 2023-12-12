from transformers import AutoTokenizer
import transformers


class Falcon:
    model_name = "tiiuae/falcon-7b"

    def __init__(self, device="auto") -> None:
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.pipeline = transformers.pipeline(
            "text-generation",
            model=self.model_name,
            device_map=device,
            trust_remote_code=True
        )

    def generate(self, prompt: str, max_length: int =50 ) -> str:
        sequences = self.pipeline(
            prompt,
            do_sample=True,
            top_k=10,
            num_return_sequences=1,
            eos_token_id=self.tokenizer.eos_token_id,
            max_length=max_length,
        )
        return sequences[0]["generated_text"]


if __name__ == "__main__":
    falcon = Falcon()
    prompt = "I am a llama. I like to eat grass and"
    print(falcon.generate(prompt))
