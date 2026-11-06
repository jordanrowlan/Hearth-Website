// =====================================================================
// HEARTH KITCHEN CO. — EASY-EDIT SETTINGS
// Change prices, dates, links and contact details here. Every page reads
// from this file, so you only edit it in one place.
// =====================================================================

var HEARTH = {
  contact: {
    name: "Jordan Rowlan",
    phone: "918-968-5002",
    email: "jordansrowlan@gmail.com",
    area: "Tulsa Metro area",
    // Leave "" until the handles are decided, and the links stay hidden.
    tiktok: "",
    instagram: ""
  },

  // Formspree endpoint for the Contact form and email signup.
  // Replace FORMSPREE_ID with the ID from formspree.io (looks like "abcdwxyz").
  formspree: "https://formspree.io/f/FORMSPREE_ID",

  // Stripe checkout for paying an invoice (customer enters the amount due). TEST link until live mode is on.
  invoicePayLink: "https://buy.stripe.com/test_3cI9AL1XQbu72Do7nH8IU05",

  thanksgiving: {
    orderBy: "2026-11-14T23:59:00-06:00",   // orders close (Central time)
    orderByText: "Saturday, Nov 14",
    deliveryText: "Wednesday, Nov 25",
    // Stripe checkout links. These are TEST links until live mode is on.
    dinnerLink: "https://buy.stripe.com/test_28E6ozbyqcybcdY7nH8IU04",
    plateLink: "https://buy.stripe.com/test_eVq7sDbyqaq31zkcI18IU01",
    platePrice: 39,
    // Delivery area: ZIP codes within about 20 miles of Broken Arrow.
    // Add or remove ZIPs here. Orders from other ZIPs see a "sorry" message instead of the order buttons.
    deliveryZips: [
      "74011","74012","74013","74014",            // Broken Arrow
      "74008",                                     // Bixby
      "74037",                                     // Jenks
      "74055",                                     // Owasso
      "74429",                                     // Coweta
      "74033",                                     // Glenpool
      "74015",                                     // Catoosa
      "74103","74104","74105","74106","74107","74108","74110","74112","74114","74115","74116",
      "74119","74120","74126","74127","74128","74129","74130","74132","74133","74134","74135",
      "74136","74137","74145","74146"              // Tulsa
    ],
    dinnersStartAt: 150,
    menu: [
      { course: "The Main", note: "Cooked fully, sliced and ready to warm.", items: [
        { name: "Herb-Roasted Turkey Breast", desc: "About 4 lb boneless breast with butter, sage and thyme, sliced, with a cup of pan gravy.", size: "About 4 lb, serves 8 with leftovers", price: 98 }
      ]},
      { course: "Sides", note: "Each tray comes in an oven-safe pan. Portions are generous, so expect leftovers.", items: [
        { name: "Sage Stuffing", desc: "Cubed bread, butter, celery, onion and fresh sage.", size: "9x13 pan, serves 8", price: 40 },
        { name: "Gluten-Free Sage Stuffing", desc: "The same stuffing made with gluten-free bread. Made in a kitchen that also uses wheat, so please tell me about any severe allergy.", size: "8x8 pan, serves 4 to 6", price: 31 },
        { name: "Mashed Potatoes", desc: "Russet potatoes whipped smooth with cream and butter.", size: "2-quart pan, serves 6 to 8", price: 31 },
        { name: "Green Beans with Mushrooms and Crispy Shallots", desc: "Fresh green beans and sautéed mushrooms in a light, from-scratch sauce, topped with crispy shallots.", size: "2-quart pan, serves 6 to 8", price: 47 },
        { name: "Classic Sweet Potatoes", desc: "Whipped sweet potatoes with maple and brown butter, topped with toasted marshmallows and pecans.", size: "2-quart pan, serves 6 to 8", price: 36 },
        { name: "Brown Butter Sweet Potatoes (No Added Sugar)", desc: "Roasted sweet potatoes with brown butter, fresh sage, orange zest and toasted pecans.", size: "2-quart pan, serves 6 to 8", price: 36 },
        { name: "Baked Three-Cheese Macaroni", desc: "Sharp cheddar, gruyère and a golden crumb top.", size: "2-quart pan, serves 6 to 8", price: 42 },
        { name: "Honey-Thyme Roasted Carrots", desc: "Whole carrots roasted until caramelized.", size: "1.5-quart pan, serves 6", price: 30 },
        { name: "Turkey Gravy", desc: "Rich, smooth and made from roasted turkey stock.", size: "1 quart, serves 8 to 10", price: 17 },
        { name: "Orange Cranberry Relish", desc: "Fresh cranberries, orange zest and a little honey.", size: "1 pint, serves 8", price: 15 },
        { name: "Soft Dinner Rolls", desc: "Buttery pull-apart rolls, baked the day before.", size: "One dozen", price: 26 }
      ]},
      { course: "Pies", note: "Nine-inch pies, baked fresh on Tuesday.", items: [
        { name: "Pecan Pie", desc: "Toasted pecans in a brown sugar and vanilla filling.", size: "9 inch, serves 8", price: 46 },
        { name: "Pumpkin Pie", desc: "Silky pumpkin custard with warm spices.", size: "9 inch, serves 8", price: 40 },
        { name: "Apple Crumble Pie", desc: "Tart and sweet apples under a buttery oat crumble.", size: "9 inch, serves 8", price: 46 }
      ]}
    ]
  }
};
