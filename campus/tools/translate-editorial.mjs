// One-off editorial tool. Not part of the browser or production build.
import {pipeline, env} from '@huggingface/transformers';
import fs from 'node:fs';
const model='Xenova/opus-mt-es-en';
const revision='2cfbfecd5ddd066218bcc5a7b964d94b48d84066';
const source=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const output=process.argv[3];
env.allowLocalModels=false;
env.backends.onnx.logLevel='error';
const translator=await pipeline('translation',model,{revision,dtype:'q8',device:'cpu'});
const entries={};
try {
  const items=Object.entries(source);
  for(let i=0;i<items.length;i+=4){
    const batch=items.slice(i,i+4);
    const translated=await translator(batch.map(([,text])=>text),{max_new_tokens:256,num_beams:3});
    for(let j=0;j<batch.length;j++){
      const [key,text]=batch[j];const target=translated[j]?.translation_text;
      if(typeof target!=='string'||!target.trim())throw new Error('Empty translation '+key);
      entries[key]={source:text,target};
    }
    if(i%100===0)console.log(`${Math.min(i+4,items.length)}/${items.length}`);
  }
  fs.mkdirSync(output.slice(0,output.lastIndexOf('/')),{recursive:true});
  fs.writeFileSync(output,JSON.stringify({schema:1,model,revision,method:'machine-assisted editorial translation; review overrides maintained separately',entries},null,2)+'\n');
} finally {await translator.dispose();}
