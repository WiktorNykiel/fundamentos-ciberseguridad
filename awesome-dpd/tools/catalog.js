/** Local filtering only. Never fetches external pages or stores personal information. */
const normalise=s=>String(s).normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
const cards=[...document.querySelectorAll('[data-source]')];
function filter(){
 const terms=normalise(document.querySelector('#q').value).trim().split(/\s+/).filter(Boolean);
 const category=document.querySelector('#category').value;
 let count=0;
 for(const card of cards){card.hidden=!(category==='all'||card.dataset.category===category)||!terms.every(t=>normalise(card.textContent).includes(t));if(!card.hidden)count++;}
 document.querySelector('#count').textContent=`${count} de ${cards.length} fuentes visibles`;
 document.querySelector('#empty').hidden=count!==0;
}
document.querySelector('#q').addEventListener('input',filter);
document.querySelector('#category').addEventListener('change',filter);
document.querySelector('#reset').addEventListener('click',()=>{document.querySelector('#q').value='';document.querySelector('#category').value='all';filter();document.querySelector('#q').focus();});
document.querySelector('#print').addEventListener('click',()=>window.print());
filter();
