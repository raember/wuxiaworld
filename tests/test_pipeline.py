import unittest

from urllib3.util import parse_url

from lightnovel.wuxiaworld_com import WuxiaWorldComApi
from pipeline import ChapterConflation
from tests.config import Har, prepare_browser


class WuxiaWorldComApiHjcTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = prepare_browser(Har.WW_HJC_COVER_C1_2)

    def test_conflation_chapter_1_2(self):
        api = WuxiaWorldComApi(self.browser)
        novel = api.get_novel(parse_url('https://www.wuxiaworld.com/novel/heavenly-jewel-change'))
        novel.parse()
        chapter1 = api.get_chapter(
            parse_url('https://www.wuxiaworld.com/novel/heavenly-jewel-change/hjc-book-1-chapter-1-01'))
        chapter1.parse()
        chapter1._book = novel.books[0]
        chapter1.book.chapters.append(chapter1)
        chapter2 = api.get_chapter(
            parse_url('https://www.wuxiaworld.com/novel/heavenly-jewel-change/hjc-book-1-chapter-1-02'))
        chapter2.parse()
        chapter2._book = novel.books[0]
        chapter2.book.chapters.append(chapter2)

        chapter1.clean_content()
        chapter2.clean_content()

        self.assertTrue(ChapterConflation.can_be_conflated(chapter1, chapter2))
        ChapterConflation.conflate(chapter1, chapter2)

        self.maxDiff = None
        # noinspection SpellCheckingInspection
        self.assertEqual("""
Heavenly Bow Empire Capital City, Heavenly Bow City, Official Roads.
Heavenly Bow Empire is a small country in the western regions of Boundless Mainland (Hao Miao Da Lu). It isn’t bound to any larger countries, and its environment and climate are extremely suitable for humans to live in.
The weather was great today, the vast expanse of the sky seemed like a large blue crystal, with nary a blemish in sight. The only issue one might find would be that the clarity of the air caused the sunshine to be rather glaring on the eyes. Luckily, the official roads were lined with 100-year or older Sycamore Trees, their thick branches massed with leaves sheltering the wide roadways. This formed the famous boulevard which everyone in Heavenly Bow Empire knew about, stretching for nearly 100 li (50km) into a forest.
Heavenly Bow City had a very unique geographical location, in fact it could be almost described as second-to-none. This was because this capital city was totally surrounded by huge forests, and Heavenly Bow City was just like a brilliant jewel in the midst of the forest. Although Heavenly Bow Empire wasn’t particularly strong, its capital city was still quite famous. The surrounding forests were called Stars Forest, because this was the only place in the whole continent where the Stars Trees grew. The heart of the Stars Trees were extremely valuable materials in making top end bows. As such, with such an important natural resource, one could imagine the prosperity that Heavenly Bow City enjoyed.
Currently, a youth who looked around 15-16 years old was walking along the boulevard, muttering to himself.
“To be a playboy is to train the mind, to have an affair is to train the heart, chasing after girls will prevent old age, flirting is therapeutic, having a crush on someone means your heart will always be young, being lovesick is the cure for insomnia!
They often say that Heroes are unable to cross the beautiful maiden barrier [1. It's a chinese saying that means heroes are often susceptible to a pretty face, causing them to be fallen.], but what hero will think like this? Should the hero leave the beauty to some useless fellow? And what would the beauty think, wouldn’t she prefer to have the hero instead as well?
Another saying is that Rabbits don’t eat the grass near their nests [2. Literal translation of another Chinese idiom, it means that even villains won’t commit sins close to home. However his rant here is talking on the literal meaning of it.], but why would rabbits do that? Should they let other rabbits eat the grass? Even the grass won’t think like that, after all being eaten is being eaten, does it matter by whom? Why not let someone familiar eat them!
Yet another saying is that if you have money, you can make the devil push the millstone for you [3. Money makes the world go round], but the devil would think that it’s a given thing – after all shouldn’t labour of pushing the millstone be rewarded? Even money would think differently, after all, being given to the devil will not harm the devil, but if given to humans the scenario might be different! Hahahaha…”
The youth was tall, with broad shoulders, with a healthy strong look. He had black eyes and hair, and was dressed in a cloth shirt with its sleeves rolled up, showing off his arms. His skin colour was a healthy sheen of bronze, and his features had a heroic spirit within. He might not be very handsome, but was overall pleasing to the eye. Just judging by outward appearance, the words simple and honest would be an apt description. However, the words that streamed out from his mouth were the total opposite of simple and honest. Of course, he only revealed his true colours when there was nobody else around.
“Sigh… not being able to cultivate heavenly energy is such a tragedy. In today’s day and age, looking good is useless, only heavenly energy and heavenly jewels are king. Ahhhh… Heavens! Earth! Gods! Why do you play me like this, letting I, Zhou Weiqing, be born with such a body with blocked meridians yet such a handsome face? Not letting me be a Heavenly Jewel Master is such a waste of great talent ah!” Of course, the handsome face he referred to was only of his own belief, and as he spoke the youth rudely gave the sky the finger.
Of course, he wasn’t the sort to just blame heaven, after pointing the middle finger he said comfortingly to himself: “Oh well, not being able to cultivate Heavenly Energy has its good side as well. That old geezer is already so strict, if I really awakened a Heavenly Jewel, maybe my life would be worse now by a hundred times? At least now the old geezer has given up on me, and leading the decadent life of a rich official’s son seems not a bad choice. I’ll go take a bath now!” As he spoke, his face revealed his trademark honest smile. Of course, those who really knew him, Zhou Weiqing’s honest smile hid his true rascally nature.
Even though Zhou Weiqing was unable to cultivate heavenly energy, his youthful body was still extremely healthy and strong. He was only 13 years old this year, and yet he looked like a youth of 15 – 16. At least in this, he was following in his father’s footsteps.
After walking about 5 li along the boulevard to the Stars Forest, Zhou Weiqing suddenly swerved into the woods. He had grown up in the woods, especially ever since he was 8 years old when he had tested out to have his meridians blocked and unable to cultivate heavenly energy. Zhou Weiqing’s father no longer forced him to train, so his favourite thing to do was to run alone into the forest to play. There were no Heavenly Beasts in the Stars Forest, and it was one of the safest forests on the continent.
After entering the Stars Forest, Zhou Weiqing could practically navigate his way around with his eyes closed, after all he knew the place like the back of his hand. After walking for about an hour, he finally heard sounds of running water as he neared his destination. Thinking about the sweet, clear lakewater, Zhou Weiqing hastened his steps. It was a hot day and he was eager to relax in the cooling waters of the lake.
Not far from the path in the Stars Forest there lay a lake, and its waters originated from an underground ice spring. It was only about 100m in diameter, and was surrounded by large thick trees. As a result, not many people knew about this lake, but Zhou Weiqing had came across it by accident in the past. He had a natural liking for water and since he had no friends, he spent a lot of time bathing and relaxing in the lake.
Moving around a large tree, the Ice Spring Lake was right ahead. Zhou Weiqing did not rush to dive into the waters, but first took off his clothes and laid them at the side, before squatting down at the edge of the waters to look at his reflection, muttering to himself: “Damn! I’ve become more handsome again!”
Just as he was reflecting on his own looks narcissistically, he suddenly heard a splash, causing him to look up, and the sight that greeted him caused him to gape in surprise.
From the other end of the lake, someone else had just jumped into the water, causing the waters to splash out. As the rays of sunshine shone upon the lake, the refraction of light causing the area to seem to be bathed in gold. In the midst of the water ripples, a head of pink hair captured Zhou Weiqing’s attention.
The Ice Spring Lake’s water was pretty shallow, only a metre or so deep, and the young girl who had leapt into the lake had her back facing Zhou Weiqing, and the lake waters just covered her buttocks. Still, Zhou Weiqing was able to see her slim waist and alluring figure.
“This… this…”
With a light *pooh* sound, 2 lines of blood streamed down from Zhou Weiqing’s nostrils. Even though this fellow often had sexual fantasies, he was after all still a 13 year old virgin boy, no matter how precocious. Seeing a naked young girl at such close proximity for the first time was so exciting to him that his nose started bleeding.
“Wow, this is so awesome!” Zhou Weiqing quickly held his nose, but his eyes kept staring at the girl, completely forgetting how exposed he was to being found, he could only chant in his mind Turn around! Turn around!
As if the pink haired girl had heard his internal prayers, she actually slowly turned around, she seemed excited and her hands were on the top of the water as she turned towards Zhou Weiqing.
Zhou Weiqing’s eyes widened as his dreams were about to come true. Just at that moment, a feminine voice shouted out “Your highness, be careful! There’s someone here!”
Upon hearing the shout, the pink haired girl acted like a startled little bird, quickly ducking into the water up to her neck, as she looked around in panic.
Before Zhou Weiqing could react, he felt his body lighten, and the world spin around him. With a plopping sound, he landed on the ground.
“What happened?” Although Zhou Weiqing was unable to cultivate heavenly energy, but he had been training under his strict father since young, and his body was in a fit condition, definitely stronger and more agile than any commoner, and he executed a roll on the ground before standing up.
About 3 metres in front of him, a young lady of about 20 years of age stood glaring at him. She seemed rather plain looking, and was dressed in leather armor with a sword in hand, with a bow made of Star Wood holstered on her back.
Zhou Weiqing immediately recognized the symbols of Star Flowers etched upon her leather armor, it was reserved only for the Royal household – could this young lady in front of him be a Royal Guard?
What really drew Zhou Weiqing’s attention was the 3 Jewels surrounding the lady’s right wrist. The 3 jewels were a type of jade, and with Zhou Weiqing’s good vision and the radiance of the jade, he could see clearly that it was about 30% Waxy Jade, 30% Ice Jade and 40% Dragonstone Jade.
Even though Zhou Weiqing personally could not cultivate, but he knew that those 3 jewels on her right wrist were no mere ornaments, but a sign of power.
In the Boundless Mainland, a person’s actual strength could be determined in 3 ways, and if you stood out in any particular way, you could be considered a strong person. The 3 ways were Heavenly Energy, Physical Jewels and Elemental Jewels.
Humans believed that they were the highest ranked species in the world that the gods have created, and that the human body was truly a gift from the gods. There were many different types of cultivating methods, and the strength achieved from that was known as heavenly energy. Heavenly energy was divided into 4 large hierarchies, Heavenly Jing Energy, Heavenly Xu Energy, Heavenly God Energy, and Heavenly Dao Energy.
Each of those hierarchies were further divided into 12 levels. It was rumoured that someone who had reached the highest level of the Heavenly Dao Energy was able to harness the energies of the universe, able to destroy and create and be extremely long lived. In any case, no matter Physical Jewel Masters or Elemental Jewel Masters, the basics of everything was Heavenly Energy. Without sufficient Heavenly Energy, it did not matter how good the quality of the Power Jewels were.
In the huge Boundless Mainland, when humans were born, they all had their own inborn Power Jewel. However, nobody could tell in advance what their Jewel was, and only when Heavenly Energy had been cultivated till the 3rd level of Heavenly Jing Energy, would their Power Jewels be Awakened.
The cultivation of Heavenly Jing Energy was extremely difficult, especially the introductory stages, one had to have the talent to communicate with their own Power Jewels to be able to cultivate successfully. The first 3 levels of Heavenly Jing Energy was tantamount to being reborn 3 times, and less than 1% of the population could actually complete it.
Once someone could complete the first 3 levels of Heavenly Jing Energy cultivation and Awaken their Power Jewels, then they would finally break out of being a commoner and take the first step into being a powerhouse. As Zhou Weiqing had blocked meridians and could not cultivate, thus he was doomed to be unable to complete the first 3 levels and Awaken his Power Jewels, and could only be an ordinary person.
Power Jewels had 2 forms after Awakening. Those that appeared around the right wrist were known as Physical Jewels. Those that appeared around the left wrist were known as Elemental Jewels. Physical Jewels and Elemental Jewels were inherently different. In general those with Physical Jewels were strong warriors, and each Physical Jewel could not only strengthen the physical attributes of the Physical Jewel Master, but also coalesce into a weapon or armor piece, which greatly strengthened the Physical Jewel Master. On the other hand, those with Elemental Jewels were gifted with greater brain energy, and they could make use of their Elemental Jewels to control the various elements they were aligned to, and they could also seal skills into their Elemental Jewels.
For both Physical Jewel Masters and Elemental Jewel Masters, the basic way to tell their strength was the number of jewels. For them, there was a max of 9 Power Jewels, those who had 1-3 Jewels were known as Shi Stage, 4-6 Jewels were known as Zun Stage, and 7-9 Jewels were known as Zong Stage. Each Stage also had an lower, middle and upper level. As such, the lady Royal Guard in front of Zhou Weiqing now was a upper level Shi Stage Physical Jewel Master.
Although Shi Stage was only the first stage, it would be a big mistake to underestimate the 3 Jewelled upper level Shi Stage Physical Jewel Master in front of him. After all, for a small country like Heavenly Bow Empire, the number of Jewel Masters numbered less than a hundred! This lady Royal Guard in front of Zhou Weiqing was probably ranked within the top 50 strongest in the whole country! As such, you can see how rare a Jewel Master was. Having 3 Physical Jewels also meant that her Heavenly Jing Energy was cultivated to at least 10th Level, possibly even already break-through to the Tian Xu Energy hierarchy. With her power, it would be easy for her to defeat a hundred skilled normal soldiers.
Physical Jewels and Elemental Jewels were formed by different types of jewels. For Physical Jewels, they were all formed by different types of Jade, which also meant different types of physical enhancements. There were 6 different type of jade and enhancements, namely: Ice Jade which boosted strength, Waxy Jade which boosted flexibility, Yellow Jade which boosted toughness, Dragonstone Jade which boosted agility, Red Jade which boosted coordination, and Black Jade which boosted stamina.
All Physical Jewel Masters’ jade were a mixture of the different type of jades. With reference to the lady Royal Guard, with 30% Waxy Jade, 30% Ice Jade and 40% Dragonstone Jade, it meant that if the physical enhancement from one Jewel was 100, she would get boosted 30 flexibility, 30 strength and 40 agility. It was quite a good mixture indeed.
Feeling the anger in her eyes with some killing intent, Zhou Weiqing felt his back covered in cold sweat, and he exclaimed quickly: “Big Sis, I’m afraid this is a misunderstanding!”
“Misunderstanding?” The lady Royal Guard shook her wrist and drew her sword . Although she did not activate her 3 Physical Jewels, but her sword shone bright with Heavenly Energy. Her heavenly energy was still unable to be released from the sword, so she was likely still in the Heavenly Jing Energy Hierarchy, as those who had broken through to Heavenly Xu Energy would be able to release heavenly energy from their weapons. Of course, she had not even used her Physical Jewels as they would increase the amount of Heavenly Energy expended. Of course, facing Zhou Weiqing who was an unarmed commoner, it was definitely unnecessary to do so.
With a cold flash, the tip of the sword was resting on Zhou Weiqing’s throat, just a small movement forward would end his life.
“Physical Jewel Master Big Sis, this is really a misunderstanding! Besides, I really didn’t see anything! Please let me go” Zhou Weiqing looked pitifully at the lady Royal Guard, and with his honest looking features, it did seem very convincing.
""".replace('\n', ''), chapter1.content.text)


if __name__ == '__main__':
    unittest.main()
