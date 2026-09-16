import test from 'node:test';
import assert from 'node:assert/strict';
import {setLanguage,language,t} from '../assets/i18n.js';
test('English UI has explicit labels',()=>{setLanguage('en');assert.equal(t('Teoría'),'Theory');assert.equal(t('Mi progreso · 32 %'),'My progress · 32 %');assert.equal(t('32 de 32 módulos visibles.'),'32 of 32 modules visible.');});
test('Spanish remains source default on request',()=>{setLanguage('es');assert.equal(t('Teoría'),'Teoría');});
test('identifiers and commands are not translated by the UI dictionary',()=>{setLanguage('en');for(const v of ['M05','L05A','Get-WinEvent -LogName System','pwd\nid'])assert.equal(t(v),v);});
test('language rejects unrecognized values',()=>assert.throws(()=>setLanguage('../secrets')));
test('dynamic counts are localized without changing values',()=>{setLanguage('en');assert.equal(t('5/8 completados'),'5/8 complete');assert.equal(t('Prácticas (3)'),'Labs (3)');assert.equal(t('DIAPOSITIVA 2 / 5'),'SLIDE 2 / 5');});
test('English outputs are idempotent and Spanish switching remains possible',()=>{setLanguage('en');assert.equal(t(t('Comprobar respuesta')),'Check answer');setLanguage('es');assert.equal(language(),'es');});
