import os, sys
ROOT = sys.argv[1]

FLAME = '<path d="M60 4c6 9 15 15 15 27 0 9-7 15-15 15s-15-6-15-15c0-6 3-10 6-13 0 5 3 8 6 8-3-8 0-16 3-22z" fill="currentColor"/>'
LOGO = ('<svg viewBox="0 0 120 92" role="img" aria-label="Hearth"><g transform="translate(0,0) scale(.62) translate(36,0)">' + FLAME +
        '</g><text x="60" y="66" text-anchor="middle" font-family="DM Serif Display, Georgia, serif" font-size="30" fill="currentColor">Hearth</text>'
        '<line x1="30" y1="76" x2="90" y2="76" stroke="currentColor" stroke-width="1.4"/></svg>')
SEAL = ('<svg class="seal" viewBox="0 0 120 120" aria-hidden="true"><defs><path id="ring" d="M60 60m-40 0a40 40 0 1 1 80 0a40 40 0 1 1-80 0"/></defs>'
        '<circle cx="60" cy="60" r="56" fill="#914117"/><circle cx="60" cy="60" r="49" fill="none" stroke="#F4EDE4" stroke-opacity=".55" stroke-width="1.2"/>'
        '<text font-family="Figtree, sans-serif" font-size="9.5" letter-spacing="3" fill="#F4EDE4"><textPath href="#ring" textLength="244" lengthAdjust="spacing">HEARTH · KITCHEN CO · TULSA METRO ·</textPath></text>'
        '<g transform="translate(43,36) scale(.58)" style="color:#F4EDE4">' + FLAME + '</g></svg>')
SPRIG = ('<svg class="sprig" viewBox="0 0 200 40" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round">'
         '<path d="M10 22 C60 18 140 18 190 22"/><path d="M50 20c-6-10 2-16 10-14-2 8-5 12-10 14z"/><path d="M80 19c6-10 16-9 20-4-8 4-14 5-20 4z"/>'
         '<path d="M110 20c-4-11 5-15 12-12-3 8-7 11-12 12z"/><path d="M140 20c7-8 16-6 19 0-8 3-14 3-19 0z"/><path d="M68 21c-5 9-12 10-17 5 6-4 11-5 17-5z"/>'
         '<path d="M126 21c4 9 12 11 17 6-6-4-11-6-17-6z"/><circle cx="170" cy="19" r="3"/><circle cx="30" cy="22" r="2.5"/></svg>')

NAV = [("index.html", "Home"), ("story.html", "My Story"), ("thanksgiving.html", "Thanksgiving"), ("contact.html", "Contact"), ("pay.html", "Pay Invoice")]
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Figtree:wght@400;500;600&family=Pinyon+Script&display=swap">')
LD = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"FoodEstablishment","name":"Hearth Kitchen Co.",'
      '"legalName":"Hearth Kitchen Co., LLC","description":"Personal chef and in-home meal preparation serving the Tulsa Metro area.",'
      '"telephone":"+1-918-968-5002","email":"jordansrowlan@gmail.com","founder":{"@type":"Person","name":"Jordan Rowlan","jobTitle":"Owner and Chef"},'
      '"areaServed":{"@type":"Place","name":"Tulsa Metro area, Oklahoma"},"address":{"@type":"PostalAddress","addressLocality":"Broken Arrow","addressRegion":"OK","addressCountry":"US"},'
      '"servesCuisine":"Global, seasonal, home-cooked","slogan":"Nourishing your body starts with how you treat your food."}</script>')

def page(fname, title, desc, body, current, extra_js=""):
    cur = ' aria-current="page"'
    nav = "".join('<li><a href="%s"%s>%s</a></li>' % (h, cur if h == current else "", t) for h, t in NAV)
    ANNOUNCE = '<a class="announce" href="thanksgiving.html"><b>Thanksgiving pre-orders are open!</b> Order by Nov 14 &middot; See the menu &rarr;</a>\n' if fname == "index.html" else ""
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#914117">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="style.css">
{LD if fname == "index.html" else ""}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{ANNOUNCE}<div class="wrap">
<header class="site-head">
  <a class="brand" href="index.html" aria-label="Hearth Kitchen Co. home">{LOGO}</a>
  <nav class="site-nav" aria-label="Main"><ul>{nav}</ul></nav>
</header>
<main id="main">
{body}
</main>
</div>
<footer class="site-foot">
  <div class="wrap">
    <div class="tagline">Nourishing your body starts with how you treat your food.</div>
    <div>Serving the Tulsa Metro area</div>
    <div><a href="mailto:jordansrowlan@gmail.com">jordansrowlan@gmail.com</a> &middot; <a href="tel:+19189685002">918-968-5002</a></div>
    <div class="social" data-social></div>
    <small><a href="pay.html">Pay an invoice</a> &middot; <a href="policies.html">Policies</a> &middot; &copy; <span data-year>2026</span> Hearth Kitchen Co., LLC</small>
  </div>
</footer>
<script src="data.js"></script>
<script src="site.js"></script>
{extra_js}
</body>
</html>
'''
    open(os.path.join(ROOT, fname), "w").write(html)

# ---------------- Home (coming soon) ----------------
home = f'''
<section class="hero" aria-labelledby="hi">
  <div class="portrait">
    <img src="images/chef-jordan.jpg" width="900" height="1193" alt="Chef Jordan Rowlan of Hearth Kitchen Co., smiling in her Hearth chef coat." fetchpriority="high">
    {SEAL}
  </div>
  <div class="stack">
    <div class="label">Hearth Kitchen Co.</div>
    <h1 id="hi">Hi, I'm <span class="script">Chef Jordan</span>.</h1>
    <p class="tagline">Nourishing your body starts with how you treat your food.</p>
    <p class="lede">Personal chef and in-home meal preparation serving the Tulsa Metro area. Cuisine from around the world, tailored to your table.</p>
    <div class="ctas">
      <a class="btn" href="thanksgiving.html">Order Thanksgiving</a>
      <a class="btn ghost" href="contact.html">Get in touch</a>
    </div>
  </div>
</section>

<section class="feature" aria-labelledby="tg-feature">
  <div class="stack">
    <div class="label">Now taking orders</div>
    <h2 id="tg-feature">Thanksgiving, made for you.</h2>
    <p>Herb-roasted turkey, from-scratch sides and homemade pies, cooked in small batches and delivered to your door the day before Thanksgiving. Just reheat, gather and enjoy. Celebrating solo? There's a Thanksgiving Plate for One, too.</p>
    <p class="feature-dates"><b>Order by Saturday, Nov 14</b> &middot; <b>Delivered Wednesday, Nov 25</b> &middot; Free delivery across the Tulsa Metro area</p>
    <p><a class="btn" href="thanksgiving.html">See the Thanksgiving menu</a></p>
  </div>
</section>

{SPRIG}

<section aria-labelledby="help">
  <div class="stack" style="text-align:center;justify-items:center;margin-bottom:24px">
    <div class="label">How I can help</div>
    <h2 id="help">Let me bring the warmth back to your kitchen.</h2>
  </div>
  <div class="offer">
    <article class="card stack"><h3>Weekly meal prep</h3><p>Dinner's done, waiting in your fridge, labeled and ready.</p><p><a href="contact.html">Ask about it</a></p></article>
    <article class="card stack"><h3>Kitchen Reset</h3><p>A fresh start for your pantry and fridge, with glass containers to keep.</p><p><a href="contact.html">Ask about it</a></p></article>
    <article class="card stack"><h3>Dinners and gatherings</h3><p>Menus from around the world, built around your celebration.</p><p><a href="contact.html">Ask about it</a></p></article>
  </div>
</section>

<section class="dark stack" aria-labelledby="news">
  <div class="label">Stay close</div>
  <h2 id="news">Seasonal menus, first.</h2>
  <p>Join my list for holiday menus, new services and the occasional recipe. No more than a few emails a season.</p>
  <form class="inline-form" action="#" method="POST" data-formspree data-thanks="You're on the list. Thank you! With love, Jordan.">
    <label for="news-email" class="skip">Email</label>
    <input id="news-email" name="email" type="email" autocomplete="email" placeholder="Your email" required>
    <input type="hidden" name="_subject" value="New email signup">
    <input type="hidden" name="list" value="newsletter">
    <button class="btn" type="submit">Sign me up</button>
    <p class="formmsg" hidden role="status" style="flex-basis:100%"></p>
  </form>
</section>
'''
page("index.html", "Hearth Kitchen Co. | Chef Jordan, Tulsa Metro",
     "Personal chef and in-home meal preparation serving the Tulsa Metro area. Cuisine from around the world, tailored to your table.",
     home, "index.html", '<script src="form.js"></script>')

# ---------------- My Story ----------------
story = f'''
<section class="stack" style="padding-top:12px">
  <div class="prose">
    <div class="label">My Story</div>
    <h1>Food has always meant family to me.</h1>
    <p class="tagline" style="margin-top:-6px">I'm Jordan, but my friends and family call me Jordi.</p>
    <p>My love of cooking started at my grandparents' hamburger and ice cream restaurant, with an arcade upstairs. We'd grab breakfast there, go boating or swimming all day, then come back for a late lunch. My whole family would gather around those tables, and it felt like home. That's when I told my parents, "I'm going to be a cooker when I grow up."</p>
    <p>I built Hearth Kitchen Co. for two reasons: to feed people really, really well, and to show my daughter that you can be your own boss.</p>
    <p>Hospitality is in my bones. I earned my degree in Hotel and Restaurant Administration, with a minor in Entrepreneurship, at Oklahoma State University (Go Pokes!), then headed to Napa Valley for the Accelerated Culinary Arts Program at the Culinary Institute of America in St. Helena, California.</p>
    <p>From there I cooked classic French cuisine to Michelin standards on the line at Auberge du Soleil, then came home to Tulsa as sous chef at Southern Hills Country Club. I helped build seasonal menus around local ingredients and cooked for two major golf championships: the Masters, and the 2022 PGA Championship right here at Southern Hills. Along the way I earned my Introductory Sommelier Certificate and served on the Wine Forum of Oklahoma's culinary committee with Ree Drummond and Tiffany Poe.</p>
    <ul class="creds">
      <li>Culinary Institute of America</li><li>Oklahoma State University</li><li>Former sous chef, Southern Hills CC</li><li>Introductory Sommelier</li>
    </ul>
    {SPRIG}
    <p>I've spent years studying the food of many cultures, and I love bringing those flavors to your table, tailored to your family, a theme or a celebration.</p>
    <p>To me, food is love made visible. I believe the way we treat our food matters, from how it's grown, to how it's prepared, to the words we speak over it. <em>Nourishing your body starts with how you treat your food.</em></p>
    <p>Nobody told me to do this. Opening my own kitchen was a leap of faith, built on believing in myself and trusting God, and He has been holding me the whole time.</p>
    <p>Hearth was born from wanting to bring that warmth back into busy homes. I come into your kitchen, shop for and cook nourishing meals, and leave everything packed and labeled, so the people you love can sit down to something made with care. It should feel like a warm hug from mom waiting in your fridge.</p>
    <p>I'd love to cook for you.</p>
    <p class="signoff">With love, Jordan</p>
    <p><a class="btn" href="contact.html">Let's talk about your kitchen</a></p>
  </div>
</section>
'''
page("story.html", "My Story | Hearth Kitchen Co.",
     "Meet Chef Jordan Rowlan: CIA-trained, former Southern Hills sous chef, cooking in homes across the Tulsa Metro area.",
     story, "story.html")

# ---------------- Thanksgiving ----------------
tg = '''
<section class="stack" style="padding-top:12px">
  <div class="label">Holiday menu</div>
  <h1>Thanksgiving Pre-Order</h1>
  <div id="circlebanner" class="circle" hidden><b>Welcome, Inner Circle!</b> <span data-circle-label>Inner Circle 10% off</span> is applied to everything you add. You'll see your savings in your order total.</div>
  <p class="lede">Homemade sides, turkey and pies, cooked in small batches and brought to your door the day before Thanksgiving. Pick what you need, pay ahead, and put your feet up.</p>
  <div class="facts">
    <div class="fact"><span class="label">Order by</span><b data-tg="orderByText">Saturday, Nov 14</b></div>
    <div class="fact"><span class="label">Delivered</span><b data-tg="deliveryText">Wednesday, Nov 25</b></div>
    <div class="fact"><span class="label">Delivery</span><b>Free, Tulsa Metro</b></div>
  </div>
  <div class="card">
    <div class="stack" style="gap:8px">
      <p>Everything arrives chilled on Wednesday, fully cooked and ready to reheat on Thanksgiving Day. Sides and turkey come in oven-safe foil pans, and every order includes reheating cards and a simple Thanksgiving Day timeline. Please list any food allergies in the notes, and I will do my best to adjust a dish when I know ahead of time.</p>
      <p><b>One tip as you order:</b> think about your oven space. Most home ovens fit about 4–5 pans on two racks. Your personal reheating timeline will help you plan around it.</p>
      <p>I plan the delivery route myself and will text you a two-hour delivery window before Thanksgiving week.</p>
      <p class="signoff" style="font-size:1.7rem">With love, Jordan</p>
    </div>
  </div>
  <form id="zipform" class="panel stack" style="gap:10px;padding:20px" novalidate>
    <label for="zip" style="font-size:1rem">Check that I deliver to you
      <span class="formnote" style="font-weight:400">I deliver across the Tulsa Metro area. Enter your delivery ZIP code to start your order.</span>
    </label>
    <div class="inline-form">
      <input id="zip" name="zip" inputmode="numeric" autocomplete="postal-code" maxlength="5" placeholder="Delivery ZIP code" style="max-width:220px">
      <button class="btn" type="submit">Check my ZIP</button>
    </div>
    <p id="zipmsg" role="status" hidden></p>
  </form>
  <div id="closed" class="closed" hidden><b>Thanksgiving orders are closed.</b> Thank you to everyone who ordered!</div>
</section>

<section id="menu" aria-label="Thanksgiving menu" style="padding-top:0"></section>

<section class="panel stack" aria-labelledby="plate">
  <div class="label">Just for you</div>
  <h2 id="plate">Thanksgiving Plate for One</h2>
  <p>Celebrating solo, or cooking for one this year? You still deserve the whole feast.</p>
  <p><b><span data-tg="platePrice">$39</span>, delivery included.</b> Herb-roasted turkey breast with gravy, your choice of any 3 sides from the menu, and a soft dinner roll. Packed in a plant-based, PFAS-free container that reheats in the microwave, and delivered chilled <span data-tg="deliveryText">Wednesday, Nov 25</span>.</p>
  <p><a class="btn" data-order="plateLink" href="#">Order a Plate for One</a></p><p class="formnote" data-ziphint>Check your ZIP code above to order.</p>
</section>

<section class="stack" aria-labelledby="order">
  <h2 id="order">Ready to order?</h2>
  <p data-cart-off>Tap below to choose your dishes and pay securely by card, Apple Pay or Google Pay. <b>Everything is à la carte.</b> Your cart opens with a few favorites, so set any of them to 0 and add exactly what you want, from a single pie to the whole feast.</p>
  <p data-cart-on hidden><b>Everything is à la carte.</b> Tap <b>Add</b> on any dish above, from a single pie to the whole feast. Your order total follows you at the bottom of the screen, and you'll pay securely by card, Apple Pay or Google Pay.</p>
  <div class="panel stack" style="gap:6px;padding:20px">
    <b>Free delivery across the Tulsa Metro area on <span data-tg="deliveryText">Wednesday, Nov 25</span>.</b>
    <span>Order a single side or a whole feast. Cooking for just yourself? The Plate for One above was made with you in mind.</span>
    <span>Oklahoma sales tax is added at checkout. Orders close <span data-tg="orderByText">Saturday, Nov 14</span>.</span>
    <span>Not sure if you're in my delivery area? Text me at 918-968-5002 before ordering.</span>
  </div>
  <div data-cart-off><p><a class="btn" data-order="dinnerLink" href="#">Order &amp; pay</a></p><p class="formnote" data-ziphint>Check your ZIP code above to order.</p></div>
  <p class="formnote">Questions or a special request? Text or call 918-968-5002.</p>
</section>

<div id="cartbar" class="cartbar" hidden role="region" aria-label="Your order">
  <div class="cb-in">
    <div class="cb-sum">
      <div><b id="cb-count">0 items</b> &middot; <span id="cb-sub">$0.00</span></div>
      <div id="cb-circle" hidden><div class="cb-circle"><span data-circle-label>Inner Circle 10% off</span>: you save <b id="cb-off"></b></div><div>Your total: <b class="cb-total" id="cb-total"></b></div></div>
      <div class="cb-note">Tax added at checkout &middot; Free delivery</div>
      <div id="cb-err" class="cb-err" role="alert" hidden></div>
    </div>
    <button id="cb-go" class="btn" type="button">Checkout</button>
  </div>
</div>
'''
tg_js = r'''<script>
(function(){
  var T=HEARTH.thanksgiving, m=document.getElementById("menu"), API=T.checkoutApi||"";
  var CART=!!API;
  document.querySelectorAll("[data-cart-on]").forEach(function(e){e.hidden=!CART;});
  document.querySelectorAll("[data-cart-off]").forEach(function(e){e.hidden=CART;});
  function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;"}[c];});}
  var byKey={}; T.menu.forEach(function(c){c.items.forEach(function(i){byKey[i.key]=i;});});
  m.innerHTML=T.menu.map(function(c){
    return '<div class="course"><h2>'+esc(c.course)+'</h2><p class="formnote" style="margin:4px 0 8px">'+esc(c.note)+'</p>'+
      c.items.map(function(i){return '<div class="item"><div><h3>'+esc(i.name)+'</h3><p class="desc">'+esc(i.desc)+'</p><p class="size">'+esc(i.size)+'</p></div>'+
        '<div class="buy"><div class="price">$'+i.price+'</div>'+(CART?'<div class="qty" data-key="'+i.key+'"></div>':'')+'</div></div>';}).join("")+'</div>';
  }).join("");
  document.querySelectorAll("[data-tg]").forEach(function(el){var k=el.dataset.tg;el.textContent=(k==="platePrice"?"$":"")+T[k];});
  var closed=new Date()>new Date(T.orderBy), zipOk=false, circle=null, circleInfo=null;
  var zf=document.getElementById("zipform"), zi=document.getElementById("zip"), zm=document.getElementById("zipmsg");

  // ---------- cart ----------
  var cart={};
  try{cart=JSON.parse(localStorage.getItem("hearthCart")||"{}")||{};}catch(e){cart={};}
  Object.keys(cart).forEach(function(k){if(!byKey[k]||!(cart[k]>0))delete cart[k];});
  function save(){try{localStorage.setItem("hearthCart",JSON.stringify(cart));}catch(e){}}
  function money(n){return "$"+n.toFixed(2);}
  function totals(){var n=0,s=0;Object.keys(cart).forEach(function(k){n+=cart[k];s+=cart[k]*byKey[k].price;});
    var off=circleInfo?Math.round(s*circleInfo.percent)/100:0;return {n:n,sub:s,off:off,total:s-off};}
  function setQty(k,q){q=Math.max(0,Math.min(20,q));if(q)cart[k]=q;else delete cart[k];save();drawCart();}
  function drawCart(){
    if(!CART)return;
    document.querySelectorAll(".qty").forEach(function(box){
      var k=box.dataset.key,q=cart[k]||0,name=esc(byKey[k].name);
      if(closed){box.innerHTML="";return;}
      box.innerHTML=q?('<button type="button" class="qbtn" data-d="-1" aria-label="One less '+name+'">&minus;</button><span class="qn" aria-live="polite">'+q+'</span><button type="button" class="qbtn" data-d="1" aria-label="One more '+name+'">+</button>')
        :('<button type="button" class="btn add" data-d="1" aria-label="Add '+name+'">Add</button>');
    });
    var t=totals(), bar=document.getElementById("cartbar");
    bar.hidden=closed||!t.n; document.body.classList.toggle("has-cart",!bar.hidden);
    document.getElementById("cb-count").textContent=t.n+(t.n===1?" item":" items");
    document.getElementById("cb-sub").textContent=money(t.sub);
    var cl=document.getElementById("cb-circle");
    if(circleInfo&&t.n){cl.hidden=false;document.getElementById("cb-off").textContent=money(t.off);document.getElementById("cb-total").textContent=money(t.total);}
    else cl.hidden=true;
    document.getElementById("cb-sub").classList.toggle("struck",!!(circleInfo&&t.n));
  }
  m.addEventListener("click",function(e){var b=e.target.closest("button[data-d]");if(!b)return;var k=b.closest(".qty").dataset.key;
    setQty(k,(cart[k]||0)+Number(b.dataset.d));var again=document.querySelector('.qty[data-key="'+k+'"] button');if(again&&!cart[k])again.focus();});

  function paint(){
    document.querySelectorAll("[data-order]").forEach(function(a){
      if(closed){a.setAttribute("aria-disabled","true");a.removeAttribute("href");a.textContent="Orders closed";}
      else if(!zipOk){a.setAttribute("aria-disabled","true");a.removeAttribute("href");}
      else {a.removeAttribute("aria-disabled");a.href=(a.dataset.order==="plateLink"&&circleInfo)?circleInfo.plateLink:T[a.dataset.order];}
    });
    document.querySelectorAll("[data-ziphint]").forEach(function(h){h.hidden=closed||zipOk;});
  }
  function check(z){
    z=(z||"").replace(/\D/g,"").slice(0,5);
    if(z.length<5){zm.hidden=false;zm.className="formmsg err";zm.textContent="Please enter a 5-digit ZIP code.";zipOk=false;paint();return;}
    zipOk=T.deliveryZips.indexOf(z)!==-1; zm.hidden=false;
    if(zipOk){zm.className="formmsg ok";zm.textContent=CART?"Good news, I deliver to "+z+"! Tap Add on any dish below.":"Good news, I deliver to "+z+"! Your order buttons are ready below.";try{localStorage.setItem("hearthZip",z)}catch(e){}}
    else{zm.className="formmsg err";zm.textContent="I'm so sorry, I only deliver within the Tulsa Metro area right now. Text me at 918-968-5002 and I'll see what I can do.";}
    paint();
  }
  zf.addEventListener("submit",function(e){e.preventDefault();check(zi.value);});

  var go=document.getElementById("cb-go"), err=document.getElementById("cb-err");
  if(go) go.addEventListener("click",function(){
    err.hidden=true;
    if(!zipOk){zf.scrollIntoView({behavior:"smooth",block:"center"});zm.hidden=false;zm.className="formmsg err";zm.textContent="Please check your delivery ZIP code first.";zi.focus({preventScroll:true});return;}
    go.disabled=true;go.textContent="One moment…";
    fetch(API+"/checkout",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({items:cart,circle:circle||undefined})})
      .then(function(r){return r.json();})
      .then(function(d){if(d.url){location.href=d.url;}else{throw new Error(d.error||"Checkout couldn't start.");}})
      .catch(function(e){err.hidden=false;err.textContent=(e&&e.message&&e.message!=="Failed to fetch")?e.message:"Checkout couldn't start. Please text Jordan at 918-968-5002.";go.disabled=false;go.textContent="Checkout";});
  });

  // ---------- Inner Circle (private link only) ----------
  function circleOn(info){
    circleInfo=info;var b=document.getElementById("circlebanner");b.hidden=false;
    b.querySelector("[data-circle-label]").textContent=info.label;drawCart();paint();
  }
  if(CART){
    var qs=new URLSearchParams(location.search), tok=qs.get("circle");
    if(tok){qs.delete("circle");history.replaceState(null,"",location.pathname+(qs.toString()?"?"+qs:"")+location.hash);}
    else{try{tok=localStorage.getItem("hearthCircle");}catch(e){}}
    if(tok){fetch(API+"/circle?t="+encodeURIComponent(tok)).then(function(r){return r.json();}).then(function(d){
      if(d.ok){circle=tok;try{localStorage.setItem("hearthCircle",tok);}catch(e){}circleOn(d);}
      else{try{localStorage.removeItem("hearthCircle");}catch(e){}}
    }).catch(function(){});}
  }

  if(closed) zf.hidden=true;
  try{var saved=localStorage.getItem("hearthZip");if(saved&&!closed){zi.value=saved;check(saved);}}catch(e){}
  paint(); drawCart();
  if(closed) document.getElementById("closed").hidden=false;
})();
</script>'''
page("thanksgiving.html", "Thanksgiving Pre-Order | Hearth Kitchen Co.",
     "Order Thanksgiving turkey, sides and pies from Chef Jordan, delivered free across the Tulsa Metro area on Wednesday, Nov 25.",
     tg, "thanksgiving.html", tg_js)

# ---------------- Contact ----------------
contact = '''
<section class="stack" style="padding-top:12px;max-width:720px">
  <div class="label">Contact</div>
  <h1>Let's talk about your kitchen.</h1>
  <p class="lede">Tell me a little about your family and your kitchen, and I'll be in touch within two days.</p>
  <form class="card" action="#" method="POST" data-formspree data-thanks="Thank you! I'll be in touch within two days. With love, Jordan.">
    <div class="row">
      <label for="c-name">Name<input id="c-name" name="name" autocomplete="name" required></label>
      <label for="c-phone">Phone<input id="c-phone" name="phone" type="tel" autocomplete="tel"></label>
    </div>
    <label for="c-email">Email<input id="c-email" name="email" type="email" autocomplete="email" required></label>
    <label for="c-help">What can I help with?
      <select id="c-help" name="service">
        <option>Kitchen Reset</option><option>Weekly meal prep</option><option>Event</option><option>Holiday menu</option><option>Other</option>
      </select>
    </label>
    <label for="c-msg">Message<textarea id="c-msg" name="message" placeholder="Who you're feeding, favorite foods, allergies, and the days that work for you."></textarea></label>
    <input type="hidden" name="_subject" value="New Hearth Kitchen Co. inquiry">
    <button class="btn" type="submit">Send</button>
    <p class="formmsg" hidden role="status"></p>
  </form>
  <p class="formnote">Prefer to talk? Text or call 918-968-5002, or email jordansrowlan@gmail.com.</p>
</section>
'''
page("contact.html", "Contact | Hearth Kitchen Co.",
     "Ask Chef Jordan about weekly in-home meal preparation, a Kitchen Reset, events or holiday menus in the Tulsa Metro area.",
     contact, "contact.html", '<script src="form.js"></script>')
print("built")

# ---------------- Policies ----------------
prose = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "policies_prose.html")).read()
for a, b in [
    ("<li><b>Weekly private chef service:</b> invoiced weekly, due upon receipt.</li>",
     "<li><b>Weekly and biweekly meal preparation:</b> invoiced after each cook day, due upon receipt. Groceries are billed separately at cost, with receipts.</li>"),
    ('<h2 id="weekly">Weekly private chef service</h2>', '<h2 id="weekly">Weekly and biweekly meal preparation</h2>'),
    ("<li><b>Catering and private chef events:</b>", "<li><b>Events, dinners and gatherings:</b>"),
    ('<h2 id="preorders">Pre-orders</h2>\n  <ul>', '<h2 id="preorders">Pre-orders and delivery</h2>\n  <ul>\n    <li><b>Delivery area:</b> delivery is available only within the Tulsa Metro area, about 20 miles from Broken Arrow. Orders outside the area will be refunded.</li>'),
]:
    prose = prose.replace(a, b)
# Full policies (in `prose`) are on hold until Jordan approves them; show a coming-soon note instead.
pol = ('<section class="stack" style="padding-top:12px;max-width:640px"><div class="label">Hearth Kitchen Co.</div><h1>Policies</h1>'
       '<p class="lede">My full policies are coming soon.</p>'
       '<p>In the meantime, if you have a question about deposits, changes, cancellations or delivery, just text or call me at 918-968-5002. I\'m always happy to help.</p>'
       '<p class="signoff" style="font-size:1.8rem">With love, Jordan</p></section>')
page("policies.html", "Policies | Hearth Kitchen Co.",
     "Deposits, payment, cancellation and privacy policies for Hearth Kitchen Co., serving the Tulsa Metro area.", pol, "")
print("policies built")

# ---------------- Pay an invoice ----------------
pay = '''
<section class="stack" style="padding-top:12px;max-width:720px">
  <div class="label">Payments</div>
  <h1>Pay your invoice</h1>
  <p class="lede">Thank you for letting me cook for you. Paying is quick and secure, by card, Apple Pay or Google Pay.</p>
  <div class="card stack">
    <h2 style="font-size:1.4rem">Pay from your invoice email</h2>
    <p>Open the invoice email from Hearth Kitchen Co. and tap <b>Pay this invoice</b>. Your amount, including tax, is already filled in, and you'll get a receipt right away.</p>
    <p class="formnote">Can't find it? Search your inbox and spam folder for "Hearth Kitchen Co." I'll also send a friendly reminder email with your pay link a few days before it's due.</p>
  </div>
  <div class="card stack">
    <h2 style="font-size:1.4rem">Need it sent again?</h2>
    <p>Text me at 918-968-5002 and I'll resend your invoice.</p>
  </div>
  <p class="formnote">Paying by check or cash? Make it out to Hearth Kitchen Co., LLC.</p>
</section>
'''
pay_js = ""
page("pay.html", "Pay Your Invoice | Hearth Kitchen Co.",
     "Pay your Hearth Kitchen Co. invoice securely online by card, Apple Pay or Google Pay.", pay, "pay.html", pay_js)
print("pay built")

# ---------------- Thank you (after a website-cart checkout) ----------------
thanks = '''
<section class="stack" style="padding-top:12px;max-width:640px">
  <div class="label">Order received</div>
  <h1>Thank you for your Thanksgiving order!</h1>
  <p class="lede">Your food will be delivered chilled on Wednesday, Nov 25. I'll text you a two-hour delivery window before Thanksgiving week, and your receipt is on its way to your email.</p>
  <p>Questions or a change? Text or call me at 918-968-5002.</p>
  <p class="signoff" style="font-size:1.8rem">With love, Jordan</p>
  <p><a class="btn ghost" href="index.html">Back to Hearth Kitchen Co.</a></p>
</section>
'''
thanks_js = '<script>try{localStorage.removeItem("hearthCart")}catch(e){}</script>'
page("thanks.html", "Thank You | Hearth Kitchen Co.", "Thank you for your Thanksgiving order from Hearth Kitchen Co.", thanks, "", thanks_js)
