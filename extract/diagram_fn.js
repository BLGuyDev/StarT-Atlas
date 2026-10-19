function diagram(ch){
  const N=ch.n.map(([id,l,t,ic])=>({id,l,t,ic,lines:wrap(l,17)})),by=Object.fromEntries(N.map(n=>[n.id,n]));
  const E=ch.e.filter(e=>by[e[0]]&&by[e[1]]).map(([a,b,l])=>({a,b,l:l==null?'':String(l)})); N.forEach(n=>n.r=0);
  for(let k=0;k<N.length;k++)E.forEach(e=>{if(by[e.b].r<by[e.a].r+1)by[e.b].r=Math.min(by[e.a].r+1,N.length)});
  const cols=[];N.forEach(n=>(cols[n.r]=cols[n.r]||[]).push(n));
  const W=122,H=84,GY=14,LW=l=>l.length*6.4+12;
  const maxL=Math.max(0,...E.map(e=>e.l?LW(e.l):0)),GX=Math.max(64,maxL+30);
  const maxN=Math.max(...cols.map(c=>c.length)),TH=maxN*(H+GY)-GY;
  const place=col=>{const h=col.length*(H+GY)-GY;col.forEach((n,i)=>n.y=(TH-h)/2+i*(H+GY))};
  cols.forEach(place);
  for(let p=0;p<2;p++)cols.forEach((col,ci)=>{if(!ci)return;col.forEach(n=>{const ps=E.filter(e=>e.b===n.id).map(e=>by[e.a].y);n.k=ps.length?ps.reduce((a,b)=>a+b)/ps.length:n.y});col.sort((a,b)=>a.k-b.k);place(col)});
  cols.forEach((col,ci)=>col.forEach(n=>n.x=ci*(W+GX)));
  /* spread ports so arrows never share an endpoint */
  N.forEach(n=>{
    const ins=E.filter(e=>e.b===n.id).sort((p,q)=>by[p.a].y-by[q.a].y);
    ins.forEach((e,i)=>e.y2=n.y+H*(i+1)/(ins.length+1));
    const outs=E.filter(e=>e.a===n.id).sort((p,q)=>by[p.b].y-by[q.b].y);
    outs.forEach((e,i)=>e.y1=n.y+H*(i+1)/(outs.length+1));
  });
  const HH=Math.max(...N.map(n=>n.y+H))+4,WW=cols.length*(W+GX)-GX+4;
  let s=`<svg viewBox="-2 -2 ${WW} ${HH}" width="${WW}" style="max-width:none;height:auto" role="img" aria-label="${esc(ch.t)}"><defs><marker id="ar" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L8 4L0 8z" fill="var(--muted)"/></marker></defs>`;
  const placed=[];let labels='';
  const hit=(r)=>placed.some(o=>r.x<o.x+o.w+4&&r.x+r.w+4>o.x&&r.y<o.y+o.h+2&&r.y+r.h+2>o.y)||N.some(n=>r.x<n.x+W&&r.x+r.w>n.x&&r.y<n.y+H&&r.y+r.h>n.y);
  E.forEach(e=>{const A=by[e.a],B=by[e.b];const x1=A.x+W,y1=e.y1,x2=B.x,y2=e.y2,mx=(x1+x2)/2;
    s+=`<path d="M${x1} ${y1}C${mx} ${y1} ${mx} ${y2} ${x2-2} ${y2}" fill="none" stroke="var(--muted)" stroke-opacity=".7" stroke-width="1.4" marker-end="url(#ar)"/>`;
    if(!e.l)return;
    const w=LW(e.l),h=17,bz=t=>{const u=1-t;return [u*u*u*x1+3*u*u*t*mx+3*u*t*t*mx+t*t*t*x2,u*u*u*y1+3*u*u*t*y1+3*u*t*t*y2+t*t*t*y2]};
    let best=null;
    for(const t of [.5,.38,.62,.28,.72,.18,.82]){const [px,py]=bz(t);const r={x:px-w/2,y:py-h/2,w,h};if(!hit(r)){best=r;break}}
    if(!best){const [px,py]=bz(.5);best={x:px-w/2,y:py-h/2,w,h};for(let dy=1;dy<12&&hit(best);dy++)best={...best,y:py-h/2+(dy%2?1:-1)*Math.ceil(dy/2)*(h+2)}}
    placed.push(best);
    labels+=`<rect x="${best.x}" y="${best.y}" width="${w}" height="${h}" rx="3" fill="var(--bg)" stroke="var(--line)"/><text x="${best.x+w/2}" y="${best.y+12.5}" text-anchor="middle" font-size="10.5" font-family="IBM Plex Mono,monospace" fill="var(--fg)">${esc(e.l)}</text>`});
  N.forEach(n=>{const st=NT[n.t]||NT.x;const fg=n.t==='m'?'var(--node-m-fg)':'var(--fg)';
    s+=`<g><title>${esc(n.l)}</title><rect x="${n.x}" y="${n.y}" width="${W}" height="${H}" rx="6" fill="${st[0]}" stroke="${st[1]}" stroke-width="${st[3]}" stroke-dasharray="${st[2]}"/>`;
    if(n.t==='m')s+=`<rect x="${n.x+W/2-22}" y="${n.y+6}" width="44" height="44" rx="5" fill="var(--panel)"/>`;
    s+=svgIcon(n.ic,n.x+W/2-20,n.y+8,40);
    n.lines.forEach((ln,i)=>s+=`<text x="${n.x+W/2}" y="${n.y+62+i*12.5}" text-anchor="middle" font-size="11" font-family="IBM Plex Sans,sans-serif" font-weight="${n.t==='m'?600:500}" fill="${fg}">${esc(ln)}</text>`);
    if(n.t==='s')s+=`<text x="${n.x+W-7}" y="${n.y+15}" text-anchor="end" font-size="14" font-weight="700" fill="var(--ok)">&#8734;</text>`;
    s+='</g>'});
  return s+labels+'</svg>'}
