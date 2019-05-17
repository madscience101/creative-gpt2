## use
##!pip install pytorch-pretrained-bert
## to install pytorch-pretrained-bert from https://github.com/huggingface/pytorch-pretrained-BERT
 
from pytorch_pretrained_bert import GPT2Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
 
def get_token_composition(s):
  return [tokenizer.decode([t]) for t in tokenizer.encode(s)]
 
 
get_token_composition('Hello, world!')
