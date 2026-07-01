import requests
from datetime import datetime

TELEGRAM_TOKEN = "8339553316:AAEiYm006f9EutF13mX3ks2b-GJZIGOW5Po"
USER_ID = "1297205897"

YEMEK_LISTESI = {
    "01": "🥣 Sebze Çorba\n🍆 Patlıcan Musakka\n🍚 Pirinç Pilavı\n🍰 Gelin Pastası",
    "02": "🥣 Ezogelin Çorbası\n🧆 İzmir Köfte\n🍝 Makarna\n🍏 Meyve",
    "03": "🥣 Düğün Çorbası\n🫑 Biber Dolma (Yoğurtlu)\n🥮 Puf Börek\n🍫 Supangle",
    "04": "🥣 Köz Biber Çorbası\n🍗 Piliç Sote\n🍝 Tereyağlı Erişte\n🥤 Gazoz",
    "05": "📴 Tatil (Çalışma ve yemek yok)",
    "06": "🥣 Domates Çorba\n🧆 Rosto Köfte / Püre\n🌾 Bulgur Pilavı\n🍰 Karagöz Tatlısı",
    "07": "🥣 Tavuk Suyu Çorba\n🍲 Yeşil Mercimek\n🍚 Arpa Şehriyeli Pirinç Pilavı\n🍰 Mozaik Pasta",
    "08": "🥣 Brokoli Çorba\n🍗 Piliç Finger / Elma Dilim Patates\n🍝 Makarna\n🍏 Meyve",
    "09": "🥣 Mercimek Çorbası\n🥕 Karışık Kızartma\n🥮 Peynirli Kol Böreği\n🍮 Kuru Üzümlü İrmik Helvası",
    "10": "🥣 Yoğurt Çorbası\n🥩 Karışık Izgara / Garnitür Sebze\n🌾 Bulgur Pilavı\n🍦 Dondurma",
    "11": "🥣 Kilis Çorba\n🍆 Karnıyarık\n🍚 Nohutlu Pilav\n🍏 Meyve",
    "12": "📴 Tatil (Çalışma ve yemek yok)",
    "13": "🥣 Düğün Çorbası\n🍲 Nohut\n🍚 Tel Şehriyeli Pirinç Pilavı\n🍮 Çıtır Muhallebi",
    "14": "🥣 Mercimek Çorbası\n🍗 Fırın Piliç Baget\n🍝 Makarna\n🍏 Meyve",
    "15": "📴 Tatil (Çalışma ve yemek yok)",
    "16": "🥣 Naneli Yoğurt Çorbası\n🍆 Patlıcan Musakka\n🍚 Pirinç Pilavı\n🍰 Peynir Tatlısı",
    "17": "🥣 Ezogelin Çorbası\n🧆 Kadınbudu Köfte\n🥔 Garnitürlü Püre\n🍝 Makarna\n🍫 Browni",
    "18": "🥣 Ayranaşı Çorbası\n🥔 Patates Musakka\n🌾 Bulgur Pilavı\n🍮 Keşkül",
    "19": "📴 Tatil (Çalışma ve yemek yok)",
    "20": "🥣 Sebze Çorba\n🍲 Kuru Fasulye\n🍚 Pirinç Pilavı\n🥮 Baklava",
    "21": "🥣 Domates Çorba\n🧆 Pideli Köfte (T)\n🍝 Erişte (Kavurma)\n🍏 Meyve",
    "22": "🥣 Mercimek Çorbası\n🍲 Fırın Türlü\n🥮 Gül Börek (Ispanaklı)\n🍰 Fincan Kadayıf",
    "23": "🥣 Yayla Çorbası\n🍗 Piliç Kavurma\n🍚 Pirinç Pilavı\n🍫 Supangle",
    "24": "🥣 Tarhana Çorbası\n🥕 Karışık Kızartma\n🍝 Peynirli Burgu Makarna\n🍰 Şekerpare",
    "25": "🥣 Ezogelin Çorbası\n🧆 Terbiyeli Köfte\n🍝 Makarna\n🍏 Meyve",
    "26": "📴 Tatil (Çalışma ve yemek yok)",
    "27": "🥣 Mercimek Çorbası\n🍆 Patlıcan Kebap\n🌾 Bulgur Pilavı\n🍏 Meyve",
    "28": "🥣 Tavuk Suyu Çorba\n🍲 Nohut\n🍚 Pirinç Pilavı\n🍮 Süt Helva",
    "29": "🥣 Kaşarlı Domates Çorbası\n🍗 Fırın Piliç But\n🍝 Makarna\n🍏 Meyve Günü",
    "30": "🥣 Ezogelin Çorbası\n🍲 Taze Fasulye\n🍚 Tavuklu Mengen Pilavı\n🍰 Kemalpaşa Tatlısı",
    "31": "🥣 Naneli Yoğurt Çorbası\n🧆 Terbiyeli Köfte\n🍝 Fırın Makarna\n🍫 Supangle"
}

def yemek_hatirlat():
    bugun = datetime.now().strftime("%d")
    bugunun_yemegi = YEMEK_LISTESI.get(bugun)
    if bugunun_yemegi:
        mesaj_metni = f"📋 *{bugun} Temmuz 2026 Yemek Menüsü*\n\n{bugunun_yemegi}"
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": USER_ID, "text": mesaj_metni, "parse_mode": "Markdown"})

if __name__ == "__main__":
    yemek_hatirlat()
