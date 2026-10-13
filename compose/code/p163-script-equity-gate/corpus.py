#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The equity corpus: ONE essay answer, the same content, in nine scripts.

The question is a school-biology staple -- "explain photosynthesis" -- so that
every row is a VALID answer a real learner could submit. Content parity is the
whole point: if a gate treats these differently, it is treating the SCRIPT
differently, not the answer.

Rows 10-13 are controls, labelled as such.
"""

CORPUS = [
    # --- the nine equivalent answers --------------------------------------
    ("en", "Latin", "English",
     "Photosynthesis is the process by which green plants convert light energy into "
     "chemical energy. Chlorophyll in the leaves absorbs sunlight, and the plant "
     "combines water drawn up from the roots with carbon dioxide taken in through the "
     "stomata. The products are glucose, which the plant uses for growth, and oxygen, "
     "which is released into the atmosphere."),

    ("de", "Latin", "German",
     "Die Photosynthese ist der Vorgang, bei dem grüne Pflanzen Lichtenergie in "
     "chemische Energie umwandeln. Das Chlorophyll in den Blättern nimmt das Sonnenlicht "
     "auf, und die Pflanze verbindet das über die Wurzeln aufgenommene Wasser mit dem "
     "durch die Spaltöffnungen eintretenden Kohlendioxid. Die Produkte sind Glukose, die "
     "die Pflanze zum Wachstum nutzt, und Sauerstoff, der in die Atmosphäre abgegeben wird."),

    ("es", "Latin", "Spanish",
     "La fotosíntesis es el proceso por el cual las plantas verdes convierten la energía "
     "luminosa en energía química. La clorofila de las hojas absorbe la luz del sol, y la "
     "planta combina el agua extraída por las raíces con el dióxido de carbono que entra "
     "por los estomas. Los productos son la glucosa, que la planta usa para crecer, y el "
     "oxígeno, que se libera a la atmósfera."),

    ("zh", "Han", "Chinese (Simplified)",
     "光合作用是绿色植物把光能转化为化学能的过程。叶片中的叶绿素吸收阳光,植物把从根部"
     "吸收的水和通过气孔进入的二氧化碳结合起来。产物是葡萄糖和氧气,葡萄糖供植物生长"
     "使用,氧气则被释放到大气中。"),

    ("ja", "Han+Kana", "Japanese",
     "光合成は、緑色植物が光エネルギーを化学エネルギーに変える働きです。葉の葉緑素が"
     "日光を吸収し、根から吸い上げた水と気孔から取り込んだ二酸化炭素を結びつけます。"
     "できるのはブドウ糖と酸素で、ブドウ糖は成長に使われ、酸素は大気中に放出されます。"),

    ("ko", "Hangul", "Korean",
     "광합성은 녹색 식물이 빛 에너지를 화학 에너지로 바꾸는 과정이다. 잎의 엽록소가 "
     "햇빛을 흡수하고, 식물은 뿌리에서 끌어올린 물과 기공으로 들어온 이산화탄소를 "
     "결합한다. 생성물은 포도당과 산소이며, 포도당은 생장에 쓰이고 산소는 대기로 "
     "방출된다."),

    ("ar", "Arabic", "Arabic (unvocalised)",
     "التركيب الضوئي هو العملية التي تحول بها النباتات الخضراء الطاقة الضوئية إلى طاقة "
     "كيميائية. يمتص الكلوروفيل في الأوراق ضوء الشمس، ويجمع النبات الماء الممتص من الجذور "
     "مع ثاني أكسيد الكربون الداخل عبر الثغور. والناتج هو الجلوكوز الذي يستخدمه النبات "
     "للنمو، والأكسجين الذي يتحرر في الغلاف الجوي."),

    ("ar-voc", "Arabic", "Arabic (vocalised, as in a primary reader)",
     "التَّرْكِيبُ الضَّوْئِيُّ هُوَ الْعَمَلِيَّةُ الَّتِي تُحَوِّلُ بِهَا النَّبَاتَاتُ الْخَضْرَاءُ الطَّاقَةَ الضَّوْئِيَّةَ إِلَى "
     "طَاقَةٍ كِيمِيَائِيَّةٍ. يَمْتَصُّ الْكْلُورُوفِيلُ فِي الْأَوْرَاقِ ضَوْءَ الشَّمْسِ، وَيَجْمَعُ النَّبَاتُ الْمَاءَ "
     "الْمُمْتَصَّ مِنَ الْجُذُورِ مَعَ ثَانِي أُكْسِيدِ الْكَرْبُونِ الدَّاخِلِ عَبْرَ الثُّغُورِ."),

    ("hi", "Devanagari", "Hindi",
     "प्रकाश संश्लेषण वह प्रक्रिया है जिसके द्वारा हरे पौधे प्रकाश ऊर्जा को रासायनिक ऊर्जा में बदलते हैं। "
     "पत्तियों में उपस्थित पर्णहरित सूर्य के प्रकाश को अवशोषित करता है, और पौधा जड़ों से खींचे गए पानी को "
     "रंध्रों से लिए गए कार्बन डाइऑक्साइड के साथ जोड़ता है। उत्पाद ग्लूकोज़ और ऑक्सीजन हैं।"),

    ("th", "Thai", "Thai",
     "การสังเคราะห์ด้วยแสงเป็นกระบวนการที่พืชสีเขียวเปลี่ยนพลังงานแสงให้เป็นพลังงานเคมี "
     "คลอโรฟิลล์ในใบดูดกลืนแสงแดด และพืชรวมน้ำที่ดูดขึ้นมาจากรากกับคาร์บอนไดออกไซด์"
     "ที่เข้ามาทางปากใบ ผลผลิตคือกลูโคสและออกซิเจน"),

    # --- controls, labelled -----------------------------------------------
    ("CTRL-mash", "Latin", "CONTROL: keyboard mash (must be REJECTED)",
     "a" * 49),

    ("CTRL-symbols", "n/a", "CONTROL: symbol spam (must be REJECTED)",
     "1234567890!@#$%^&*()1234567890!@#$%^&*()"),

    ("CTRL-extA", "Han ExtA", "CONTROL: Han outside the listed ranges (Ext A + Compatibility)",
     "㐀㐁㐂㐃㐄㐅㐆㐇㐈㐉㐊㐋㐌㐍㐎㐏豈更車賈滑串句龜龜契金喇奈"),

    ("CTRL-extB", "Han ExtB", "CONTROL: astral Han (CJK Extension B, surrogate pairs)",
     "\U00020000\U00020001\U00020002\U00020003\U00020004\U00020005\U00020006"
     "\U00020007\U00020008\U00020009\U0002000A\U0002000B\U0002000C\U0002000D"
     "\U0002000E\U0002000F\U00020010\U00020011"),
]
