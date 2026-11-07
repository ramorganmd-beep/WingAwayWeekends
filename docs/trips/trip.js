// WingAway Weekends multi-stop trip planner (prototype). Each trip page sets window.TRIP before loading this file.
(function(){
// Route config comes from the page: window.TRIP = {id, route:[[slug, nights, [alternatives]]], regions:[...], season:{slug:[months]}, defaultSeason:[months]}
const T=window.TRIP;const ROUTE=T.route;
const SEASON=T.season||{};const DEF=T.defaultSeason||[5,6,7,8,9,10];
const MON=['January','February','March','April','May','June','July','August','September','October','November','December'];
const ALL=(window.WINGAWAY_DESTINATIONS||[]).filter(d=>d.guide&&!d.draft&&isFinite(d.lat));
const BY={};ALL.forEach(d=>BY[d.guide.replace(/\/$/,'')]=d);
const NE=ALL.filter(d=>T.regions.includes(d.region));
const AP=window.WINGAWAY_AIRPORTS||[];const APX=new Map();AP.forEach(a=>{APX.set(a[0],a);if(a[1])APX.set(a[1],a)});
const A=window.WingAwayAircraft;const FUEL=window.WINGAWAY_FUEL||[];
const $=id=>document.getElementById(id);
let stops=[],home=null;
const R=3440.065,rad=x=>x*Math.PI/180;
function nm(a,b){const h=Math.sin(rad(b.lat-a.lat)/2)**2+Math.cos(rad(a.lat))*Math.cos(rad(b.lat))*Math.sin(rad(b.lon-a.lon)/2)**2;return 2*R*Math.asin(Math.sqrt(h));}
function esc(s){return String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}
function season(slug){return SEASON[slug]||DEF;}
function lookup(code){code=(code||'').trim().toUpperCase();const a=APX.get(code)||APX.get('K'+code);return a?{code:a[0],name:a[2],city:a[3]+', '+a[4],lat:+a[5],lon:+a[6]}:null;}
function profile(){const v=$('ac').value;if(v==='saved')return A.load();if(v==='default')return null;return A.PRESETS.find(p=>p.id===v)||null;}
function fmtDate(d){return d.toLocaleDateString('en-US',{weekday:'short',month:'short',day:'numeric'});}
function addDays(d,n){const x=new Date(d);x.setDate(x.getDate()+n);return x;}
function ymd(d){return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');}
// Pick a fuel stop from FAA data: an airport with the right fuel, both sub-legs within range, as balanced and direct as possible.
function fuelStop(a,b,p){const jet=p&&/jet a|tbm|turbine/i.test(p.label),need=jet?2:1,d=nm(a,b);let best=null,bs=1e9,far=null,fs=-1;
  for(const f of FUEL){if(!(f[6]&need))continue;const c={lat:f[4],lon:f[5]};const d1=nm(a,c),d2=nm(c,b);if(d1<20||d2<20||d1+d2>d*1.15)continue;
    const ok1=!A.estimate(d1,p).stop;if(!ok1)continue;
    if(!A.estimate(d2,p).stop){const s=Math.max(d1,d2)+(d1+d2-d)*2-(f[7]>=4000?15:0);if(s<bs){bs=s;best=f;}}
    else{const prog=d-d2;if(prog>fs){fs=prog;far=f;}}}
  return best?{f:best,one:true}:(far?{f:far,one:false}:null);}
function fuelText(r){const f=r.f;return esc(f[0])+' ('+esc(f[1])+', '+esc(f[2])+', '+esc(f[3])+') · '+(f[6]===3?'100LL and Jet A':f[6]===1?'100LL':'Jet A')+' · '+f[7].toLocaleString()+'-ft runway';}
function startHome(){return $('mode').value!=='stop';}
// State in the URL so a trip can be shared.
function fromURL(){const q=new URLSearchParams(location.search);const s=q.get('stops');
  if(s){const out=[];s.split(',').forEach(t=>{const [slug,n]=t.split(':');const r=ROUTE.find(x=>x[0]===slug||x[2].includes(slug));if(BY[slug])out.push({slug,nights:Math.min(4,Math.max(1,+n||1)),alts:r?[r[0],...r[2]].filter(x=>x!==slug):[]});});if(out.length)stops=out;}
  if(q.get('home'))$('home').value=q.get('home');if(q.get('start'))$('start').value=q.get('start');if(q.get('ac')&&[...$('ac').options].some(o=>o.value===q.get('ac')))$('ac').value=q.get('ac');if(q.get('pace'))$('pace').value=q.get('pace');if(q.get('from')==='stop')$('mode').value='stop';}
function toURL(){const q=new URLSearchParams();q.set('stops',stops.map(s=>s.slug+':'+s.nights).join(','));if(home)q.set('home',home.code);if($('start').value)q.set('start',$('start').value);q.set('ac',$('ac').value);q.set('pace',$('pace').value);if(!startHome())q.set('from','stop');history.replaceState(null,'','?'+q.toString());return location.href;}
function defaults(){stops=ROUTE.map(([slug,n,alts])=>({slug,nights:n,alts:alts.filter(a=>BY[a])}));}
function legs(){const S=stops.map(s=>BY[s.slug]);const pts=startHome()?[home,...S,home]:S;const p=profile(),pace=+$('pace').value;const out=[];
  for(let i=0;i<pts.length-1;i++){const a=pts[i],b=pts[i+1];const d=nm(a,b);const e=A.estimate(d,p);out.push({d,e,long:e.hours>pace,a,b});}return out;}
function draw(){
  home=lookup($('home').value)||lookup('KMYR');
  const L=legs(),start=$('start').value?new Date($('start').value+'T12:00:00'):addDays(new Date(),7);
  const nights=stops.reduce((s,x)=>s+x.nights,0),totNm=L.reduce((s,l)=>s+l.d,0),totH=L.reduce((s,l)=>s+l.e.hours,0),fuel=L.filter(l=>l.e.stop).length;
  $('sum').innerHTML='<span><b>'+nights+'</b> nights · <b>'+stops.length+'</b> stops</span><span><b>'+Math.round(totNm).toLocaleString()+'</b> nm total</span><span>About <b>'+A.formatTime(totH)+'</b> flying</span><span><b>'+fuel+'</b> leg'+(fuel===1?'':'s')+' likely need'+(fuel===1?'s':'')+' a fuel stop</span><span>'+esc(A.summary(profile()))+'</span>';
  const H=startHome();let day=start,html=H?'<li class="tp-home">Day 1 · '+fmtDate(day)+': depart '+esc(home.code)+' ('+esc(home.city)+')</li>':'<li class="tp-home">Day 1 · '+fmtDate(day)+': trip starts at '+esc(BY[stops[0].slug].name)+' ('+esc(BY[stops[0].slug].airport)+')</li>';
  stops.forEach((s,i)=>{const d=BY[s.slug],l=H?L[i]:L[i-1];
    if(l)html+=legHTML(l);
    const arrive=day,leave=addDays(day,s.nights),m=arrive.getMonth()+1,ok=season(s.slug).includes(m);
    const img=d.photo&&d.photo.remote?d.photo.remote+'&w=400&h=300&fit=crop&q=75':d.photo?'../../assets/destinations/'+d.photo.slug+'-480.jpg':'';
    const opts=[s.slug,...s.alts].map(x=>'<option value="'+x+'"'+(x===s.slug?' selected':'')+'>'+esc(BY[x].name)+' ('+esc(BY[x].airport)+')</option>').join('');
    html+='<li class="tp-stop"><img src="'+img+'" alt="'+esc(d.photo?d.photo.alt:'')+'" loading="lazy"><div><span class="when">Stop '+(i+1)+' · '+fmtDate(arrive)+' – '+fmtDate(leave)+'</span><h3><a href="../../'+d.guide+'">'+esc(d.name)+'</a></h3><p>'+esc(d.desc||'')+'</p>'+
      (ok?'':'<p class="tp-warn">Heads up: '+MON[m-1]+' is outside the usual season here. Check what’s open.</p>')+
      '<div class="tp-ctl"><label>Stop <select data-swap="'+i+'">'+opts+'</select></label><label>Nights <select data-n="'+i+'">'+[1,2,3,4].map(n=>'<option'+(n===s.nights?' selected':'')+'>'+n+'</option>').join('')+'</select></label>'+(stops.length>2?'<button data-rm="'+i+'">Remove stop</button>':'')+'<a href="../../'+d.guide+'">Open the guide</a><a href="'+s22(d,arrive,leave)+'" target="_blank" rel="sponsored noopener">Compare hotels for these dates →</a></div></div></li>';
    html+=addHTML(i);
    day=leave;});
  if(H){html+=legHTML(L[L.length-1]);html+='<li class="tp-home">Day '+(nights+1)+' · '+fmtDate(day)+': home to '+esc(home.code)+'</li>';}
  else html+='<li class="tp-home">Day '+(nights+1)+' · '+fmtDate(day)+': trip ends at '+esc(BY[stops[stops.length-1].slug].name)+'</li>';
  $('days').innerHTML=html;
  drawMap(L);toURL();
}
function legHTML(l){const p=profile();let w='';
  if(l.e.stop){const r=fuelStop(l.a,l.b,p);w+=' <span class="tp-warn">'+(r?(r.one?'Fuel stop needed. Suggested: ':'Needs more than one fuel stop. First suggestion: ')+fuelText(r)+'. Confirm fuel and hours before you go.':'Likely fuel stop; no suitable fuel airport found along the route.')+'</span>';}
  else if(!p)w+=' <span>Set an aircraft to check fuel.</span>';
  if(l.long)w+=' <span class="tp-warn">Longer than your daily limit; plan an overnight on the way'+((l.a===home||l.b===home)?', or set “Trip starts” to the first stop':'')+'.</span>';
  return '<li class="tp-leg"><span aria-hidden="true">✈</span><span><b>'+esc(l.a.code||l.a.airport)+' → '+esc(l.b.code||l.b.airport)+'</b> · '+Math.round(l.d)+' nm · about '+A.formatTime(l.e.hours)+(l.e.gal?' · '+Math.round(l.e.gal)+' gal':'')+w+'</span></li>';}
function s22(d,a,b){const q=new URLSearchParams({aid:'wingawayweekend',lat:d.lat,lng:d.lon,address:d.name.replace(/ & .*|,.*/,'')+', '+d.state,checkin:ymd(a),checkout:ymd(b),campaign:'trip-'+T.id});return 'https://www.stay22.com/allez/roam?'+q.toString();}
function addHTML(i){const from=BY[stops[i].slug],used=new Set(stops.map(s=>s.slug));
  const near=NE.filter(d=>!used.has(d.guide.replace(/\/$/,''))).map(d=>[d,nm(from,d)]).sort((a,b)=>a[1]-b[1]).slice(0,10);
  return '<li class="tp-add"><label>Add a stop after '+esc(from.name)+': <select data-add="'+i+'"><option value="">Choose…</option>'+near.map(([d,n])=>'<option value="'+d.guide.replace(/\/$/,'')+'">'+esc(d.name)+' · '+Math.round(n)+' nm</option>').join('')+'</select></label></li>';}
let states=null;
function drawMap(L){if(!states)return;const svg=d3.select('#m');svg.selectAll('*').remove();
  const H=startHome();const pts=H?[home,...stops.map(s=>BY[s.slug])]:stops.map(s=>BY[s.slug]);
  const fc={type:'FeatureCollection',features:pts.map(p=>({type:'Feature',geometry:{type:'Point',coordinates:[p.lon,p.lat]}}))};
  const lo=d3.extent(pts,p=>p.lon),la=d3.extent(pts,p=>p.lat);const proj=d3.geoConicConformal().parallels([la[0],la[1]+0.01]).rotate([-(lo[0]+lo[1])/2,0]).fitExtent([[40,40],[860,580]],fc);const path=d3.geoPath(proj);
  svg.append('g').selectAll('path').data(states).join('path').attr('class','st').attr('d',path);
  const g=svg.append('g');
  L.forEach(l=>g.append('path').attr('class','leg').attr('d',path({type:'LineString',coordinates:[[l.a.lon,l.a.lat],[l.b.lon,l.b.lat]]})));
  if(H){const hp=proj([home.lon,home.lat]);g.append('circle').attr('class','home').attr('cx',hp[0]).attr('cy',hp[1]).attr('r',9);g.append('text').attr('x',hp[0]).attr('y',hp[1]+4).attr('text-anchor','middle').text('H');}
  stops.forEach((s,i)=>{const d=BY[s.slug],p=proj([d.lon,d.lat]);g.append('circle').attr('class','stop').attr('cx',p[0]).attr('cy',p[1]).attr('r',10);
    g.append('text').attr('x',p[0]).attr('y',p[1]+4).attr('text-anchor','middle').text(i+1);
    const crowd=stops.some((o,j)=>{if(j===i)return false;const q=proj([BY[o.slug].lon,BY[o.slug].lat]);return q[0]>p[0]&&q[0]-p[0]<120&&Math.abs(q[1]-p[1])<16;});
    g.append('text').attr('class','nm').attr('x',crowd?p[0]-14:p[0]+14).attr('y',p[1]+4).attr('text-anchor',crowd?'end':'start').text(d.name.replace(/ & .*|,.*/,''));});
}
// Controls
const acSel=$('ac');const saved=A.load();
acSel.innerHTML=(saved?'<option value="saved">My aircraft: '+esc(saved.label)+'</option>':'')+'<option value="default">Default (150 kt, no fuel check)</option>'+A.PRESETS.filter(p=>p.gear==='land').map(p=>'<option value="'+p.id+'">'+esc(p.label)+'</option>').join('');
acSel.value=saved?'saved':'pa28';
let hc='';try{hc=localStorage.getItem('wingaway-home')||''}catch(e){}$('home').value=hc||'KMYR';
if(window.WingAwaySuggest)WingAwaySuggest($('home'),$('home-list'),AP);
(function(){let d=addDays(new Date(),7);for(let k=0;k<400&&!DEF.includes(d.getMonth()+1);k++)d=addDays(d,1);while(d.getDay()!==5)d=addDays(d,1);$('start').value=ymd(d);})();
defaults();fromURL();
['home','start','ac','pace','mode'].forEach(id=>$(id).addEventListener('change',draw));
$('days').addEventListener('change',e=>{const t=e.target;
  if(t.dataset.swap!=null){const i=+t.dataset.swap,old=stops[i].slug;stops[i].alts=[old,...stops[i].alts].filter(x=>x!==t.value);stops[i].slug=t.value;}
  else if(t.dataset.n!=null)stops[+t.dataset.n].nights=+t.value;
  else if(t.dataset.add!=null&&t.value){const i=+t.dataset.add,from=BY[stops[i].slug];const alts=NE.filter(d=>d.guide!==t.value+'/').map(d=>[d.guide.replace(/\/$/,''),nm(BY[t.value],d)]).sort((a,b)=>a[1]-b[1]).slice(1,5).map(x=>x[0]);stops.splice(i+1,0,{slug:t.value,nights:1,alts});}
  draw();});
$('days').addEventListener('click',e=>{const t=e.target;if(t.dataset.rm!=null){stops.splice(+t.dataset.rm,1);draw();}});
function say(m){$('msg').textContent=m;setTimeout(()=>{if($('msg').textContent===m)$('msg').textContent='';},4000);}
function copy(t,m){(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(()=>say(m),()=>{prompt('Copy this:',t);});}
$('share').onclick=()=>copy(toURL(),'Trip link copied.');
$('ff').onclick=()=>copy((startHome()?[home.code,...stops.map(s=>BY[s.slug].airport),home.code]:stops.map(s=>BY[s.slug].airport)).join(' '),'Route copied. Paste it into ForeFlight’s route field.');
$('print').onclick=()=>window.print();
$('reset').onclick=()=>{defaults();draw();};
$('ics').onclick=()=>{const start=new Date($('start').value+'T12:00:00');let day=start;const ev=[],stamp=new Date().toISOString().replace(/[-:]/g,'').slice(0,15)+'Z';
  const f=d=>ymd(d).replace(/-/g,'');
  stops.forEach((s,i)=>{const d=BY[s.slug],out=addDays(day,s.nights);
    ev.push('BEGIN:VEVENT\r\nUID:wingaway-'+f(day)+'-'+s.slug+'@wingawayweekends.com\r\nDTSTAMP:'+stamp+'\r\nDTSTART;VALUE=DATE:'+f(day)+'\r\nDTEND;VALUE=DATE:'+f(out)+'\r\nSUMMARY:'+d.name.replace(/[,;]/g,' ')+' ('+d.airport+')\r\nDESCRIPTION:WingAway Weekends guide: https://wingawayweekends.com/'+d.guide+'\r\nEND:VEVENT');day=out;});
  const blob=new Blob(['BEGIN:VCALENDAR\r\nVERSION:2.0\r\nPRODID:-//WingAway Weekends//Trip//EN\r\n'+ev.join('\r\n')+'\r\nEND:VCALENDAR\r\n'],{type:'text/calendar'});
  const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='wingaway-'+T.id+'-trip.ics';document.body.appendChild(a);a.click();a.remove();say('Calendar file downloaded.');};
d3.json('../../map/states-10m.json').then(us=>{states=topojson.feature(us,us.objects.states).features;draw();});
draw();
})();
