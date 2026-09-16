"""One-off native Marian translation; no user data, secrets or runtime inference."""
import json,sys,re
from pathlib import Path
import torch
from transformers import MarianMTModel, MarianTokenizer
from huggingface_hub import HfApi
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from translations import extract
from build import collect
model_id='Helsinki-NLP/opus-mt-es-en'
revision=HfApi().model_info(model_id).sha
if not revision.startswith('c96e2c5'):raise ValueError('Model revision changed; review before execution')
torch.set_num_threads(4)
tokenizer=MarianTokenizer.from_pretrained(model_id,revision=revision,trust_remote_code=False)
model=MarianMTModel.from_pretrained(model_id,revision=revision,trust_remote_code=False,weights_only=True).eval()
shard=int(sys.argv[1]);count=8
if not 0<=shard<count:raise ValueError('Invalid shard')
items=list(extract(collect()).items())[shard::count]
entries={}
# Pure IDs must not pass through a language model.
for start in range(0,len(items),8):
    batch=items[start:start+8]
    regular=[]
    for ident,text in batch:
        if re.fullmatch(r'M\d{2}(?:[ ,–-]+M\d{2})*\.?',text):entries[ident]={'source':text,'target':text}
        else:regular.append((ident,text))
    if regular:
        inputs=tokenizer([text for _,text in regular],return_tensors='pt',padding=True,truncation=False)
        with torch.inference_mode():
            outputs=model.generate(**inputs,max_new_tokens=220,num_beams=4,renormalize_logits=True,early_stopping=True)
        for (ident,text),target in zip(regular,tokenizer.batch_decode(outputs,skip_special_tokens=True)):
            if not target.strip() or re.search(r'\.{8}',target):raise ValueError('Invalid translation '+ident)
            entries[ident]={'source':text,'target':target}
    if start%40==0:print(shard,start,len(items),flush=True)
output=Path('/tmp/editorial-native');output.mkdir(exist_ok=True)
(output/f'en-{shard}.json').write_text(json.dumps({'schema':1,'model':model_id,'revision':revision,'engine':'transformers/MarianTokenizer native fp32','entries':entries},ensure_ascii=False),encoding='utf-8')
print('Completed',len(entries),'segments',revision,flush=True)
