from flask import Blueprint
from . import db
from .models import WatchCategory, Watch, Order
import datetime


bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database
@bp.route('/dbseed/')
def dbseed():
    category1 = WatchCategory(name='Automatic')
    category2 = WatchCategory(name='Quartz')
    category3 = WatchCategory(name='Chronograph')
    category4 = WatchCategory(name='Digital')
    category5 = WatchCategory(name='Dive watches')
      
    try:
        db.session.add(category1)
        db.session.add(category2)
        db.session.add(category3)
        db.session.add(category4)
        db.session.add(category5)
        db.session.commit()
    except:
        return 'There was an issue adding the cities in dbseed function'

    watch1 = Watch( 
        name="Longines Avigation BigEye Heritage Men's 41mm Titanium Automatic Chronograph Watch L2.816.1.93.2",\
        description= "Throughout its long history, Longines has created pieces that have stood the test of time. A re-issue of a chronograph with a 1930s’ design, The Longines Avigation BigEye is now available in titanium with a petrol blue dial. This timepiece – characterised by the visibility of its dial and its oversized 30-minute counter – joins the great tradition of pilot watches.",\
        image='longines1.webp', 
        price=6250.00,
        brand = 'Longines',
        movement_type = 'Automatic Chronograph',
        dial_colour = 'Blue',
        strap_type = 'Leather',
        style = 'Shape/Round',
        material = 'Stainless Steel',
        collection = 'Heritage',
        glass = 'Sapphire Crystal',
        water_resistance = '30M',
        featured = True,
        quantity = 1,
        categories=[category1, category3] 
        ) 

    watch2 = Watch( 
        name="TAG HEUER FORMULA 1 QUARTS CHRONOGRAPH 43MM CAZ101AP.BA0842",\
        description= "Bold in spirit, striking in design. Adorned with a radiant green dial, this energetic TAG Heuer Formula 1 watch pays a daring tribute to the fearless challengers of the racetrack. Marrying strength and versatility, it stands as a testament to those who dare to outpace.",\
        image='tag1.webp', 
        price=3150.00,
        brand = 'TAG HEUER',
        movement_type = 'Quartz Chronograph',
        dial_colour = 'Green',
        strap_type = 'Bracelet',
        style = 'Shape/Round',
        material = 'Stainless Steel',
        collection = 'F1',
        glass = 'Sapphire Crystal',
        water_resistance = '200M',
        featured = True,
        quantity = 1,
        categories=[category2, category3] 
        )
    
    watch3 = Watch( 
        name="Casio G-Shock GA-2100-1A1",\
        description= "Ever since the first DW-5000C went on sale back in 1983, G-SHOCK has continued to push the limits of timekeeping toughness while creating new and original designs. These new models embody these efforts in an attractively thin configuration.",\
        image='casio1.webp', 
        price=279.00,
        brand = 'Casio',
        movement_type = 'Analogue Digital',
        dial_colour = 'Black',
        strap_type = 'Rubber',
        style = 'Shape/Round',
        material = 'Resin',
        collection = 'G-Shock',
        glass = 'Mineral',
        water_resistance = '200M',
        featured = True,
        quantity = 1,
        categories=[category4] 
        )

    watch4 = Watch( 
        name="Longines Mini DolceVita Women’s 29mm Stainless Steel Quartz Watch L5.200.4.71.6",\
        description= "With its discreet profile, classic styling, and aesthetic variations that are at once timely and timeless, the Mini DolceVita is a small but mighty masterpiece that exquisitely expresses, in equal part, Longines’ quiet luxury and contemporary elegance. Each reference in the Mini DolceVita collection features a rectangular 21.50mm x 29.00mm stainless steel case and is powered by a highly-accurate L178 quartz movement. The rectangular silver-coloured Roman rectangular dial inside the case calls attention to its uncompromising elegance. The watch is available on alligator strap as well as on a newly-designed stainless steel bracelet which, thanks to its 198 links, enhances the jewelled spirit of the watch and offers extraordinary wearer comfort.",\
        image='longines2.webp', 
        price=3075.00,
        brand = 'Longines',
        movement_type = 'Quartz',
        dial_colour = 'Silver',
        strap_type = 'Bracelet',
        style = 'Shape/Square',
        material = 'Stainless Steel',
        collection = 'Dolce Vita',
        glass = 'Sapphire Crystal',
        water_resistance = '30M',
        featured = True,
        quantity = 1,
        categories=[category2] 
        )
    
    watch5 = Watch( 
        name="Loyal Scuba Professional Men’s 41.50mm Quartz Watch Blue",\
        description= "The Loyal Scuba Men's 41.50mm Quartz Watch is not just a watch; it's a testament to precision, style, and reliability. This timepiece is your passport to the world of exceptional timekeeping. Every aspect of the Loyal Scuba Watch reflects impeccable craftsmanship. Encased in a sturdy 41.50mm stainless steel frame, this watch is designed to withstand the test of time. With a remarkable water resistance of 500m, it's your perfect companion for underwater escapades and beyond. Powered by a high-precision quartz movement, this watch guarantees that you're always on time, no matter where your adventures take you. Unmatched accuracy ensures that you can rely on it for your daily activities and beyond. Make the Loyal Scuba Men's 41.50mm Quartz Watch your constant companion and embrace every moment with confidence and style. Order yours today and experience the perfect fusion of functionality and fashion.",\
        image='loyalscuba1.webp', 
        price=399.00,
        brand = 'Loyal Scuba',
        movement_type = 'Quartz',
        dial_colour = 'Blue',
        strap_type = 'Rubber',
        style = 'Shape/Round',
        material = 'Stainless Steel',
        collection = 'Scuba',
        glass = 'Mineral',
        water_resistance = '500M',
        featured = True,
        quantity = 1,
        categories=[category2, category5] 
        )
    
    watch6 = Watch( 
        name="Luminox Pacific Diver Men’s 39mm Quartz Watch XS.3124M",\
        description= "Introducing the Luminox Pacific Diver Men's 39mm Quartz Watch XS.3124M – The Perfect Blend of Elegance and Durability! The Luminox Pacific Diver XS.3124M is a testament to timeless design. With a sleek 39mm stainless steel case, it strikes the perfect balance between elegance and durability. Equipped with a Swiss quartz movement, this watch guarantees unbeatable accuracy, so you're always punctual and on time for life's most important moments. This watch is more than just a fashion statement; it's a reliable tool for divers and adventurers. With water resistance up to 200 meters (660 feet) and a unidirectional rotating bezel, it's ready to accompany you on any aquatic expedition. Don't compromise on style or functionality. The Luminox Pacific Diver Men's 39mm Quartz Watch XS.3124M is the embodiment of luxury and utility in one elegant package. Elevate your wrist game and make a statement wherever life takes you.",\
        image='Luminox1.webp', 
        price=999.00,
        brand = 'Luminox',
        movement_type = 'Quartz',
        dial_colour = 'Mother-Of-Pearl',
        strap_type = 'Rubber',
        style = 'Shape/Round',
        material = 'Stainless Steel',
        collection = 'Pacific Diver',
        glass = 'Sapphire Crystal',
        water_resistance = '200M',
        featured = True,
        quantity = 1,
        categories=[category2, category5] 
        )
    
    watch7 = Watch( 
        name="Loyal Scuba Diver Men's 44mm Stainless Steel Quartz Watch",\
        description= "Scuba is Loyal’s most popular and longest-serving collection. Available in five new colour-ways, this durable watch is your greatest companion. This masculine design offers advanced technology and water resistance. As a result, Scuba reigns as one of the toughest watches nationwide. ",\
        image='loyalscuba2.webp', 
        price=349.00,
        brand = 'Loyal Scuba',
        movement_type = 'Quartz',
        dial_colour = 'Black',
        strap_type = 'Rubber',
        style = 'Shape/Round',
        material = 'Stainless Steel',
        collection = 'Diver',
        glass = 'Mineral',
        water_resistance = '200M',
        featured = True,
        quantity = 1,
        categories=[category2, category5] 
        )
    
    watch8 = Watch( 
        name="Luminox Pacific Diver Men's 44mm Stainless Steel Quartz Chronograph Watch XS.3155",\
        description= "The new Pacific Diver Chrono is a beautiful addition to the Luminox collection. With a stainless steel case, carbon fibre bezel, and black unidirectional rotating bezel, this 44mm timepiece features luminescent materials which allow the watch to glow for up to 25 years without charging. A valuable tool for any diver who needs to keep track of time at all times, it also comes with a genuine rubber strap that makes it easy to adjust.",\
        image='luminox2.webp', 
        price=1199.00,
        brand = 'Luminox',
        movement_type = 'Quartz Chronograph',
        dial_colour = 'Black',
        strap_type = 'Rubber',
        style = 'Shape/Round',
        material = 'Stainless Steel',
        collection = 'Pacific Diver',
        glass = 'Sapphire Crystal',
        water_resistance = '200M',
        featured = True,
        quantity = 1,
        categories=[category2, category3, category5] 
        )
    
    watch9 = Watch( 
        name="Rado Centrix Men's 39.50mm Quartz Watch R30 022 712",\
        description= "Introducing the Rado Centrix Men's 39.50mm Quartz Watch R30 022 712 – a classic timepiece reimagined both technically and aesthetically. This iconic watch seamlessly blends innovation with style, creating a perfect fusion of form and function.",\
        image='rado1.webp', 
        price=3075.00,
        brand = 'Rado',
        movement_type = 'Quartz',
        dial_colour = 'Black Diamond',
        strap_type = 'Bracelet',
        style = 'Shape/Round',
        material = 'Ceramic and Yellow Gold',
        collection = 'Centrix',
        glass = 'Sapphire Crystal',
        water_resistance = '50M',
        featured = True,
        quantity = 1,
        categories=[category2] 
        )
    
    watch10 = Watch( 
        name="Tissot Everytime Men's 40mm Quartz Watch T143.410.16.041.00",\
        description= "The Tissot Everytime collection reflects the ultimate in Swiss understated watchmaking chic. A selection of vintage-inspired stainless steel bracelets and leather straps make Everytime a perfect model to experiment with your look.",\
        image='tissot1.webp', 
        price=420.00,
        brand = 'Tissot',
        movement_type = 'Quartz',
        dial_colour = 'Blue',
        strap_type = 'Leather',
        style = 'Shape/Round',
        material = 'Stainless Steel',
        collection = 'Everytime',
        glass = 'Sapphire Crystal',
        water_resistance = '50M',
        featured = True,
        quantity = 1,
        categories=[category2] 
        )
    
    watch11 = Watch( 
        name="Seiko Prospex Limited Edition 'Black Series' Men's 40.5mm Black & Steel Automatic Watch SPB253J",\
        description= "Seiko Prospex Limited Edition 'Black Series' Men's 40.5mm Black & Steel Automatic Watch SPB253J",\
        image='seiko2.webp', 
        price=1895.00,
        brand = 'Seiko',
        movement_type = 'Automatic',
        dial_colour = 'Black',
        strap_type = 'NATO',
        style = 'Shape/Round',
        material = 'Black and Steel',
        collection = 'Prospex',
        glass = 'Sapphire Crystal',
        water_resistance = '200M',
        featured = False,
        quantity = 1,
        categories=[category1] 
        )

    watch12 = Watch( 
        name="Casio Baby-G Women's Resin Analogue Digital Watch BA110PL-1A",\
        description= "Casio Baby-G Women's Resin Analogue Digital Watch BA110PL-1A",\
        image='casio2.webp', 
        price=299.00,
        brand = 'Casio',
        movement_type = 'Analogue Digital',
        dial_colour = 'Pink',
        strap_type = 'Resin',
        style = 'Shape/Round',
        material = 'Resin',
        collection = 'Baby-G',
        glass = 'Mineral',
        water_resistance = '100M',
        featured = False,
        quantity = 1,
        categories=[category4] 
        )

    watch13 = Watch( 
        name="Seiko 5 Supercars 2023 Limited Edition Men's 42.50mm Automatic Watch SRPJ95K",\
        description= "Introducing the Seiko 5 Supercars 2023 Limited Edition Men's 42.50mm Automatic Watch SRPJ95K – a luxurious, modern statement piece with only 2,023 pieces worldwide! Crafted from high-quality stainless steel and 100m water resistance, this watch features an impressive thickness of 13.4mm and diameter of 42.5mm, along with a length of 46mm and distance between lugs of 22mm. With a special box included, this limited edition watch also comes with an additional silicon strap to complete the look. Make sure to get one before it’s gone. Please note, watches are sent at random, serial number selection is not possible.",\
        image='seiko1.webp', 
        price=725.00,
        brand = 'Seiko',
        movement_type = 'Automatic',
        dial_colour = 'Black',
        strap_type = 'Bracelet',
        style = 'Shape/Round',
        material = 'Stainless Steel',
        collection = 'Seiko 5',
        glass = 'Mineral',
        water_resistance = '100M',
        featured = False,
        quantity = 1,
        categories=[category1] 
        )
    
    watch14 = Watch( 
        name="Casio G-Shock Men's Resin Analogue Digital Watch GA400GB-1A9",\
        description= "From super-tough G-SHOCK comes the GA400GB-1A9, with a large rotary switch for intuitive operation and ISO764 class magnetic resistance",\
        image='casio3.webp', 
        price=349.00,
        brand = 'Casio',
        movement_type = 'Analogue Digital',
        dial_colour = 'Black',
        strap_type = 'Rubber',
        style = 'Shape/Round',
        material = 'Resin',
        collection = 'G-Shock',
        glass = 'Mineral',
        water_resistance = '200M',
        featured = False,
        quantity = 1,
        categories=[category4] 
        )
    
    watch15 = Watch( 
        name="Citizen Promaster Men’s 44mm Eco Drive Watch BN0166-01L",\
        description= "Inspired by the beautiful oceans that unite our world, the new Limited Edition UNITE with BLUE Promaster captures the captivating and countless shades of blue of the ocean. Made of 100% recycled polycarbonate materials, the structural colour ink on the dial produces a variety of glittering colours by using light to reflect off the surface to create a range of hues and tones. Notable features include a two-tone blue and green bezel against a stainless-steel case, black biomass-based polyurethane strap made from plant-based materials, bold indices for improved readability and 200 meters water resistance.",\
        image='citizen1.webp', 
        price=799.00,
        brand = 'Citizen',
        movement_type = 'Eco Drive',
        dial_colour = 'Mother-Of-Pearl',
        strap_type = 'Rubber',
        style = 'Shape/Round',
        material = 'Stainless Steel',
        collection = 'Promaster',
        glass = 'Mineral',
        water_resistance = '200M',
        featured = False,
        quantity = 1,
        categories=[category1, category5] 
        )
    
    watch16 = Watch( 
        name="Casio G-SHOCK Men's 'Aim High' Bluetooth Chronograph Watch DWB5600AH-6D",\
        description= "For those who aim higher in the virtual world — and in real life! Introducing G-SHOCK inspired by the determination it takes to make it to the highest levels of computer and survival games. Gamers know what it takes to score high in action and shooting games. These watches recreate the exciting, ever-changing game world with polarized paint in purple and green that changes color depending on the viewing angle. Details like a target scope for setting one’s sights on the target are incorporated in orange accents and LCD screen graphics for a playful design that moves seamlessly between real and virtual worlds. Choose your favourite — the octagonal GA-2100AH, the classic digital DW-B5600AH with Bluetooth, or the digital-analogue combination GA-B001AH in an innovative construction, also with Bluetooth.",\
        image='casio4.webp', 
        price=299.00,
        brand = 'Casio',
        movement_type = 'Bluetooth Chronograph',
        dial_colour = 'LCD',
        strap_type = 'Resin',
        style = 'Shape/Square',
        material = 'Resin',
        collection = 'G-Shock',
        glass = 'Mineral',
        water_resistance = '200M',
        featured = False,
        quantity = 1,
        categories=[category3, category4] 
        )
    
    watch17 = Watch( 
        name="Seiko Presage 40.50mm Automatic Watch SRPK50J",\
        description= "The SRPK50J pays a tribute to LARK's creation, Irori Moments, a bespoke cocktail inspired by the traditional Japanese hearth, a cherished gathering place to socialise, relax, and create shared memories. This cocktail captures the essence of time and shared moments, aligning perfectly with LARK's vision of sharing 'whisky moments.' The SRPK50J's dial mirrors the rich, golden hues of this exceptional creation. The textured face of the SRPK50J beautifully replicates the warm, inviting colours of Irori Moments. The watch's slender, gleaming markers draw inspiration from the graceful lines of a cocktail glass, harmoniously blending the worlds of timekeeping and mixology. This limited edition timepiece is a true collector's gem, with each watch individually numbered on the case back. Presented in a distinctive whisky barrel timber box, it further enhances its allure as a timeless keepsake. Irori Moments is a bespoke cocktail that harmonises the heritage of LARK’s Tasmanian Peated Whisky with the classical peated whiskies of Japan, such as Yoichi. The ingredients include Tasmanian-grown wasabi from Shima Wasabi and local plums which introduces fruity and floral notes, skilfully balancing the soft, earthy tones of LARK’s Tasmanian Peated Whisky. The result is a rich, velvety texture with a subtle smoky finish. The cocktail boasts a rich golden colour that mirrors the golden hues found on the SRPK50J's watch dial. SRPK50J will be available from October 2023 with limited edition stock of only 1000 models being produced.",\
        image='seiko3.webp', 
        price=950.00,
        brand = 'Seiko',
        movement_type = 'Automatic',
        dial_colour = 'Yellow',
        strap_type = 'Leather',
        style = 'Shape/Round',
        material = 'Stainless Steel',
        collection = 'Presage',
        glass = 'Mineral',
        water_resistance = '50M',
        featured = False,
        quantity = 1,
        categories=[category1] 
        )
    
    watch18 = Watch( 
        name="Casio G-Shock Men's Stainless Steel Analogue Digital Watch GM2100-1A",\
        description= "G-SHOCK gives the popular 'CasiOak' a stainless steel makeover! Capitalising on the great success of its “CasiOak” model, G-SHOCK introduces the GM-2100 series crafted from metal.",\
        image='casio5.webp', 
        price=539.00,
        brand = 'Casio',
        movement_type = 'Analogue Digital',
        dial_colour = 'Black',
        strap_type = 'Resin',
        style = 'Shape/Round',
        material = 'Stainless Steel',
        collection = 'G-Shock',
        glass = 'Mineral',
        water_resistance = '200M',
        featured = False,
        quantity = 1,
        categories=[category4] 
        )
    
    watch19 = Watch( 
        name="Luminox Carbon SEAL 45mm Automatic Military Dive Watch XS.3877",\
        description= "The Luminox Carbon SEAL 45mm Automatic Military Dive Watch XS.3877 is a perfect combination of Swiss made automatic movement and Luminox's renowned toughness, water resistance, and legibility. This watch is three times lighter than titanium as it is housed in a CARBONOX™+ case, which makes it extremely durable for military and outdoor activities. Best for those who want a sophisticated and luxurious watch that can endure the harshest environments. The Master Carbon SEAL Automatic is perfect for military personnel, adventurers, and anyone who wants a reliable timepiece that can withstand extreme conditions. With its constant glow feature for up to 25 years, Swiss automatic movement, and anti-reflective sapphire crystal glass material, this watch ensures ultimate visibility in any light condition.The day and date function of the watch also makes it perfect for everyday wear. Get ready to explore the world with the Luminox Carbon SEAL 45mm Automatic Military Dive Watch XS.3877 on your wrist!",\
        image='luminox3.webp', 
        price=1799.00,
        brand = 'Luminox',
        movement_type = 'Automatic',
        dial_colour = 'Black',
        strap_type = 'Rubber',
        style = 'Shape/Round',
        material = 'CARBONOX',
        collection = 'Master Carbon SEAL',
        glass = 'Sapphire Crystal',
        water_resistance = '200M',
        featured = False,
        quantity = 1,
        categories=[category1, category5] 
        )
    
    watch20 = Watch( 
        name="Loyal Men's Adventurer Quartz Chronograph Sport Watch",\
        description= "Discover sophisticated style and modern luxury with the Loyal Men's Adventurer Quartz Chronograph Sport Watch. This stylish timepiece is perfect for any outdoor adventure, featuring a quartz chronograph movement, rubber strap, and 100m water resistance. Whether you're swimming, diving, or just looking for an everyday watch that stands out from the crowd, the Adventurer is your go-to choice. Its sporty design and contemporary style make it the perfect accessory for any man who appreciates quality and craftsmanship. With its timeless elegance and functionality, this watch is essential for any modern gentleman's wardrobe.",\
        image='loyal1.webp', 
        price=499.00,
        brand = 'Loyal',
        movement_type = 'Quartz Chronograph',
        dial_colour = 'Black',
        strap_type = 'Rubber',
        style = 'Shape/Round',
        material = 'IP Grey',
        collection = 'Adventurer',
        glass = 'Mineral',
        water_resistance = '100M',
        featured = False,
        quantity = 1,
        categories=[category2, category3, category5] 
        )
    
    watch21 = Watch( 
        name="Casio G-Shock Women's Analogue Digital Watch GMAS2100GA-7A",\
        description= "The Casio G-Shock Women's Analogue Digital Watch GMAS2100GA-7A is a stylish and comfortable timepiece that combines analog and digital functionality. With its slim and compact design, this watch is perfect for those who want a modern and fashionable accessory. The watch features a flat face and simple bar index marks,",\
        image='casio6.webp', 
        price=259.00,
        brand = 'Casio',
        movement_type = 'Analogue Digital',
        dial_colour = 'Cream',
        strap_type = 'Rubber',
        style = 'Shape/Round',
        material = 'Resin',
        collection = 'G-Shock',
        glass = 'Mineral',
        water_resistance = '200M',
        featured = False,
        quantity = 1,
        categories=[category4] 
        )

    watches = [watch1, watch2, watch3, watch4, watch5, watch6, watch7, watch8, watch9, watch10, watch11, watch12, watch13, watch14, watch15, watch16, watch17, watch18, watch19, watch20, watch21]
    try:
        for watch in watches:
            db.session.add(watch)
        db.session.commit()
    except:
        return 'There was an issue adding a tour in dbseed function'

    return 'DATA LOADED'


