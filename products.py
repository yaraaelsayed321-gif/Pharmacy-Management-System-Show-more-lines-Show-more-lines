import json
import os
class PharmacyStore:
    def __init__(self):
        if os.path.exists("products.json"):
            with open("products.json", "r", encoding="utf-8") as f:
                products = json.load(f)

            self.medicines = [p for p in products if 100 <= p["id"] < 200]
            self.skincare = [p for p in products if 200 <= p["id"] < 300]
            self.haircare = [p for p in products if 300 <= p["id"] < 400]
            self.bodycare = [p for p in products if 400 <= p["id"] < 500]
            self.mother_and_child = [p for p in products if 500 <= p["id"] < 600]

            return
        self.medicines = [
            {"id": 101, "name": "Panadol Extra", "price": 30.0, "stock": 25, "expiry_date": "2028-05-10", "description": "Analgesic and antipyretic containing paracetamol and caffeine."},
            {"id": 102, "name": "Vitamin C 1000mg", "price": 45.0, "stock": 15, "expiry_date": "2027-11-20", "description": "Dietary supplement to support immunity and fight colds."},
            {"id": 103, "name": "Augmentin 1g", "price": 95.0, "stock": 8, "expiry_date": "2027-03-15", "description": "Broad-spectrum antibiotic for treating bacterial infections."},
            {"id": 104, "name": "Ibuprofen 400mg", "price": 35.0, "stock": 30, "expiry_date": "2028-01-10", "description": "Anti-inflammatory, pain reliever, and fever reducer."},
            {"id": 105, "name": "Omega 3 Fish Oil", "price": 150.0, "stock": 12, "expiry_date": "2027-08-30", "description": "Fish oil rich in fatty acids to support heart and brain health."},
            {"id": 106, "name": "Aspirin Protect", "price": 22.0, "stock": 40, "expiry_date": "2028-06-18", "description": "Antiplatelet for protecting cardiovascular health."},
            {"id": 107, "name": "Cataflam 50mg", "price": 42.0, "stock": 18, "expiry_date": "2027-10-05", "description": "Fast-acting pain reliever and anti-inflammatory for muscles and joints."},
            {"id": 108, "name": "Strepsils Lozenges", "price": 35.0, "stock": 50, "expiry_date": "2028-12-01", "description": "Lozenges for soothing sore throats and mouth infections."},
            {"id": 109, "name": "Amoxil 500mg Capsules", "price": 55.0, "stock": 20, "expiry_date": "2027-09-14", "description": "Penicillin-based antibiotic for treating infections."},
            {"id": 110, "name": "Antinal Antidiarrheal", "price": 28.0, "stock": 35, "expiry_date": "2028-04-22", "description": "Intestinal antiseptic for treating diarrhea and bacterial infections."},
            {"id": 111, "name": "Congestal Cold & Flu", "price": 31.0, "stock": 45, "expiry_date": "2028-02-17", "description": "Fever reducer and decongestant for cold and flu symptoms."},
            {"id": 112, "name": "Claritin 10mg Allergy", "price": 68.0, "stock": 16, "expiry_date": "2027-12-10", "description": "Non-drowsy antihistamine for allergy symptoms."},
            {"id": 113, "name": "Voltarene Emulgel 50g", "price": 50.0, "stock": 22, "expiry_date": "2028-07-08", "description": "Topical gel for relieving muscle, joint, and back pain."},
            {"id": 114, "name": "Zyrtec Antihistamine", "price": 48.0, "stock": 28, "expiry_date": "2028-03-30", "description": "Antihistamine for allergies, runny nose, and skin itching."},
            {"id": 115, "name": "Gaviscon Liquid Antacid", "price": 85.0, "stock": 14, "expiry_date": "2027-11-05", "description": "Liquid antacid for heartburn and indigestion relief."}
        ]

        self.skincare = [
            {"id": 201, "name": "Nivea Soft Cream", "price": 60.0, "stock": 20, "expiry_date": "2028-04-12", "description": "Light moisturizing cream for face and body with jojoba oil and vitamin E."},
            {"id": 202, "name": "Bioderma Sunscreen SPF50", "price": 380.0, "stock": 10, "expiry_date": "2027-09-15", "description": "High-protection sunscreen for sensitive and combination skin."},
            {"id": 203, "name": "CeraVe Foaming Cleanser", "price": 320.0, "stock": 14, "expiry_date": "2028-02-28", "description": "Foaming cleanser for normal to oily skin with ceramides."},
            {"id": 204, "name": "La Roche-Posay Effaclar", "price": 450.0, "stock": 6, "expiry_date": "2027-07-19", "description": "Purifying cleansing gel for acne-prone and oily skin."},
            {"id": 205, "name": "Vichy Mineral89 Serum", "price": 520.0, "stock": 9, "expiry_date": "2028-05-14", "description": "Skin-strengthening serum with hyaluronic acid and mineral water."},
            {"id": 206, "name": "Vaseline Lip Therapy", "price": 45.0, "stock": 35, "expiry_date": "2029-01-10", "description": "Lip balm to protect and moisturize dry, chapped lips."},
            {"id": 207, "name": "Garnier Micellar Water", "price": 110.0, "stock": 25, "expiry_date": "2028-03-22", "description": "Micellar water to gently remove makeup and cleanse the skin."},
            {"id": 208, "name": "The Ordinary Niacinamide", "price": 290.0, "stock": 12, "expiry_date": "2027-10-30", "description": "Serum to regulate oil production, minimize pores, and brighten skin."},
            {"id": 209, "name": "Neutrogena Hydro Boost", "price": 240.0, "stock": 18, "expiry_date": "2028-06-15", "description": "Face gel moisturizer with hyaluronic acid for deep hydration."},
            {"id": 210, "name": "Avene Thermal Spring Water", "price": 210.0, "stock": 15, "expiry_date": "2029-03-01", "description": "Soothing and anti-irritating thermal spring water spray for sensitive skin."},
            {"id": 211, "name": "Cetaphil Gentle Cleanser", "price": 295.0, "stock": 11, "expiry_date": "2028-08-20", "description": "Soap-free gentle cleanser for sensitive and dry skin."},
            {"id": 212, "name": "Eucerin Spotless Serum", "price": 610.0, "stock": 7, "expiry_date": "2027-12-05", "description": "Serum for treating pigmentation, dark spots, and evening skin tone."},
            {"id": 213, "name": "L'Oreal Hyaluronic Acid", "price": 330.0, "stock": 16, "expiry_date": "2028-01-18", "description": "Serum to plump fine lines and give skin ultimate radiance."},
            {"id": 214, "name": "Bioré UV Aqua Sunscreen", "price": 270.0, "stock": 13, "expiry_date": "2028-09-12", "description": "Water-based, fast-absorbing, and lightweight sunscreen."},
            {"id": 215, "name": "COSRX Snail Mucin Essence", "price": 480.0, "stock": 8, "expiry_date": "2028-04-09", "description": "Snail secretion filtrate essence to repair, hydrate, and renew skin cells."}
        ]

        self.haircare = [
            {"id": 301, "name": "Head & Shoulders Shampoo", "price": 95.0, "stock": 25, "expiry_date": "2028-06-11", "description": "Anti-dandruff shampoo and scalp cleanser."},
            {"id": 302, "name": "Argan Hair Serum", "price": 150.0, "stock": 15, "expiry_date": "2027-12-05", "description": "Argan oil serum to nourish split ends and add shine."},
            {"id": 303, "name": "L'Oreal Extraordinary Oil", "price": 180.0, "stock": 18, "expiry_date": "2028-04-18", "description": "Moisturizing hair oil for dry and damaged hair care."},
            {"id": 304, "name": "Tresemme Keratin Conditioner", "price": 135.0, "stock": 20, "expiry_date": "2028-08-25", "description": "Keratin-infused conditioner to straighten and smooth frizzy hair."},
            {"id": 305, "name": "Clear Anti-Hair Fall", "price": 100.0, "stock": 22, "expiry_date": "2027-11-14", "description": "Shampoo to strengthen hair roots and reduce hair fall."},
            {"id": 306, "name": "Hair Mask with Shea Butter", "price": 160.0, "stock": 11, "expiry_date": "2028-02-19", "description": "Shea butter mask for deep hydration and repairing damaged hair."},
            {"id": 307, "name": "Dove Daily Care Shampoo", "price": 90.0, "stock": 30, "expiry_date": "2028-07-09", "description": "Shampoo designed for daily use to protect normal hair."},
            {"id": 308, "name": "Scalp Scrub Treatment", "price": 120.0, "stock": 7, "expiry_date": "2027-10-21", "description": "Scalp scrub to remove flakes and dead skin while stimulating circulation."},
            {"id": 309, "name": "Olaplex No.3 Repair Serum", "price": 680.0, "stock": 5, "expiry_date": "2028-01-30", "description": "Bond-building treatment and repair serum for colored and ruined hair."},
            {"id": 310, "name": "Pantan Pro-V Oil Replacement", "price": 85.0, "stock": 24, "expiry_date": "2028-09-04", "description": "Oil replacement cream to nourish and protect hair from styling damage."},
            {"id": 311, "name": "Garnier Fructis Hair Food", "price": 195.0, "stock": 13, "expiry_date": "2028-05-16", "description": "Multi-use plant-based hair food formula for hydration."},
            {"id": 312, "name": "Sunsilk Coconut Shampoo", "price": 70.0, "stock": 28, "expiry_date": "2028-11-20", "description": "Coconut-infused shampoo to provide hair with softness and vitality."},
            {"id": 313, "name": "Chi Silk Infusion Leave-in", "price": 420.0, "stock": 9, "expiry_date": "2028-03-25", "description": "Alcohol-free leave-in silk treatment for hair protection and shine."},
            {"id": 314, "name": "Palmer's Coconut Oil Mask", "price": 140.0, "stock": 16, "expiry_date": "2027-08-11", "description": "Coconut oil and vitamin E deep hair conditioning mask."},
            {"id": 315, "name": "Schwarzkopf Gliss Conditioner", "price": 115.0, "stock": 19, "expiry_date": "2028-06-02", "description": "Conditioner for hair repair, softness, and easy detangling."}
        ]

        self.bodycare = [
            {"id": 401, "name": "Victoria's Secret Body Splash", "price": 250.0, "stock": 15, "expiry_date": "2029-01-15", "description": "Refreshing body mist with a long-lasting scent."},
            {"id": 402, "name": "Dove Shower Gel", "price": 115.0, "stock": 28, "expiry_date": "2028-05-20", "description": "Moisturizing shower gel with rich lather and deep skin hydration."},
            {"id": 403, "name": "Johnson's Body Lotion", "price": 95.0, "stock": 22, "expiry_date": "2028-03-12", "description": "Ultra-soft body lotion with fast absorption."},
            {"id": 404, "name": "Beesline Whitening Roll-on", "price": 140.0, "stock": 19, "expiry_date": "2027-11-30", "description": "Deodorant and natural skin whitener for sensitive underarm area."},
            {"id": 405, "name": "Kamill Hand Cream", "price": 75.0, "stock": 30, "expiry_date": "2028-09-08", "description": "Hand moisturizing cream with natural chamomile extract."},
            {"id": 406, "name": "Sea Salt Body Scrub", "price": 130.0, "stock": 14, "expiry_date": "2027-12-19", "description": "Dead Sea salt body scrub to remove dead cells and clean the body."},
            {"id": 407, "name": "Imperial Leather Soap", "price": 25.0, "stock": 60, "expiry_date": "2029-06-10", "description": "Classic bathing soap with a distinctive cleansing scent for the skin."},
            {"id": 408, "name": "Foot Care Cracked Heel Cream", "price": 85.0, "stock": 16, "expiry_date": "2028-04-05", "description": "Treatment cream to moisturize and soften cracked heels and feet."},
            {"id": 409, "name": "Bath & Body Works Lotion", "price": 320.0, "stock": 10, "expiry_date": "2028-10-14", "description": "Luxuriously scented body lotion that lasts long."},
            {"id": 410, "name": "Nivea Pearl Anti-perspirant", "price": 65.0, "stock": 32, "expiry_date": "2029-02-28", "description": "Anti-perspirant with pearl extracts for 48-hour protection."},
            {"id": 411, "name": "Palmolive Aromatherapy Wash", "price": 80.0, "stock": 21, "expiry_date": "2028-07-22", "description": "Shower gel infused with essential oils for relaxation."},
            {"id": 412, "name": "Vaseline Cocoa Body Butter", "price": 160.0, "stock": 17, "expiry_date": "2028-01-15", "description": "Body butter with pure cocoa butter to nourish very dry skin."},
            {"id": 413, "name": "Sanex Sensitive Body Wash", "price": 105.0, "stock": 20, "expiry_date": "2028-04-01", "description": "Gentle shower wash specifically for sensitive and allergy-prone skin."},
            {"id": 414, "name": "Dettol Anti-Bacterial Wash", "price": 70.0, "stock": 40, "expiry_date": "2029-05-18", "description": "Anti-bacterial body wash for ultimate protection and hygiene."},
            {"id": 415, "name": "Eveline Slimming Body Serum", "price": 210.0, "stock": 9, "expiry_date": "2027-10-29", "description": "Topical serum to help tighten skin and fight cellulite."}
        ]

        self.mother_and_child = [
            {"id": 501, "name": "Fine Baby Diapers Size 3", "price": 230.0, "stock": 40, "expiry_date": "2029-03-10", "description": "Comfortable and highly absorbent baby diapers size 3."},
            {"id": 502, "name": "Johnson's Baby Oil", "price": 80.0, "stock": 25, "expiry_date": "2028-08-15", "description": "Moisturizing and soothing baby oil for sensitive skin."},
            {"id": 503, "name": "Sudocrem Diaper Rash Cream", "price": 150.0, "stock": 18, "expiry_date": "2028-01-20", "description": "Medical cream for treating and preventing diaper rash in infants."},
            {"id": 504, "name": "Pampers Sensitive Wipes", "price": 65.0, "stock": 50, "expiry_date": "2028-06-12", "description": "Sensitive, alcohol-free baby wipes for gentle cleaning."},
            {"id": 505, "name": "Similac Infant Formula Stage 1", "price": 310.0, "stock": 12, "expiry_date": "2027-10-10", "description": "Stage 1 infant formula milk for babies from birth to 6 months."},
            {"id": 506, "name": "Johnson's Baby Shampoo", "price": 75.0, "stock": 22, "expiry_date": "2028-05-30", "description": "No More Tears baby shampoo free of harsh ingredients."},
            {"id": 507, "name": "Baby Powder 200g", "price": 55.0, "stock": 30, "expiry_date": "2029-02-14", "description": "Baby powder to dry skin and protect it from friction."},
            {"id": 508, "name": "Bonjela Teething Gel", "price": 95.0, "stock": 14, "expiry_date": "2027-09-01", "description": "Soothing gel for infant teething pain and sensitive gums."},
            {"id": 509, "name": "Avent Anti-Colic Feeding Bottle", "price": 260.0, "stock": 15, "expiry_date": "2030-01-01", "description": "Anti-colic and gas-reducing baby feeding bottle."},
            {"id": 510, "name": "Bebelac 2 Follow-on Milk", "price": 285.0, "stock": 10, "expiry_date": "2027-11-25", "description": "Follow-on milk formula for infants aged 6 months and above."},
            {"id": 511, "name": "Cerelac Rice & Milk 400g", "price": 110.0, "stock": 28, "expiry_date": "2028-04-18", "description": "Nutritious dried rice and milk meal for infants."},
            {"id": 512, "name": "Mustela Stretch Marks Cream", "price": 420.0, "stock": 8, "expiry_date": "2028-02-10", "description": "Special cream for pregnant women to prevent and treat stretch marks."},
            {"id": 513, "name": "Chicco Silicone Soother 0m+", "price": 125.0, "stock": 20, "expiry_date": "2030-05-01", "description": "Medical silicone pacifier designed for newborns."},
            {"id": 514, "name": "Sanosan Baby Wash & Shampoo", "price": 175.0, "stock": 16, "expiry_date": "2028-07-20", "description": "Milk protein wash and shampoo for complete baby bath care."},
            {"id": 515, "name": "Nuk Sterilizer & Bottle Cleaner", "price": 90.0, "stock": 23, "expiry_date": "2029-08-11", "description": "Safe liquid cleanser for sterilizing baby bottles and tools."}
        ]

    def display_all_categories(self):
        categories = [
            ("Medicines ", self.medicines),
            ("Skin Care ", self.skincare),
            ("Hair Care ", self.haircare),
            ("Body Care", self.bodycare),
            ("Mother and Child ", self.mother_and_child)
        ]
        
        for title, products in categories:
            print(f"--- {title} ---")
            for p in products:
                print(f"ID: {p['id']} | Name: {p['name']} | Price: {p['price']} EGP | Stock: {p['stock']} | Expiry: {p['expiry_date']} | Desc: {p['description']}")

    def get_stock(self, product_name):
        all_prods = self.medicines + self.skincare + self.haircare + self.bodycare + self.mother_and_child
        for product in all_prods:
            if product_name == product["name"]:
                return product["stock"]
        return None

    def set_stock(self, product_name, new_stock):
        all_prods = self.medicines + self.skincare + self.haircare + self.bodycare + self.mother_and_child
        for product in all_prods:
            if product_name == product["name"]:
                product["stock"] = new_stock
                return True
        return False

    def get_all_product(self):
        return self.medicines+self.skincare+self.haircare+self.bodycare+self.mother_and_child

