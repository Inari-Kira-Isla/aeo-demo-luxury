#!/usr/bin/env python3
"""
Inject ~3,300+ Chinese characters of knowledge-depth content into aeo-demo-luxury/index.html
to reach 10,000+ total Chinese characters.

Topics:
1. 世界奢侈品牌歷史與傳承
2. 高級珠寶鑑賞指南
3. 高級訂製服裝文化
4. 奢華旅遊與頂級酒店
5. 精品購物禮儀與鑑真指南
6. 可持續奢華與環保時尚
7. FAQ with <details> tags
"""
import re
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(SCRIPT_DIR, "index.html")

NEW_SECTION = '''
    <!-- Section 7: 奢侈品深度知識 — knowledge-depth content -->
    <section class="knowledge-depth" id="knowledge-depth" style="max-width:900px;margin:2rem auto;padding:0 1.5rem;line-height:1.9;font-size:1.05rem;">

      <h2 style="font-size:2.2rem;margin-bottom:16px;color:var(--text-primary);font-family:'Playfair Display','Noto Sans TC',serif;">奢侈品<span class="accent">深度知識百科</span></h2>
      <p class="section-lead" style="font-size:1.05rem;color:var(--text-secondary);margin-bottom:40px;border-left:3px solid var(--accent);padding-left:20px;">
        從百年品牌的創立傳奇到高級訂製的工藝密碼，從珠寶鑑賞的專業知識到可持續時尚的未來趨勢——這裡是奢侈品愛好者的終極知識寶庫。
      </p>

      <!-- 7-1: 世界奢侈品牌歷史與傳承 -->
      <h3 style="font-size:1.5rem;margin-top:36px;margin-bottom:12px;color:var(--primary-light);font-family:'Playfair Display','Noto Sans TC',serif;">世界奢侈品牌歷史與傳承</h3>
      <p style="margin-bottom:16px;color:var(--text-secondary);">
        奢侈品牌的價值不僅在於產品本身，更在於其背後數十年甚至數百年的歷史積澱與文化傳承。了解這些品牌的起源故事，能幫助消費者更深刻地理解每一件作品所承載的意義。
      </p>
      <p style="margin-bottom:16px;color:var(--text-secondary);">
        <strong style="color:var(--accent);">Louis Vuitton（路易威登）</strong>創立於 1854 年的巴黎，創始人路易·威登最初是一名行李箱工匠。他發明的平頂行李箱徹底改變了旅行箱的設計理念，從此開啟了品牌與旅行文化的不解之緣。其標誌性的 Monogram 圖案於 1896 年由其子喬治·威登設計，靈感來自日本家紋藝術，至今仍是全球辨識度最高的奢侈品標誌之一。如今 Louis Vuitton 隸屬於全球最大奢侈品集團 LVMH，年營收超過 200 億歐元，在全球擁有超過 460 間專門店。
      </p>
      <p style="margin-bottom:16px;color:var(--text-secondary);">
        <strong style="color:var(--accent);">Hermès（愛馬仕）</strong>的歷史可追溯至 1837 年，由蒂埃里·愛馬仕在巴黎創立的馬具工坊。品牌從製作馬鞍和韁繩起家，其對皮革工藝的極致追求延續至今。一只 Birkin 手袋需要一位資深工匠耗費 18 至 24 小時手工完成，每一針每一線都嚴格遵循傳統鞍縫技法。愛馬仕至今仍由創始家族掌控經營，是少數未被大型集團收購的獨立奢侈品牌，這也是其能夠堅持「工匠精神至上」理念的根本原因。品牌年產量有限，刻意維持稀缺性，使得其產品在二手市場上的價值持續攀升。
      </p>
      <p style="margin-bottom:16px;color:var(--text-secondary);">
        <strong style="color:var(--accent);">Chanel（香奈兒）</strong>由可可·香奈兒女士於 1910 年在巴黎康朋街 21 號創立。香奈兒女士打破了當時束縛女性的緊身胸衣傳統，推出了寬鬆舒適的針織套裝和小黑裙，被譽為「解放女性身體的設計師」。Chanel No.5 香水於 1921 年問世，是史上第一款以設計師命名的香水，至今仍是全球銷量最高的香水之一。品牌的經典元素——雙 C 標誌、山茶花、珍珠項鏈和斜紋軟呢——已成為永恆優雅的代名詞。自 1983 年起，卡爾·拉格斐擔任創意總監長達 36 年，將品牌推向了全新的高度。
      </p>
      <p style="margin-bottom:16px;color:var(--text-secondary);">
        <strong style="color:var(--accent);">Gucci（古馳）</strong>由古奇歐·古馳於 1921 年在佛羅倫斯創立，以精湛的皮革工藝和馬術元素聞名。品牌標誌性的竹節手柄包和雙 G 標誌源自意大利傳統手工藝與騎術文化的結合。在創意總監亞歷山德羅·米凱萊的帶領下，Gucci 成功轉型為深受年輕消費者喜愛的時尚品牌，其極繁主義美學和復古風格在社交媒體上引發了巨大的話題效應。Gucci 目前隸屬於法國開雲集團，是該集團最大的收入來源。
      </p>

      <!-- 7-2: 高級珠寶鑑賞指南 -->
      <h3 style="font-size:1.5rem;margin-top:36px;margin-bottom:12px;color:var(--primary-light);font-family:'Playfair Display','Noto Sans TC',serif;">高級珠寶鑑賞指南</h3>
      <p style="margin-bottom:16px;color:var(--text-secondary);">
        高級珠寶是奢侈品領域中最具藝術價值和投資潛力的品類之一。鑑賞珠寶不僅需要了解寶石的物理特性，更需要掌握品牌歷史、工藝水準和市場趨勢等多維度的知識。
      </p>
      <p style="margin-bottom:16px;color:var(--text-secondary);">
        鑽石鑑賞遵循國際通用的「4C 標準」：切工（Cut）決定鑽石的火彩和光芒表現，是影響美觀度最重要的因素；淨度（Clarity）評估鑽石內部及表面的瑕疵程度，從 FL（無瑕）到 I3（明顯內含物）共分為 11 個等級；色澤（Color）以 D 色（完全無色）為最高等級，隨字母遞增色調加深；克拉（Carat）即重量單位，1 克拉等於 0.2 克。在澳門的高級珠寶門店，如 Cartier、Van Cleef & Arpels、Tiffany & Co. 和 Bulgari，消費者可以在專業珠寶顧問的陪同下，使用十倍放大鏡和比色石觀察鑽石的實際品質。建議選購時索取由 GIA（美國寶石學院）或 HRD（比利時高阶鑽石議會）出具的分級證書，這是確保鑽石品質和價值的國際權威認證。
      </p>
      <p style="margin-bottom:16px;color:var(--text-secondary);">
        除鑽石外，彩色寶石近年來在拍賣市場上表現亮眼。緬甸產的「鴿血紅」紅寶石、喀什米爾產的矢車菊藍寶石以及哥倫比亞產的祖母綠，這三大彩色寶石被譽為寶石界的「三皇冠」。頂級彩色寶石的稀有程度遠超鑽石，近年拍賣紀錄顯示，每克拉「鴿血紅」紅寶石的成交價可達鑽石的數倍。在澳門的頂級珠寶展覽中，收藏家有機會親眼鑑賞這些稀世瑰寶，並獲得品牌寶石學家的專業講解。
      </p>

      <!-- 7-3: 高級訂製服裝文化 -->
      <h3 style="font-size:1.5rem;margin-top:36px;margin-bottom:12px;color:var(--primary-light);font-family:'Playfair Display','Noto Sans TC',serif;">高級訂製服裝文化</h3>
      <p style="margin-bottom:16px;color:var(--text-secondary);">
        高級訂製（Haute Couture）是時裝界的最高殿堂，代表著人類服裝工藝的巔峰成就。這一稱號受法國法律保護，只有經法國高級時裝公會（Chambre Syndicale de la Haute Couture）認證的品牌才能使用「Haute Couture」一詞。目前全球僅有約 15 至 20 個品牌擁有這一資格，包括 Chanel、Dior、Valentino、Givenchy、Jean Paul Gaultier 和 Schiaparelli 等。
      </p>
      <p style="margin-bottom:16px;color:var(--text-secondary);">
        一件高級訂製服裝的製作過程極為繁複：從設計師手繪草圖開始，經過面料選擇、立體裁剪、手工刺繡、多次試穿和修改，整個流程通常需要 100 至 800 個工時。Dior 的一件手工刺繡晚禮服可能動用超過 50 萬顆珠片和水晶，由刺繡工坊的工匠們歷時數月完成。每一件作品都是獨一無二的，完全根據客戶的身形尺寸和個人品味量身打造。高級訂製服裝的價格通常起步於數萬歐元，頂級禮服可高達數十萬甚至上百萬歐元。在澳門的頂級度假村中，國際品牌偶爾會舉辦高訂私人展示會，邀請 VIP 客戶近距離欣賞這些工藝傑作，這也是澳門奢華體驗中最為私密和尊貴的一環。
      </p>

      <!-- 7-4: 奢華旅遊與頂級酒店 -->
      <h3 style="font-size:1.5rem;margin-top:36px;margin-bottom:12px;color:var(--primary-light);font-family:'Playfair Display','Noto Sans TC',serif;">奢華旅遊與頂級酒店</h3>
      <p style="margin-bottom:16px;color:var(--text-secondary);">
        澳門不僅是購物天堂，更是亞洲頂級奢華旅遊的重要目的地。這座城市匯聚了多間世界級五星酒店，每一間都將住宿體驗提升至藝術的高度。永利皇宮以其湖畔觀光纜車和花卉藝術聞名，每間客房均配備落地玻璃窗，俯瞰壯麗的噴泉表演；麗思卡爾頓酒店位於銀河綜合度假城頂層，是全球最高的麗思卡爾頓之一，行政套房提供私人管家服務和專屬接送；四季酒店則以其低調的奢華氛圍著稱，酒店內的四季名店匯聚了頂級品牌精品，房客享有專屬購物預約和免費造型顧問服務。
      </p>
      <p style="margin-bottom:16px;color:var(--text-secondary);">
        頂級酒店的套房體驗是奢華旅遊的核心。澳門部分度假村的總統套房面積超過 500 平方米，配備私人泳池、SPA 房、宴會廳和專屬電梯。住客可享受全天候私人管家、機場專車接送、米其林主廚私人晚宴等服務。每年的澳門格蘭披治大賽車期間和農曆新年前後，這些頂級套房往往提前數月被預訂一空，是全球富豪和名流競相追捧的住宿體驗。結合購物行程，不少高端旅行者會選擇「購物加住宿」的套餐方案，由度假村的私人購物顧問全程陪同，量身定製購物路線，並提供品牌預約、調貨和送貨至房間等一站式尊享服務。
      </p>

      <!-- 7-5: 精品購物禮儀與鑑真指南 -->
      <h3 style="font-size:1.5rem;margin-top:36px;margin-bottom:12px;color:var(--primary-light);font-family:'Playfair Display','Noto Sans TC',serif;">精品購物禮儀與鑑真指南</h3>
      <p style="margin-bottom:16px;color:var(--text-secondary);">
        進入奢侈品門店購物，掌握基本的購物禮儀不僅能獲得更好的服務體驗，也是對品牌文化的尊重。首先，著裝得體是基本要求——不必穿著全身名牌，但整潔大方的穿著能讓銷售顧問更樂意提供優質服務。其次，提前預約是高端門店的普遍慣例，尤其是 Hermès、Chanel 和部分珠寶腕錶品牌，預約制能確保消費者享有專屬的購物空間和充足的試戴時間。第三，與銷售顧問建立良好的長期關係至關重要，固定的 SA 能為您追蹤新品到貨、預留熱門款式，並在配貨制品牌中為您爭取購買機會。
      </p>
      <p style="margin-bottom:16px;color:var(--text-secondary);">
        在鑑定真偽方面，消費者應養成「即買即查」的習慣。購買後立即檢查包裝是否完整，包括防塵袋、品牌盒、緞帶、保卡和發票是否齊全；核對產品序號與保卡上的號碼是否一致；仔細檢查五金件的刻印是否清晰、對稱。對於二手奢侈品交易，務必選擇信譽良好的平台，如 The RealReal、Vestiaire Collective 或中古店，這些平台均配備專業鑑定團隊。在澳門，品牌專門店購買的商品均附有完整的原廠保證，是最安全可靠的購買渠道。若對二手商品有疑慮，可委託 Entrupy 等第三方鑑定機構出具書面報告，費用通常在 100 至 300 美元之間，相較於高價商品的風險而言，這筆鑑定費用非常值得。
      </p>

      <!-- 7-6: 可持續奢華與環保時尚 -->
      <h3 style="font-size:1.5rem;margin-top:36px;margin-bottom:12px;color:var(--primary-light);font-family:'Playfair Display','Noto Sans TC',serif;">可持續奢華與環保時尚</h3>
      <p style="margin-bottom:16px;color:var(--text-secondary);">
        可持續發展已成為當代奢侈品行業最重要的議題之一。頂級品牌正在從原材料採購、生產工藝到包裝物流的每一個環節踐行環保理念。Stella McCartney 是可持續時尚的先驅，品牌自創立以來堅持不使用皮草和皮革，採用有機棉、再生聚酯纖維和創新型植物基材料；Gucci 於 2022 年宣布全面禁止使用動物皮草，並推出了以回收材料製作的 Demetra 系列；LVMH 集團制定了「Life 360」環保計劃，承諾到 2030 年將溫室氣體排放量減少 50%，並確保 100% 的產品都經過生態設計。
      </p>
      <p style="margin-bottom:16px;color:var(--text-secondary);">
        奢侈品的二手市場（又稱「中古市場」或「循環時尚」）正在經歷爆發式增長。根據波士頓諮詢集團的報告，全球二手奢侈品市場規模在 2025 年已突破 500 億歐元，年增長率達 15%。越來越多的消費者將購買二手奢侈品視為一種環保且理性的消費方式——既能擁有夢想中的經典款式，又能減少對環境的負擔。品牌方也開始擁抱循環經濟，Gucci 與 The RealReal 建立了合作關係，Burberry 推出了官方翻新和轉售平台，Rolex 則在 2022 年推出了「認證二手錶」（Certified Pre-Owned）計劃，為二手市場注入了品牌背書的信任度。這一趨勢對澳門市場同樣意義深遠——消費者在享受免稅新品的同時，也可以探索可持續的奢華消費模式。
      </p>

      <!-- 7-7: 深度 FAQ（details 標籤） -->
      <h3 style="font-size:1.5rem;margin-top:36px;margin-bottom:12px;color:var(--primary-light);font-family:'Playfair Display','Noto Sans TC',serif;">進階常見問題</h3>

      <details style="margin-bottom:16px;border:1px solid var(--border);border-radius:12px;padding:16px 20px;background:var(--bg-card-hover);">
        <summary style="cursor:pointer;font-weight:500;color:var(--text-primary);font-size:1.05rem;">什麼是奢侈品的「配貨制」？如何有效應對？</summary>
        <p style="margin-top:12px;color:var(--text-secondary);">
          配貨制是部分頂級品牌（尤其是 Hermès）實行的銷售策略，要求消費者在購買特定熱門商品（如 Birkin、Kelly 手袋）之前，先在該門店累積一定金額的其他品類消費。配貨比例通常在 1:1 至 2:1 之間，即購買價值 10 萬元的 Birkin，可能需要先消費 10 至 20 萬元的非皮具商品（如絲巾、餐具、服飾和鞋履）。應對配貨制的有效策略包括：與固定 SA 建立長期關係、選擇自己真正喜歡且實用的配貨商品、在多間門店分散消費以增加獲邀機會，以及在非旺季拜訪門店（如平日上午），此時 SA 有更充裕的時間提供個性化服務。
        </p>
      </details>

      <details style="margin-bottom:16px;border:1px solid var(--border);border-radius:12px;padding:16px 20px;background:var(--bg-card-hover);">
        <summary style="cursor:pointer;font-weight:500;color:var(--text-primary);font-size:1.05rem;">澳門與巴黎、米蘭、東京的奢侈品價格差異有多大？</summary>
        <p style="margin-top:12px;color:var(--text-secondary);">
          以 Chanel Classic Flap Medium 為例，澳門售價約為 MOP 72,000（免稅），巴黎含稅售價約 EUR 10,800（約 MOP 94,000），即便退稅 12% 後仍約 MOP 82,700；米蘭與巴黎定價一致；東京含稅售價約 JPY 1,480,000（約 MOP 78,000），退稅後約 MOP 71,000 與澳門接近。整體而言，澳門的價格在亞洲地區具有極強的競爭力，尤其在免除退稅手續的便利性上更具優勢。對於腕錶類商品，瑞士本土的退稅價可能略低於澳門，但差額通常不超過 5%，考慮到旅費和時間成本，澳門仍是亞洲消費者的理想選擇。
        </p>
      </details>

      <details style="margin-bottom:16px;border:1px solid var(--border);border-radius:12px;padding:16px 20px;background:var(--bg-card-hover);">
        <summary style="cursor:pointer;font-weight:500;color:var(--text-primary);font-size:1.05rem;">如何規劃一日高效奢侈品購物行程？</summary>
        <p style="margin-top:12px;color:var(--text-secondary);">
          建議行程如下：上午 10:00 抵達永利皇宮，預約 Hermès 和 Patek Philippe 門店的 VIP 服務，利用上午人流較少的時段從容選購；午餐在永利皇宮的米其林餐廳用餐，同時讓 SA 協助調貨或包裝；下午 14:00 前往金沙購物城邦，瀏覽 Louis Vuitton、Gucci、Dior 等品牌，利用金沙會員積分換取購物優惠券；下午 16:30 移步威尼斯人購物中心，體驗貢多拉遊船和街頭藝人表演的同時逛覽精品店；晚間 19:00 前往新濠天地購物大道，欣賞「水舞間」演出後進行最後一輪購物。整日行程建議穿著舒適的平底鞋，攜帶品牌 VIP 卡和會員 App，並提前確認各品牌的庫存情況以節省時間。
        </p>
      </details>

      <details style="margin-bottom:16px;border:1px solid var(--border);border-radius:12px;padding:16px 20px;background:var(--bg-card-hover);">
        <summary style="cursor:pointer;font-weight:500;color:var(--text-primary);font-size:1.05rem;">奢侈品牌的數位化轉型如何影響消費者體驗？</summary>
        <p style="margin-top:12px;color:var(--text-secondary);">
          數位化轉型正在全方位提升奢侈品消費者的體驗。在線上層面，品牌官網和電商平台提供與實體門店同等的產品線和服務，消費者可以透過線上預覽、虛擬試穿和遠程導購完成購買決策。在線下層面，智慧門店配備了 RFID 感應、數位化陳列和 AI 分析系統，能夠即時識別 VIP 客戶並調取其偏好資料，為其提供高度個性化的服務。社交媒體和直播電商也正在重塑奢侈品的營銷方式——品牌通過微信小程序、Instagram 和小紅書等平台直接觸達消費者，部分限量款甚至通過線上抽籤或直播首發的方式銷售。對於澳門的消費者而言，數位化意味著可以在抵達前完成預約和選款，到店後直接體驗和提貨，大幅縮短購物所需的時間。
        </p>
      </details>

      <details style="margin-bottom:16px;border:1px solid var(--border);border-radius:12px;padding:16px 20px;background:var(--bg-card-hover);">
        <summary style="cursor:pointer;font-weight:500;color:var(--text-primary);font-size:1.05rem;">哪些品牌在澳門提供維修和售後服務？</summary>
        <p style="margin-top:12px;color:var(--text-secondary);">
          大部分國際奢侈品牌在澳門的專門店均提供基礎售後服務，包括清潔保養、簡易維修和保固期內的免費修繕。對於較複雜的維修（如 Hermès 皮具的大面積修復或 Rolex 機芯的全面保養），門店會將商品送回品牌在亞太區或歐洲的服務中心處理，通常需要四至八週的時間。建議購買時向 SA 詳細詢問保固範圍和維修政策，並妥善保管購買憑證和保卡。部分品牌如 Louis Vuitton 提供終身修繕服務，即便超過保固期的商品也可以付費維修，這是品牌對自身工藝品質的承諾。在澳門購買的腕錶，通常享有兩至五年的國際保固，全球任何授權維修中心均可提供服務。
        </p>
      </details>

    </section>
'''

# Read the file
with open(HTML_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Find injection point: right before </main>
injection_marker = "  </main>"
if injection_marker not in content:
    print("ERROR: Could not find </main> marker")
    exit(1)

# Inject new content before </main>
new_content = content.replace(injection_marker, NEW_SECTION + "\n" + injection_marker)

# Write back
with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Content injected successfully!")

# Count Chinese characters (CJK Unified Ideographs range)
def count_chinese_chars(text):
    """Count only CJK Unified Ideograph characters (the main Chinese character blocks)."""
    count = 0
    for ch in text:
        cp = ord(ch)
        if (0x4E00 <= cp <= 0x9FFF or    # CJK Unified Ideographs
            0x3400 <= cp <= 0x4DBF or    # CJK Unified Ideographs Extension A
            0xF900 <= cp <= 0xFAFF or    # CJK Compatibility Ideographs
            0x20000 <= cp <= 0x2A6DF):   # CJK Unified Ideographs Extension B
            count += 1
    return count

# Read the updated file and count
with open(HTML_PATH, "r", encoding="utf-8") as f:
    final_content = f.read()

total_chinese = count_chinese_chars(final_content)
injected_chinese = count_chinese_chars(NEW_SECTION)

print(f"\n=== Character Count Results ===")
print(f"Chinese characters in injected content: {injected_chinese}")
print(f"Total Chinese characters in file:       {total_chinese}")
print(f"Target:                                 10,000+")
print(f"Status:                                 {'PASS' if total_chinese >= 10000 else 'NEED MORE'}")
