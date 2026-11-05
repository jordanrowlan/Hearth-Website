// Sends any form on the page to Formspree and shows a thank-you message in place.
// To connect: replace FORMSPREE_ID in each form's action with the ID from formspree.io.
document.querySelectorAll("form[action*='formspree.io']").forEach(function (form) {
  var msg = form.querySelector(".formmsg");
  function show(text, ok) {
    if (!msg) return;
    msg.textContent = text;
    msg.className = "formmsg " + (ok ? "ok" : "err");
    msg.hidden = false;
  }
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    if (typeof form.beforeSend === "function" && form.beforeSend() === false) return;
    if (form.action.indexOf("FORMSPREE_ID") !== -1) {
      show("Online inquiries are almost ready. For now, please text or call Jordan at 918-968-5002 or email jordansrowlan@gmail.com.", false);
      return;
    }
    var btn = form.querySelector("button[type=submit]");
    if (btn) { btn.disabled = true; btn.dataset.label = btn.textContent; btn.textContent = "Sending..."; }
    fetch(form.action, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } })
      .then(function (r) {
        if (!r.ok) throw new Error("bad status");
        form.reset();
        if (typeof form.afterSend === "function") form.afterSend();
        show(form.dataset.thanks || "Thank you! Jordan will reply within a day or two.", true);
      })
      .catch(function () {
        show("That didn't go through. Please try again, or text Jordan at 918-968-5002.", false);
      })
      .then(function () {
        if (btn) { btn.disabled = false; btn.textContent = btn.dataset.label; }
      });
  });
});
