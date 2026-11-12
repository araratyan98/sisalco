const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:400,height:800}});
await p.route('**/*',r=>{const u=r.request().url(); if(u.startsWith('http://local/')) return r.fulfill({contentType:'text/html; charset=utf-8',body:'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{margin:0}[hidden]{display:none!important}</style></head><body>'+fs.readFileSync('../web/sis-alco.html','utf8')+'</body></html>'}); r.abort();});
await p.goto('http://local/'); await p.waitForTimeout(800);
console.log(await p.evaluate(()=>{const W=innerWidth,out=[];document.querySelectorAll('body *').forEach(e=>{const r=e.getBoundingClientRect(); if(r.width&&r.right>W+1&&getComputedStyle(e).position!=='fixed'){let a=e,clip=false;while(a=a.parentElement){const o=getComputedStyle(a).overflowX;if(o==='hidden'||o==='auto'){clip=true;break}} if(!clip) out.push(e.tagName+'#'+e.id+'.'+e.className+' '+Math.round(r.right))}});return out.slice(0,8)}));
await b.close()})();
