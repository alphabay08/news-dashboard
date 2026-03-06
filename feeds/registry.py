# feeds/registry.py
# Complete RSS Feed Registry — 90+ feeds across 11 categories

FEEDS = {
    "world": {
        "label": "World",
        "icon": "🌍",
        "subcategories": None,
        "feeds": [
            {"name": "BBC World", "url": "http://feeds.bbci.co.uk/news/world/rss.xml", "logo": "https://logo.clearbit.com/bbc.com"},
            {"name": "Reuters World", "url": "https://feeds.reuters.com/reuters/worldNews", "logo": "https://logo.clearbit.com/reuters.com"},
            {"name": "Al Jazeera", "url": "https://www.aljazeera.com/xml/rss/all.xml", "logo": "https://logo.clearbit.com/aljazeera.com"},
            {"name": "The Guardian World", "url": "https://www.theguardian.com/world/rss", "logo": "https://logo.clearbit.com/theguardian.com"},
            {"name": "DW News", "url": "https://rss.dw.com/rdf/rss-en-all", "logo": "https://logo.clearbit.com/dw.com"},
            {"name": "France 24", "url": "https://www.france24.com/en/rss", "logo": "https://logo.clearbit.com/france24.com"},
            {"name": "AP News", "url": "https://rsshub.app/apnews/topics/apf-topnews", "logo": "https://logo.clearbit.com/apnews.com"},
            {"name": "NPR World", "url": "https://feeds.npr.org/1004/rss.xml", "logo": "https://logo.clearbit.com/npr.org"},
            {"name": "Sky News World", "url": "https://feeds.skynews.com/feeds/rss/world.xml", "logo": "https://logo.clearbit.com/skynews.com"},
            {"name": "ABC News World", "url": "https://abcnews.go.com/abcnews/internationalheadlines", "logo": "https://logo.clearbit.com/abcnews.go.com"},
        ]
    },
    "pakistan": {
        "label": "Pakistan",
        "icon": "🇵🇰",
        "subcategories": None,
        "feeds": [
            {"name": "Dawn News", "url": "https://www.dawn.com/feeds/home", "logo": "https://logo.clearbit.com/dawn.com"},
            {"name": "The News Int'l", "url": "https://www.thenews.com.pk/rss/1/1", "logo": "https://logo.clearbit.com/thenews.com.pk"},
            {"name": "Geo News", "url": "https://www.geo.tv/rss/1/", "logo": "https://logo.clearbit.com/geo.tv"},
            {"name": "ARY News", "url": "https://arynews.tv/feed/", "logo": "https://logo.clearbit.com/arynews.tv"},
            {"name": "Express Tribune", "url": "https://tribune.com.pk/feed/", "logo": "https://logo.clearbit.com/tribune.com.pk"},
            {"name": "Business Recorder", "url": "https://www.brecorder.com/feed", "logo": "https://logo.clearbit.com/brecorder.com"},
            {"name": "Pakistan Today", "url": "https://www.pakistantoday.com.pk/feed/", "logo": "https://logo.clearbit.com/pakistantoday.com.pk"},
            {"name": "The Nation PK", "url": "https://nation.com.pk/rss/home.xml", "logo": "https://logo.clearbit.com/nation.com.pk"},
            {"name": "Dunya News", "url": "https://dunyanews.tv/index.php/en?format=feed&type=rss", "logo": "https://logo.clearbit.com/dunyanews.tv"},
            {"name": "24 News HD", "url": "https://24newshd.tv/feed", "logo": "https://logo.clearbit.com/24newshd.tv"},
        ]
    },
    "asia": {
        "label": "Asia",
        "icon": "🌏",
        "subcategories": None,
        "feeds": [
            {"name": "South China Morning Post", "url": "https://www.scmp.com/rss/91/feed", "logo": "https://logo.clearbit.com/scmp.com"},
            {"name": "The Hindu", "url": "https://www.thehindu.com/news/international/?service=rss", "logo": "https://logo.clearbit.com/thehindu.com"},
            {"name": "Times of India", "url": "https://timesofindia.indiatimes.com/rssfeedstopstories.cms", "logo": "https://logo.clearbit.com/timesofindia.indiatimes.com"},
            {"name": "Nikkei Asia", "url": "https://asia.nikkei.com/rss/feed/nar", "logo": "https://logo.clearbit.com/asia.nikkei.com"},
            {"name": "Channel NewsAsia", "url": "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml", "logo": "https://logo.clearbit.com/channelnewsasia.com"},
            {"name": "Bangkok Post", "url": "https://www.bangkokpost.com/rss/data/topstories.xml", "logo": "https://logo.clearbit.com/bangkokpost.com"},
            {"name": "Korea JoongAng Daily", "url": "https://koreajoongangdaily.joins.com/rss/feed/contents.xml", "logo": "https://logo.clearbit.com/koreajoongangdaily.joins.com"},
            {"name": "Straits Times", "url": "https://www.straitstimes.com/news/asia/rss.xml", "logo": "https://logo.clearbit.com/straitstimes.com"},
            {"name": "The Japan Times", "url": "https://www.japantimes.co.jp/feed/", "logo": "https://logo.clearbit.com/japantimes.co.jp"},
            {"name": "Dhaka Tribune", "url": "https://www.dhakatribune.com/feed", "logo": "https://logo.clearbit.com/dhakatribune.com"},
        ]
    },
    "middle_east": {
        "label": "Middle East",
        "icon": "🕌",
        "subcategories": None,
        "feeds": [
            {"name": "Al Jazeera ME", "url": "https://www.aljazeera.com/xml/rss/all.xml", "logo": "https://logo.clearbit.com/aljazeera.com"},
            {"name": "Arab News", "url": "https://www.arabnews.com/rss.xml", "logo": "https://logo.clearbit.com/arabnews.com"},
            {"name": "The National UAE", "url": "https://www.thenationalnews.com/rss/", "logo": "https://logo.clearbit.com/thenationalnews.com"},
            {"name": "Jerusalem Post", "url": "https://www.jpost.com/Rss/RssFeedsHeadlines.aspx", "logo": "https://logo.clearbit.com/jpost.com"},
            {"name": "Times of Israel", "url": "https://www.timesofisrael.com/feed/", "logo": "https://logo.clearbit.com/timesofisrael.com"},
            {"name": "Middle East Eye", "url": "https://www.middleeasteye.net/rss", "logo": "https://logo.clearbit.com/middleeasteye.net"},
            {"name": "Iran International", "url": "https://www.iranintl.com/en/rss", "logo": "https://logo.clearbit.com/iranintl.com"},
            {"name": "Turkish Minute", "url": "https://www.turkishminute.com/feed/", "logo": "https://logo.clearbit.com/turkishminute.com"},
            {"name": "Al-Monitor", "url": "https://www.al-monitor.com/rss", "logo": "https://logo.clearbit.com/al-monitor.com"},
            {"name": "Haaretz", "url": "https://www.haaretz.com/cmlink/1.628765", "logo": "https://logo.clearbit.com/haaretz.com"},
        ]
    },
    "europe": {
        "label": "Europe",
        "icon": "🇪🇺",
        "subcategories": None,
        "feeds": [
            {"name": "BBC Europe", "url": "http://feeds.bbci.co.uk/news/world/europe/rss.xml", "logo": "https://logo.clearbit.com/bbc.com"},
            {"name": "The Guardian Europe", "url": "https://www.theguardian.com/world/europe-news/rss", "logo": "https://logo.clearbit.com/theguardian.com"},
            {"name": "Euronews", "url": "https://www.euronews.com/rss", "logo": "https://logo.clearbit.com/euronews.com"},
            {"name": "POLITICO Europe", "url": "https://www.politico.eu/feed/", "logo": "https://logo.clearbit.com/politico.eu"},
            {"name": "Deutsche Welle EU", "url": "https://rss.dw.com/rdf/rss-en-eu", "logo": "https://logo.clearbit.com/dw.com"},
            {"name": "The Local (EU)", "url": "https://www.thelocal.com/feed/", "logo": "https://logo.clearbit.com/thelocal.com"},
            {"name": "EUobserver", "url": "https://euobserver.com/rss.xml", "logo": "https://logo.clearbit.com/euobserver.com"},
            {"name": "Le Monde (EN)", "url": "https://www.lemonde.fr/en/rss/une.xml", "logo": "https://logo.clearbit.com/lemonde.fr"},
            {"name": "Spiegel International", "url": "https://www.spiegel.de/international/index.rss", "logo": "https://logo.clearbit.com/spiegel.de"},
            {"name": "RFI English", "url": "https://www.rfi.fr/en/rss", "logo": "https://logo.clearbit.com/rfi.fr"},
        ]
    },
    "americas": {
        "label": "Americas",
        "icon": "🌎",
        "subcategories": None,
        "feeds": [
            {"name": "CNN", "url": "http://rss.cnn.com/rss/cnn_topstories.rss", "logo": "https://logo.clearbit.com/cnn.com"},
            {"name": "NYT World", "url": "https://rss.nytimes.com/services/xml/rss/nyt/World.xml", "logo": "https://logo.clearbit.com/nytimes.com"},
            {"name": "Washington Post", "url": "https://feeds.washingtonpost.com/rss/world", "logo": "https://logo.clearbit.com/washingtonpost.com"},
            {"name": "NPR News", "url": "https://feeds.npr.org/1001/rss.xml", "logo": "https://logo.clearbit.com/npr.org"},
            {"name": "CBC Canada", "url": "https://www.cbc.ca/cmlink/rss-world", "logo": "https://logo.clearbit.com/cbc.ca"},
            {"name": "BBC Americas", "url": "http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml", "logo": "https://logo.clearbit.com/bbc.com"},
            {"name": "Latin Times", "url": "https://www.latintimes.com/rss/headlines", "logo": "https://logo.clearbit.com/latintimes.com"},
            {"name": "Miami Herald", "url": "https://www.miamiherald.com/news/nation-world/?widgetName=rssfeed&widgetContentId=712015&getXmlFeed=true", "logo": "https://logo.clearbit.com/miamiherald.com"},
            {"name": "Reuters Americas", "url": "https://feeds.reuters.com/reuters/americasNews", "logo": "https://logo.clearbit.com/reuters.com"},
            {"name": "AP Latin America", "url": "https://rsshub.app/apnews/topics/apf-latinamerica", "logo": "https://logo.clearbit.com/apnews.com"},
        ]
    },
    "africa": {
        "label": "Africa",
        "icon": "🌍",
        "subcategories": None,
        "feeds": [
            {"name": "BBC Africa", "url": "http://feeds.bbci.co.uk/news/world/africa/rss.xml", "logo": "https://logo.clearbit.com/bbc.com"},
            {"name": "Al Jazeera Africa", "url": "https://www.aljazeera.com/xml/rss/all.xml", "logo": "https://logo.clearbit.com/aljazeera.com"},
            {"name": "Daily Maverick", "url": "https://www.dailymaverick.co.za/feed/", "logo": "https://logo.clearbit.com/dailymaverick.co.za"},
            {"name": "The East African", "url": "https://www.theeastafrican.co.ke/tea/rss", "logo": "https://logo.clearbit.com/theeastafrican.co.ke"},
            {"name": "AllAfrica", "url": "https://allafrica.com/tools/headlines/rdf/latest/headlines.rdf", "logo": "https://logo.clearbit.com/allafrica.com"},
            {"name": "Africa Report", "url": "https://www.theafricareport.com/feed/", "logo": "https://logo.clearbit.com/theafricareport.com"},
            {"name": "Nigerian Tribune", "url": "https://tribuneonlineng.com/feed/", "logo": "https://logo.clearbit.com/tribuneonlineng.com"},
            {"name": "Mail & Guardian", "url": "https://mg.co.za/feed/", "logo": "https://logo.clearbit.com/mg.co.za"},
            {"name": "Premium Times NG", "url": "https://www.premiumtimesng.com/feed", "logo": "https://logo.clearbit.com/premiumtimesng.com"},
            {"name": "RFI Africa", "url": "https://www.rfi.fr/en/africa/rss", "logo": "https://logo.clearbit.com/rfi.fr"},
        ]
    },
    "technology": {
        "label": "Technology",
        "icon": "💻",
        "subcategories": None,
        "feeds": [
            {"name": "TechCrunch", "url": "https://techcrunch.com/feed/", "logo": "https://logo.clearbit.com/techcrunch.com"},
            {"name": "The Verge", "url": "https://www.theverge.com/rss/index.xml", "logo": "https://logo.clearbit.com/theverge.com"},
            {"name": "Wired", "url": "https://www.wired.com/feed/rss", "logo": "https://logo.clearbit.com/wired.com"},
            {"name": "Ars Technica", "url": "https://feeds.arstechnica.com/arstechnica/index", "logo": "https://logo.clearbit.com/arstechnica.com"},
            {"name": "Hacker News", "url": "https://hnrss.org/frontpage", "logo": "https://logo.clearbit.com/news.ycombinator.com"},
            {"name": "MIT Tech Review", "url": "https://www.technologyreview.com/feed/", "logo": "https://logo.clearbit.com/technologyreview.com"},
            {"name": "Engadget", "url": "https://www.engadget.com/rss.xml", "logo": "https://logo.clearbit.com/engadget.com"},
            {"name": "ZDNet", "url": "https://www.zdnet.com/news/rss.xml", "logo": "https://logo.clearbit.com/zdnet.com"},
            {"name": "VentureBeat", "url": "https://venturebeat.com/feed/", "logo": "https://logo.clearbit.com/venturebeat.com"},
            {"name": "9to5Google", "url": "https://9to5google.com/feed/", "logo": "https://logo.clearbit.com/9to5google.com"},
        ]
    },
    "business": {
        "label": "Business",
        "icon": "💼",
        "subcategories": None,
        "feeds": [
            {"name": "Financial Times", "url": "https://www.ft.com/rss/home/uk", "logo": "https://logo.clearbit.com/ft.com"},
            {"name": "Bloomberg Markets", "url": "https://feeds.bloomberg.com/markets/news.rss", "logo": "https://logo.clearbit.com/bloomberg.com"},
            {"name": "Reuters Business", "url": "https://feeds.reuters.com/reuters/businessNews", "logo": "https://logo.clearbit.com/reuters.com"},
            {"name": "Forbes", "url": "https://www.forbes.com/real-time/feed2/", "logo": "https://logo.clearbit.com/forbes.com"},
            {"name": "Business Insider", "url": "https://feeds.businessinsider.com/custom/all", "logo": "https://logo.clearbit.com/businessinsider.com"},
            {"name": "CNBC", "url": "https://www.cnbc.com/id/100003114/device/rss/rss.html", "logo": "https://logo.clearbit.com/cnbc.com"},
            {"name": "The Economist", "url": "https://www.economist.com/finance-and-economics/rss.xml", "logo": "https://logo.clearbit.com/economist.com"},
            {"name": "MarketWatch", "url": "https://feeds.marketwatch.com/marketwatch/topstories/", "logo": "https://logo.clearbit.com/marketwatch.com"},
            {"name": "Quartz", "url": "https://qz.com/feed", "logo": "https://logo.clearbit.com/qz.com"},
            {"name": "Inc. Magazine", "url": "https://www.inc.com/rss/", "logo": "https://logo.clearbit.com/inc.com"},
        ]
    },
    "science": {
        "label": "Science",
        "icon": "🔬",
        "subcategories": None,
        "feeds": [
            {"name": "NASA", "url": "https://www.nasa.gov/rss/dyn/breaking_news.rss", "logo": "https://logo.clearbit.com/nasa.gov"},
            {"name": "Nature", "url": "https://www.nature.com/nature.rss", "logo": "https://logo.clearbit.com/nature.com"},
            {"name": "Science Daily", "url": "https://www.sciencedaily.com/rss/all.xml", "logo": "https://logo.clearbit.com/sciencedaily.com"},
            {"name": "New Scientist", "url": "https://www.newscientist.com/feed/home/", "logo": "https://logo.clearbit.com/newscientist.com"},
            {"name": "Scientific American", "url": "https://rss.sciam.com/ScientificAmerican-Global", "logo": "https://logo.clearbit.com/scientificamerican.com"},
            {"name": "Live Science", "url": "https://www.livescience.com/feeds/all", "logo": "https://logo.clearbit.com/livescience.com"},
            {"name": "Phys.org", "url": "https://phys.org/rss-feed/", "logo": "https://logo.clearbit.com/phys.org"},
            {"name": "Space.com", "url": "https://www.space.com/feeds/all", "logo": "https://logo.clearbit.com/space.com"},
            {"name": "IFLScience", "url": "https://www.iflscience.com/rss/", "logo": "https://logo.clearbit.com/iflscience.com"},
            {"name": "EurekAlert", "url": "https://www.eurekalert.org/rss.xml", "logo": "https://logo.clearbit.com/eurekalert.org"},
        ]
    },
    "showbiz": {
        "label": "Showbiz",
        "icon": "🎬",
        "subcategories": {
            "hollywood": {
                "label": "Hollywood",
                "icon": "🎥",
                "feeds": [
                    {"name": "Variety", "url": "https://variety.com/feed/", "logo": "https://logo.clearbit.com/variety.com"},
                    {"name": "Hollywood Reporter", "url": "https://www.hollywoodreporter.com/feed/", "logo": "https://logo.clearbit.com/hollywoodreporter.com"},
                    {"name": "Deadline", "url": "https://deadline.com/feed/", "logo": "https://logo.clearbit.com/deadline.com"},
                    {"name": "Entertainment Weekly", "url": "https://ew.com/feed/", "logo": "https://logo.clearbit.com/ew.com"},
                    {"name": "Screen Rant", "url": "https://screenrant.com/feed/", "logo": "https://logo.clearbit.com/screenrant.com"},
                ]
            },
            "bollywood": {
                "label": "Bollywood",
                "icon": "🎭",
                "feeds": [
                    {"name": "Bollywood Hungama", "url": "https://www.bollywoodhungama.com/rss/news.xml", "logo": "https://logo.clearbit.com/bollywoodhungama.com"},
                    {"name": "Filmfare", "url": "https://www.filmfare.com/rss/news.xml", "logo": "https://logo.clearbit.com/filmfare.com"},
                    {"name": "Pinkvilla", "url": "https://www.pinkvilla.com/rss/allstories", "logo": "https://logo.clearbit.com/pinkvilla.com"},
                    {"name": "Koimoi", "url": "https://www.koimoi.com/feed/", "logo": "https://logo.clearbit.com/koimoi.com"},
                    {"name": "Masala.com", "url": "https://www.masala.com/rss/", "logo": "https://logo.clearbit.com/masala.com"},
                ]
            },
            "punjabi": {
                "label": "Punjabi",
                "icon": "🎵",
                "feeds": [
                    {"name": "PTC Punjabi", "url": "https://www.ptcnetwork.com/feed/", "logo": "https://logo.clearbit.com/ptcnetwork.com"},
                    {"name": "Punjabi Janta", "url": "https://www.punjabjanta.com/feed/", "logo": "https://logo.clearbit.com/punjabjanta.com"},
                    {"name": "Dainik Bhaskar Punjab", "url": "https://www.bhaskar.com/rss-v1--catid--6.xml", "logo": "https://logo.clearbit.com/bhaskar.com"},
                    {"name": "NewsX Punjab", "url": "https://newsx.com/feed/", "logo": "https://logo.clearbit.com/newsx.com"},
                    {"name": "Tribune Punjab", "url": "https://www.tribuneindia.com/rss/feed.cms?sec=punjab", "logo": "https://logo.clearbit.com/tribuneindia.com"},
                ]
            }
        }
    },
    "sports": {
        "label": "Sports",
        "icon": "⚽",
        "subcategories": {
            "cricket": {
                "label": "Cricket",
                "icon": "🏏",
                "feeds": [
                    {"name": "ESPNcricinfo", "url": "https://www.espncricinfo.com/rss/content/story/feeds/0.xml", "logo": "https://logo.clearbit.com/espncricinfo.com"},
                    {"name": "CricBuzz", "url": "https://www.cricbuzz.com/cricket-rss-feeds/feed.rss", "logo": "https://logo.clearbit.com/cricbuzz.com"},
                    {"name": "ICC Cricket", "url": "https://www.icc-cricket.com/news/rss.xml", "logo": "https://logo.clearbit.com/icc-cricket.com"},
                    {"name": "PCB", "url": "https://www.pcb.com.pk/rss/feed.xml", "logo": "https://logo.clearbit.com/pcb.com.pk"},
                    {"name": "Cricket Country", "url": "https://www.cricketcountry.com/feed/", "logo": "https://logo.clearbit.com/cricketcountry.com"},
                ]
            },
            "football": {
                "label": "Football",
                "icon": "⚽",
                "feeds": [
                    {"name": "BBC Sport Football", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml", "logo": "https://logo.clearbit.com/bbc.com"},
                    {"name": "Sky Sports Football", "url": "https://www.skysports.com/rss/12040", "logo": "https://logo.clearbit.com/skysports.com"},
                    {"name": "Goal.com", "url": "https://www.goal.com/feeds/en/news", "logo": "https://logo.clearbit.com/goal.com"},
                    {"name": "ESPN FC", "url": "https://www.espnfc.com/rss", "logo": "https://logo.clearbit.com/espnfc.com"},
                    {"name": "The Athletic Football", "url": "https://theathletic.com/rss/", "logo": "https://logo.clearbit.com/theathletic.com"},
                ]
            },
            "basketball": {
                "label": "Basketball",
                "icon": "🏀",
                "feeds": [
                    {"name": "ESPN NBA", "url": "https://www.espn.com/espn/rss/nba/news", "logo": "https://logo.clearbit.com/espn.com"},
                    {"name": "NBA.com News", "url": "https://www.nba.com/news/rss.xml", "logo": "https://logo.clearbit.com/nba.com"},
                    {"name": "Bleacher Report NBA", "url": "https://bleacherreport.com/articles/feed?tag_id=10", "logo": "https://logo.clearbit.com/bleacherreport.com"},
                    {"name": "HoopsHype", "url": "https://hoopshype.com/feed/", "logo": "https://logo.clearbit.com/hoopshype.com"},
                    {"name": "The Ringer NBA", "url": "https://www.theringer.com/nba/rss", "logo": "https://logo.clearbit.com/theringer.com"},
                ]
            },
            "f1": {
                "label": "Formula 1",
                "icon": "🏎️",
                "feeds": [
                    {"name": "F1 Official", "url": "https://www.formula1.com/content/fom-website/en/latest/all.xml", "logo": "https://logo.clearbit.com/formula1.com"},
                    {"name": "Autosport F1", "url": "https://www.autosport.com/rss/feed/f1", "logo": "https://logo.clearbit.com/autosport.com"},
                    {"name": "Motorsport.com", "url": "https://www.motorsport.com/rss/f1/news/", "logo": "https://logo.clearbit.com/motorsport.com"},
                    {"name": "RaceFans", "url": "https://www.racefans.net/feed/", "logo": "https://logo.clearbit.com/racefans.net"},
                    {"name": "Planet F1", "url": "https://www.planetf1.com/feed/", "logo": "https://logo.clearbit.com/planetf1.com"},
                ]
            },
            "tennis": {
                "label": "Tennis",
                "icon": "🎾",
                "feeds": [
                    {"name": "Tennis.com", "url": "https://www.tennis.com/rss-feed/", "logo": "https://logo.clearbit.com/tennis.com"},
                    {"name": "ATP Tour", "url": "https://www.atptour.com/en/media/rss-feed/xml-feed", "logo": "https://logo.clearbit.com/atptour.com"},
                    {"name": "BBC Sport Tennis", "url": "https://feeds.bbci.co.uk/sport/tennis/rss.xml", "logo": "https://logo.clearbit.com/bbc.com"},
                    {"name": "Tennis World USA", "url": "https://www.tennisworldusa.org/rss.xml", "logo": "https://logo.clearbit.com/tennisworldusa.org"},
                    {"name": "Ubitennis", "url": "https://www.ubitennis.net/feed/", "logo": "https://logo.clearbit.com/ubitennis.net"},
                ]
            },
            "boxing": {
                "label": "Boxing",
                "icon": "🥊",
                "feeds": [
                    {"name": "ESPN Boxing", "url": "https://www.espn.com/espn/rss/boxing/news", "logo": "https://logo.clearbit.com/espn.com"},
                    {"name": "Sky Sports Boxing", "url": "https://www.skysports.com/rss/12183", "logo": "https://logo.clearbit.com/skysports.com"},
                    {"name": "Boxing Scene", "url": "https://www.boxingscene.com/rss.php", "logo": "https://logo.clearbit.com/boxingscene.com"},
                    {"name": "Bad Left Hook", "url": "https://www.badlefthook.com/rss/current", "logo": "https://logo.clearbit.com/badlefthook.com"},
                    {"name": "Fight News", "url": "https://fightnews.com/feed", "logo": "https://logo.clearbit.com/fightnews.com"},
                ]
            },
            "wrestling": {
                "label": "Wrestling",
                "icon": "🤼",
                "feeds": [
                    {"name": "WWE.com", "url": "https://www.wwe.com/article/rss", "logo": "https://logo.clearbit.com/wwe.com"},
                    {"name": "WrestlingInc", "url": "https://www.wrestlinginc.com/feed/", "logo": "https://logo.clearbit.com/wrestlinginc.com"},
                    {"name": "PWInsider", "url": "https://www.pwinsider.com/rss.php", "logo": "https://logo.clearbit.com/pwinsider.com"},
                    {"name": "Fightful Wrestling", "url": "https://www.fightful.com/wrestling/rss", "logo": "https://logo.clearbit.com/fightful.com"},
                    {"name": "411Mania Wrestling", "url": "https://411mania.com/wrestling/feed/", "logo": "https://logo.clearbit.com/411mania.com"},
                ]
            }
        }
    }
}

def get_all_feeds_flat():
    """Return a flat list of all feeds with category/subcategory metadata."""
    all_feeds = []
    for cat_key, category in FEEDS.items():
        if category.get("subcategories"):
            for sub_key, subcategory in category["subcategories"].items():
                for feed in subcategory["feeds"]:
                    all_feeds.append({
                        **feed,
                        "category": cat_key,
                        "subcategory": sub_key,
                        "category_label": category["label"],
                        "subcategory_label": subcategory["label"],
                    })
        else:
            for feed in category["feeds"]:
                all_feeds.append({
                    **feed,
                    "category": cat_key,
                    "subcategory": None,
                    "category_label": category["label"],
                    "subcategory_label": None,
                })
    return all_feeds
