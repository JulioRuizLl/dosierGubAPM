import re
import os
HERE=os.path.dirname(os.path.abspath(__file__))
os.makedirs(HERE+'/out',exist_ok=True)
D=HERE+'/base/'
VARIANT=open(HERE+'/variante.txt').read().strip() if os.path.exists(HERE+'/variante.txt') else 'apm'
TITLE={'apm':'APM · App para jueces y magistrados','dosier':'Dosier gubernativo APM · Guía del primer destino'}[VARIANT]
f=open(D+'dosier-gubernativo-apm.html',encoding='utf-8').read(); s=open(D+'Dosier_gubernativo_APM.html',encoding='utf-8').read()
body=open(HERE+'/apm_body.html',encoding='utf-8').read().replace('__VARIANT__',VARIANT)
if VARIANT=='dosier': body=body.replace('julioruizll.github.io/app-apm','julioruizll.github.io/dosierGubAPM')
brand=re.search(r'<a class="brand" href="#top"><img[^>]*></a>',f).group(0)
CSS='.sr-only{position:absolute!important;width:1px!important;height:1px!important;padding:0!important;margin:-1px!important;overflow:hidden!important;clip:rect(0,0,0,0)!important;white-space:nowrap!important;border:0!important}\n.tl-same{display:flex!important;align-items:center;gap:8px;font-weight:600;color:var(--ink)!important}\n.tl-same input{width:17px;height:17px;accent-color:var(--blue-deep)}\n'
JOIN_CSS='''.join-pill{flex:none;display:inline-flex;align-items:center;height:34px;padding:0 14px;border-radius:17px;background:var(--accent);color:var(--accent-ink)!important;font-weight:700;font-size:14px;text-decoration:none!important;border:1px solid var(--sky)}
.join-pill:hover{filter:brightness(1.12)}
.hero-join{display:table;margin-top:14px;color:var(--h-ink)!important;text-decoration:none!important;font-size:15.5px;border-bottom:2px solid var(--sky);padding-bottom:2px}
.hero-join b{font-weight:700}
.hero-join:hover{border-bottom-color:currentColor}
.join{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);gap:0;border:1px solid var(--line);border-left:4px solid var(--sky);background:var(--card);margin-top:6px}
.join-main{padding:22px 24px}
.join-main h4{margin:10px 0 12px;font-size:23px;line-height:1.2;color:var(--band-ink)}
.join-ben{margin:0 0 18px;padding-left:18px}
.join-ben li{margin:0 0 8px}
.join-btn{display:inline-flex;align-items:center;gap:8px;background:var(--accent);color:var(--accent-ink)!important;text-decoration:none!important;font-weight:700;padding:12px 18px;border-radius:4px;font-size:16px}
.join-btn:hover{filter:brightness(1.12)}
.join-btn svg{width:14px;height:14px}
.join-foot{margin:12px 0 0;font-size:13.5px;color:var(--muted)}
.join-side{background:var(--band);padding:22px 24px}
.join-side h5{margin:0 0 4px;font-size:15px;color:var(--band-ink)}
.join-side p{margin:0 0 14px;font-size:14.5px}
@media (max-width:760px){.join{grid-template-columns:1fr}.join-main,.join-side{padding:18px 16px}.hero-join{font-size:15px}}
@media (max-width:560px){.join-pill{height:30px;padding:0 10px;font-size:13px}}
'''
LOC_CSS='''.loc{margin-top:18px;border:1px solid var(--line);border-top:3px solid var(--blue);background:var(--card);padding:20px 22px}
.loc-t{margin:0 0 6px;font-size:21px;line-height:1.25;color:var(--band-ink);font-family:var(--serif)}
.loc .body{margin:0 0 14px}
.loc h5{margin:0 0 6px;font-size:15px;color:var(--band-ink)}
.loc-g{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,1fr);gap:18px;margin-bottom:16px}
.loc-gen ul{margin:0 0 10px;padding-left:18px}
.loc-gen li{margin:0 0 6px;font-size:15px}
.loc-sup{background:var(--band);padding:14px 16px}
.loc-dl{font-size:14.5px;padding:10px 14px;margin-top:4px}
.loc-cases{grid-template-columns:repeat(3,minmax(0,1fr))}
.loc-cases .chk label{font-size:14.5px}
@media (max-width:980px){.loc-cases{grid-template-columns:1fr}}
@media (max-width:760px){.loc{padding:16px}.loc-g{grid-template-columns:1fr}}
'''
INFO_CSS='''.loc-h{margin:6px 0 8px;font-size:15px;color:var(--band-ink)}
.loc-apps{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-bottom:16px}
.loc-app{background:var(--surface);padding:12px 14px;display:flex;flex-direction:column;gap:4px;font-size:14.5px}
.loc-app b{font-size:16px}
.loc-app a{font-size:14px;margin-top:2px}
.loc-eq{margin-bottom:10px}
.loc-eq b{font-size:15px}
.loc-eq .d{margin:2px 0 4px}
.loc-s{border-top:1px solid var(--line);padding-top:10px;margin-top:10px}
.loc-s b{font-size:14.5px}
.loc-s .d{margin:2px 0 4px;font-size:14px}
.loc-mat{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px 16px;margin-bottom:14px;font-size:14.5px}
.loc-mat span{display:block;font-weight:600}
.loc-min .body{margin:0 0 6px}
.loc-link{margin:10px 0 0;font-size:15px}
#informatica .terr{margin-bottom:6px}
@media (max-width:760px){.loc-apps,.loc-mat{grid-template-columns:1fr}}
'''
ASK_CSS='''.ask-terr{margin:0 0 16px;padding:0 0 16px;border-bottom:1px solid var(--line)}
.ask-terr label{display:flex;align-items:center;gap:8px;font-family:var(--serif);font-weight:700;font-size:20px;color:var(--h-ink);margin:0 0 8px}
.ask-terr select{font:inherit;font-size:16px;width:100%;padding:10px 12px;border:1px solid var(--line);border-radius:6px;background:var(--surface);color:var(--ink)}
.ask .n{display:inline-flex;align-items:center;justify-content:center;flex:none;width:26px;height:26px;border-radius:50%;background:var(--accent);color:var(--accent-ink);font-family:var(--sans,inherit);font-size:14px;font-weight:700;margin-right:8px;vertical-align:3px}
.ask-terr .n{margin-right:0}
'''
NOW_CSS='''.terr-now{display:flex;flex-wrap:wrap;align-items:baseline;gap:6px;background:var(--band);border-left:4px solid var(--sky);padding:10px 14px;margin:0 0 16px;font-size:15.5px}
.terr-now b{color:var(--band-ink)}
footer .credit a{color:inherit}
'''
ACT_CSS='''.act-btn{display:inline-flex;align-items:center;gap:8px;font:inherit;font-weight:700;font-size:15px;background:var(--accent);color:var(--accent-ink);border:0;border-radius:4px;padding:10px 16px;cursor:pointer}
.act-btn:hover{filter:brightness(1.12)}
.act-btn.sm{font-size:14px;padding:6px 12px;margin-left:auto}
.tl-act{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px;margin-top:14px}
.tl-act span{font-size:14px;color:var(--muted)}
.rep{display:inline-block;margin-top:10px;font-size:12.5px;color:var(--muted)!important;text-decoration:underline dotted!important}
.rep:hover{color:var(--link)!important}
.loc > .rep{margin-left:2px}
.inst-pill{flex:none;height:34px;padding:0 14px;border-radius:17px;background:transparent;color:var(--accent);border:1px solid var(--accent);font:inherit;font-weight:700;font-size:14px;cursor:pointer}
.inst-pill[hidden]{display:none}
footer .inst-note{flex-basis:100%;font-size:13px;font-style:normal}
@media (max-width:560px){.act-btn.sm{margin-left:0}.inst-pill{height:30px;padding:0 10px;font-size:13px}}
'''
INST_CSS='''.inst-sheet{position:fixed;inset:auto 0 0 0;z-index:80;display:flex;justify-content:center;padding:0 12px 12px;pointer-events:none;transform:translateY(110%);transition:transform .25s ease}
.inst-sheet.on{transform:none}
.inst-sheet[hidden]{display:none}
.inst-card{pointer-events:auto;position:relative;width:min(460px,100%);background:var(--card);color:var(--ink);border:1px solid var(--line);border-top:4px solid var(--sky);border-radius:14px;box-shadow:0 18px 50px rgba(8,20,32,.30);padding:18px 18px 12px}
.inst-h{display:flex;align-items:center;gap:12px;margin:0 28px 12px 0}
.inst-h img{border-radius:12px;border:1px solid var(--line);flex:none}
.inst-h b{display:block;font-size:18px;color:var(--band-ink)}
.inst-h span{font-size:13.5px;color:var(--muted)}
.inst-card p{margin:0 0 12px;font-size:15px}
.inst-tip{font-size:13.5px!important;color:var(--muted)}
.inst-steps{list-style:none;margin:0 0 10px;padding:0;display:grid;gap:10px}
.inst-steps li{display:grid;grid-template-columns:34px 1fr;gap:10px;align-items:center;font-size:15px}
.inst-steps .ic{width:34px;height:34px;border-radius:8px;background:var(--band);color:var(--band-ink);display:flex;align-items:center;justify-content:center;font-weight:700}
.inst-go{width:100%;justify-content:center;font-size:16px;padding:12px 16px;margin-bottom:6px}
.inst-x{position:absolute;top:8px;right:10px;border:0;background:none;font-size:26px;line-height:1;color:var(--muted);cursor:pointer;padding:4px 8px}
.inst-later{display:block;margin:2px auto 0;border:0;background:none;color:var(--muted);font:inherit;font-size:14px;text-decoration:underline;cursor:pointer;padding:6px}
@media (prefers-reduced-motion: reduce){.inst-sheet{transition:none}}
'''
MAPMI_CSS='''.map-es{margin:2px 0 4px}
.map-es svg{display:block;width:100%;height:auto;max-height:300px}
.map-r{fill:var(--surface-2);stroke:var(--card);stroke-width:1.2;cursor:pointer;transition:fill .15s}
.map-r.hov{fill:color-mix(in srgb,var(--sky) 55%,var(--surface-2))}
.map-r.on{fill:var(--accent)}
.map-dot{stroke-width:2}
.map-inset{fill:none;stroke:var(--line);stroke-dasharray:3 3}
.map-cap{font-size:14px;color:var(--muted);margin:0 0 8px;min-height:20px}
.map-cap b{color:var(--h-ink)}
.mi-chip{display:flex;align-items:center;gap:8px;margin-top:10px;padding:9px 12px;border-radius:8px;background:var(--band);color:var(--band-ink)!important;text-decoration:none!important;font-size:14.5px;border-left:4px solid var(--sky)}
.mi-chip.urg{border-left-color:#C0392B}
.mi-chip svg{flex:none}
.mi-card{border:1px solid var(--line);border-top:4px solid var(--sky);background:var(--card);padding:20px 22px}
.mi-top{display:flex;gap:20px;align-items:center;flex-wrap:wrap;margin-bottom:16px}
.mi-cd{min-width:150px;background:var(--accent);color:var(--accent-ink);border-radius:10px;padding:14px 18px;text-align:center}
.mi-cd b{display:block;font-family:var(--serif);font-size:48px;line-height:1}
.mi-cd span{display:block;font-size:14px;margin-top:4px}
.mi-cd.urg{background:#A93226;color:#fff}
.mi-who{display:flex;flex-direction:column;gap:2px;font-size:15px}
.mi-who b{font-size:19px;color:var(--band-ink)}
.mi-who span{color:var(--muted)}
.mi-who .mi-sub{color:var(--band-ink);font-weight:600}
.mi-steps{list-style:none;margin:0 0 14px;padding:0;display:grid;gap:6px}
.mi-steps li{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1.4fr) auto;gap:10px;align-items:center;padding:8px 12px;background:var(--surface);border-left:4px solid var(--line);font-size:14.5px}
.mi-steps li.next{border-left-color:var(--accent)}
.mi-steps li.today{border-left-color:#C0392B;font-weight:700}
.mi-steps li.past{opacity:.6}
.mi-steps .dt{font-weight:700}
.mi-steps .rl{font-size:13px;color:var(--muted);white-space:nowrap}
.mi-row{display:flex;flex-wrap:wrap;gap:12px 20px;align-items:center;margin-bottom:12px}
.mi-done{display:flex;gap:8px;align-items:center;font-weight:600}
.mi-done input{width:17px;height:17px;accent-color:var(--blue-deep)}
.mi-prog{position:relative;flex:1;min-width:220px;display:flex;justify-content:space-between;gap:10px;padding:8px 12px 12px;background:var(--surface);text-decoration:none!important;color:var(--ink)!important;font-size:14.5px;overflow:hidden}
.mi-prog i{position:absolute;left:0;bottom:0;height:4px;background:var(--accent)}
.mi-contacts{display:flex;flex-wrap:wrap;gap:6px 16px;align-items:center;margin-bottom:12px;font-size:14.5px}
.mi-contacts .lines{display:flex;flex-wrap:wrap;gap:4px 16px}
.mi-lt{font-weight:700;font-size:14px;color:var(--band-ink)}
.mi-act{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.act-btn.ghost{background:transparent;color:var(--accent);border:1px solid var(--accent)}
.lnk{border:0;background:none;color:var(--link);font:inherit;font-size:14.5px;text-decoration:underline;cursor:pointer;padding:6px}
.mi-form{margin-top:14px;background:var(--surface);padding:16px 18px;border-radius:2px}
.mi-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px 16px}
.mi-grid label{display:flex;flex-direction:column;gap:4px;font-weight:600;font-size:14.5px}
.mi-grid label span{font-weight:400;color:var(--muted)}
.mi-grid input[type=text],.mi-grid input[type=date]{font:inherit;font-size:15.5px;padding:8px 10px;border:1px solid var(--line);border-radius:5px;background:var(--card);color:var(--ink)}
.mi-grid .tl-same{flex-direction:row!important;align-self:end}
.mi-l{display:flex;flex-direction:column;gap:4px}
@media (max-width:760px){.mi-grid{grid-template-columns:1fr}.mi-steps li{grid-template-columns:1fr auto}.mi-steps .lb{grid-column:1/-1;order:3}.mi-card{padding:16px}.mi-cd b{font-size:40px}}
'''
APP_CSS='''/*APP-SHELL*/
html.js .view{display:none}
html.js .view.on{display:grid}
.view{gap:44px;min-width:0}
.appshell{max-width:1240px;margin:0 auto;padding:26px 20px 70px;display:grid;grid-template-columns:196px minmax(0,1fr);gap:34px;text-align:left}
.appshell main{display:block;min-width:0}
.home-left,.home-side{display:flex;flex-direction:column;gap:12px;min-width:0}
.home-stats span{display:inline-block}
nav.side{position:sticky;top:84px;align-self:start;display:flex;flex-direction:column;gap:4px}
nav.side a{display:flex;align-items:center;gap:12px;padding:11px 14px;border-radius:10px;color:var(--ink);text-decoration:none;font-weight:600;font-size:16px;transition:background .15s}
nav.side a:hover{background:var(--surface)}
nav.side a[aria-current]{background:var(--accent);color:var(--accent-ink)}
nav.side a svg{flex:none}
.side-note{margin-top:14px;padding:0 14px;font-size:13px;color:var(--muted);font-style:italic}
.subnav{position:sticky;top:62px;z-index:15;display:flex;gap:6px;overflow-x:auto;background:var(--bg);padding:10px 0;margin:-10px 0 -20px;border-bottom:1px solid var(--line);scrollbar-width:none}
.subnav::-webkit-scrollbar{display:none}
.subnav[hidden]{display:none}
.subnav a{flex:none;white-space:nowrap;padding:6px 14px;border:1px solid var(--line);border-radius:999px;background:var(--card);color:var(--ink);text-decoration:none;font-size:14.5px}
.subnav a.on{background:var(--band);color:var(--band-ink);border-color:transparent;font-weight:700}
nav.tabbar{display:none}
.home-hero{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.25fr);gap:26px;align-items:start}
.home-wel{background:linear-gradient(150deg,#0F1C33 0%,#1B2F57 65%,#24406F 100%);color:#fff;border-radius:14px;padding:30px 28px;position:relative;overflow:hidden;box-shadow:0 18px 40px rgba(8,20,32,.18)}
.home-wel::after{content:"";position:absolute;left:0;right:0;bottom:0;height:5px;background:#B8964A}
.home-wel .eyebrow{color:#E4D6AE;font-size:13px;letter-spacing:.08em;text-transform:uppercase;font-weight:700}
.home-wel h1{font-family:var(--serif);font-size:clamp(34px,4.4vw,50px);line-height:1.02;margin:14px 0 14px;color:#fff;text-wrap:balance}
.home-wel .lede{color:#E4E9F2;font-size:16.5px;margin:0 0 18px}
.home-stats{display:flex;flex-wrap:wrap;gap:8px}
.home-stats span{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.22);border-radius:999px;padding:5px 12px;font-size:14px;color:#E4E9F2}
.home-stats b{color:#fff}
.home-hero .ask{animation:none}
.tiles{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.tile{display:flex;flex-direction:column;gap:4px;padding:16px;border:1px solid var(--line);border-radius:12px;background:var(--card);color:var(--ink)!important;text-decoration:none!important;transition:transform .15s,box-shadow .15s,border-color .15s;min-height:118px}
.tile:hover{transform:translateY(-2px);box-shadow:var(--shadow);border-color:var(--sky)}
.tile .ti{width:42px;height:42px;border-radius:10px;background:var(--band);color:var(--band-ink);display:flex;align-items:center;justify-content:center;margin-bottom:6px}
.tile b{font-size:16px;line-height:1.25}
.tile .ts{font-size:13.5px;color:var(--muted);line-height:1.35}
.tile.hl{border-color:var(--sky);background:color-mix(in srgb,var(--sky) 9%,var(--card))}
.tile.hl .ts{color:var(--band-ink);font-weight:600}
.home-row{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin-top:12px}
.home-card{border:1px solid var(--line);border-radius:12px;padding:18px 20px;background:var(--card);display:flex;flex-direction:column;gap:4px}
.hc-k{font-size:12.5px;letter-spacing:.06em;text-transform:uppercase;font-weight:700;color:var(--muted)}
.hc-t{font-family:var(--serif);font-size:21px;font-weight:700;color:var(--band-ink);margin-top:4px}
.hc-s{font-size:15px;color:var(--ink)}
.hc-a{display:flex;flex-wrap:wrap;gap:8px 16px;align-items:center;margin-top:10px;font-size:14.5px}
.join-card{background:linear-gradient(150deg,#1B2F57,#24406F);border-color:transparent;color:#fff}
.join-card .hc-k{color:#E4D6AE}.join-card .hc-t{color:#fff}.join-card .hc-s{color:#E4E9F2}
.join-card .act-btn{background:#B8964A;color:#0D1118}
.about-act{display:flex;flex-wrap:wrap;gap:10px;margin-top:12px}
.about-ul{margin:0;padding-left:18px}.about-ul li{margin:0 0 6px}
#foot{max-width:1240px}
html[data-size="l"] .appshell main{zoom:1.12}
html[data-size="xl"] .appshell main{zoom:1.25}
.card-tools{display:flex;flex-wrap:wrap;align-items:center;gap:6px 14px;margin-top:12px;padding-top:10px;border-top:1px dashed var(--line)}
.ct-b{display:inline-flex;align-items:center;gap:6px;border:0;background:none;color:var(--muted);font:inherit;font-size:13.5px;cursor:pointer;padding:4px 2px}
.ct-b:hover{color:var(--link)}
.ct-b.on{color:var(--sky);font-weight:700}
.card-tools .rep{margin:0 0 0 auto}
.tn-act{display:flex;flex-wrap:wrap;gap:8px;margin-left:auto}
.tn-act .act-btn.sm{margin-left:0}
.favs{margin-top:14px;border:1px solid var(--line);border-radius:12px;padding:16px 18px;background:var(--card)}
.favs-h{display:flex;flex-wrap:wrap;gap:4px 12px;align-items:baseline;margin-bottom:10px}
.favs-h b{display:inline-flex;align-items:center;gap:6px;font-size:16px;color:var(--band-ink)}
.favs-h b svg{color:var(--sky)}
.favs-h span{font-size:13px;color:var(--muted)}
.favs-g{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.fav{background:var(--surface);border-radius:8px;padding:10px 12px;min-width:0}
.fav-t{display:flex;justify-content:space-between;gap:8px;align-items:start;font-size:14.5px;margin-bottom:4px}
.fav-x{border:0;background:none;color:var(--muted);font-size:20px;line-height:1;cursor:pointer;padding:0 4px}
.home-ev{display:flex;gap:10px;align-items:center;margin-top:12px;padding:12px 14px;border-radius:10px;background:var(--band);color:var(--band-ink)!important;text-decoration:none!important;font-size:15px}
.glos .nolist{display:grid;grid-template-columns:200px 1fr;gap:12px;align-items:baseline}
.glos .gd{font-size:15px;color:var(--ink)}
.set-row{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px;margin-bottom:12px}
.r-rec{padding:8px 14px 4px;font-size:12.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}
.mi-apm{display:flex;flex-wrap:wrap;gap:12px;align-items:center;background:var(--band);border-radius:10px;padding:12px 14px;margin:4px 0 12px}
.mi-apm .ti{width:40px;height:40px;border-radius:10px;background:var(--card);color:var(--band-ink);display:flex;align-items:center;justify-content:center;flex:none}
.mi-apm div{display:flex;flex-direction:column;gap:2px;flex:1;min-width:200px}
.mi-apm b{color:var(--band-ink)}
.mi-apm span{font-size:14px;color:var(--muted)}
.mi-apm-a{flex-direction:row!important;align-items:center;gap:8px!important;flex:none!important;min-width:0!important}
.welc-steps button{border:0;background:none;color:var(--link);font:inherit;font-size:15.5px;text-align:left;padding:0;cursor:pointer;text-decoration:underline}
section[hidden]{display:none!important}
.ev-big{grid-column:1/-1}
.ev-tag{display:inline-block;vertical-align:3px;font-family:var(--font);font-size:12px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;background:var(--band);color:var(--band-ink);border-radius:4px;padding:2px 7px;margin-right:4px}
.ev-notas{margin:6px 0 10px;padding-left:18px;font-size:14.5px}.ev-notas li{margin:0 0 4px}
.ev-lema{font-family:var(--serif);font-style:italic;font-size:18px;color:var(--band-ink);margin:0 0 8px}
.ev-ses{list-style:none;margin:8px 0 10px;padding:0;display:grid;gap:6px}
.ev-ses li{display:grid;grid-template-columns:150px 1fr;gap:10px;background:var(--card);border-left:3px solid var(--sky);padding:8px 10px;font-size:14.5px}
.ev-d{font-weight:700;color:var(--band-ink);text-transform:capitalize}
.ev-org{font-size:13.5px;color:var(--muted)}
@media (max-width:560px){.ev-ses li{grid-template-columns:1fr;gap:2px}}
@media (max-width:1100px){.tiles{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:760px){.favs-g{grid-template-columns:1fr}.glos .nolist{grid-template-columns:1fr;gap:2px}.tn-act{margin-left:0}}
@media (max-width:920px){
 .appshell{grid-template-columns:1fr;padding:14px 16px 96px;gap:0}
 nav.side{display:none}
 nav.tabbar{display:flex;position:fixed;left:0;right:0;bottom:0;z-index:60;background:var(--card);border-top:1px solid var(--line);padding:6px 4px calc(6px + env(safe-area-inset-bottom,0px));box-shadow:0 -6px 20px rgba(8,20,32,.08)}
 nav.tabbar a{flex:1;display:flex;flex-direction:column;align-items:center;gap:2px;padding:4px 0;color:var(--muted);text-decoration:none;font-size:11.5px;font-weight:600}
 nav.tabbar a[aria-current]{color:var(--accent)}
 nav.tabbar a[aria-current] svg{transform:translateY(-1px)}
 .home-hero{display:flex;flex-direction:column;gap:14px}
 .home-left{display:contents}
 .home-wel{order:1}.home-hero .ask{order:2}.home-side{order:3}
 .home-wel h1{font-size:34px;margin:10px 0}
 .home-wel .lede{font-size:15.5px;margin-bottom:14px}
 .home-wel{padding:22px 20px}
 .home-row{grid-template-columns:1fr}
 .subnav{top:56px;margin:-4px -16px -16px;padding:10px 16px}
 #foot{padding-bottom:96px}
 .inst-sheet{bottom:64px}
}
@media (max-width:560px){.tiles{gap:10px}.tile{padding:13px;min-height:108px}.tile b{font-size:15px}}
'''
def head(x):
    h=x[:x.index('</style>')]
    if '.tl-same{' not in h: h+=CSS
    if '.join-pill{' not in h: h+=JOIN_CSS
    if '.loc-g{' not in h: h+=LOC_CSS
    if '.loc-apps{' not in h: h+=INFO_CSS
    if '.ask-terr{' not in h: h+=ASK_CSS
    if '.terr-now{' not in h: h+=NOW_CSS
    if '.act-btn{' not in h: h+=ACT_CSS
    if '.inst-sheet{' not in h: h+=INST_CSS
    if '.map-es{' not in h: h+=MAPMI_CSS
    if '/*APP-SHELL*/' in h: h=h[:h.index('/*APP-SHELL*/')]
    h+=APP_CSS
    if 'footer .visits' not in h: h+='footer .visits{flex-basis:100%;font-size:13px;font-style:normal;font-variant-numeric:tabular-nums}\nfooter .visits[hidden]{display:none}\n'
    return h+'</style>\n'
b=body
old='<a class="brand" href="#top"><b>APM</b><span>Dosier gubernativo</span></a>'
assert b.count(old)==1; b=b.replace(old,brand)
open(HERE+'/out/dosier-gubernativo-apm.html','w',encoding='utf-8').write(head(f)+b.rstrip('\n')+'\n')
PWA_HEAD='<link rel="manifest" href="manifest.webmanifest">\n<meta name="theme-color" content="#1B2F57">\n<link rel="apple-touch-icon" href="apple-touch-icon.png">\n<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-title" content="APM">\n'
PWA_JS='<script>if(\'serviceWorker\' in navigator && (location.protocol===\'https:\'||location.hostname===\'localhost\')){window.addEventListener(\'load\',function(){navigator.serviceWorker.register(\'sw.js\').catch(function(){});});}</script>\n'
hs=head(s).replace('<title>APM · App para jueces y magistrados</title>','<title>'+TITLE+'</title>',1)
if 'rel="manifest"' not in hs: hs=hs.replace('<title>',PWA_HEAD+'<title>',1)
open(HERE+'/../index.html','w',encoding='utf-8').write(hs+'</head>\n<body>\n'+b.rstrip('\n')+'\n'+PWA_JS+'\n</body>\n</html>\n')
print('built')
