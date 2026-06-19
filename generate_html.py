import json

with open('final_all.json') as f:
    funcs = json.load(f)

with open('types_info.json') as f:
    types = json.load(f)

# Sort functions by name
funcs.sort(key=lambda x: x.get('name', ''))

funcs_js = json.dumps(funcs)
types_js = json.dumps(types)

html = """<!DOCTYPE html>
<html class="dark" lang="pt-BR">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>OpenMPI v4.0.7 - Documentação</title>
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600;700&family=Inter:wght@400;500&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet"/>
    
    <script id="tailwind-config">
        tailwind.config = {
          darkMode: "class",
          theme: {
            extend: {
              "colors": {
                      "surface-container-high": "#252a31",
                      "error": "#ffb4ab",
                      "on-primary-fixed-variant": "#004f54",
                      "surface-bright": "#343a41",
                      "background": "#0e141a",
                      "surface-container": "#1a2027",
                      "on-secondary-fixed-variant": "#74009f",
                      "primary-container": "#00f2ff",
                      "surface-variant": "#2f353c",
                      "primary-fixed": "#74f5ff",
                      "surface-tint": "#00dbe7",
                      "tertiary-fixed": "#d9e3f4",
                      "error-container": "#93000a",
                      "on-primary-fixed": "#002022",
                      "secondary-fixed-dim": "#ebb2ff",
                      "secondary-container": "#ce5dff",
                      "on-tertiary-fixed": "#121c28",
                      "surface-dim": "#0e141a",
                      "on-tertiary": "#27313e",
                      "on-background": "#dde3ec",
                      "on-primary-container": "#006a71",
                      "tertiary": "#f6f8ff",
                      "surface": "#0e141a",
                      "on-secondary": "#520071",
                      "inverse-on-surface": "#2b3138",
                      "surface-container-lowest": "#090f15",
                      "primary": "#e1fdff",
                      "on-secondary-fixed": "#320047",
                      "secondary": "#ebb2ff",
                      "on-surface-variant": "#b9cacb",
                      "tertiary-fixed-dim": "#bdc7d8",
                      "tertiary-container": "#d2dced",
                      "outline": "#849495",
                      "inverse-surface": "#dde3ec",
                      "surface-container-low": "#161c23",
                      "surface-container-highest": "#2f353c",
                      "on-tertiary-fixed-variant": "#3e4755",
                      "inverse-primary": "#00696f",
                      "on-error": "#690005",
                      "primary-fixed-dim": "#00dbe7",
                      "outline-variant": "#3a494b",
                      "on-surface": "#dde3ec",
                      "on-primary": "#00363a",
                      "on-tertiary-container": "#57616f",
                      "secondary-fixed": "#f8d8ff",
                      "on-error-container": "#ffdad6",
                      "on-secondary-container": "#480064"
              },
              "spacing": {
                      "gutter": "24px", "xs": "4px", "md": "16px", "sm": "8px", "base": "4px", "xl": "48px", "lg": "24px", "container-max": "1280px"
              },
              "fontFamily": {
                      "code-sm": ["Space Mono"], "label-caps": ["Space Mono"], "headline-xl": ["Geist"], "headline-lg-mobile": ["Geist"], "headline-lg": ["Geist"], "body-md": ["Inter"]
              },
              "fontSize": {
                      "code-sm": ["14px", {"lineHeight": "1.5", "fontWeight": "400"}],
                      "label-caps": ["12px", {"lineHeight": "1", "letterSpacing": "0.1em", "fontWeight": "700"}],
                      "headline-xl": ["48px", {"lineHeight": "1.1", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                      "headline-lg-mobile": ["24px", {"lineHeight": "1.2", "fontWeight": "600"}],
                      "headline-lg": ["32px", {"lineHeight": "1.2", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                      "body-md": ["16px", {"lineHeight": "1.6", "letterSpacing": "0", "fontWeight": "400"}]
              }
            }
          }
        }
    </script>
    <style>
        .cyber-grid {
            background-size: 40px 40px;
            background-image: 
                linear-gradient(to right, rgba(0, 242, 255, 0.03) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(0, 242, 255, 0.03) 1px, transparent 1px);
        }
        .hud-border {
            border: 1px solid #1e293b;
            box-shadow: inset 0 0 10px rgba(0, 242, 255, 0.02);
            transition: all 0.3s ease;
        }
        .hud-border:hover, .hud-border-active {
            border-color: #00f2ff;
            box-shadow: inset 0 0 15px rgba(0, 242, 255, 0.1);
        }
        .stripe-bg {
            background: repeating-linear-gradient(
                45deg,
                rgba(0, 242, 255, 0.03),
                rgba(0, 242, 255, 0.03) 10px,
                transparent 10px,
                transparent 20px
            );
        }
        .code-syntax { color: #b9cacb; }
        .code-keyword { color: #ebb2ff; }
        .code-function { color: #00f2ff; }
        .code-type { color: #74f5ff; }
        .code-string { color: #ffb4ab; }
        .code-comment { color: #849495; font-style: italic; }

        ::-webkit-scrollbar { width: 8px; height: 8px; }
        ::-webkit-scrollbar-track { background: #0e141a; }
        ::-webkit-scrollbar-thumb { background: #2f353c; border-radius: 0; }
        ::-webkit-scrollbar-thumb:hover { background: #00f2ff; }
    </style>
</head>
<body class="bg-background text-on-background font-body-md text-body-md min-h-screen cyber-grid overflow-hidden selection:bg-primary-container selection:text-on-primary-container">

<header class="bg-surface dark:bg-surface w-full border-b border-outline-variant dark:border-outline-variant h-[65px] flex-shrink-0 z-30 relative">
    <div class="flex justify-between items-center px-lg py-sm w-full max-w-container-max mx-auto h-full">
        <div class="flex items-center gap-md">
            <button class="md:hidden flex items-center justify-center p-xs text-primary-container hover:bg-surface-container-high focus:outline-none animate-pulse" onclick="toggleSidebar(true)">
                <span class="material-symbols-outlined text-[24px]">menu</span>
            </button>
            <span class="font-headline-lg text-[24px] font-bold text-primary-container tracking-tighter cursor-pointer" onclick="showWelcome()">OpenMPI</span>
            <span class="font-label-caps text-label-caps text-on-surface-variant ml-sm py-xs px-sm border border-outline-variant rounded-none opacity-80">v4.0.7</span>
        </div>
        <div class="flex items-center gap-sm">
            <div class="relative hidden sm:block">
                <span class="material-symbols-outlined absolute left-sm top-1/2 -translate-y-1/2 text-on-surface-variant text-[18px]">search</span>
                <input id="search-input" class="bg-surface-container-high border-b-2 border-x-0 border-t-0 border-outline-variant focus:border-primary-container focus:ring-0 text-on-surface font-code-sm text-code-sm py-sm pl-xl pr-sm w-64 transition-colors placeholder:text-outline" placeholder="Pesquisar API..." type="text"/>
            </div>
        </div>
    </div>
</header>

<div class="flex w-full max-w-container-max mx-auto h-[calc(100vh-65px)] relative">
    <!-- Overlay de fundo para fechar o menu no mobile -->
    <div id="sidebar-overlay" class="fixed inset-0 z-40 bg-black/60 backdrop-blur-xs hidden md:hidden transition-opacity duration-300" onclick="toggleSidebar(false)"></div>
    
    <aside id="sidebar" class="fixed inset-y-0 left-0 z-50 flex flex-col w-72 bg-surface-container-low border-r border-outline-variant py-lg gap-sm overflow-y-auto transform -translate-x-full transition-transform duration-300 ease-in-out md:relative md:translate-x-0 md:flex md:z-10">
        <div class="px-md mb-md flex justify-between items-center">
            <div>
                <p class="font-label-caps text-label-caps text-on-surface-variant mb-xs">Documentação</p>
                <p class="font-code-sm text-code-sm text-outline">High-Performance Computing</p>
            </div>
            <button class="md:hidden text-primary-container p-xs hover:bg-surface-container-high focus:outline-none" onclick="toggleSidebar(false)">
                <span class="material-symbols-outlined text-[20px]">close</span>
            </button>
        </div>
        
        <!-- Mobile Search Input inside Sidebar -->
        <div class="px-md mb-sm block sm:hidden">
            <div class="relative w-full">
                <span class="material-symbols-outlined absolute left-sm top-1/2 -translate-y-1/2 text-on-surface-variant text-[18px]">search</span>
                <input id="search-input-mobile" class="bg-surface-container-high border-b-2 border-x-0 border-t-0 border-outline-variant focus:border-primary-container focus:ring-0 text-on-surface font-code-sm text-code-sm py-sm pl-xl pr-sm w-full transition-colors placeholder:text-outline" placeholder="Pesquisar API..." type="text"/>
            </div>
        </div>

        <nav class="flex-1 flex flex-col gap-xs font-code-sm text-code-sm">
            <a id="nav-welcome" class="flex items-center gap-md text-primary-container bg-primary-container/10 border-l-2 border-primary-container px-md py-sm cursor-pointer" onclick="showWelcome()">
                <span class="material-symbols-outlined text-[20px]">rocket_launch</span> Visão Geral
            </a>
            <a id="nav-types" class="flex items-center gap-md text-on-surface-variant px-md py-sm hover:bg-surface-container-highest hover:text-on-surface transition-all cursor-pointer" onclick="showTypes()">
                <span class="material-symbols-outlined text-[20px]">memory</span> Tipos MPI
            </a>
            <a id="nav-api" class="flex items-center gap-md text-on-surface-variant px-md py-sm hover:bg-surface-container-highest hover:text-on-surface transition-all cursor-pointer" onclick="showApiReference()">
                <span class="material-symbols-outlined text-[20px]">api</span> API Reference
            </a>
            <div id="func-list" class="pl-xl pr-md py-xs flex flex-col gap-xs mt-xs mb-sm border-l border-outline-variant ml-[24px]">
                <!-- Funcs inserted by JS -->
            </div>
        </nav>
    </aside>

    <main id="main-content" class="flex-1 px-md md:px-xl py-xl overflow-y-auto">
        <!-- Content injected via JS -->
    </main>
</div>

<script>
    const funcs = FUNC_DATA_PLACEHOLDER;
    const types = TYPES_DATA_PLACEHOLDER;

    // KMP (Knuth-Morris-Pratt)
    function computeLPS(p) { let m=p.length,lps=Array(m).fill(0),len=0,i=1; while(i<m) { if(p[i]===p[len]) { len++; lps[i]=len; i++; } else if(len!==0) len=lps[len-1]; else { lps[i]=0; i++; } } return lps; }
    function KMPSearch(t, p) { if(!p) return true; if(!t) return false; let n=t.length,m=p.length,lps=computeLPS(p),i=0,j=0; while(i<n) { if(t[i].toLowerCase()===p[j].toLowerCase()) { i++; j++; } if(j===m) return true; else if(i<n&&t[i].toLowerCase()!==p[j].toLowerCase()) { if(j!==0) j=lps[j-1]; else i++; } } return false; }

    let searchIndex = [];
    function buildSearchIndex() {
        searchIndex = [];
        funcs.forEach(f => {
            let parts = [f.name, f.short_desc, f.description, f.synopsis, f.example||''];
            if(f.params) f.params.forEach(p=>parts.push(p.name,p.desc));
            searchIndex.push({type:'func',func:f,st:parts.join(' ')});
        });
        types.forEach(c => c.types.forEach(t => searchIndex.push({type:'type',category:c.category, type:t, st:t.name+' '+t.desc+' '+c.category})));
    }
    function searchAll(q) {
        if(!q) return funcs.map(f=>({type:'func',func:f}));
        let r=[];
        searchIndex.forEach(i => { if(KMPSearch(i.st,q)) r.push(i); });
        return r;
    }
    buildSearchIndex();
    const allFuncItems = funcs.map(f=>({type:'func',func:f}));
    function findFunc(name) { return funcs.find(f=>f.name===name); }

    function escapeHTML(s) { return (s||'').replace(/[&<>"']/g, m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m])); }

    function highlightSyntax(code) {
        if(!code) return '';
        let html = escapeHTML(code);
        html = html.replace(/\\b(int|void|char|double|float|long|short|unsigned|struct|MPI_Comm|MPI_Datatype|MPI_Op|MPI_Aint|MPI_Count|MPI_Win|MPI_Info|MPI_Request|MPI_Status)\\b/g, '<span class="code-type">$1</span>');
        html = html.replace(/\\b(if|else|return|for|while|do|break|continue|#include)\\b/g, '<span class="code-keyword">$1</span>');
        html = html.replace(/\\b(MPIX?_\\w+)\\b/g, '<span class="code-function">$1</span>');
        html = html.replace(/(&quot;.*?&quot;)/g, '<span class="code-string">$1</span>');
        html = html.replace(/(\\/\\*.*?\\*\\/|\\/\\/.*)/g, '<span class="code-comment">$1</span>');
        return html;
    }

    function renderSearchList(list) {
        const nav = document.getElementById('func-list');
        nav.innerHTML = '';
        list.forEach(item => {
            const a = document.createElement('a');
            a.className = 'text-on-surface-variant hover:text-primary-container text-[13px] transition-colors py-xs cursor-pointer truncate block w-full';
            if(item.type === 'func') {
                a.textContent = item.func.name;
                a.onclick = () => {
                    document.querySelectorAll('#func-list a').forEach(el => {
                        el.className = 'text-on-surface-variant hover:text-primary-container text-[13px] transition-colors py-xs cursor-pointer truncate block w-full';
                    });
                    a.className = 'text-primary-container font-bold text-[13px] py-xs flex items-center before:content-[\'>\'] before:mr-xs before:text-primary-container truncate block w-full';
                    showDetail(item.func.name);
                };
            } else {
                a.textContent = item.type.name;
                a.className = 'text-on-surface-variant hover:text-secondary-container text-[13px] transition-colors py-xs cursor-pointer truncate block w-full';
                a.onclick = () => {
                    showTypes();
                    setTimeout(() => {
                        const el = document.getElementById('type-'+item.type.name.replace(/[^a-zA-Z0-9]/g,'-'));
                        if(el) el.scrollIntoView({behavior:'smooth',block:'center'});
                    }, 50);
                };
            }
            nav.appendChild(a);
        });
    }

    function setActiveNav(id) {
        const navIds = ['nav-welcome', 'nav-types', 'nav-api'];
        navIds.forEach(navId => {
            const el = document.getElementById(navId);
            if (!el) return;
            if (navId === id) {
                el.className = 'flex items-center gap-md text-primary-container bg-primary-container/10 border-l-2 border-primary-container px-md py-sm cursor-pointer';
            } else {
                el.className = 'flex items-center gap-md text-on-surface-variant px-md py-sm hover:bg-surface-container-highest hover:text-on-surface transition-all cursor-pointer';
            }
        });
        if (id !== 'nav-api') {
            document.querySelectorAll('#func-list a').forEach(el => {
                el.className = 'text-on-surface-variant hover:text-primary-container text-[13px] transition-colors py-xs cursor-pointer truncate block w-full';
            });
        }
        toggleSidebar(false);
    }

    function selectSidebarItem(name) {
        document.querySelectorAll('#func-list a').forEach(el => {
            if (el.textContent === name) {
                el.className = 'text-primary-container font-bold text-[13px] py-xs flex items-center before:content-[\'>\'] before:mr-xs before:text-primary-container truncate block w-full';
                el.scrollIntoView({behavior:'smooth',block:'center'});
            } else {
                el.className = 'text-on-surface-variant hover:text-primary-container text-[13px] transition-colors py-xs cursor-pointer truncate block w-full';
            }
        });
    }

    function showWelcome() {
        setActiveNav('nav-welcome');
        document.getElementById('main-content').innerHTML = `
            <div class="mb-xl border-b border-outline-variant pb-md">
                <div class="flex items-center gap-sm mb-sm">
                    <span class="bg-primary-container/10 text-primary-container border border-primary-container/30 px-sm py-xs font-label-caps text-label-caps rounded-none">SYS.INFO</span>
                </div>
                <h1 class="font-headline-xl text-[48px] font-bold text-on-background">Open MPI v4.0.7 DevDocs</h1>
                <p class="mt-sm text-on-surface-variant font-body-md text-body-md max-w-2xl">
                    Sistema de documentação técnica cibernética com algoritmo KMP e design Neon Protocol.
                    Fornece acesso instantâneo a referências de API, descrições detalhadas em PT-BR e exemplos práticos para ${funcs.length} funções MPI.
                </p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-lg">
                <section class="hud-border bg-surface-container rounded-none p-lg">
                    <h2 class="font-label-caps text-label-caps text-primary-container mb-md flex items-center gap-sm"><span class="material-symbols-outlined text-[16px]">speed</span> Performance</h2>
                    <p class="text-sm text-on-surface-variant">A pesquisa utiliza o algoritmo KMP (Knuth-Morris-Pratt) para busca de subpalavras em toda a documentação sem chamadas de rede externas.</p>
                </section>
                <section class="hud-border bg-surface-container rounded-none p-lg">
                    <h2 class="font-label-caps text-label-caps text-primary-container mb-md flex items-center gap-sm"><span class="material-symbols-outlined text-[16px]">translate</span> Tradução Integral</h2>
                    <p class="text-sm text-on-surface-variant">Toda a documentação do manual, casos de aplicação prática e descrições de parâmetros foram enriquecidas e traduzidas para PT-BR.</p>
                </section>
            </div>
        `;
    }

    function showTypes() {
        setActiveNav('nav-types');
        let html = `
            <div class="mb-xl border-b border-outline-variant pb-md">
                <div class="flex items-center gap-sm mb-sm">
                    <span class="bg-primary-container/10 text-primary-container border border-primary-container/30 px-sm py-xs font-label-caps text-label-caps rounded-none">SYS.TYPES</span>
                </div>
                <h1 class="font-headline-xl text-[48px] font-bold text-on-background">Tipos MPI (MPI Types)</h1>
                <p class="mt-sm text-on-surface-variant font-body-md">Referência estruturada para os principais tipos de dados e abstrações do MPI.</p>
            </div>
            <div class="space-y-lg mb-xl">
        `;
        
        types.forEach(category => {
            html += `
            <section class="hud-border bg-surface-container rounded-none flex flex-col">
                <div class="stripe-bg border-b border-outline-variant p-md">
                    <h2 class="font-label-caps text-label-caps text-primary-container flex items-center gap-sm">
                        <span class="material-symbols-outlined text-[16px]">data_object</span> ${escapeHTML(category.category)}
                    </h2>
                </div>
                <div class="p-lg flex-1">
                    <ul class="space-y-sm">
            `;
            category.types.forEach(type => {
                html += `
                        <li id="type-${escapeHTML(type.name).replace(/[^a-zA-Z0-9]/g,'-')}" class="flex flex-col border-b border-outline-variant/50 pb-sm">
                            <code class="font-code-sm text-code-sm text-primary-fixed">${escapeHTML(type.name)}</code>
                            <span class="text-on-surface-variant text-sm mt-xs">${escapeHTML(type.desc)}</span>
                        </li>
                `;
            });
            html += `</ul></div></section>`;
        });
        
        html += `</div>`;
        document.getElementById('main-content').innerHTML = html;
        document.getElementById('main-content').scrollTo(0,0);
    }

    function showApiReference() {
        setActiveNav('nav-api');
        document.getElementById('search-input').value = '';
        renderSearchList(allFuncItems);
        
        const groups = {};
        funcs.forEach(f => {
            const letter = f.name.replace(/^MPI_/, '')[0].toUpperCase();
            if (!groups[letter]) groups[letter] = [];
            groups[letter].push(f);
        });

        const letters = Object.keys(groups).sort();
        let quicklinks = '<div class="flex flex-wrap gap-xs mb-lg border-b border-outline-variant pb-md">';
        letters.forEach(l => {
            quicklinks += `<a href="#group-${l}" class="px-sm py-xs border border-outline-variant hover:border-primary-container hover:text-primary-container text-xs font-code-sm transition-all">${l}</a>`;
        });
        quicklinks += '</div>';

        let html = `
            <div class="mb-xl border-b border-outline-variant pb-md">
                <div class="flex items-center gap-sm mb-sm">
                    <span class="bg-primary-container/10 text-primary-container border border-primary-container/30 px-sm py-xs font-label-caps text-label-caps rounded-none">API.REF</span>
                </div>
                <h1 class="font-headline-xl text-[48px] font-bold text-on-background">Referência da API Open MPI</h1>
                <p class="mt-sm text-on-surface-variant font-body-md">Lista completa de funções disponíveis para programação paralela de alta performance.</p>
            </div>
            
            ${quicklinks}
            
            <div class="space-y-xl">
        `;

        letters.forEach(letter => {
            html += `
                <section id="group-${letter}" class="hud-border bg-surface-container rounded-none flex flex-col">
                    <div class="stripe-bg border-b border-outline-variant p-md">
                        <h2 class="font-label-caps text-label-caps text-primary-container text-[18px] font-bold">${letter}</h2>
                    </div>
                    <div class="p-lg grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-md">
            `;
            groups[letter].forEach(f => {
                html += `
                    <div onclick="showDetail('${escapeHTML(f.name)}'); selectSidebarItem('${escapeHTML(f.name)}');" class="p-md border border-outline-variant hover:border-primary-container bg-surface-container-low/50 hover:bg-surface-container-high transition-all cursor-pointer flex flex-col gap-xs">
                        <code class="font-code-sm text-code-sm text-primary-fixed truncate block">${escapeHTML(f.name)}</code>
                        <span class="text-xs text-on-surface-variant line-clamp-2">${escapeHTML(f.short_desc)}</span>
                    </div>
                `;
            });
            html += `
                    </div>
                </section>
            `;
        });

        html += `</div>`;
        document.getElementById('main-content').innerHTML = html;
        document.getElementById('main-content').scrollTo(0,0);
    }

    function showDetail(name) {
        setActiveNav('nav-api');
        const func = findFunc(name);
        if (!func) return;

        let paramsHtml = '';
        if (func.params && func.params.length > 0) {
            paramsHtml = func.params.map(p => `
                <li class="flex flex-col border-b border-outline-variant/50 pb-sm">
                    <code class="font-code-sm text-code-sm text-secondary">${escapeHTML(p.name)}</code>
                    <span class="text-on-surface-variant text-sm mt-xs">${escapeHTML(p.desc)}</span>
                </li>
            `).join('');
        } else {
            paramsHtml = `<li class="text-outline text-sm italic">Parâmetros vazios ou não especificados.</li>`;
        }

        document.getElementById('main-content').innerHTML = `
            <div class="mb-xl flex items-center justify-between border-b border-outline-variant pb-md">
                <div>
                    <div class="flex items-center gap-sm mb-sm">
                        <span class="bg-primary-container/10 text-primary-container border border-primary-container/30 px-sm py-xs font-label-caps text-label-caps rounded-none">API.REF</span>
                        <span class="text-outline font-code-sm text-code-sm">SYSTEM.READY</span>
                    </div>
                    <h1 class="font-headline-xl text-[48px] leading-[1.1] tracking-[-0.02em] font-bold text-on-background break-words">${escapeHTML(func.name)}</h1>
                    <p class="mt-sm text-on-surface-variant font-body-md text-body-md">${escapeHTML(func.short_desc)}</p>
                </div>
            </div>

            <!-- Parâmetros -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-lg mb-xl">
                <section class="hud-border bg-surface-container rounded-none flex flex-col">
                    <div class="stripe-bg border-b border-outline-variant p-md">
                        <h2 class="font-label-caps text-label-caps text-primary-container flex items-center gap-sm">
                            <span class="material-symbols-outlined text-[16px]">data_object</span> Parâmetros
                        </h2>
                    </div>
                    <div class="p-lg flex-1">
                        <ul class="space-y-sm">
                            ${paramsHtml}
                        </ul>
                    </div>
                </section>

                <div class="flex flex-col gap-lg">
                    <!-- Contexto -->
                    <section class="hud-border bg-surface-container rounded-none">
                        <div class="border-b border-outline-variant p-md bg-[#1a2027]/50">
                            <h2 class="font-label-caps text-label-caps text-primary-container flex items-center gap-sm">
                                <span class="material-symbols-outlined text-[16px]">info</span> Aplicação Prática
                            </h2>
                        </div>
                        <div class="p-lg space-y-md">
                            <p class="text-on-surface-variant text-sm whitespace-pre-wrap">${escapeHTML(func.application || 'Aplicação geral MPI.')}</p>
                        </div>
                    </section>
                </div>
            </div>

            <!-- Sinopse -->
            <section class="mb-xl">
                <h2 class="font-headline-lg-mobile md:font-headline-lg text-on-background mb-md">Sinopse (C)</h2>
                <div class="hud-border bg-[#020408] rounded-none">
                    <div class="flex items-center px-md py-sm border-b border-[#1e293b] bg-[#0a1420]">
                        <div class="flex gap-2 mr-md">
                            <div class="w-3 h-3 rounded-full bg-[#3a494b]"></div>
                            <div class="w-3 h-3 rounded-full bg-[#3a494b]"></div>
                            <div class="w-3 h-3 rounded-full bg-[#3a494b]"></div>
                        </div>
                        <span class="font-code-sm text-code-sm text-outline text-[12px]">header.h</span>
                    </div>
                    <div class="p-lg overflow-x-auto">
                        <pre class="font-code-sm text-code-sm leading-relaxed"><code class="code-syntax">${highlightSyntax(func.synopsis)}</code></pre>
                    </div>
                </div>
            </section>

            <!-- Descrição Completa -->
            <section class="mb-xl">
                <h2 class="font-headline-lg-mobile md:font-headline-lg text-on-background mb-md">Descrição Detalhada</h2>
                <div class="hud-border bg-surface-container p-lg text-on-surface-variant font-body-md text-sm leading-relaxed whitespace-pre-wrap">${escapeHTML(func.description)}</div>
            </section>

            ${func.example ? `
            <section class="mb-xl">
                <h2 class="font-headline-lg-mobile md:font-headline-lg text-on-background mb-md flex items-center gap-sm">Exemplo em C</h2>
                <div class="hud-border bg-[#020408] rounded-none">
                    <div class="flex items-center px-md py-sm border-b border-[#1e293b] bg-[#0a1420]">
                        <div class="flex gap-2 mr-md">
                            <div class="w-3 h-3 rounded-full bg-[#3a494b]"></div>
                            <div class="w-3 h-3 rounded-full bg-[#3a494b]"></div>
                            <div class="w-3 h-3 rounded-full bg-[#3a494b]"></div>
                        </div>
                        <span class="font-code-sm text-code-sm text-outline text-[12px]">example.c</span>
                    </div>
                    <div class="p-lg overflow-x-auto">
                        <pre class="font-code-sm text-code-sm leading-relaxed"><code class="code-syntax">${highlightSyntax(func.example)}</code></pre>
                    </div>
                </div>
            </section>` : ''}
        `;
        document.getElementById('main-content').scrollTo(0,0);
    }

    function toggleSidebar(isOpen) {
        const sidebar = document.getElementById('sidebar');
        const overlay = document.getElementById('sidebar-overlay');
        if (!sidebar || !overlay) return;
        if (isOpen) {
            sidebar.classList.remove('-translate-x-full');
            sidebar.classList.add('translate-x-0');
            overlay.classList.remove('hidden');
        } else {
            sidebar.classList.remove('translate-x-0');
            sidebar.classList.add('-translate-x-full');
            overlay.classList.add('hidden');
        }
    }

    const searchHandler = (e) => {
        const q = e.target.value;
        const otherSearch = e.target.id === 'search-input' ? document.getElementById('search-input-mobile') : document.getElementById('search-input');
        if (otherSearch) otherSearch.value = q;
        renderSearchList(q ? searchAll(q) : allFuncItems);
    };

    document.getElementById('search-input').oninput = searchHandler;
    const mobileSearch = document.getElementById('search-input-mobile');
    if (mobileSearch) mobileSearch.oninput = searchHandler;

    renderSearchList(allFuncItems);
    showWelcome();
</script>
<footer class="fixed bottom-0 left-0 right-0 z-40 bg-surface-container-low/95 backdrop-blur-md border-t border-outline-variant/30 py-1.5 text-center select-none pointer-events-auto font-code-sm text-[11px] text-on-surface-variant flex items-center justify-center gap-xs">
    <span class="w-1.5 h-1.5 rounded-full bg-[#00f2ff] animate-pulse"></span>
    <span>Made with 💜 by <a href="https://github.com/grejc" target="_blank" rel="noopener noreferrer" class="text-primary-container hover:text-secondary-container hover:underline font-bold transition-colors">@grejc</a></span>
</footer>
</body>
</html>"""
html = html.replace('FUNC_DATA_PLACEHOLDER', funcs_js)
html = html.replace('TYPES_DATA_PLACEHOLDER', types_js)

with open('index.html', 'w') as f:
    f.write(html)
