// Shared page bits: footer year, social links and form destinations,
// all read from data.js so they're edited in one place.
(function () {
  var C = HEARTH.contact;
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  var social = document.querySelector("[data-social]");
  if (social) {
    var links = [];
    if (C.tiktok) links.push('<a href="https://www.tiktok.com/@' + C.tiktok.replace(/^@/, "") + '" rel="noopener">TikTok</a>');
    if (C.instagram) links.push('<a href="https://www.instagram.com/' + C.instagram.replace(/^@/, "") + '" rel="noopener">Instagram</a>');
    if (links.length) social.innerHTML = links.join(""); else social.remove();
  }

  document.querySelectorAll("form[data-formspree]").forEach(function (f) { f.setAttribute("action", HEARTH.formspree); });
})();
