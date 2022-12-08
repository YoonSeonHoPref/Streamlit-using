import torch
import streamlit as st
from transformers import GPT2LMHeadModel
from transformers import PreTrainedTokenizerFast
tokenizer = PreTrainedTokenizerFast.from_pretrained("skt/kogpt2-base-v2",
  bos_token='</s>', eos_token='</s>', unk_token='<unk>',
  pad_token='<pad>', mask_token='<mask>') 

st.title("Streamlit을 활용한 문장 생성기")
model = GPT2LMHeadModel.from_pretrained('skt/kogpt2-base-v2')

prompt_text=st.text_input(label = "문장을 생성하기 위한 키워드를 입력하세요",
              value="챗봇을 만들기 위해서는")


input_ids = tokenizer.encode(prompt_text)
gen_ids = model.generate(torch.tensor([input_ids]),
                           max_length=128,
                           repetition_penalty=2.0,
                           pad_token_id=tokenizer.pad_token_id,
                           eos_token_id=tokenizer.eos_token_id,
                           bos_token_id=tokenizer.bos_token_id,
                           use_cache=True)
generated = tokenizer.decode(gen_ids[0,:].tolist())

st.text(generated)
