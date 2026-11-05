# Hearth Kitchen Co. — Website Brief

> Hand this file to Claude in the `hearth website` repo. It is the source of truth for the build: business facts, brand, page content, the Thanksgiving ordering system, and technical requirements. Where something is still undecided it is marked **TBD** — ask Jordan rather than guessing.

---

## 1. Project summary

**Owner:** Jordan Rowlan, sole member of Hearth Kitchen Co., LLC (Oklahoma)
**What we're building:** the first Hearth Kitchen Co. website, hosted from GitHub, with online ordering and card payments through **Stripe**.

### Phase 1 — launch now (needed by about Nov 7, 2026)
1. A warm, simple **"coming soon"** home page so people can see Hearth exists, with email signup and social links.
2. A **Thanksgiving pre-order page** where customers choose dishes, enter delivery details, and **pay by card through Stripe**. Orders close **Saturday, Nov 14, 2026**; delivery is **Wednesday, Nov 25, 2026** (the day before Thanksgiving).
3. A **My Story** page with Jordan's portrait and her story.
4. A basic **Contact / inquiry** form.

### Phase 2 — after the graphic designer delivers branding
- Swap in the designer's logo, colors, fonts and photography.
- Add full **Services**, **About**, **Kitchen Reset**, **Events**, and future **Workshops** pages.
- Reuse the ordering system for future seasonal menus (Christmas, Easter, etc.).

### Success looks like
- A customer on a phone can order Thanksgiving and pay in under 3 minutes.
- Jordan gets an email for every paid order and can see all orders in one place (Stripe dashboard).
- No customer personal data is ever stored in the GitHub repo.
- Jordan can change prices, dates and menu items by editing one data file.

---

## 2. The business

**Hearth Kitchen Co.** (goes by **"Hearth"**) is a high-touch, concierge-level personal chef and in-home meal preparation service.

- **Service area:** the **Tulsa Metro area** (Broken Arrow, Tulsa, Owasso, Bixby, Jenks, Glenpool). On the site, just say **"Tulsa Metro area."**
- **Based in:** Broken Arrow, Oklahoma.
- **No storefront / brick-and-mortar.** Jordan cooks in clients' own homes; holiday orders are **delivered** (no pickup).
- **Who it's for:** primarily women ages 35–65 who want warmth and comfort back in their kitchen and need help with grocery shopping, meal prep and packaging, or a personal chef for special events. Also high-net-worth individuals, families and discerning clients.
- **Cuisine:** food from all over the world. Jordan has studied many cultures and cuisines and tailors each menu to the client's theme or request. Site line: *"Cuisine from around the world, tailored to your table."*
- **How it works for recurring clients:** start with a holistic **Kitchen Reset**, then Jordan shops and preps meals **weekly or biweekly** in the client's home. Every meal is packed in the client's own glass containers with **reheating instructions**. Personalized beverages, specialty tea blends and **wellness shots** are available.
- Food handler's permit is current.

### Services (public descriptions)
| Service | Description for the site | Price on site |
|---|---|---|
| **Kitchen Reset** | A one-time welcome service and a complete energy revamp of your kitchen: organizing, refreshing, and setting your kitchen up for nourishing meals. Includes your own set of glass meal containers and wellness-shot bottles, sized to your household. | "Inquire" (pricing TBD) |
| **Weekly & Biweekly Meal Preparation** | Jordan shops, cooks and packages your meals in your own kitchen. Every container is labeled with reheating instructions. Menus are built around your family's tastes, dietary needs and favorites. | "Inquire" |
| **Personal Chef for Events** | Intimate dinners, gatherings and celebrations, with custom menus from cuisines around the world, built around your theme or request. | "Inquire" |
| **Wellness Shots & Beverages** | Small-batch wellness shots (for example beet, pomegranate and ginger) and personalized beverages, added to your weekly service. | Included with service / inquire |
| **Seasonal Holiday Menus** | Order ahead, pay ahead, delivered to your door. Thanksgiving 2026 is open now. | Menu prices listed |
| **Coming soon: Girls' Night Cooking Workshops** | Women cooking together in a special space. Working names: *Keepers of the Hearth*, *Moonlit Supper*, *Sisters of the Spoon*. Faith-forward offerings may be included. | "Coming soon" — do not use the word "circle" |

### Seasonal membership (Phase 2, launching 2027 — show as "coming soon" only)
Three tiers, paid by season (winter, spring, summer, fall), groceries billed separately at cost. **Do not show per-meal math or prices yet.**
- **Heritage** — 5 dinners a week
- **Gather** — 5 breakfasts, 5 lunches, 5 dinners a week (**the featured tier**)
- **Full Harvest** — 7 breakfasts, 7 lunches, 7 dinners a week

---

## 3. Brand

- **Name:** Hearth Kitchen Co. (short: Hearth)
- **Tagline:** *Nourishing your body starts with how you treat your food.*
- **Feel:** "a warm hug from mother." Cozy, elegant, inviting, organic, generous.
- **Philosophy:** Jordan teaches people how to prepare food and show love to it. Hearth centers on the energy and frequencies of food, balance (yin and yang, dark and light), and how food's energy interacts with the body — she believes even the frequency of an apple changes if you speak kindly to it. Use this gently on the About page; keep the rest of the site practical.

### Voice
- Warm, personal, first person from Jordan ("I'll plan the route and send you a delivery window").
- Plain, short sentences. Generous, never salesy.
- Food descriptions are simple and appetizing, not fancy.
- Sign-offs: "With love, Jordan."

### Visual direction (interim, until the designer's files arrive)
**Read `vision-board/NOTES.md` first.** Jordan's Pinterest board calls for an earthy, old-world look: Ivory Sand backgrounds, Burnt Sienna buttons, Sage and deep olive panels, charcoal text, wax seals, botanical line art, natural-light photography. **Use the vision-board palette in `HEARTH_BRAND_GUIDE.md` §7 for the site.** The tokens below are the older printed-menu palette, kept for reference. Put them in CSS variables so the designer's palette can replace them in one place.

| Token | Hex | Use |
|---|---|---|
| `--bg` | `#fbf1e1` | page background (cream) |
| `--card` | `#fffaf1` | cards, form fields |
| `--ink` | `#3b2316` | body text (deep brown) |
| `--muted` | `#7a5a45` | secondary text |
| `--rule` | `#e8d2b4` | dividers, borders |
| `--wheat` | `#f6e0bd` | highlight panels |
| `--accent` | `#c4561a` | burnt orange: buttons, rules |
| `--accent-ink` | `#9a3e0b` | small caps labels, links |
| `--band` | `#7b2d12` | deep red-brown: feature blocks |
| gold | `#d9a233` | decorative |
| olive | `#7c8a3a` / `#4f7a2a` | decorative leaves/vines |

- **Fonts:** headings **DM Serif Display**; body **Figtree** (both Google Fonts).
- **Signature motif:** a thin four-color band across the top of each page: deep red-brown → burnt orange → gold → olive, in equal quarters.
- **Seasonal decoration (Thanksgiving page):** hand-drawn style pumpkins, vines and autumn leaves.
- Support **dark mode** with a warm dark palette (`--bg #26170f`, `--ink #f7eadb`, `--accent #f0933f`).
- Mobile-first. Most customers will order from a phone.

### Visual-first: people should see Jordan
Hearth is a personal, in-home service, so **trust comes from seeing Jordan's face**. The site must feel visual and personal, not text-heavy.
- **Home hero:** a large portrait of Jordan (`images/chef-jordan.jpg`, see below) beside or behind the name and tagline, with a warm greeting such as "Hi, I'm Chef Jordan." On phones, the photo sits above the text.
- **Thanksgiving page:** a smaller round portrait of Jordan near the intro, with a note signed "With love, Jordan."
- **About / My Story page:** a large portrait at the top, then the story (see §5), broken up with food photos.
- Use generous photo areas throughout: Jordan cooking, food in glass containers, wellness shots, holiday dishes. Let photos lead, keep text short.
- Every photo needs descriptive alt text.

### Assets available now
- **Portrait of Jordan** (professional headshot): smiling, in a white double-breasted chef coat embroidered with the Hearth logo and "Chef Jordan," in a warm, softly blurred restaurant kitchen. Save as `images/chef-jordan.jpg`. Alt text: "Chef Jordan Rowlan of Hearth Kitchen Co., smiling in her Hearth chef coat."
- Photos of Jordan's food in client glass containers and wellness shots (Jordan will add to `/images`).
- **Logo (from the chef coat embroidery):** the word **"Hearth"** in a classic serif, a small **flame** icon above it, and a thin rule underneath. **Use terracotta (`#914117`) for the logo and primary color** (Jordan's decision, Nov 2026; the coat embroidery is plum, which is retired for now). Until the designer sends official files, recreate it as a simple SVG wordmark (serif "Hearth" + small flame + rule). Keep all colors in CSS variables.

---

## 4. Sitemap

**Phase 1:** `/` Home (coming soon) · `/my-story` · `/thanksgiving` · `/thanksgiving/thank-you` · `/contact` · `/policies`
**Phase 2:** `/services` · `/kitchen-reset` · `/events` · `/workshops` · `/membership`

Navigation (Phase 1): Home · My Story · Thanksgiving · Contact. Footer: tagline, "Serving the Tulsa Metro area," email, phone, socials, © Hearth Kitchen Co., LLC.

---

## 5. Page content

### Home (coming soon)
Large portrait of Jordan as the hero (see §3).
> **Hearth Kitchen Co.**
> *Hi, I'm Chef Jordan.*
> *Nourishing your body starts with how you treat your food.*
>
> Personal chef and in-home meal preparation serving the Tulsa Metro area. Cuisine from around the world, tailored to your table. Our full website is coming soon.
>
> **Thanksgiving pre-orders are open.** Let us bring the warmth to your table this year.
> **[Order Thanksgiving →]**
>
> Be the first to know when we launch. **[Email signup]**
> Follow along: **TikTok · Instagram**

### Thanksgiving page
- **Title:** Thanksgiving Pre-Order
- **Intro:** "Homemade sides, turkey and pies, cooked in small batches and brought to your door the day before Thanksgiving. Pick what you need, pay ahead, and put your feet up."
- **Key facts strip:** Order by **Saturday, Nov 14** · Delivered **Wednesday, Nov 25** · **Pay ahead** to confirm
- **How it arrives:** "All food is fully cooked and packed in oven-safe pans. You only need to reheat it. Please list any food allergies in the notes, and I will do my best to adjust a dish when I know ahead of time."
- **Delivery:** "Complimentary delivery across the Tulsa Metro area on Wednesday, Nov 25, on orders of $150 or more. Orders under $150 have a $20 delivery fee. I plan the delivery route to reach everyone efficiently and will send you a two-hour delivery window before Thanksgiving week."
- Menu grouped by course with quantity steppers (see §6), live order summary, then delivery form and **Pay with card** button.
- Each item gets an "add reheating instructions" note in the confirmation email (TBD — Jordan to supply).

### My Story (About) — Phase 1, linked in the main menu
Jordan wants to **tell her story**. Layout: large portrait → a short opening line in big serif type → the story in short paragraphs, with food photos between sections → her philosophy as a pull quote → a warm call to action ("Let me bring the warmth back to your kitchen" → Contact).

**Draft structure (Jordan fills in the bracketed parts; keep her words, edit lightly):**
> **Hi, I'm Chef Jordan.**
>
> [Where my love of cooking began: who taught me, the kitchen I grew up in, a food memory.]
>
> [The moment I knew this was what I was meant to do, and why I started Hearth.]
>
> To me, food is love made visible. I believe the way we treat our food matters, from how it's grown, to how it's prepared, to the words we speak over it. *Nourishing your body starts with how you treat your food.*
>
> Hearth was born from wanting to bring that warmth back into busy homes. I come into your kitchen, shop for and cook nourishing meals, and leave everything packed and labeled, so the people you love can sit down to something made with care. It should feel like a warm hug from mom waiting in your fridge.
>
> [Something personal: family, faith, what I love outside the kitchen. Optional.]
>
> I'd love to cook for you.
> — Jordan

### Contact
Fields: name, email, phone, "What can I help with?" (Kitchen Reset / Weekly meal prep / Event / Holiday menu / Other), message. Sends Jordan an email. Copy: "Tell me a little about your family and your kitchen, and I'll be in touch within two days."

### Policies (draft — Jordan to confirm, **TBD**)
- Orders are confirmed once paid.
- Cancellations for a full refund until the order deadline (Nov 14); after that, orders are being shopped for and are non-refundable. **TBD**
- Food is prepared in a kitchen that handles wheat, dairy, eggs and tree nuts (pecans).
- Delivery is to the Tulsa Metro area only; someone should be home during the delivery window, or tell Jordan a safe place to leave it. **TBD**

---

## 6. Thanksgiving ordering system — spec

### Menu data (`data/thanksgiving-2026.json`)
Keep all menu, price and date settings in one file so Jordan can edit them.

```json
{
  "season": "Thanksgiving 2026",
  "orderDeadline": "2026-11-14T23:59:00-06:00",
  "deliveryDate": "2026-11-25",
  "freeDeliveryThreshold": 150,
  "deliveryFee": 20,
  "serviceArea": "Tulsa Metro area",
  "courses": [
    { "course": "The Main", "note": "Cooked fully, sliced and ready to warm.", "items": [
      { "id": "turkey", "name": "Herb-Roasted Turkey Breast", "desc": "About 4 lb boneless breast with butter, sage and thyme, sliced, with a cup of pan gravy.", "size": "About 4 lb, serves 8 with leftovers", "price": 98, "maxQty": null }
    ]},
    { "course": "Sides", "note": "Each tray comes in an oven-safe pan. Portions are generous, so expect leftovers.", "items": [
      { "id": "dressing", "name": "Sage Stuffing", "desc": "Cubed bread, butter, celery, onion and fresh sage.", "size": "9x13 pan, serves 8", "price": 40 },
      { "id": "gfdressing", "name": "Gluten-Free Sage Stuffing", "desc": "The same stuffing made with gluten-free bread. Made in a kitchen that also uses wheat, so please tell me about any severe allergy.", "size": "8x8 pan, serves 4 to 6", "price": 31 },
      { "id": "potatoes", "name": "Mashed Potatoes", "desc": "Russet potatoes whipped smooth with cream and butter.", "size": "2-quart pan, serves 6 to 8", "price": 31 },
      { "id": "greenbean", "name": "Green Beans with Mushrooms and Crispy Shallots", "desc": "Fresh green beans and sautéed mushrooms in a light, from-scratch sauce, topped with crispy shallots.", "size": "2-quart pan, serves 6 to 8", "price": 40 },
      { "id": "sweetpot", "name": "Classic Sweet Potatoes", "desc": "Whipped sweet potatoes with maple and brown butter, topped with toasted marshmallows and pecans.", "size": "2-quart pan, serves 6 to 8", "price": 36 },
      { "id": "sweetpotsf", "name": "Brown Butter Sweet Potatoes (No Added Sugar)", "desc": "Roasted sweet potatoes with brown butter, fresh sage, orange zest and toasted pecans. No added sugar.", "size": "2-quart pan, serves 6 to 8", "price": 36 },
      { "id": "mac", "name": "Baked Three-Cheese Macaroni", "desc": "Sharp cheddar, gruyère and a golden crumb top.", "size": "2-quart pan, serves 6 to 8", "price": 42 },
      { "id": "carrots", "name": "Honey-Thyme Roasted Carrots", "desc": "Whole carrots roasted until caramelized.", "size": "1.5-quart pan, serves 6", "price": 30 },
      { "id": "gravy", "name": "Turkey Gravy", "desc": "Rich, smooth and made from roasted turkey stock.", "size": "1 quart, serves 8 to 10", "price": 17 },
      { "id": "cranberry", "name": "Orange Cranberry Relish", "desc": "Fresh cranberries, orange zest and a little honey.", "size": "1 pint, serves 8", "price": 15 },
      { "id": "rolls", "name": "Soft Dinner Rolls", "desc": "Buttery pull-apart rolls, baked the day before.", "size": "One dozen", "price": 20 }
    ]},
    { "course": "Pies", "note": "Nine-inch pies, baked fresh on Tuesday.", "items": [
      { "id": "pecan", "name": "Pecan Pie", "desc": "Toasted pecans in a brown sugar and vanilla filling.", "size": "9 inch, serves 8", "price": 44 },
      { "id": "pumpkin", "name": "Pumpkin Pie", "desc": "Silky pumpkin custard with warm spices.", "size": "9 inch, serves 8", "price": 38 },
      { "id": "apple", "name": "Apple Crumble Pie", "desc": "Tart and sweet apples under a buttery oat crumble.", "size": "9 inch, serves 8", "price": 42 }
    ]}
  ]
}
```

### Order rules
- **Delivery fee:** $20 if items subtotal is under $150; **free** at $150 or more. Show a live nudge: "Add $X more for complimentary delivery."
- **No pickup option.** Delivery only, Tulsa Metro area.
- **No delivery-time picker.** Jordan routes deliveries and sends each customer a two-hour window later.
- **Order deadline:** after Nov 14, 11:59 pm Central, the page shows "Thanksgiving orders are closed — thank you!" and the pay button is disabled. The server must also reject late checkouts.
- **Capacity limits:** each item may have a `maxQty` (Jordan sets these). Also support an overall cap on total orders (realistic delivery capacity is about **12–15 orders** in one day). When sold out, show "Sold out." **TBD:** exact caps.
- Quantity per item 0–20 on the form.

### Checkout fields
Required: full name, phone, email, delivery address (street, city, ZIP). Optional: allergies or notes, gate code / delivery instructions. Validate the ZIP is in an Oklahoma Tulsa-area ZIP list (soft warning, not a hard block). **TBD:** confirm ZIP list.

### Payments — Stripe
- Use **Stripe Checkout** (hosted payment page). The site sends the cart to a small **serverless function** that **re-prices every line from the server-side menu file** (never trust prices from the browser), adds the delivery fee line when it applies, and creates a Checkout Session.
- Collect the phone number and shipping address in Stripe Checkout (restrict to US). Pass the notes as session metadata.
- Success → `/thanksgiving/thank-you`. Cancel → back to the order page with the cart intact.
- Turn on Apple Pay / Google Pay. Statement descriptor: **HEARTH KITCHEN CO**.
- Jordan creates the Stripe account as Hearth Kitchen Co., LLC; Claude never handles her keys directly. Keys live only in the hosting provider's environment variables (`STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`). Use **test mode** until Jordan approves a test order.

### After an order
- A Stripe **webhook** (`checkout.session.completed`) sends Jordan an **email** with the full order (items, quantities, totals, name, phone, address, notes). Customers get Stripe's receipt plus a warm confirmation email:
  > Thank you for your Thanksgiving order! Your food will be delivered on Wednesday, Nov 25. I'll send you a two-hour delivery window before Thanksgiving week. With love, Jordan — Hearth Kitchen Co.
- **Where orders live:** the Stripe dashboard (plus the email). Do **not** write customer data into the GitHub repo.
- Nice to have: an "Export orders" script (run by Jordan) that pulls paid sessions from Stripe into a CSV, grouped by item totals (for shopping/prep) and by ZIP (for routing).

---

## 7. Technical requirements

- **Repo:** `hearth website` on Jordan's GitHub.
- **Hosting:** GitHub Pages alone can't run the Stripe checkout function. Recommended: deploy the repo to **Netlify, Vercel or Cloudflare Pages** (free tiers) connected to GitHub, using their serverless functions. Claude should pick one, explain why in one paragraph, and walk Jordan through connecting it.
- **Stack:** keep it simple — static HTML/CSS/vanilla JS (or a light framework like Astro) plus one or two serverless functions. Jordan is not a developer: favor fewer moving parts.
- **Domain:** `hearthkitchenco.com` if available (**TBD** — Jordan to buy), with HTTPS.
- **Email signup:** a free service such as Buttondown, Mailchimp or Kit (**TBD** which).
- **Contact form:** send to Jordan's email via the host's form handling or a function. Add spam protection (honeypot).
- **SEO:** page titles and descriptions; `LocalBusiness` / `FoodEstablishment` schema with service area "Tulsa Metro area"; Open Graph image for link previews on TikTok, Instagram and texts.
- **Accessibility:** good contrast in light and dark mode, real labels on inputs, keyboard-usable quantity steppers, alt text on photos.
- **Performance:** fast on phones; compress images.
- **Privacy:** add a short privacy note (what's collected, used only to fulfill orders, payments handled by Stripe).
- **Editing:** a short `README` for Jordan explaining how to change prices, dates and menu items in the JSON file and how to republish.

---

## 8. Contact details for the site

- **Name:** Jordan Rowlan, Owner & Chef
- **Phone:** 918-968-5002
- **Email:** jordansrowlan@gmail.com (a hello@hearthkitchenco.com address may replace it later — **TBD**)
- **TikTok:** Hearth Kitchen Co. — handle **TBD** (suggested @hearthkitchenco)
- **Instagram:** **TBD**
- **Business:** Hearth Kitchen Co., LLC · Broken Arrow, Oklahoma · Serving the Tulsa Metro area
- Do not publish Jordan's home address.

---

## 9. Do NOT put on the website or in the repo
- Client names or any client details.
- Internal costs, food-cost percentages, Jordan's hourly rate, margins, or income goals.
- Kitchen Reset test prices or seasonal tier prices (show "Inquire" / "Coming soon").
- Customer order data, receipts, or Stripe secret keys.

---

## 10. Open questions for Jordan (TBD)
1. Final per-item quantity caps and total-order cap for Thanksgiving.
2. Cancellation / refund policy wording.
3. Domain name purchase and which business email to show.
4. TikTok and Instagram handles.
5. Email-signup provider.
6. Reheating instructions per dish for the confirmation email.
7. Photos to use on the home and Thanksgiving pages.
8. When the designer's logo, palette and fonts arrive, replace the interim tokens in §3.
9. Jordan's story for the My Story page (§5).

---

## 11. Launch checklist
- [ ] Coming-soon home page live on the domain with HTTPS, with Jordan's portrait as the hero
- [ ] My Story page live with portrait and story
- [ ] Thanksgiving page shows all 15 items with correct prices from the JSON file
- [ ] Delivery fee logic: $20 under $150, free at $150+, nudge message works
- [ ] Stripe test-mode order succeeds end to end; Jordan receives the order email; customer receives confirmation
- [ ] Prices are re-checked on the server; tampering with prices in the browser does not change the charge
- [ ] Orders automatically close after Nov 14, 11:59 pm Central
- [ ] Sold-out handling works
- [ ] Works on iPhone and Android, light and dark mode
- [ ] Switch Stripe to live mode; place one real $1 test and refund it
- [ ] Share the link on TikTok, Instagram, and in Jordan's networking groups
