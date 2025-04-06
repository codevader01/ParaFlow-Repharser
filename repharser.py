from transformers import T5Tokenizer, T5ForConditionalGeneration

def rephrase_text(text):
    # Load the T5 model and tokenizer
    model_name = "t5-small"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    # Prepare input text for paraphrasing
    input_text = f"paraphrase: {text} </s>"
    encoding = tokenizer.encode_plus(input_text, return_tensors="pt", max_length=512, truncation=True)

    # Generate paraphrased text
    output = model.generate(
        encoding["input_ids"], 
        max_length=512, 
        num_return_sequences=1, 
        temperature=0.9, 
        top_k=50, 
        top_p=0.95
    )

    # Decode and return the output
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Example usage
paragraph = "Natural language processing enables computers to understand and generate human language, improving AI communication."
rephrased_paragraph = rephrase_text(paragraph)
print("Original Paragraph:", paragraph)
print("Rephrased Paragraph:", rephrased_paragraph)
