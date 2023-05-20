from transformers import GPT2LMHeadModel, GPT2Tokenizer

# ChatGPT modelini ve tokenizer'ı yükleyin
model_name = 'gpt2'  # veya başka bir model adı
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Prompt dosyasını okuyun
with open('chat_prompt.txt', 'r', encoding='utf-8') as file:
    prompts = file.read().splitlines()

# Her bir prompt için ChatGPT ile etkileşim kurun
for prompt in prompts:
    encoded_prompt = tokenizer.encode(prompt, return_tensors='pt')
    output = model.generate(encoded_prompt, max_length=100, num_return_sequences=1)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    print('Prompt:', prompt)
    print('Model:', response)
    print()
