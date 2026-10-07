#!/usr/bin/env python3
"""Ten Impossible Problems — writes docs/index.html, docs/th/index.html, llms.txt, sitemap, robots, icon."""
import html, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
BASE = "https://nanobotco.github.io/impossible/"

PAGE = {
    "en": {
        "title": "Ten Impossible Problems",
        "kick": "NaN Peacock · hongdam.net, Chiang Rai",
        "lede": "Ten problems that looked impossible, and what NaN Peacock built for each. Tap a picture to open the live site.",
        "desc": "Ten problems that looked impossible, and what NaN Peacock built for each: learning apps, games, drawn maps, Thai search, open-weight models, maths of Thai design.",
        "problem": "Problem", "built": "Built", "open": "Open",
        "other": "ไทย", "other_href": "th/",
        "foot": "Text CC BY 4.0, NaNoBotCo. Code MIT.",
    },
    "th": {
        "title": "สิบโจทย์ที่ว่าทำไม่ได้",
        "kick": "NaN Peacock · hongdam.net เชียงราย",
        "lede": "สิบโจทย์ที่ดูเหมือนทำไม่ได้ กับสิ่งที่ NaN Peacock สร้างขึ้นตอบแต่ละข้อ แตะรูปเพื่อเปิดเว็บ",
        "desc": "สิบโจทย์ที่ดูเหมือนทำไม่ได้ กับสิ่งที่ NaN Peacock สร้างขึ้นตอบ: แอปเรียน เกม แผนที่วาด ค้นภาษาไทย โมเดลเปิด คณิตศาสตร์ของลายไทย",
        "problem": "โจทย์", "built": "สิ่งที่สร้าง", "open": "เปิด",
        "other": "EN", "other_href": "../",
        "foot": "ข้อความ CC BY 4.0, NaNoBotCo · โค้ด MIT",
    },
}

ITEMS = [
    {
        "img": "thai-drawn", "url": "https://motdang.net/sites/thai-drawn/",
        "en": ("Thai, Drawn",
               "Learn to read Thai — 44 consonants, five tones, and a tone rule that turns on consonant class, vowel length and the final sound — from study material scattered across ten sources in her projects.",
               "One app in one drawn style. A letter answered right twice moves its picture into the letter village. A tone machine, checked by 25 tests. 467 words in 24 decks, 1,117 street signs from Chiang Mai and Chiang Rai, 44 animated paper-cut letter pictures."),
        "th": ("Thai, Drawn · ไทยวาดเล่น",
               "อ่านภาษาไทยให้ได้ พยัญชนะ 44 ตัว วรรณยุกต์ 5 เสียง กฎผันเสียงที่ขึ้นกับอักษรกลางสูงต่ำ สระสั้นยาว และตัวสะกด จากสื่อเรียนที่กระจายอยู่สิบแหล่งในโปรเจกต์ของเธอ",
               "แอปเดียว ภาพวาดสไตล์เดียว ตอบตัวอักษรถูกสองครั้ง รูปของมันย้ายเข้าหมู่บ้านตัวอักษร เครื่องผันวรรณยุกต์ผ่านการทดสอบ 25 ข้อ คำศัพท์ 467 คำใน 24 ชุด ป้ายร้าน 1,117 ป้ายจากเชียงใหม่และเชียงราย ภาพตัดกระดาษเคลื่อนไหวของพยัญชนะ 44 ตัว"),
    },
    {
        "img": "rider", "url": "https://motdang.net/sites/rider/",
        "en": ("Rider",
               "A daily delivery puzzle needs a fair target score every day, on Chiang Mai's one-way roads, with shops that open only at their posted hours.",
               "Each day the game tries every order of stops and sets par in under 5 ms. Riding to the nearest stop lands about 87% of par, so three stars take planning. After each leg it shows the better next stop and the baht given up. One-way moat roads, the evening walking streets and this hour's rain change the routes; 234 legend cards wait along them."),
        "th": ("Rider · ไรเดอร์",
               "เกมส่งของรายวันต้องมีคะแนนเป้าที่ยุติธรรมทุกวัน บนถนนวันเวย์ของเชียงใหม่ กับร้านที่เปิดตามเวลาที่ติดไว้เท่านั้น",
               "ทุกวันเกมลองทุกลำดับจุดส่ง แล้วตั้งค่าพาร์ในเวลาไม่ถึง 5 มิลลิวินาที ขี่ไปจุดที่ใกล้ที่สุดเรื่อยๆ ได้ราว 87% ของพาร์ สามดาวต้องวางแผน จบแต่ละช่วงเกมบอกจุดถัดไปที่ดีกว่าและเงินที่เสียไป ถนนวันเวย์รอบคูเมือง ถนนคนเดินตอนเย็น และฝนชั่วโมงนี้เปลี่ยนเส้นทาง การ์ดตำนาน 234 ใบรออยู่ระหว่างทาง"),
    },
    {
        "img": "kranok", "url": "https://motdang.net/sites/kranok/",
        "en": ("Kranok, Drawn",
               "Write the Thai flame motif as maths. It is taught by hand, stroke by stroke; no published formula for its curl turned up.",
               "The flame comes from one bending graph: curvature along the line, a log-spiral curl, a flick at the tip. The page nests it, sorts friezes into their seven symmetry groups, and lets readers draw their own. The research set two common readings straight: กนก alone means gold, and the pattern word is กระหนก."),
        "th": ("Kranok, Drawn · กระหนก",
               "เขียนลายกระหนกเป็นคณิตศาสตร์ ลายนี้สอนกันด้วยมือทีละเส้น ไม่พบสูตรของขดเปลวที่ตีพิมพ์ไว้",
               "เปลวทั้งตัวเกิดจากกราฟความโค้งเส้นเดียว: ความโค้งไล่ตามเส้น ขดแบบเกลียวลอการิทึม และตวัดที่ปลาย หน้าเว็บซ้อนลายเป็นชั้น จัดลายขอบเป็นกลุ่มสมมาตร 7 แบบ และให้ผู้อ่านวาดเอง งานค้นคว้ายังแก้ความเข้าใจที่พบบ่อยสองข้อ: กนก คำเดียวแปลว่าทอง ส่วนชื่อลายคือ กระหนก"),
    },
    {
        "img": "warp", "url": "https://nanobotco.github.io/warp-and-weft/",
        "en": ("Warp and Weft",
               "Read a Khmer ikat shawl from one phone photo. A vision model called its animals elephants.",
               "Checked against rendered Khmer script, the gold word matches គោ, cow. The site redraws the shawl and turns weaving into toys: a loom, a draft from threading, tie-up and treadling, ikat in seven steps, the gcd rule for satin, the ~900 m of silk in one cocoon. In English, Thai and Khmer."),
        "th": ("Warp and Weft · เส้นยืน เส้นพุ่ง",
               "อ่านผ้าคลุมไหล่มัดหมี่เขมรจากรูปถ่ายมือถือรูปเดียว โมเดลอ่านภาพบอกว่าสัตว์บนผ้าคือช้าง",
               "เทียบกับอักษรเขมร คำสีทองตรงกับ គោ แปลว่าวัว เว็บวาดผ้าผืนนั้นขึ้นใหม่ และเปลี่ยนการทอเป็นของเล่น: กี่ทอ แบบร้อยตะกอ มัดหมี่ 7 ขั้น กฎ ห.ร.ม. ของลายต่วน เส้นไหมราว 900 เมตรในรังไหมหนึ่งรัง เป็นภาษาอังกฤษ ไทย และเขมร"),
    },
    {
        "img": "thai-time", "url": "https://nanobotco.github.io/thai-time/",
        "en": ("Telling Time in Thai",
               "Rebuild Lanna time: a day of 16 watches, 90 minutes each, and a 60-day cycle of named days. An earlier clock project dropped the day cycle for want of a fixed date to count from.",
               "The anchor came from the 2022 RMUTL Lanna calendar — 1 January 2022 is กาบยี — and its arithmetic matches the calendar's April and December rows. The Royal Gazette page that set the six-hour clock was read from the original: dated 1900, where English Wikipedia says 1901. A coconut water clock sinks on Torricelli's law."),
        "th": ("Telling Time in Thai · บอกเวลาแบบไทย",
               "สร้างเวลาล้านนาขึ้นใหม่: วันหนึ่งมี 16 ยาม ยามละ 90 นาที และวันไทที่วนรอบ 60 วัน โปรเจกต์นาฬิกาก่อนหน้าตัดรอบวันไทออก เพราะไม่มีวันตั้งต้นให้นับ",
               "จุดตั้งต้นมาจากปฏิทินล้านนา มทร.ล้านนา ปี 2565: 1 มกราคม 2565 เป็นวันกาบยี เลขคำนวณตรงกับแถวเดือนเมษายนและธันวาคมในปฏิทินเล่มนั้น ราชกิจจานุเบกษาที่กำหนดการนับโมงทุ่ม อ่านจากต้นฉบับ: ลงวันที่ ร.ศ. 119 (ค.ศ. 1900) ส่วนวิกิพีเดียภาษาอังกฤษเขียน 1901 กะลาลอยจมตามกฎของทอร์ริเชลลี"),
    },
    {
        "img": "north", "url": "https://motdang.net/sites/doodle-north/",
        "en": ("The North, Doodled",
               "Hand-draw a map of northern Thailand at every zoom, down to the soi. No hand can redraw a region street by street.",
               "An engine reads a 244 MB open map archive tile by tile in the reader's browser and draws it as a doodle: washes without seams at the tile edges, small trees in the woods, names in one language at a time. 84,147 place pages on motdang.net open on a drawn map."),
        "th": ("The North, Doodled · ภาคเหนือ ลายเส้น",
               "วาดแผนที่ภาคเหนือด้วยลายมือทุกระดับซูมจนถึงซอย ไม่มีมือไหนวาดทั้งภาคทีละถนนไหว",
               "ตัวโปรแกรมอ่านคลังแผนที่เปิดขนาด 244 MB ทีละแผ่นในเบราว์เซอร์ของผู้อ่าน แล้ววาดเป็นลายเส้น: สีระบายไม่มีรอยต่อที่ขอบแผ่น ต้นไม้เล็กๆ ในป่า ชื่อทีละภาษา หน้าสถานที่ 84,147 หน้าบน motdang.net เปิดบนแผนที่วาด"),
    },
    {
        "img": "own", "url": "https://hongdam.net/own",
        "en": ("Your own builder",
               "Get open-weight models, cheap enough for a Thai small business, to write pages without inventing facts. Every model tested gave the same hospital a different phone number.",
               "One instruction file, tested on seven models: 65% of checks passed with no file, 99.4% with it in English, 96.8% in Thai. With it, an open-weights agent wrote and published Golden Triangle, nine pages in Thai and English, from one brief in 10 minutes 21 seconds."),
        "th": ("Your own builder · เครื่องสร้างเว็บของคุณเอง",
               "ทำให้โมเดลเปิด ราคาที่ธุรกิจเล็กในไทยจ่ายไหว เขียนเว็บได้โดยไม่แต่งข้อเท็จจริงเอง ทุกโมเดลที่ทดสอบให้เบอร์โทรโรงพยาบาลเดียวกันคนละเบอร์",
               "ไฟล์คำสั่งไฟล์เดียว ทดสอบกับ 7 โมเดล: ไม่มีไฟล์ผ่าน 65% ฉบับอังกฤษผ่าน 99.4% ฉบับไทยผ่าน 96.8% เอเจนต์โมเดลเปิดใช้ไฟล์นี้เขียนและเผยแพร่เว็บสามเหลี่ยมทองคำ เก้าหน้า ไทยและอังกฤษ จากบรีฟเดียวใน 10 นาที 21 วินาที"),
    },
    {
        "img": "nitpick", "url": "https://nanobotco.github.io/nitpick/",
        "en": ("nitpick",
               "Read every shop sign from a 360° camera on a moving scooter. Each frame is 7680 × 3840, the Mac's Thai text reader works only at full scale, and sending whole frames to a model burns through the budget.",
               "The Mac reads every sign first and matches it to known places; the model sees only the crops it could not place, packed onto sheets. On the same 12 frames: 33 places found against 34 the old way, 54k tokens of context re-read per frame against 241k, 9 turns against 138."),
        "th": ("nitpick",
               "อ่านป้ายร้านทุกป้ายจากกล้อง 360° บนสกู๊ตเตอร์ที่กำลังวิ่ง ภาพละ 7680 × 3840 พิกเซล ตัวอ่านอักษรไทยใน Mac อ่านได้เฉพาะที่ขนาดเต็ม และการส่งภาพทั้งภาพให้โมเดลกินงบหมด",
               "Mac อ่านป้ายทุกป้ายก่อน แล้วจับคู่กับสถานที่ที่รู้จัก โมเดลเห็นเฉพาะภาพตัดที่จับคู่ไม่ได้ จัดเรียงลงแผ่น ภาพชุดเดียวกัน 12 ภาพ: พบ 33 สถานที่ วิธีเดิมพบ 34 อ่านบริบทซ้ำ 54k โทเคนต่อภาพ วิธีเดิม 241k ใช้ 9 รอบ วิธีเดิม 138 รอบ"),
    },
    {
        "img": "find", "url": "https://motdang.net/find",
        "en": ("motdang.net/find",
               "Search Thai, a language written without spaces. The standard database search treats Thai tone marks as word breaks, so ก matched inside ก๋วยเตี๋ยว.",
               "One search box over 113,567 pages of her sites: Thai split by dictionary when indexing and when searching, a boolean door and a lucky door, 40–100 ms at the edge, and a meaning re-rank for what the words miss. On a public test set of spoken requests, the unspaced Thai it reads rose from 17% to 66%."),
        "th": ("motdang.net/find · ค้นหา",
               "ค้นภาษาไทย ภาษาที่เขียนติดกันไม่เว้นวรรค ระบบค้นหามาตรฐานของฐานข้อมูลถือว่าวรรณยุกต์เป็นตัวตัดคำ ค้น ก เลยไปเจอใน ก๋วยเตี๋ยว",
               "ช่องค้นเดียวครอบคลุมเว็บของเธอ 113,567 หน้า ตัดคำไทยด้วยพจนานุกรมทั้งตอนเก็บและตอนค้น มีทางบูลีนและปุ่ม Lucky ตอบใน 40–100 มิลลิวินาที และจัดอันดับตามความหมายเมื่อคำไม่ตรง ในชุดทดสอบคำขอแบบพูดที่เปิดสาธารณะ คำขอภาษาไทยไม่เว้นวรรคที่อ่านออกเพิ่มจาก 17% เป็น 66%"),
    },
    {
        "img": "wave", "url": "https://motdang.net/sites/wave-at-home/",
        "en": ("Wave It at Home",
               "Thai 7-Eleven meals carry a button code, กด 5, for the store's commercial oven. No official table turning a code into minutes on a home microwave turned up.",
               "From the pack labels: the store ovens are named at 1,800 W and 1,300 W, and codes 2 to 6 rise ×1.46 a step. Code 1 comes from the curve, 7 and 8 from frozen packs. 24 packs, each with its home time. The gaps are listed on the page."),
        "th": ("Wave It at Home · เวฟที่บ้าน",
               "อาหารเซเว่นมีรหัสปุ่ม เช่น กด 5 สำหรับไมโครเวฟของร้าน ยังไม่พบตารางทางการที่แปลงรหัสเป็นนาทีบนไมโครเวฟที่บ้าน",
               "จากฉลากบนแพ็ก: เตาในร้านระบุ 1,800 วัตต์และ 1,300 วัตต์ รหัส 2 ถึง 6 เพิ่มขั้นละ ×1.46 รหัส 1 ได้จากเส้นโค้ง รหัส 7 และ 8 ได้จากแพ็กแช่แข็ง 24 แพ็ก พร้อมเวลาที่บ้านทุกแพ็ก ช่องว่างที่ยังขาดเขียนไว้บนหน้า"),
    },
]

CSS = """:root{--night:#100c1c;--rock:#1b1530;--ink:#f4eee0;--dim:#bdb4d0;--gold:#ffc94d;--coral:#ff7a6b;--line:#2e2648}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--night);color:var(--ink);font:18px/1.6 "Noto Sans Thai",system-ui,-apple-system,"Segoe UI",sans-serif;overflow-x:hidden}
html[lang=th] body{line-height:1.75}
a{color:var(--gold)}
h1,h2{font-family:Fraunces,"Noto Serif Thai",Georgia,serif;font-weight:700;line-height:1.1;margin:0}
html[lang=th] h1,html[lang=th] h2{font-family:"Noto Serif Thai",Fraunces,serif;line-height:1.35}
.in{max-width:1080px;margin:0 auto;padding:0 16px}
header{padding:20px 0 0}
header .in{display:flex;justify-content:flex-end}
.lang{font-size:15px;border:1px solid var(--line);border-radius:999px;padding:4px 14px;text-decoration:none;color:var(--dim)}
.hero{padding:56px 0 40px}
.kick{font-size:15px;letter-spacing:.03em;color:var(--dim);margin:0 0 14px;font-weight:600}
h1{font-size:clamp(44px,9vw,104px);color:var(--gold)}
h1 .ten{color:var(--coral)}
.lede{max-width:34em;color:var(--dim);font-size:clamp(18px,2.2vw,21px);margin:20px 0 0}
ol.list{list-style:none;margin:0;padding:0}
li.item{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:36px;align-items:start;padding:44px 0;border-top:1px solid var(--line)}
li.item:nth-child(even) a.shot{order:2}
a.shot{position:relative;display:block;overflow:hidden;border-radius:14px;border:1px solid var(--line);color:#fff;text-decoration:none}
a.shot .bg{position:absolute;inset:0;background-size:cover;background-position:center top;transition:transform .9s cubic-bezier(.3,1.1,.4,1)}
a.shot .scrim{position:absolute;inset:0;background:linear-gradient(180deg,rgba(16,12,28,0) 45%,rgba(16,12,28,.92) 100%)}
a.shot .sp{display:block;padding-top:52.5%}
a.shot .tx{position:absolute;left:0;right:0;bottom:0;padding:14px 18px;display:flex;justify-content:space-between;align-items:baseline;gap:12px}
a.shot .tx b{font-family:Fraunces,"Noto Serif Thai",Georgia,serif;font-size:22px;color:var(--gold)}
a.shot .tx i{font-style:normal;font-size:14px;color:var(--dim);white-space:nowrap}
a.shot:hover .bg{transform:scale(1.04)}
a.shot:focus-visible{outline:2px solid var(--gold);outline-offset:3px}
.num{font-family:Fraunces,Georgia,serif;font-size:56px;line-height:1;color:var(--coral);margin:0 0 8px}
h2{font-size:clamp(26px,3.6vw,36px);margin-bottom:16px}
.lab{display:block;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--gold);font-weight:700;margin-top:14px}
html[lang=th] .lab{letter-spacing:0;text-transform:none;font-size:15px}
.txt p{margin:4px 0 0}
.txt p.prob{color:var(--ink)}
.txt p.built{color:var(--dim)}
footer{border-top:1px solid var(--line);padding:28px 0 40px;color:var(--dim);font-size:14px}
html.card body{width:1200px;height:630px;overflow:hidden}
html.card header,html.card ol.list,html.card footer{display:none}
html.card .lede{font-size:22px;margin-top:14px}
html.card .hero{padding:44px 0 0}
html.card h1{font-size:96px}
.mosaic{display:none}
html.card .mosaic{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;max-width:1080px;margin:28px auto 0;padding:0 16px}
.mosaic div{padding-top:52.5%;background-size:cover;background-position:center top;border-radius:8px;border:1px solid var(--line)}
@media (max-width:760px){li.item{grid-template-columns:1fr;gap:20px;padding:32px 0}li.item:nth-child(even) a.shot{order:0}.num{font-size:44px}.hero{padding:36px 0 28px}}"""


def esc(s):
    return html.escape(s, quote=True)


def page(lang):
    P = PAGE[lang]
    pre = "" if lang == "en" else "../"
    url = BASE if lang == "en" else BASE + "th/"
    rows = []
    for n, it in enumerate(ITEMS, 1):
        name, prob, built = it[lang]
        host = it["url"].split("//", 1)[1].rstrip("/")
        rows.append(
            f'<li class="item" id="n{n}"><a class="shot" href="{esc(it["url"])}">'
            f'<span class="bg" style="background-image:url({pre}img/{it["img"]}.jpg)"></span><span class="scrim"></span><span class="sp"></span>'
            f'<span class="tx"><b>{esc(P["open"])} →</b><i>{esc(host)}</i></span></a>'
            f'<div class="txt"><p class="num">{n:02d}</p><h2>{esc(name)}</h2>'
            f'<span class="lab">{esc(P["problem"])}</span><p class="prob">{esc(prob)}</p>'
            f'<span class="lab">{esc(P["built"])}</span><p class="built">{esc(built)}</p></div></li>')
    mosaic = "".join(f'<div style="background-image:url({pre}img/{it["img"]}.jpg)"></div>' for it in ITEMS)
    title = P["title"]
    h1 = esc(title).replace("Ten", '<span class="ten">Ten</span>', 1).replace("สิบ", '<span class="ten">สิบ</span>', 1)
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": title, "url": url, "inLanguage": lang,
          "author": {"@type": "Person", "name": "NaN Peacock"},
          "publisher": {"@type": "Organization", "name": "Hongdam", "url": "https://hongdam.net/"},
          "hasPart": [{"@type": "WebSite", "name": it[lang][0], "url": it["url"]} for it in ITEMS]}
    return f"""<!doctype html><html lang="{lang}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(P['desc'])}">
<meta name="theme-color" content="#100c1c">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{BASE}"><link rel="alternate" hreflang="th" href="{BASE}th/"><link rel="alternate" hreflang="x-default" href="{BASE}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Ten Impossible Problems · สิบโจทย์ที่ว่าทำไม่ได้">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(P['desc'])}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}card.jpg"><meta property="og:image:type" content="image/jpeg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Ten Impossible Problems, over pictures of the ten sites">
<meta property="og:locale" content="{'en_US' if lang == 'en' else 'th_TH'}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{BASE}card.jpg">
<link rel="icon" href="{pre}icon.svg" type="image/svg+xml">
<link rel="alternate" type="text/plain" href="{BASE}llms.txt" title="llms.txt">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,700&family=Noto+Sans+Thai:wght@400;600;700&family=Noto+Serif+Thai:wght@700&display=swap" rel="stylesheet">
<script>if(/[?&]card/.test(location.search))document.documentElement.classList.add("card")</script>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{CSS}</style></head><body>
<header><div class="in"><a class="lang" href="{P['other_href']}" hreflang="{'th' if lang == 'en' else 'en'}">{P['other']}</a></div></header>
<main><section class="hero"><div class="in"><p class="kick">{esc(P['kick'])}</p><h1>{h1}</h1><p class="lede">{esc(P['lede'])}</p></div>
<div class="mosaic">{mosaic}</div></section>
<div class="in"><ol class="list">{''.join(rows)}</ol></div></main>
<footer><div class="in">{esc(P['foot'])} · <a href="https://github.com/NaNoBotCo/impossible">GitHub</a> · <a href="https://motdang.net/">motdang.net</a> · <a href="https://hongdam.net/">hongdam.net</a></div></footer>
</body></html>
"""


def llms():
    out = ["# Ten Impossible Problems · สิบโจทย์ที่ว่าทำไม่ได้", "", "> " + PAGE["en"]["desc"], "",
           "Made by hongdam.net, Chiang Rai. English: " + BASE + " · Thai: " + BASE + "th/", ""]
    for n, it in enumerate(ITEMS, 1):
        name, prob, built = it["en"]
        out += [f"## {n}. {name}", it["url"], "", "Problem: " + prob, "", "Built: " + built, ""]
    return "\n".join(out)


ICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#100c1c"/><text x="32" y="44" text-anchor="middle" font-family="Georgia,serif" font-size="34" font-weight="700" fill="#ffc94d">10</text></svg>
"""

if __name__ == "__main__":
    (DOCS / "th").mkdir(parents=True, exist_ok=True)
    (DOCS / "index.html").write_text(page("en"), encoding="utf-8")
    (DOCS / "th" / "index.html").write_text(page("th"), encoding="utf-8")
    (DOCS / "llms.txt").write_text(llms(), encoding="utf-8")
    (DOCS / "icon.svg").write_text(ICON, encoding="utf-8")
    (DOCS / "robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: " + BASE + "sitemap.xml\n", encoding="utf-8")
    (DOCS / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"<url><loc>{BASE}</loc></url><url><loc>{BASE}th/</loc></url></urlset>\n", encoding="utf-8")
    print("built", DOCS)
