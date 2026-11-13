// Sends the Contact form and email sign-up to Jordan's Gmail (through the
// hearth-checkout service) and shows a thank-you message in place.
document.querySelectorAll("form[data-formspree]").forEach(function (form) {
  var msg = form.querySelector(".formmsg");
  // Hidden field that people never see; spam bots fill it in and get ignored.
  var hp = document.createElement("input");
  hp.type = "text"; hp.name = "website"; hp.tabIndex = -1; hp.autocomplete = "off"; hp.setAttribute("aria-hidden", "true");
  hp.style.cssText = "position:absolute;left:-9999px;width:1px;height:1px;opacity:0";
  form.appendChild(hp);
  function show(text, ok) {
    if (!msg) return;
    msg.textContent = text;
    msg.className = "formmsg " + (ok ? "ok" : "err");
    msg.hidden = false;
  }
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    if (typeof form.beforeSend === "function" && form.beforeSend() === false) return;
    var btn = form.querySelector("button[type=submit]");
    if (btn) { btn.disabled = true; btn.dataset.label = btn.textContent; btn.textContent = "Sending..."; }
    var data = {};
    new FormData(form).forEach(function (v, k) { data[k] = String(v); });
    fetch(form.getAttribute("action") || HEARTH.formsApi, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data) })
      .then(function (r) { return r.json().then(function (d) { if (!r.ok || !d.ok) throw new Error(d.error || "failed"); }); })
      .then(function () {
        form.reset();
        if (typeof form.afterSend === "function") form.afterSend();
        show(form.dataset.thanks || "Thank you! I'll be in touch within two days. With love, Jordan.", true);
      })
      .catch(function () {
        show("That didn't go through. Please try again, or text me at 918-968-5002 or email jordansrowlan@gmail.com.", false);
      })
      .then(function () {
        if (btn) { btn.disabled = false; btn.textContent = btn.dataset.label; }
      });
  });
});
