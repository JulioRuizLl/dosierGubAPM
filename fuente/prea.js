const { chromium } = require('playwright'); const fs=require('fs');
const path=require('path'); const F=path.resolve(__dirname,'../index.html');
(async()=>{ const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1280,height:800}});
 await p.goto('file://'+F); await p.waitForTimeout(1800);
 const main=await p.evaluate(()=>{document.querySelectorAll('[id^="ix"]').forEach(e=>e.removeAttribute('id')); document.querySelectorAll('.flash').forEach(e=>e.classList.remove('flash')); return document.getElementById('main').innerHTML;});
 let h=fs.readFileSync(F,'utf8');
 const re=/(<main id="main">)[\s\S]*?(<\/main>)/; if(!re.test(h)) throw 'main';
 h=h.replace(re,(m,a,c)=>a+main+c);
 fs.writeFileSync(F,h); await b.close(); console.log('prerendered',h.length);})();
