# Hearth Kitchen Co.

**Personal chef and in-home meal preparation serving the Tulsa Metro area.**
*Nourishing your body starts with how you treat your food.*

Live site: **[hearthkitchencompany.com](https://hearthkitchencompany.com)**

Hearth Kitchen Co., LLC is owned and run by Chef Jordan Rowlan in Broken Arrow, Oklahoma. Hearth brings warmth back to the kitchen with in-home meal prep, kitchen resets, wellness shots, and personal chef service for gatherings and holidays across Broken Arrow, Tulsa, Owasso, Bixby, Jenks and Glenpool.

---

## What's on the site

| Page | File | What it does |
|---|---|---|
| Home | `index.html` | Jordan's portrait, Hearth's services, and the Thanksgiving pre-order banner |
| My Story | `story.html` | Jordan's story: *"Food has always meant family to me."* |
| Thanksgiving | `thanksgiving.html` | Thanksgiving 2026 menu with a cart and secure Stripe checkout |
| Contact | `contact.html` | Inquiry form for meal prep, events and wellness shots |
| Pay Invoice | `pay.html` | Lets clients pay an invoice by card through Stripe |
| Thank You | `thanks.html` | Shown after a successful order |
| Policies | `policies.html` | Shows "coming soon" until the policies are approved |

The live site is published from the **`master`** branch with GitHub Pages, using the custom domain in `CNAME`.

---

## For Jordan: everyday changes

Almost everything you'll want to change lives in **one file: `data.js`**. Every page reads from it.

**To edit it on GitHub:**
1. Open `data.js` and click the **pencil icon** (Edit).
2. Change the words or numbers *inside the quotation marks* only. Leave commas, brackets and quotes in place.
3. Click **Commit changes**. The live site updates within a few minutes.

**What you can change in `data.js`:**
- **Contact info:** phone, email, and TikTok and Instagram links (leave them `""` to keep the icons hidden)
- **Thanksgiving dates:** order deadline and delivery day
- **Menu:** dish names, descriptions and prices
- **Delivery ZIP codes:** add or remove ZIP codes you deliver to
- **Stripe links and checkout service:** only change these if Stripe gives you new ones

Not sure about an edit? Ask Claude to make it for you.

---

## How payments work

- **Thanksgiving orders:** customers build a cart on the Thanksgiving page. A small checkout service (`hearth-checkout`, hosted on Cloudflare Workers) turns the cart into a **Stripe Checkout** page, adds Oklahoma sales tax, and limits orders to Hearth's capacity. Money goes straight to Hearth's Stripe account.
- **Invoices:** clients pay from the link in their invoice email or on the Pay Invoice page.
- **Contact form:** sends through Formspree. Add the Formspree form ID in `data.js` (replace `FORMSPREE_ID`) to turn it on.

No card numbers or customer details are ever stored on this website or in this repository.

---

## Behind-the-scenes tools (`tools/`)

These help Jordan run Thanksgiving. They run on a computer, not on the website.

| Tool | What it makes |
|---|---|
| `build_site.py` | Rebuilds the site pages from one shared template |
| `build_tracker.py` | An Excel order tracker from Stripe orders: dish counts, pans and packaging |
| `build_timelines.py` | A personal Thanksgiving Day reheating timeline for each customer |

Order data is used on the computer only and is **never** saved to this repository.

---

## Brand and planning files

- `HEARTH_WEBSITE_BRIEF.md`: the full website plan, page content and launch checklist
- `HEARTH_BRAND_GUIDE.md`: voice, colors (terracotta-led earthy palette), fonts and photography
- `vision-board/NOTES.md`: notes from Jordan's Pinterest vision board
- `images/`: photos, including Jordan's portrait

---

## Rules for this repository

This repository is **public**, so anyone can read it.

- Never commit customer names, orders, receipts, addresses or API keys. Stripe secret keys belong only in the checkout service's private settings.
- Never publish client names, internal costs, hourly rates or profit margins.

---

## Contact

**Chef Jordan Rowlan**, Hearth Kitchen Co., LLC
📞 [918-968-5002](tel:+19189685002) · ✉️ [jordansrowlan@gmail.com](mailto:jordansrowlan@gmail.com)
Serving the Tulsa Metro area

© 2026 Hearth Kitchen Co., LLC. All rights reserved.
