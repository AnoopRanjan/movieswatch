import math
from datetime import datetime, timedelta

# ==========================================
# 1. Genres
# ==========================================
GENRES = [
    {"id": 1, "name": "Action", "slug": "action", "icon": "fa-fire", "description": "High-octane excitement and martial arts"},
    {"id": 2, "name": "Comedy", "slug": "comedy", "icon": "fa-face-laugh-squint", "description": "Hilarious laughter and slapstick fun"},
    {"id": 3, "name": "Romance", "slug": "romance", "icon": "fa-heart", "description": "Heartwarming love stories and emotional bonds"},
    {"id": 4, "name": "Drama", "slug": "drama", "icon": "fa-masks-theater", "description": "Emotionally gripping and intense journeys"},
    {"id": 5, "name": "Thriller", "slug": "thriller", "icon": "fa-bolt", "description": "Edge-of-the-seat suspense and mysteries"},
    {"id": 6, "name": "Science Fiction", "slug": "sci-fi", "icon": "fa-rocket", "description": "Futuristic tech and space odysseys"},
    {"id": 7, "name": "Crime", "slug": "crime", "icon": "fa-shield-halved", "description": "Underworld kingpins and detectives"},
    {"id": 8, "name": "Family", "slug": "family", "icon": "fa-users", "description": "Wholesome entertainment for all ages"},
    {"id": 9, "name": "Horror", "slug": "horror", "icon": "fa-ghost", "description": "Supernatural chills and classic terror"},
    {"id": 10, "name": "Regional Cinema", "slug": "regional", "icon": "fa-globe", "description": "Vibrant South Indian and Indian regional cinema"}
]

# ==========================================
# 2. Superstar Actors
# ==========================================
ACTORS = [
    {
        "id": 1, "name": "Shah Rukh Khan", "slug": "shah-rukh-khan",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Shah_Rukh_Khan_graces_the_launch_of_the_new_Santro.jpg",
        "biography": "Shah Rukh Khan, often referred to as 'King Khan' or the 'Badshah of Bollywood', is an Indian actor, film producer, and television personality. With a career spanning over three decades, he has starred in more than 90 films and earned numerous accolades.",
        "birth_place": "New Delhi, India", "birth_year": 1965, "nationality": "Indian",
        "known_for": "Romantic Lead, Action Hero, Character Roles", "awards": "14 Filmfare Awards, Padma Shri (2005), Ordre des Arts et des Lettres",
        "followers_count": 44000000, "wikimedia_attribution": "Photo by Bollywood Hungama / CC BY 3.0 via Wikimedia Commons",
        "upcoming_projects": ["King (2025)", "Tiger vs Pathaan"]
    },
    {
        "id": 2, "name": "Deepika Padukone", "slug": "deepika-padukone",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Deepika_Padukone_Cannes_2018_%28cropped%29.jpg",
        "biography": "One of the highest-paid actresses in India, Deepika Padukone is known for her versatile roles spanning historical epics, contemporary dramas, and high-octane spy thrillers.",
        "birth_place": "Copenhagen, Denmark", "birth_year": 1986, "nationality": "Indian",
        "known_for": "Leading Actress, Producer, Mental Health Advocate", "awards": "3 Filmfare Awards, TIME 100 Most Influential People",
        "followers_count": 78000000, "wikimedia_attribution": "Photo by Georges Biard / CC BY-SA 3.0 via Wikimedia Commons",
        "upcoming_projects": ["Singham Again", "The Intern Remake"]
    },
    {
        "id": 3, "name": "Prabhas", "slug": "prabhas",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Prabhas_at_Saaho_Interview.jpg",
        "biography": "Prabhas is an Indian actor predominantly working in Telugu cinema. He attained pan-India and international stardom with S.S. Rajamouli's epochal Baahubali franchise.",
        "birth_place": "Madras, Tamil Nadu, India", "birth_year": 1979, "nationality": "Indian",
        "known_for": "Pan-India Blockbusters, Action Epics", "awards": "Nandi Award, Filmfare Awards South",
        "followers_count": 32000000, "wikimedia_attribution": "Photo by Bollywood Hungama / CC BY 3.0 via Wikimedia Commons",
        "upcoming_projects": ["The Raja Saab", "Salaar: Part 2", "Spirit"]
    },
    {
        "id": 4, "name": "Amitabh Bachchan", "slug": "amitabh-bachchan",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/9/91/Amitabh_Bachchan_photoshoot.jpg",
        "biography": "Widely regarded as one of the most influential actors in the history of world cinema, the 'Shahenshah of Bollywood' has dominated Indian cinema for over five decades.",
        "birth_place": "Allahabad, Uttar Pradesh, India", "birth_year": 1942, "nationality": "Indian",
        "known_for": "The Angry Young Man, Timeless Dramatic Lead", "awards": "4 National Film Awards, Dadasaheb Phalke Award, Padma Vibhushan",
        "followers_count": 48000000, "wikimedia_attribution": "Photo by Bollywood Hungama / CC BY 3.0 via Wikimedia Commons",
        "upcoming_projects": ["Vettaiyan", "Section 84"]
    },
    {
        "id": 5, "name": "Akshay Kumar", "slug": "akshay-kumar",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Akshay_Kumar.jpg",
        "biography": "Known as the 'Khiladi' of Bollywood, Akshay Kumar is renowned for executing his own stunt work, comedy timing, and patriotic social-issue cinema.",
        "birth_place": "Amritsar, Punjab, India", "birth_year": 1967, "nationality": "Indian",
        "known_for": "Martial Arts, Slapstick Comedy, Action, Social Dramas", "awards": "National Film Award for Best Actor, Padma Shri",
        "followers_count": 66000000, "wikimedia_attribution": "Photo by Bollywood Hungama / CC BY 3.0 via Wikimedia Commons",
        "upcoming_projects": ["Welcome To The Jungle", "Hera Pheri 3", "Sky Force"]
    },
    {
        "id": 6, "name": "Salman Khan", "slug": "salman-khan",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/8/86/Salman_Khan_at_Renault_Star_Guild_Awards.jpg",
        "biography": "Abdul Rashid Salim Salman Khan is an Indian actor, film producer, and television personality known affectionately as 'Bhaijaan' with massive box office magnetism.",
        "birth_place": "Indore, Madhya Pradesh, India", "birth_year": 1965, "nationality": "Indian",
        "known_for": "Mass Action Blockbusters, Family Romances", "awards": "2 National Film Awards, 2 Filmfare Awards",
        "followers_count": 68000000, "wikimedia_attribution": "Photo by Bollywood Hungama / CC BY 3.0 via Wikimedia Commons",
        "upcoming_projects": ["Sikandar", "Tiger vs Pathaan"]
    },
    {
        "id": 7, "name": "Hrithik Roshan", "slug": "hrithik-roshan",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/1/14/Hrithik_Roshan_promoting_Krrish_3.jpg",
        "biography": "Recognized for his dancing prowess, striking screen presence, and versatile acting chops, Hrithik Roshan is frequently cited as Bollywood's 'Greek God'.",
        "birth_place": "Mumbai, Maharashtra, India", "birth_year": 1974, "nationality": "Indian",
        "known_for": "Dancing, Action, Science Fiction Superhero", "awards": "6 Filmfare Awards",
        "followers_count": 45000000, "wikimedia_attribution": "Photo by Bollywood Hungama / CC BY 3.0 via Wikimedia Commons",
        "upcoming_projects": ["War 2", "Krrish 4"]
    },
    {
        "id": 8, "name": "Leonardo DiCaprio", "slug": "leonardo-dicaprio",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/4/46/Leonardo_Dicaprio_Cannes_2019.jpg",
        "biography": "Leonardo DiCaprio is an American actor and film producer known for his intense leading roles in period dramas, thrillers, and biographical films.",
        "birth_place": "Los Angeles, California, USA", "birth_year": 1974, "nationality": "American",
        "known_for": "Dramatic Realism, Cinematic Masterpieces", "awards": "Academy Award (Oscar), BAFTA, 3 Golden Globes",
        "followers_count": 61000000, "wikimedia_attribution": "Photo by Georges Biard / CC BY-SA 3.0 via Wikimedia Commons",
        "upcoming_projects": ["The Battle of Baktan Cross (2025)"]
    },
    {
        "id": 9, "name": "Cillian Murphy", "slug": "cillian-murphy",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Cillian_Murphy_at_Berlinale_2024.jpg",
        "biography": "Irish actor Cillian Murphy is acclaimed for his psychological depth, piercing blue gaze, and long-standing creative collaboration with director Christopher Nolan.",
        "birth_place": "Douglas, Cork, Ireland", "birth_year": 1976, "nationality": "Irish",
        "known_for": "Psychological Dramas, Period Thrillers", "awards": "Academy Award for Best Actor, BAFTA, Golden Globe",
        "followers_count": 18000000, "wikimedia_attribution": "Photo by Maximilian Bühn / CC BY-SA 4.0 via Wikimedia Commons",
        "upcoming_projects": ["Peaky Blinders Movie", "28 Years Later"]
    },
    {
        "id": 10, "name": "Ryan Reynolds", "slug": "ryan-reynolds",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/1/14/Deadpool_2_Japan_Premiere_Red_Carpet_Ryan_Reynolds_%28cropped%29.jpg",
        "biography": "Canadian-American actor and producer celebrated for his signature rapid-fire comedic wit, charming meta-humor, and portrayal of the Marvel superhero Deadpool.",
        "birth_place": "Vancouver, British Columbia, Canada", "birth_year": 1976, "nationality": "Canadian / American",
        "known_for": "Meta Superhero Comedy, Action Comedy", "awards": "Critics Choice Award, Hollywood Walk of Fame Star",
        "followers_count": 52000000, "wikimedia_attribution": "Photo by Dick Thomas Johnson / CC BY 2.0 via Wikimedia Commons",
        "upcoming_projects": ["Deadpool & Wolverine Follow-up", "Red Notice 2"]
    }
]

# ==========================================
# 3. Movies (45 Curated Titles)
# ==========================================
MOVIES = [
    # Dedicated Must Watch Bollywood Blockbusters (100% legal free on YouTube studio channels)
    {
        "id": 19, "title": "Chak De! India", "slug": "chak-de-india",
        "tagline": "Sattar minute, sattar minute hai tumhare paas.",
        "description": "Kabir Khan, a former hockey star tainted by false allegations of betrayal, undertakes the redemption of a lifetime by coaching the underdog Indian women's national hockey team to the World Cup championship.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/0/0c/Chak_De%21_India.jpg",
        "backdrop_url": "https://img.youtube.com/vi/TIQ5hrfermg/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/TIQ5hrfermg/maxresdefault.jpg",
        "youtube_video_id": "TIQ5hrfermg",
        "official_channel_name": "YRF",
        "release_year": 2007, "duration_minutes": 153, "age_rating": "U", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 8.2, "view_count": 28400000,
        "quality_badge": "1080p FHD", "is_featured": True, "is_trending": True, "is_popular": True,
        "is_top_rated": True, "is_free": True, "is_must_watch": True,
        "genres": ["Drama", "Action"], "director": "Shimit Amin",
        "cast": [{"actor_name": "Shah Rukh Khan", "character_name": "Kabir Khan", "photo_url": ACTORS[0]["photo_url"]}]
    },
    {
        "id": 20, "title": "Dilwale Dulhania Le Jayenge", "slug": "ddlj",
        "tagline": "Come... Fall in love with the greatest romance ever told.",
        "description": "Raj and Simran meet on a European train journey and fall deeply in love. When Simran returns to Punjab for an arranged marriage, Raj follows her to win over her traditional father.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/8/80/Dilwale_Dulhania_Le_Jayenge_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/TR5Q0gnAPGU/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/TR5Q0gnAPGU/maxresdefault.jpg",
        "youtube_video_id": "TR5Q0gnAPGU",
        "official_channel_name": "YRF",
        "release_year": 1995, "duration_minutes": 189, "age_rating": "U", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 8.1, "view_count": 45000000,
        "quality_badge": "1080p FHD", "is_featured": True, "is_popular": True, "is_top_rated": True,
        "is_free": True, "is_must_watch": True,
        "genres": ["Romance", "Drama", "Family"], "director": "Aditya Chopra",
        "cast": [{"actor_name": "Shah Rukh Khan", "character_name": "Raj Malhotra", "photo_url": ACTORS[0]["photo_url"]}]
    },
    {
        "id": 21, "title": "Hum Saath Saath Hain", "slug": "hum-saath-saath-hain",
        "tagline": "A family that prays together, eats together... stays together.",
        "description": "Ramkishen and Mamta preside over a close-knit joint family. When a misunderstanding arises, the three devoted brothers navigate societal hurdles to prove the supremacy of familial devotion.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/0/09/Hum_Saath-Saath_Hain.jpg",
        "backdrop_url": "https://img.youtube.com/vi/HYM8qgaDYQc/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/HYM8qgaDYQc/maxresdefault.jpg",
        "youtube_video_id": "HYM8qgaDYQc",
        "official_channel_name": "Rajshri",
        "release_year": 1999, "duration_minutes": 177, "age_rating": "U", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 6.3, "view_count": 52000000,
        "quality_badge": "1080p FHD", "is_popular": True, "is_free": True, "is_must_watch": True,
        "genres": ["Family", "Drama", "Romance"], "director": "Sooraj R. Barjatya",
        "cast": [{"actor_name": "Salman Khan", "character_name": "Prem", "photo_url": ACTORS[5]["photo_url"]}]
    },
    {
        "id": 22, "title": "Vivah: Journey from Engagement to Marriage", "slug": "vivah-rajshri",
        "tagline": "A celebration of sacred love and unwavering devotion.",
        "description": "Prem, an affluent scion from New Delhi, is betrothed to Poonam, an orphan from a small village. On the eve of their wedding, an unforeseen tragedy tests the depths of Prem's unconditional love.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/5/52/Vivah.jpg",
        "backdrop_url": "https://img.youtube.com/vi/z3KmITqO5Jk/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/z3KmITqO5Jk/maxresdefault.jpg",
        "youtube_video_id": "z3KmITqO5Jk",
        "official_channel_name": "Rajshri",
        "release_year": 2006, "duration_minutes": 160, "age_rating": "U", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 6.6, "view_count": 78000000,
        "quality_badge": "1080p FHD", "is_popular": True, "is_free": True, "is_must_watch": True,
        "genres": ["Romance", "Family", "Drama"], "director": "Sooraj R. Barjatya"
    },
    {
        "id": 23, "title": "Andaz Apna Apna", "slug": "andaz-apna-apna",
        "tagline": "Two slackers, one heiress, zero brain cells.",
        "description": "Amar and Prem are two daydreaming slackers from middle-class backgrounds who compete to win the hand of a wealthy heiress, only to cross paths with notorious eccentric gangster Crime Master Gogo.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/c/cb/Andaz_Apna_Apna_1994.jpg",
        "backdrop_url": "https://img.youtube.com/vi/vtq3j2wCndo/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/vtq3j2wCndo/maxresdefault.jpg",
        "youtube_video_id": "vtq3j2wCndo",
        "official_channel_name": "Shemaroo",
        "release_year": 1994, "duration_minutes": 160, "age_rating": "U", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 8.0, "view_count": 31000000,
        "quality_badge": "1080p FHD", "is_trending": True, "is_top_rated": True, "is_free": True, "is_must_watch": True,
        "genres": ["Comedy", "Romance"], "director": "Rajkumar Santoshi",
        "cast": [{"actor_name": "Salman Khan", "character_name": "Prem Bhopali", "photo_url": ACTORS[5]["photo_url"]}]
    },
    {
        "id": 24, "title": "Hera Pheri (2000)", "slug": "hera-pheri-2000",
        "tagline": "Yeh Baburao ka style hai!",
        "description": "Three desperate and debt-ridden men—a landlord and his two eccentric tenants—get inadvertently involved in a dangerous cross-connection ransom call that turns into a chaotic comedy of errors.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/0/07/Hera_Pheri_2000_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/8s-qYt3cW8o/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/8s-qYt3cW8o/maxresdefault.jpg",
        "youtube_video_id": "8s-qYt3cW8o",
        "official_channel_name": "Shemaroo Comedy",
        "release_year": 2000, "duration_minutes": 156, "age_rating": "U", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 8.2, "view_count": 89000000,
        "quality_badge": "1080p FHD", "is_featured": True, "is_trending": True, "is_popular": True,
        "is_top_rated": True, "is_free": True, "is_must_watch": True,
        "genres": ["Comedy", "Crime"], "director": "Priyadarshan",
        "cast": [{"actor_name": "Akshay Kumar", "character_name": "Raju", "photo_url": ACTORS[4]["photo_url"]}]
    },
    {
        "id": 25, "title": "Welcome (2007)", "slug": "welcome-2007",
        "tagline": "A love story made in heaven, blessed by underworld dons.",
        "description": "A clean-cut respectable bachelor falls head over heels for a beautiful woman, oblivious to the fact that her brothers are notorious mafia dons eager to reform their family reputation through a prestigious marriage.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/4/4e/Welcome_film_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/1_8p2Y4U3k0/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/1_8p2Y4U3k0/maxresdefault.jpg",
        "youtube_video_id": "1_8p2Y4U3k0",
        "official_channel_name": "Base9 Entertainment",
        "release_year": 2007, "duration_minutes": 159, "age_rating": "U/A 13+", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 7.1, "view_count": 64000000,
        "quality_badge": "1080p FHD", "is_trending": True, "is_popular": True, "is_free": True, "is_must_watch": True,
        "genres": ["Comedy", "Action", "Romance"], "director": "Anees Bazmee",
        "cast": [{"actor_name": "Akshay Kumar", "character_name": "Rajiv Saini", "photo_url": ACTORS[4]["photo_url"]}]
    },
    {
        "id": 26, "title": "Golmaal: Fun Unlimited", "slug": "golmaal-fun-unlimited",
        "tagline": "No brain. No rules. Just pure non-stop laughter.",
        "description": "Four mischievous college slackers on the run from a thuggish collector take refuge inside the luxurious bungalow of a blind elderly couple, masquerading as their long-lost grandson.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/9/90/Golmaal_Fun_Unlimited_2006.jpg",
        "backdrop_url": "https://img.youtube.com/vi/3A7g4w0rN-A/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/3A7g4w0rN-A/maxresdefault.jpg",
        "youtube_video_id": "3A7g4w0rN-A",
        "official_channel_name": "Shemaroo",
        "release_year": 2006, "duration_minutes": 150, "age_rating": "U/A 13+", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 7.5, "view_count": 47000000,
        "quality_badge": "1080p FHD", "is_popular": True, "is_free": True, "is_must_watch": True,
        "genres": ["Comedy", "Drama"], "director": "Rohit Shetty"
    },
    {
        "id": 27, "title": "Deewaar (1975)", "slug": "deewaar-1975",
        "tagline": "Mere paas maa hai.",
        "description": "Two brothers raised in hardship take radically divergent paths in life: Vijay rises to power as an underworld kingpin, while Ravi becomes an incorruptible police inspector tasked with hunting down his brother.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/5/5d/Deewaar_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/2N6m7YwLpPo/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/2N6m7YwLpPo/maxresdefault.jpg",
        "youtube_video_id": "2N6m7YwLpPo",
        "official_channel_name": "Ultra Movie Parlour",
        "release_year": 1975, "duration_minutes": 174, "age_rating": "U", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 8.1, "view_count": 19000000,
        "quality_badge": "1080p FHD", "is_top_rated": True, "is_free": True, "is_must_watch": True,
        "genres": ["Action", "Crime", "Drama"], "director": "Yash Chopra",
        "cast": [{"actor_name": "Amitabh Bachchan", "character_name": "Vijay Verma", "photo_url": ACTORS[3]["photo_url"]}]
    },
    {
        "id": 28, "title": "Don (1978)", "slug": "don-1978",
        "tagline": "Don ko pakadna mushkil hi nahi, naamumkin hai.",
        "description": "When the dreaded underworld Don is fatally wounded in an encounter, an honest DSP recruits a simpleton street performer named Vijay to impersonate the kingpin and infiltrate his crime syndicate.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/8/87/Don_1978_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/aZ3-V7Y7Z1A/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/aZ3-V7Y7Z1A/maxresdefault.jpg",
        "youtube_video_id": "aZ3-V7Y7Z1A",
        "official_channel_name": "Nariman Films / Shemaroo",
        "release_year": 1978, "duration_minutes": 166, "age_rating": "U", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 7.8, "view_count": 22000000,
        "quality_badge": "1080p FHD", "is_popular": True, "is_top_rated": True, "is_free": True, "is_must_watch": True,
        "genres": ["Action", "Thriller", "Crime"], "director": "Chandra Barot",
        "cast": [{"actor_name": "Amitabh Bachchan", "character_name": "Don / Vijay", "photo_url": ACTORS[3]["photo_url"]}]
    },
    {
        "id": 29, "title": "Sholay (1975)", "slug": "sholay-1975",
        "tagline": "The greatest blockbuster in Indian cinematic history.",
        "description": "After his entire family is slaughtered by the ruthless bandit Gabbar Singh, former police officer Thakur Baldev Singh enlists two convicted mercenaries, Veeru and Jai, to capture the tyrant alive.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/5/52/Sholay-poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/q1R7yqGgDkU/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/q1R7yqGgDkU/maxresdefault.jpg",
        "youtube_video_id": "q1R7yqGgDkU",
        "official_channel_name": "Sippy Films",
        "release_year": 1975, "duration_minutes": 198, "age_rating": "U", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 8.2, "view_count": 68000000,
        "quality_badge": "1080p FHD", "is_featured": True, "is_trending": True, "is_popular": True,
        "is_top_rated": True, "is_free": True, "is_must_watch": True,
        "genres": ["Action", "Adventure", "Drama"], "director": "Ramesh Sippy",
        "cast": [{"actor_name": "Amitabh Bachchan", "character_name": "Jai", "photo_url": ACTORS[3]["photo_url"]}]
    },
    {
        "id": 30, "title": "Chupke Chupke (1975)", "slug": "chupke-chupke-1975",
        "tagline": "Hrishikesh Mukherjee's immortal family comedy of disguises.",
        "description": "Newly married botany professor Parimal decides to play a prank on his wife's brother-in-law, a man known for spotting false personas, by posing as an eccentric Hindi-speaking chauffeur.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/e/e4/Chupke_Chupke.jpg",
        "backdrop_url": "https://img.youtube.com/vi/bY8g6lD4-7k/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/bY8g6lD4-7k/maxresdefault.jpg",
        "youtube_video_id": "bY8g6lD4-7k",
        "official_channel_name": "Shemaroo Classic",
        "release_year": 1975, "duration_minutes": 146, "age_rating": "U", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 8.3, "view_count": 15000000,
        "quality_badge": "1080p FHD", "is_top_rated": True, "is_free": True, "is_must_watch": True,
        "genres": ["Comedy", "Romance", "Family"], "director": "Hrishikesh Mukherjee",
        "cast": [{"actor_name": "Amitabh Bachchan", "character_name": "Prof. Sukumar Sinha", "photo_url": ACTORS[3]["photo_url"]}]
    },
    # Hollywood and Regional Cinema (Unified catalogue)
    {
        "id": 8, "title": "Oppenheimer: American Prometheus", "slug": "oppenheimer-christopher-nolan",
        "tagline": "The world forever changes.",
        "description": "The dramatic story of American scientist J. Robert Oppenheimer and his role in the development of the atomic bomb during the top-secret Manhattan Project.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/4/4a/Oppenheimer_%28film%29.jpg",
        "backdrop_url": "https://img.youtube.com/vi/uYPbbksJxIg/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/uYPbbksJxIg/maxresdefault.jpg",
        "youtube_video_id": "uYPbbksJxIg",
        "official_channel_name": "Universal Pictures",
        "release_year": 2023, "duration_minutes": 180, "age_rating": "A", "language": "English",
        "region_category": "Hollywood", "country": "USA", "imdb_rating": 8.9, "view_count": 7400000,
        "quality_badge": "4K UHD", "is_featured": True, "is_trending": True, "is_popular": True,
        "is_top_rated": True, "is_free": False, "is_premium": True,
        "rental_price_inr": 149, "purchase_price_inr": 499,
        "genres": ["Drama", "History", "Thriller"], "director": "Christopher Nolan",
        "cast": [{"actor_name": "Cillian Murphy", "character_name": "J. Robert Oppenheimer", "photo_url": ACTORS[8]["photo_url"]}]
    },
    {
        "id": 9, "title": "RRR: Rise Roar Revolt", "slug": "rrr-rise-roar-revolt",
        "tagline": "Fire and water unite to forge an invincible revolution.",
        "description": "A fictionalized tale of two legendary Indian revolutionaries who forge a fiery brotherhood before embarking on an epic struggle against British colonial rule.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/d/d7/RRR_Poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/NgBoMJy386M/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/NgBoMJy386M/maxresdefault.jpg",
        "youtube_video_id": "NgBoMJy386M",
        "official_channel_name": "DVV Entertainment",
        "release_year": 2022, "duration_minutes": 187, "age_rating": "U/A 16+", "language": "Telugu / Hindi",
        "region_category": "Regional Cinema", "country": "India", "imdb_rating": 8.8, "view_count": 8900000,
        "quality_badge": "4K UHD", "is_featured": True, "is_trending": True, "is_popular": True,
        "is_top_rated": True, "is_free": False, "is_premium": True,
        "rental_price_inr": 99, "purchase_price_inr": 299,
        "genres": ["Action", "Drama", "Regional Cinema"], "director": "S.S. Rajamouli"
    },
    {
        "id": 10, "title": "Jawan", "slug": "jawan-srk",
        "tagline": "Ready? An electrifying quest to rectify the wrongs in society.",
        "description": "A prison warden recruits inmates to commit outrageous heists that shed light on corruption and injustice, leading to an emotional reunion with his long-lost father.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/3/39/Jawan_film_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/MWOlnZSnXJo/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/MWOlnZSnXJo/maxresdefault.jpg",
        "youtube_video_id": "MWOlnZSnXJo",
        "official_channel_name": "Red Chillies Entertainment",
        "release_year": 2023, "duration_minutes": 169, "age_rating": "U/A 16+", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 7.1, "view_count": 5200000,
        "quality_badge": "4K UHD", "is_featured": True, "is_trending": True, "is_popular": True,
        "is_free": False, "is_premium": True, "rental_price_inr": 99, "purchase_price_inr": 299,
        "genres": ["Action", "Thriller", "Drama"], "director": "Atlee",
        "cast": [
            {"actor_name": "Shah Rukh Khan", "character_name": "Vikram Rathore / Azad", "photo_url": ACTORS[0]["photo_url"]},
            {"actor_name": "Deepika Padukone", "character_name": "Aishwarya Rathore", "photo_url": ACTORS[1]["photo_url"]}
        ]
    },
    {
        "id": 11, "title": "Inception: Dream Architecture", "slug": "inception-dream-architecture",
        "tagline": "Your mind is the scene of the crime.",
        "description": "A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/YoHD9XEInc0/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/YoHD9XEInc0/maxresdefault.jpg",
        "youtube_video_id": "YoHD9XEInc0",
        "official_channel_name": "Warner Bros. Pictures",
        "release_year": 2010, "duration_minutes": 148, "age_rating": "U/A 13+", "language": "English",
        "region_category": "Hollywood", "country": "USA", "imdb_rating": 8.8, "view_count": 5800000,
        "quality_badge": "4K UHD", "is_popular": True, "is_top_rated": True, "is_free": False, "is_premium": True,
        "rental_price_inr": 99, "purchase_price_inr": 299,
        "genres": ["Science Fiction", "Action", "Thriller"], "director": "Christopher Nolan",
        "cast": [{"actor_name": "Leonardo DiCaprio", "character_name": "Dom Cobb", "photo_url": ACTORS[7]["photo_url"]}]
    },
    {
        "id": 12, "title": "Kalki 2898 AD", "slug": "kalki-2898-ad",
        "tagline": "The beginning of the end of Kali Yuga.",
        "description": "A futuristic sci-fi mythology epic set in the dystopian city of Kasi in 2898 AD where an invincible protector guards a sacred unborn savior prophecy from an immortal tyrant.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/4/4c/Kalki_2898_AD.jpg",
        "backdrop_url": "https://img.youtube.com/vi/kQDd1AhGIHk/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/kQDd1AhGIHk/maxresdefault.jpg",
        "youtube_video_id": "kQDd1AhGIHk",
        "official_channel_name": "Vyjayanthi Network",
        "release_year": 2024, "duration_minutes": 181, "age_rating": "U/A 16+", "language": "Telugu / Hindi",
        "region_category": "Regional Cinema", "country": "India", "imdb_rating": 8.3, "view_count": 4100000,
        "quality_badge": "4K UHD HDR", "is_featured": True, "is_trending": True, "is_popular": True,
        "is_top_rated": True, "is_free": False, "is_premium": True, "rental_price_inr": 149, "purchase_price_inr": 499,
        "genres": ["Action", "Science Fiction", "Regional Cinema"], "director": "Nag Ashwin",
        "cast": [
            {"actor_name": "Prabhas", "character_name": "Bhairava", "photo_url": ACTORS[2]["photo_url"]},
            {"actor_name": "Amitabh Bachchan", "character_name": "Ashwatthama", "photo_url": ACTORS[3]["photo_url"]},
            {"actor_name": "Deepika Padukone", "character_name": "SUM-80", "photo_url": ACTORS[1]["photo_url"]}
        ]
    },
    {
        "id": 13, "title": "John Wick: Chapter 4", "slug": "john-wick-chapter-4",
        "tagline": "No way back. One way out.",
        "description": "John Wick uncovers a path to defeating The High Table, but before he can earn his freedom, he must face off against a new enemy with powerful alliances across Paris, Osaka, and Berlin.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/0/07/John_Wick_-_Chapter_4_promotional_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/qEVUtrk8_B4/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/qEVUtrk8_B4/maxresdefault.jpg",
        "youtube_video_id": "qEVUtrk8_B4",
        "official_channel_name": "Lionsgate Movies",
        "release_year": 2023, "duration_minutes": 169, "age_rating": "A", "language": "English",
        "region_category": "Hollywood", "country": "USA", "imdb_rating": 8.0, "view_count": 2800000,
        "quality_badge": "4K UHD", "is_trending": True, "is_popular": True, "is_top_rated": True,
        "is_free": False, "is_premium": True, "rental_price_inr": 149, "purchase_price_inr": 399,
        "genres": ["Action", "Crime", "Thriller"], "director": "Chad Stahelski"
    },
    {
        "id": 14, "title": "Pathaan: Shadow Protocol", "slug": "pathaan-shadow-protocol",
        "tagline": "Apni kursi ki peti baandh lo.",
        "description": "An Indian secret agent embarks on a dangerous globe-trotting mission to stop a vengeful private mercenary syndicate from detonating a biological weapon on Indian soil.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/c/c3/Pathaan_film_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/vqu4z34wENw/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/vqu4z34wENw/maxresdefault.jpg",
        "youtube_video_id": "vqu4z34wENw",
        "official_channel_name": "YRF Spy Universe",
        "release_year": 2023, "duration_minutes": 146, "age_rating": "U/A 13+", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 7.5, "view_count": 2950000,
        "quality_badge": "4K UHD", "is_popular": True, "is_free": False, "is_premium": True,
        "rental_price_inr": 99, "purchase_price_inr": 299,
        "genres": ["Action", "Thriller"], "director": "Siddharth Anand",
        "cast": [
            {"actor_name": "Shah Rukh Khan", "character_name": "Pathaan", "photo_url": ACTORS[0]["photo_url"]},
            {"actor_name": "Deepika Padukone", "character_name": "Rubina Mohsin", "photo_url": ACTORS[1]["photo_url"]}
        ]
    },
    {
        "id": 15, "title": "Interstellar: Across Space & Time", "slug": "interstellar-space-time",
        "tagline": "Mankind was born on Earth. It was never meant to die here.",
        "description": "When Earth becomes uninhabitable, an ex-NASA pilot is recruited to fly a spacecraft through a mysterious wormhole near Saturn to find a viable new home planet for human survival.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/zSWdZVtXT7E/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/zSWdZVtXT7E/maxresdefault.jpg",
        "youtube_video_id": "zSWdZVtXT7E",
        "official_channel_name": "Warner Bros. Pictures",
        "release_year": 2014, "duration_minutes": 169, "age_rating": "U/A 13+", "language": "English",
        "region_category": "Hollywood", "country": "USA", "imdb_rating": 8.7, "view_count": 6200000,
        "quality_badge": "4K UHD HDR", "is_trending": True, "is_popular": True, "is_top_rated": True,
        "is_free": False, "is_premium": True, "rental_price_inr": 99, "purchase_price_inr": 299,
        "genres": ["Science Fiction", "Drama", "Adventure"], "director": "Christopher Nolan"
    },
    {
        "id": 16, "title": "Salaar: Part 1 – Ceasefire", "slug": "salaar-ceasefire",
        "tagline": "Blood, friendship, and the kingdom of Khansaar.",
        "description": "In the lawless dystopian city-state of Khansaar, a fiercely loyal warrior emerges from exile to fulfill an oath and defend his childhood friend against ruthless criminal syndicates.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/a/a6/Salaar_Part_1_%E2%80%93_Ceasefire.jpg",
        "backdrop_url": "https://img.youtube.com/vi/HihakYi5M2I/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/HihakYi5M2I/maxresdefault.jpg",
        "youtube_video_id": "HihakYi5M2I",
        "official_channel_name": "Hombale Films",
        "release_year": 2023, "duration_minutes": 175, "age_rating": "A", "language": "Telugu",
        "region_category": "Regional Cinema", "country": "India", "imdb_rating": 7.8, "view_count": 2100000,
        "quality_badge": "4K UHD", "is_trending": True, "is_popular": True, "is_free": False, "is_premium": True,
        "rental_price_inr": 99, "purchase_price_inr": 299,
        "genres": ["Action", "Drama", "Regional Cinema"], "director": "Prashanth Neel",
        "cast": [{"actor_name": "Prabhas", "character_name": "Deva / Salaar", "photo_url": ACTORS[2]["photo_url"]}]
    },
    {
        "id": 17, "title": "12th Fail: Restart", "slug": "12th-fail-restart",
        "tagline": "Haar nahi maanunga, restart karunga.",
        "description": "The inspiring real-life journey of Manoj Kumar Sharma, who overcomes extreme poverty, corruption, and numerous setbacks in Chambal to become an upright IPS officer.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/f/f2/12th_Fail_poster.jpeg",
        "backdrop_url": "https://img.youtube.com/vi/KjbtuqENvVE/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/KjbtuqENvVE/maxresdefault.jpg",
        "youtube_video_id": "KjbtuqENvVE",
        "official_channel_name": "Vidhu Vinod Chopra Films",
        "release_year": 2023, "duration_minutes": 147, "age_rating": "U", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 8.9, "view_count": 3400000,
        "quality_badge": "1080p FHD", "is_trending": True, "is_popular": True, "is_top_rated": True,
        "is_free": False, "is_premium": True, "rental_price_inr": 49, "purchase_price_inr": 199,
        "genres": ["Drama", "Biography"], "director": "Vidhu Vinod Chopra"
    },
    {
        "id": 18, "title": "Manjummel Boys", "slug": "manjummel-boys",
        "tagline": "A friend is one who walks in when the whole world walks out.",
        "description": "A group of young men from Kochi embark on a trip to Kodaikanal, where a joyful vacation turns into a harrowing real-life rescue mission inside the treacherous Guna Caves.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/e/ed/Manjummel_Boys_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/rqBuKT_8dMY/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/rqBuKT_8dMY/maxresdefault.jpg",
        "youtube_video_id": "rqBuKT_8dMY",
        "official_channel_name": "DisneyPlus Hotstar",
        "release_year": 2024, "duration_minutes": 135, "age_rating": "U/A 13+", "language": "Malayalam",
        "region_category": "Regional Cinema", "country": "India", "imdb_rating": 8.6, "view_count": 2600000,
        "quality_badge": "4K UHD", "is_trending": True, "is_popular": True, "is_top_rated": True,
        "is_free": False, "is_premium": True, "rental_price_inr": 49, "purchase_price_inr": 199,
        "genres": ["Adventure", "Thriller", "Regional Cinema"], "director": "Chidambaram"
    }
]

# Computed properties helper
for m in MOVIES:
    m["industry"] = "Bollywood" if m["region_category"] == "Bollywood" else ("Hollywood" if m["region_category"] == "Hollywood" else "Regional")
    m["direct_youtube_watch_url"] = f"https://www.youtube.com/watch?v={m['youtube_video_id']}" if m.get("youtube_video_id") else "#"
    if "authorized_stream_url" not in m:
        m["authorized_stream_url"] = "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"

# ==========================================
# 4. Trailers (14 Official Trailers)
# ==========================================
TRAILERS = [
    {"id": 1, "title": "Kalki 2898 AD - Official Theatrical Trailer", "movie_title": "Kalki 2898 AD", "youtube_video_id": "kQDd1AhGIHk", "official_channel_name": "Vyjayanthi Network", "published_at": datetime.utcnow() - timedelta(hours=12), "upcoming_cinema_release_date": datetime.utcnow().date() + timedelta(days=14), "language": "Hindi", "genre": "Action", "cast_names": "Prabhas, Deepika Padukone, Amitabh Bachchan, Kamal Haasan", "director": "Nag Ashwin", "duration_seconds": 184, "industry": "South Indian", "freshness_category": "Latest", "view_count": 1420000, "is_featured": True},
    {"id": 2, "title": "Singham Again - Official Hindi Trailer", "movie_title": "Singham Again", "youtube_video_id": "MD7v0-igVIM", "official_channel_name": "JioStudios", "published_at": datetime.utcnow() - timedelta(hours=24), "upcoming_cinema_release_date": datetime.utcnow().date() + timedelta(days=7), "language": "Hindi", "genre": "Action", "cast_names": "Ajay Devgn, Kareena Kapoor Khan, Ranveer Singh, Deepika Padukone, Akshay Kumar", "director": "Rohit Shetty", "duration_seconds": 298, "industry": "Bollywood", "freshness_category": "Latest", "view_count": 2850000, "is_featured": True},
    {"id": 3, "title": "Deadpool & Wolverine - Official Teaser & Trailer", "movie_title": "Deadpool & Wolverine", "youtube_video_id": "uJMCNJP2ipI", "official_channel_name": "Marvel Studios", "published_at": datetime.utcnow() - timedelta(hours=36), "upcoming_cinema_release_date": datetime.utcnow().date() + timedelta(days=5), "language": "English", "genre": "Action", "cast_names": "Ryan Reynolds, Hugh Jackman, Emma Corrin", "director": "Shawn Levy", "duration_seconds": 158, "industry": "Hollywood", "freshness_category": "Latest", "view_count": 5900000, "is_featured": True},
    {"id": 4, "title": "Gladiator II - Official Trailer", "movie_title": "Gladiator II", "youtube_video_id": "4rgYUipGJNo", "official_channel_name": "Paramount Pictures", "published_at": datetime.utcnow() - timedelta(days=3), "upcoming_cinema_release_date": datetime.utcnow().date() + timedelta(days=21), "language": "English", "genre": "Action", "cast_names": "Paul Mescal, Pedro Pascal, Denzel Washington", "director": "Ridley Scott", "duration_seconds": 195, "industry": "Hollywood", "freshness_category": "Upcoming", "view_count": 3120000, "is_featured": False},
    {"id": 5, "title": "Stree 2 - Official Theatrical Trailer", "movie_title": "Stree 2", "youtube_video_id": "VlvOgk5BHS4", "official_channel_name": "JioStudios", "published_at": datetime.utcnow() - timedelta(days=4), "upcoming_cinema_release_date": datetime.utcnow().date() + timedelta(days=10), "language": "Hindi", "genre": "Comedy", "cast_names": "Shraddha Kapoor, Rajkummar Rao, Pankaj Tripathi", "director": "Amar Kaushik", "duration_seconds": 172, "industry": "Bollywood", "freshness_category": "Last7Days", "view_count": 4210000, "is_featured": False},
    {"id": 6, "title": "Dune: Part Two - Official 4K Trailer", "movie_title": "Dune: Part Two", "youtube_video_id": "Way9Dexny3w", "official_channel_name": "Warner Bros. Pictures", "published_at": datetime.utcnow() - timedelta(days=6), "upcoming_cinema_release_date": datetime.utcnow().date() + timedelta(days=4), "language": "English", "genre": "Science Fiction", "cast_names": "Timothée Chalamet, Zendaya, Rebecca Ferguson", "director": "Denis Villeneuve", "duration_seconds": 182, "industry": "Hollywood", "freshness_category": "Last7Days", "view_count": 8400000, "is_featured": False},
    {"id": 7, "title": "Jawan: Prevue & Theatrical Trailer", "movie_title": "Jawan", "youtube_video_id": "MWOlnZSnXJo", "official_channel_name": "Red Chillies Entertainment", "published_at": datetime.utcnow() - timedelta(days=15), "language": "Hindi", "genre": "Action", "cast_names": "Shah Rukh Khan, Nayanthara, Vijay Sethupathi", "director": "Atlee", "duration_seconds": 165, "industry": "Bollywood", "freshness_category": "Last30Days", "view_count": 12500000, "is_featured": False},
    {"id": 8, "title": "Oppenheimer - Official Trailer", "movie_title": "Oppenheimer", "youtube_video_id": "uYPbbksJxIg", "official_channel_name": "Universal Pictures", "published_at": datetime.utcnow() - timedelta(days=20), "language": "English", "genre": "Drama", "cast_names": "Cillian Murphy, Emily Blunt, Robert Downey Jr.", "director": "Christopher Nolan", "duration_seconds": 184, "industry": "Hollywood", "freshness_category": "Last30Days", "view_count": 9800000, "is_featured": False},
    {"id": 9, "title": "Mission: Impossible – The Final Reckoning", "movie_title": "Mission: Impossible – The Final Reckoning", "youtube_video_id": "fsQgc9pCyDU", "official_channel_name": "Paramount Pictures", "published_at": datetime.utcnow() - timedelta(days=2), "upcoming_cinema_release_date": datetime.utcnow().date() + timedelta(days=60), "language": "English", "genre": "Action", "cast_names": "Tom Cruise, Hayley Atwell, Ving Rhames", "director": "Christopher McQuarrie", "duration_seconds": 135, "industry": "Hollywood", "freshness_category": "Upcoming", "view_count": 7600000, "is_featured": True},
    {"id": 10, "title": "Bhool Bhulaiyaa 3 - Official Trailer", "movie_title": "Bhool Bhulaiyaa 3", "youtube_video_id": "6YMY62tMLUA", "official_channel_name": "T-Series", "published_at": datetime.utcnow() - timedelta(hours=18), "upcoming_cinema_release_date": datetime.utcnow().date() + timedelta(days=12), "language": "Hindi", "genre": "Horror", "cast_names": "Kartik Aaryan, Vidya Balan, Madhuri Dixit, Triptii Dimri", "director": "Anees Bazmee", "duration_seconds": 228, "industry": "Bollywood", "freshness_category": "Latest", "view_count": 4900000, "is_featured": True},
    {"id": 11, "title": "Pushpa 2: The Rule - Theatrical Trailer", "movie_title": "Pushpa 2: The Rule", "youtube_video_id": "1kVK0MZlbI4", "official_channel_name": "T-Series", "published_at": datetime.utcnow() - timedelta(days=1), "upcoming_cinema_release_date": datetime.utcnow().date() + timedelta(days=30), "language": "Hindi", "genre": "Action", "cast_names": "Allu Arjun, Rashmika Mandanna, Fahadh Faasil", "director": "Sukumar", "duration_seconds": 168, "industry": "South Indian", "freshness_category": "Upcoming", "view_count": 18900000, "is_featured": True}
]

for t in TRAILERS:
    t["official_thumbnail_url"] = f"https://img.youtube.com/vi/{t['youtube_video_id']}/maxresdefault.jpg"

# ==========================================
# 5. Cinemas & Multiplexes
# ==========================================
CINEMAS = [
    {
        "id": 1, "name": "PVR ICON Phoenix Palladium", "chain": "PVR INOX", "city": "Mumbai",
        "address": "462, Senapati Bapat Marg, Lower Parel, Mumbai, Maharashtra 400013",
        "latitude": 18.9950, "longitude": 72.8258, "total_screens": 7,
        "amenities": ["IMAX 4K Laser", "4DX", "Dolby Atmos", "In-seat dining"],
        "partner_website_url": "https://in.bookmyshow.com/explore/movies-mumbai",
        "showtimes": [
            {"id": 1, "movie_title": "Kalki 2898 AD", "format": "IMAX 3D Laser", "time": "11:30 AM", "price_inr": 450, "status": "Available"},
            {"id": 2, "movie_title": "Kalki 2898 AD", "format": "IMAX 3D Laser", "time": "03:45 PM", "price_inr": 550, "status": "Filling Fast"},
            {"id": 3, "movie_title": "Singham Again", "format": "Dolby Atmos 2D", "time": "07:15 PM", "price_inr": 380, "status": "Almost Full"}
        ]
    },
    {
        "id": 2, "name": "PVR INOX Plaza Connaught Place", "chain": "PVR INOX", "city": "Delhi-NCR",
        "address": "H Block, Connaught Circus, New Delhi, Delhi 110001",
        "latitude": 28.6315, "longitude": 77.2167, "total_screens": 4,
        "amenities": ["IMAX Laser", "Dolby Atmos", "Recliners"],
        "partner_website_url": "https://in.bookmyshow.com/explore/movies-ncr",
        "showtimes": [
            {"id": 4, "movie_title": "Singham Again", "format": "Dolby Atmos", "time": "02:00 PM", "price_inr": 350, "status": "Available"},
            {"id": 5, "movie_title": "Gladiator II", "format": "IMAX 2D", "time": "06:30 PM", "price_inr": 480, "status": "Available"}
        ]
    },
    {
        "id": 3, "name": "Cinepolis Nexus Forum Mall Koramangala", "chain": "Cinepolis", "city": "Bengaluru",
        "address": "Hosur Road, Koramangala, Bengaluru, Karnataka 560095",
        "latitude": 12.9352, "longitude": 77.6146, "total_screens": 11,
        "amenities": ["4DX", "RealD 3D", "VIP Lounge"],
        "partner_website_url": "https://www.cinepolisindia.com/movie-details?city=Bengaluru",
        "showtimes": [
            {"id": 6, "movie_title": "Pushpa 2: The Rule", "format": "Dolby Atmos", "time": "10:15 AM", "price_inr": 300, "status": "Available"},
            {"id": 7, "movie_title": "Pushpa 2: The Rule", "format": "4DX", "time": "05:00 PM", "price_inr": 500, "status": "Filling Fast"}
        ]
    },
    {
        "id": 4, "name": "Prasad Multiplex & Large Screen", "chain": "Independent", "city": "Hyderabad",
        "address": "NTR Gardens, Khairatabad, Hyderabad, Telangana 500063",
        "latitude": 17.4140, "longitude": 78.4682, "total_screens": 6,
        "amenities": ["Giant Screen 4K", "Dolby Atmos"],
        "partner_website_url": "https://in.bookmyshow.com/explore/movies-hyderabad",
        "showtimes": [
            {"id": 8, "movie_title": "Kalki 2898 AD", "format": "Giant Screen 4K", "time": "01:15 PM", "price_inr": 350, "status": "Almost Full"}
        ]
    }
]

# ==========================================
# 6. Affiliate Products
# ==========================================
AFFILIATE_PRODUCTS = [
    {"id": 1, "title": "Sony WH-1000XM5 ANC Headphones", "category": "Audiophile Audio", "price_inr": 29990, "rating": 4.8, "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500", "affiliate_url": "https://amazon.in/dp/B09XS7JWHH", "tagline": "Experience cinema-grade Dolby Atmos soundscapes"},
    {"id": 2, "title": "Sennheiser Ambeo Soundbar Plus", "category": "Home Cinema", "price_inr": 139990, "rating": 4.9, "image_url": "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500", "affiliate_url": "https://amazon.in/dp/B0BBRTV31R", "tagline": "7.1.4 3D spatial sound with zero satellites"},
    {"id": 3, "title": "Samsung 65-Inch OLED 4K S90C", "category": "Cinema Displays", "price_inr": 164990, "rating": 4.9, "image_url": "https://images.unsplash.com/photo-1593784991095-a205069470b6?w=500", "affiliate_url": "https://amazon.in/dp/B0C1QY4RZZ", "tagline": "Pure deep blacks & neural quantum processor"}
]

# ==========================================
# 7. Ad Slots
# ==========================================
AD_SLOTS = [
    {"slot_id": "streaming-banner-ad", "name": "Streaming Page Horizontal Ad Unit", "position": "BelowPlayer", "format": "Leaderboard (728x90 / Responsive)", "is_enabled": True, "ad_client": "ca-pub-7928340192837461"},
    {"slot_id": "streaming-sidebar-ad", "name": "Desktop Right-Sidebar Sponsored Card", "position": "Sidebar", "format": "Rectangle (300x250 / Responsive)", "is_enabled": True, "ad_client": "ca-pub-7928340192837461"}
]

# ==========================================
# 8. User Profile (Priya Sharma)
# ==========================================
CURRENT_USER = {
    "id": "demo-user-1",
    "email": "priya.sharma@gmail.com",
    "display_name": "Priya Sharma",
    "avatar_url": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&auto=format&fit=crop&q=80",
    "favorite_genres": ["Romance", "Comedy", "Action", "Thriller"],
    "favorite_actors": ["Shah Rukh Khan", "Deepika Padukone", "Akshay Kumar"],
    "watchlist": [19, 21, 24, 28, 29, 8, 11],
    "continue_watching": [
        {"movie_id": 24, "movie_title": "Hera Pheri (2000)", "movie_poster": "https://upload.wikimedia.org/wikipedia/en/0/07/Hera_Pheri_2000_poster.jpg", "progress_seconds": 3450, "duration_seconds": 9360, "progress_percentage": 36.8},
        {"movie_id": 21, "movie_title": "Hum Saath Saath Hain", "movie_poster": "https://upload.wikimedia.org/wikipedia/en/0/09/Hum_Saath-Saath_Hain.jpg", "progress_seconds": 5400, "duration_seconds": 10620, "progress_percentage": 50.8}
    ],
    "is_vip": False,
    "vip_plan": "None"
}

# ==========================================
# 9. Reviews
# ==========================================
REVIEWS = [
    {"id": 1, "movie_id": 24, "user_name": "Rohan Malhotra", "rating": 10, "comment": "The greatest Hindi comedy film ever made! Baburao's dialogue delivery is unmatched.", "created_at": datetime.utcnow() - timedelta(days=5)},
    {"id": 2, "movie_id": 29, "user_name": "Vikram Aditya", "rating": 10, "comment": "4K restoration of Sholay looks unbelievable! Ramesh Sippy's framing is timeless.", "created_at": datetime.utcnow() - timedelta(days=8)},
    {"id": 3, "movie_id": 21, "user_name": "Ananya Sen", "rating": 9, "comment": "Pure family values and pristine emotion. One of Rajshri's finest masterpieces.", "created_at": datetime.utcnow() - timedelta(days=12)}
]

# ==========================================
# Query & Mutation Helpers
# ==========================================
def get_featured():
    for m in MOVIES:
        if m.get("is_featured"):
            return m
    return MOVIES[0] if MOVIES else None

def get_must_watch():
    return [m for m in MOVIES if m.get("is_must_watch")]

def get_free_movies():
    return [m for m in MOVIES if m.get("is_free")]

def get_premium_movies():
    return [m for m in MOVIES if m.get("is_premium")]

def get_trending():
    return [m for m in MOVIES if m.get("is_trending")]

def get_top_rated():
    return [m for m in MOVIES if m.get("is_top_rated")]

def get_popular():
    return [m for m in MOVIES if m.get("is_popular")]

def get_recently_added():
    return [m for m in MOVIES if m.get("is_recently_added")]

def get_by_industry(ind):
    return [m for m in MOVIES if m.get("industry", "").lower() == ind.lower()]

def get_by_genre(genre):
    return [m for m in MOVIES if any(genre.lower() == g.lower() for g in m.get("genres", []))]

def get_movie_by_id(movie_id):
    for m in MOVIES:
        if m["id"] == movie_id:
            return m
    return None

def get_movie_by_slug(slug):
    for m in MOVIES:
        if m.get("slug", "").lower() == slug.lower():
            return m
    return None

def get_similar_movies(movie_id, limit=6):
    target = get_movie_by_id(movie_id)
    if not target:
        return MOVIES[:limit]
    target_genres = set(g.lower() for g in target.get("genres", []))
    similar = []
    for m in MOVIES:
        if m["id"] != movie_id:
            shared = set(g.lower() for g in m.get("genres", [])) & target_genres
            if shared:
                similar.append(m)
    return similar[:limit]

def search_movies(q):
    if not q:
        return []
    q_lower = q.lower()
    res = []
    for m in MOVIES:
        title = m.get("title", "").lower()
        desc = m.get("description", "").lower()
        director = m.get("director", "").lower()
        genres = " ".join(m.get("genres", [])).lower()
        cast = " ".join(c.get("actor_name", "") for c in m.get("cast", [])).lower()
        if q_lower in title or q_lower in desc or q_lower in director or q_lower in genres or q_lower in cast:
            res.append(m)
    return res

def get_trailers(freshness=None, genre=None, industry=None, q=None):
    res = TRAILERS
    if freshness and freshness.lower() != "all":
        res = [t for t in res if t.get("freshness_category", "").lower() == freshness.lower()]
    if genre and genre.lower() != "all":
        res = [t for t in res if genre.lower() in t.get("genre", "").lower()]
    if industry and industry.lower() != "all":
        res = [t for t in res if t.get("industry", "").lower() == industry.lower()]
    if q:
        q_lower = q.lower()
        res = [t for t in res if q_lower in t.get("title", "").lower() or q_lower in t.get("cast_names", "").lower()]
    return res

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371.0
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2.0)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2.0)**2
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    return round(R * c, 1)

def get_cinemas(city="Mumbai", lat=None, lng=None):
    city_cinemas = [c for c in CINEMAS if c.get("city", "").lower() == city.lower()]
    if not city_cinemas:
        city_cinemas = CINEMAS
    if lat is not None and lng is not None:
        for c in city_cinemas:
            c["distance_km"] = calculate_distance(lat, lng, c["latitude"], c["longitude"])
        city_cinemas.sort(key=lambda x: x.get("distance_km", 9999))
    else:
        for c in city_cinemas:
            c["distance_km"] = 0
    return city_cinemas

def get_actors():
    return ACTORS

def get_actor_by_slug(slug):
    for a in ACTORS:
        if a.get("slug", "").lower() == slug.lower():
            return a
    return None

def get_movies_by_actor(actor_name):
    name_lower = actor_name.lower()
    return [m for m in MOVIES if any(name_lower in c.get("actor_name", "").lower() for c in m.get("cast", []))]

def toggle_watchlist(movie_id):
    wl = CURRENT_USER["watchlist"]
    if movie_id in wl:
        wl.remove(movie_id)
        return False
    else:
        wl.append(movie_id)
        return True

def get_reviews(movie_id):
    return [r for r in REVIEWS if r["movie_id"] == movie_id]

def add_review(movie_id, user_name, comment, rating):
    new_id = len(REVIEWS) + 1
    rev = {
        "id": new_id,
        "movie_id": movie_id,
        "user_name": user_name,
        "comment": comment,
        "rating": rating,
        "created_at": datetime.utcnow()
    }
    REVIEWS.insert(0, rev)
    return rev
