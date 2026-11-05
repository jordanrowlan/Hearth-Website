# Hearth Kitchen Co. — Website

Personal chef and in-home meal preparation serving the Tulsa Metro area.
*Nourishing your body starts with how you treat your food.*

## Start here (for Claude)
Read these in order before building anything:

1. **`HEARTH_WEBSITE_BRIEF.md`** — what to build, page content, the Thanksgiving ordering system with Stripe, technical requirements, launch checklist.
2. **`HEARTH_BRAND_GUIDE.md`** — who Hearth is, what we sell, voice, colors (terracotta-led earthy palette), fonts, photography.
3. **`vision-board/NOTES.md`** — Jordan's Pinterest vision board, summarized: palette, textures, wax seals, botanical line art, photo mood.
4. **`data/thanksgiving-2026.json`** — Thanksgiving menu, prices, dates and delivery rules. Edit this file to change the menu.
5. **`images/chef-jordan.jpg`** — Jordan's portrait. Use it as the home-page hero and on My Story.

**First task:** build Phase 1 from the brief (coming-soon home page with Jordan's portrait, My Story, Thanksgiving ordering with Stripe, Contact). Ask Jordan about anything marked **TBD**.

## Rules
- Never commit customer data, order details, receipts, or API keys. Stripe keys go only in the hosting provider's environment variables.
- Do not publish client names, internal costs, hourly rates or margins.
- This repo is public. Keep it that way only if the rules above are followed.

## For Jordan: changing the Thanksgiving menu
Open `data/thanksgiving-2026.json` on GitHub, click the pencil icon, change a name, description or price, then click **Commit changes**. The site updates automatically after it's connected to hosting.
