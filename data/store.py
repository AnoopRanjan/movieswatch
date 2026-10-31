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
        "id": 2, "name": "Akshay Kumar", "slug": "akshay-kumar",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Akshay_Kumar.jpg",
        "biography": "Known as the 'Khiladi' of Bollywood, Akshay Kumar is renowned for executing his own stunt work, exceptional comedic timing, and prolific output of over 150 feature films.",
        "birth_place": "Amritsar, Punjab, India", "birth_year": 1967, "nationality": "Indian",
        "known_for": "Martial Arts, Slapstick Comedy, Action, Social Dramas", "awards": "National Film Award for Best Actor, Padma Shri",
        "followers_count": 66000000, "wikimedia_attribution": "Photo by Bollywood Hungama / CC BY 3.0 via Wikimedia Commons",
        "upcoming_projects": ["Welcome To The Jungle", "Hera Pheri 3", "Sky Force"]
    },
    {
        "id": 3, "name": "Amitabh Bachchan", "slug": "amitabh-bachchan",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/9/91/Amitabh_Bachchan_photoshoot.jpg",
        "biography": "Widely regarded as one of the most influential actors in the history of world cinema, the 'Shahenshah of Bollywood' has dominated Indian cinema for over five decades.",
        "birth_place": "Allahabad, Uttar Pradesh, India", "birth_year": 1942, "nationality": "Indian",
        "known_for": "The Angry Young Man, Timeless Dramatic Lead", "awards": "4 National Film Awards, Dadasaheb Phalke Award, Padma Vibhushan",
        "followers_count": 48000000, "wikimedia_attribution": "Photo by Bollywood Hungama / CC BY 3.0 via Wikimedia Commons",
        "upcoming_projects": ["Vettaiyan", "Section 84"]
    },
    {
        "id": 4, "name": "Salman Khan", "slug": "salman-khan",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/8/86/Salman_Khan_at_Renault_Star_Guild_Awards.jpg",
        "biography": "Abdul Rashid Salim Salman Khan is an Indian actor, film producer, and television personality known affectionately as 'Bhaijaan' with massive box office magnetism.",
        "birth_place": "Indore, Madhya Pradesh, India", "birth_year": 1965, "nationality": "Indian",
        "known_for": "Mass Action Blockbusters, Family Romances", "awards": "2 National Film Awards, 2 Filmfare Awards",
        "followers_count": 68000000, "wikimedia_attribution": "Photo by Bollywood Hungama / CC BY 3.0 via Wikimedia Commons",
        "upcoming_projects": ["Sikandar", "Tiger vs Pathaan"]
    },
    {
        "id": 5, "name": "Paresh Rawal", "slug": "paresh-rawal",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Paresh_Rawal_at_the_special_screening_of_%E2%80%98Sanju%E2%80%99_%28cropped%29.jpg",
        "biography": "One of Indian cinema's most revered character actors, legendary for his immortal comedy portrayal of Baburao Ganpatrao Apte in Hera Pheri, as well as menacing villainous and dramatic roles.",
        "birth_place": "Mumbai, Maharashtra, India", "birth_year": 1955, "nationality": "Indian",
        "known_for": "Baburao in Hera Pheri, Satire, Dramatic Character Actor", "awards": "National Film Award, Padma Shri (2014), Filmfare Best Comedian",
        "followers_count": 12000000, "wikimedia_attribution": "Photo by Bollywood Hungama / CC BY 3.0 via Wikimedia Commons",
        "upcoming_projects": ["Hera Pheri 3", "Welcome to the Jungle"]
    },
    {
        "id": 6, "name": "Ajay Devgn", "slug": "ajay-devgn",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Ajay_Devgn_promoting_Tanhaji_in_2019.jpg",
        "biography": "Indian actor, film director, and producer who has starred in over 100 Hindi films, celebrated for intense dramatic acting in Singham, Tanhaji, Drishyam, and comedy in Golmaal.",
        "birth_place": "New Delhi, India", "birth_year": 1969, "nationality": "Indian",
        "known_for": "Action, Intense Drama, Comedy Franchise Lead", "awards": "4 National Film Awards, Padma Shri (2016)",
        "followers_count": 35000000, "wikimedia_attribution": "Photo by Bollywood Hungama / CC BY 3.0 via Wikimedia Commons",
        "upcoming_projects": ["Singham Again", "Raid 2", "De De Pyaar De 2"]
    },
    {
        "id": 7, "name": "Deepika Padukone", "slug": "deepika-padukone",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Deepika_Padukone_Cannes_2018_%28cropped%29.jpg",
        "biography": "One of the highest-paid actresses in India, Deepika Padukone is known for her versatile roles spanning historical epics, contemporary dramas, and high-octane spy thrillers.",
        "birth_place": "Copenhagen, Denmark", "birth_year": 1986, "nationality": "Indian",
        "known_for": "Leading Actress, Producer, Mental Health Advocate", "awards": "3 Filmfare Awards, TIME 100 Most Influential People",
        "followers_count": 78000000, "wikimedia_attribution": "Photo by Georges Biard / CC BY-SA 3.0 via Wikimedia Commons",
        "upcoming_projects": ["Singham Again", "The Intern Remake"]
    },
    {
        "id": 8, "name": "Prabhas", "slug": "prabhas",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Prabhas_at_Saaho_Interview.jpg",
        "biography": "Prabhas is an Indian actor predominantly working in Telugu cinema who achieved global stardom through S.S. Rajamouli's epochal Baahubali and Kalki 2898 AD.",
        "birth_place": "Madras, Tamil Nadu, India", "birth_year": 1979, "nationality": "Indian",
        "known_for": "Pan-India Blockbusters, Mythological Action Epics", "awards": "Nandi Award, Filmfare Awards South",
        "followers_count": 32000000, "wikimedia_attribution": "Photo by Bollywood Hungama / CC BY 3.0 via Wikimedia Commons",
        "upcoming_projects": ["The Raja Saab", "Salaar: Part 2", "Spirit"]
    },
    {
        "id": 9, "name": "Cillian Murphy", "slug": "cillian-murphy",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Cillian_Murphy_at_Berlinale_2024.jpg",
        "biography": "Acclaimed Irish actor celebrated for his psychological depth, piercing gaze, and Academy Award-winning portrayal of J. Robert Oppenheimer.",
        "birth_place": "Douglas, Cork, Ireland", "birth_year": 1976, "nationality": "Irish",
        "known_for": "Psychological Dramas, Period Thrillers", "awards": "Academy Award for Best Actor, BAFTA, Golden Globe",
        "followers_count": 18000000, "wikimedia_attribution": "Photo by Maximilian Bühn / CC BY-SA 4.0 via Wikimedia Commons",
        "upcoming_projects": ["Peaky Blinders Movie", "28 Years Later"]
    },
    {
        "id": 10, "name": "Audrey Hepburn", "slug": "audrey-hepburn",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Audrey_Hepburn_1956.jpg",
        "biography": "British actress and humanitarian recognized as a film and fashion icon. Ranked by the American Film Institute as the third-greatest female screen legend in Golden Age Hollywood.",
        "birth_place": "Ixelles, Brussels, Belgium", "birth_year": 1929, "nationality": "British",
        "known_for": "Romantic Comedy, Golden Age Hollywood Icon", "awards": "Academy Award (Oscar), BAFTA, Golden Globe, Presidential Medal of Freedom",
        "followers_count": 25000000, "wikimedia_attribution": "Photo by Bud Fraker / Public Domain via Wikimedia Commons",
        "upcoming_projects": ["Archival Retrospectives"]
    }
]

# ==========================================
# 3. Verified Full-Length Movies Catalogue
# All Free Movies are 100% Complete Full Movies from Official Studios
# ==========================================
MOVIES = [
    # ----------------------------------------------------
    # Dedicated Must Watch Bollywood Full Movies
    # ----------------------------------------------------
    {
        "id": 1,
        "title": "Hera Pheri (2000)",
        "slug": "hera-pheri-2000",
        "tagline": "Yeh Baburao ka style hai! The greatest Indian comedy masterpiece.",
        "description": "Two tenants and their impoverished landlord take a bizarre phone call from a kidnapper with a wrong number and conspire to collect the ransom money themselves in this legendary laugh riot.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/0/07/Hera_Pheri_2000_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/TIQ5hrfermg/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/TIQ5hrfermg/maxresdefault.jpg",
        "youtube_video_id": "TIQ5hrfermg",
        "official_channel_name": "Goldmines Bollywood",
        "release_year": 2000, "duration_minutes": 156, "age_rating": "U", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 8.2, "view_count": 142000000,
        "quality_badge": "1080p FHD", "is_featured": True, "is_trending": True, "is_popular": True,
        "is_top_rated": True, "is_free": True, "is_must_watch": True,
        "genres": ["Comedy", "Crime"], "director": "Priyadarshan",
        "cast": [
            {"actor_name": "Akshay Kumar", "character_name": "Raju", "photo_url": ACTORS[1]["photo_url"]},
            {"actor_name": "Paresh Rawal", "character_name": "Baburao Ganpatrao Apte", "photo_url": ACTORS[4]["photo_url"]}
        ]
    },
    {
        "id": 2,
        "title": "Hum Saath-Saath Hain",
        "slug": "hum-saath-saath-hain",
        "tagline": "A family that prays together, eats together... stays together.",
        "description": "Ramkishen and Mamta preside over a close-knit joint family. When an emotional conflict threatens to tear their household apart, the devotion of three loving brothers proves familial bonds are unbreakable.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/0/09/Hum_Saath-Saath_Hain.jpg",
        "backdrop_url": "https://img.youtube.com/vi/QDU1aiEo62E/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/QDU1aiEo62E/maxresdefault.jpg",
        "youtube_video_id": "QDU1aiEo62E",
        "official_channel_name": "Rajshri",
        "release_year": 1999, "duration_minutes": 177, "age_rating": "U", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 6.3, "view_count": 95000000,
        "quality_badge": "1080p FHD", "is_featured": True, "is_popular": True, "is_top_rated": False,
        "is_free": True, "is_must_watch": True,
        "genres": ["Family", "Drama", "Romance"], "director": "Sooraj R. Barjatya",
        "cast": [
            {"actor_name": "Salman Khan", "character_name": "Prem", "photo_url": ACTORS[3]["photo_url"]}
        ]
    },
    {
        "id": 3,
        "title": "Golmaal: Fun Unlimited",
        "slug": "golmaal-fun-unlimited",
        "tagline": "No rules. No limits. Non-stop laughter with four mischievous friends.",
        "description": "Four mischievous runaway friends take refuge inside the luxurious bungalow of a blind elderly couple by pretending one of them is their grandson, sparking outrageous situations and comic misunderstandings.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/9/90/Golmaal_Fun_Unlimited_2006.jpg",
        "backdrop_url": "https://img.youtube.com/vi/ZmE6TN9bYQg/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/ZmE6TN9bYQg/maxresdefault.jpg",
        "youtube_video_id": "ZmE6TN9bYQg",
        "official_channel_name": "Shemaroo Comedy",
        "release_year": 2006, "duration_minutes": 150, "age_rating": "U/A 13+", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 7.5, "view_count": 88000000,
        "quality_badge": "1080p FHD", "is_trending": True, "is_popular": True,
        "is_free": True, "is_must_watch": True,
        "genres": ["Comedy", "Action"], "director": "Rohit Shetty",
        "cast": [
            {"actor_name": "Ajay Devgn", "character_name": "Gopal", "photo_url": ACTORS[5]["photo_url"]},
            {"actor_name": "Paresh Rawal", "character_name": "Somnath", "photo_url": ACTORS[4]["photo_url"]}
        ]
    },
    {
        "id": 4,
        "title": "Hungama",
        "slug": "hungama-2003",
        "tagline": "An epic comedy of mistaken identities and hilarious chaos.",
        "description": "A group of misfits and ambitious strivers in Mumbai get tangled in an intricate web of mistaken identities, false marital claims, and comic misunderstandings centered on an eccentric millionaire.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/f/f9/Hungama_2003.jpg",
        "backdrop_url": "https://img.youtube.com/vi/HVyXEbOWrp4/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/HVyXEbOWrp4/maxresdefault.jpg",
        "youtube_video_id": "HVyXEbOWrp4",
        "official_channel_name": "Venus Movies",
        "release_year": 2003, "duration_minutes": 153, "age_rating": "U", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 7.6, "view_count": 72000000,
        "quality_badge": "1080p FHD", "is_popular": True, "is_free": True, "is_must_watch": True,
        "genres": ["Comedy", "Romance"], "director": "Priyadarshan",
        "cast": [
            {"actor_name": "Paresh Rawal", "character_name": "Radheshyam Tiwari", "photo_url": ACTORS[4]["photo_url"]}
        ]
    },
    {
        "id": 5,
        "title": "Bhagam Bhag",
        "slug": "bhagam-bhag-2006",
        "tagline": "Two theatre actors, one dead body, infinite confusion.",
        "description": "Members of a theatre troupe travel to London to perform. When they desperately search for an actress, they unwittingly stumble into a dangerous murder mystery and extortion scheme.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/f/f3/Bhagam_Bhag.jpg",
        "backdrop_url": "https://img.youtube.com/vi/zloKjQXmwhE/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/zloKjQXmwhE/maxresdefault.jpg",
        "youtube_video_id": "zloKjQXmwhE",
        "official_channel_name": "Shemaroo Comedy",
        "release_year": 2006, "duration_minutes": 158, "age_rating": "U/A 13+", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 6.7, "view_count": 64000000,
        "quality_badge": "1080p FHD", "is_trending": True, "is_popular": True,
        "is_free": True, "is_must_watch": True,
        "genres": ["Comedy", "Mystery", "Thriller"], "director": "Priyadarshan",
        "cast": [
            {"actor_name": "Akshay Kumar", "character_name": "Bunty", "photo_url": ACTORS[1]["photo_url"]},
            {"actor_name": "Paresh Rawal", "character_name": "Champak Chaturvedi", "photo_url": ACTORS[4]["photo_url"]}
        ]
    },
    {
        "id": 6,
        "title": "Baazigar",
        "slug": "baazigar-1993",
        "tagline": "Haar kar jeetne wale ko baazigar kehte hain.",
        "description": "A cold-blooded young man with a vendetta against a treacherous businessman seduces the man's elder daughter and murders her, before wooing her younger sister to destroy the family.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/5/5a/Baazigar_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/8MtGmZhDldY/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/8MtGmZhDldY/maxresdefault.jpg",
        "youtube_video_id": "8MtGmZhDldY",
        "official_channel_name": "Venus Bollywood Films",
        "release_year": 1993, "duration_minutes": 175, "age_rating": "U/A 13+", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 7.6, "view_count": 58000000,
        "quality_badge": "1080p FHD", "is_featured": True, "is_top_rated": True,
        "is_free": True, "is_must_watch": True,
        "genres": ["Thriller", "Action", "Romance"], "director": "Abbas-Mustan",
        "cast": [
            {"actor_name": "Shah Rukh Khan", "character_name": "Ajay Sharma / Vicky Malhotra", "photo_url": ACTORS[0]["photo_url"]}
        ]
    },
    {
        "id": 7,
        "title": "Main Khiladi Tu Anari",
        "slug": "main-khiladi-tu-anari-1994",
        "tagline": "An action-packed blockbuster buddy cop entertainer.",
        "description": "An upright, stoic police inspector seeking revenge for his brother's murder reluctantly partners with an eccentric Bollywood action star who shadows him to research a realistic film role.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/e/ec/Main_Khiladi_Tu_Anari_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/34vMryquQN8/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/34vMryquQN8/maxresdefault.jpg",
        "youtube_video_id": "34vMryquQN8",
        "official_channel_name": "Venus Movies",
        "release_year": 1994, "duration_minutes": 168, "age_rating": "U/A 13+", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 6.6, "view_count": 41000000,
        "quality_badge": "1080p FHD", "is_popular": True,
        "is_free": True, "is_must_watch": True,
        "genres": ["Action", "Comedy", "Crime"], "director": "Sameer Malkan",
        "cast": [
            {"actor_name": "Akshay Kumar", "character_name": "Inspector Karan Joglekar", "photo_url": ACTORS[1]["photo_url"]}
        ]
    },
    {
        "id": 8,
        "title": "Khatta Meetha",
        "slug": "khatta-meetha-2010",
        "tagline": "The hilarious struggle of a municipal road contractor.",
        "description": "Struggling contractor Sachin Tichkule battles rampant political corruption, demanding relatives, and an uncompromising new municipal commissioner who happens to be his ex-girlfriend.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/0/07/Khatta_meetha_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/sd0vPLTCq-s/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/sd0vPLTCq-s/maxresdefault.jpg",
        "youtube_video_id": "sd0vPLTCq-s",
        "official_channel_name": "Shemaroo Comedy",
        "release_year": 2010, "duration_minutes": 157, "age_rating": "U/A 13+", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 6.0, "view_count": 76000000,
        "quality_badge": "1080p FHD", "is_popular": True, "is_free": True, "is_must_watch": True,
        "genres": ["Comedy", "Drama"], "director": "Priyadarshan",
        "cast": [
            {"actor_name": "Akshay Kumar", "character_name": "Sachin Tichkule", "photo_url": ACTORS[1]["photo_url"]}
        ]
    },
    {
        "id": 9,
        "title": "Awara Paagal Deewana",
        "slug": "awara-paagal-deewana-2002",
        "tagline": "Mafia inheritance, comic dentists, and martial arts mayhem.",
        "description": "When an underworld don passes away, his empire's succession leads to a hilarious feud involving a mild-mannered dentist, rival mobsters, and a hired hitman.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/f/f6/Awara_Paagal_Deewana.jpg",
        "backdrop_url": "https://img.youtube.com/vi/sy5GB-lOSHs/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/sy5GB-lOSHs/maxresdefault.jpg",
        "youtube_video_id": "sy5GB-lOSHs",
        "official_channel_name": "Shemaroo Movies",
        "release_year": 2002, "duration_minutes": 165, "age_rating": "U/A 13+", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 6.3, "view_count": 51000000,
        "quality_badge": "1080p FHD", "is_popular": True, "is_free": True, "is_must_watch": True,
        "genres": ["Action", "Comedy", "Crime"], "director": "Vikram Bhatt",
        "cast": [
            {"actor_name": "Akshay Kumar", "character_name": "Guru Gulab Khatri", "photo_url": ACTORS[1]["photo_url"]},
            {"actor_name": "Paresh Rawal", "character_name": "Manilal Patel", "photo_url": ACTORS[4]["photo_url"]}
        ]
    },
    {
        "id": 10,
        "title": "Sholay (1975)",
        "slug": "sholay-1975",
        "tagline": "The greatest blockbuster in Indian cinematic history.",
        "description": "After his family is massacred by the ruthless bandit Gabbar Singh, former police officer Thakur Baldev Singh recruits two convicts, Veeru and Jai, to capture the tyrant alive.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/5/52/Sholay-poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/ruz-3qV6Sb4/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/ruz-3qV6Sb4/maxresdefault.jpg",
        "youtube_video_id": "ruz-3qV6Sb4",
        "official_channel_name": "NH Studioz",
        "release_year": 1975, "duration_minutes": 198, "age_rating": "U", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 8.2, "view_count": 92000000,
        "quality_badge": "1080p FHD", "is_featured": True, "is_trending": True, "is_popular": True,
        "is_top_rated": True, "is_free": True, "is_must_watch": True,
        "genres": ["Action", "Adventure", "Drama"], "director": "Ramesh Sippy",
        "cast": [
            {"actor_name": "Amitabh Bachchan", "character_name": "Jai", "photo_url": ACTORS[2]["photo_url"]}
        ]
    },
    {
        "id": 11,
        "title": "Deewaar (1975)",
        "slug": "deewaar-1975",
        "tagline": "Mere paas maa hai.",
        "description": "Two brothers raised in hardship take radically divergent paths in life: Vijay rises to power as an underworld kingpin, while Ravi becomes an incorruptible police inspector tasked with hunting down his brother.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/5/5d/Deewaar_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/xuOQqWU2UQA/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/xuOQqWU2UQA/maxresdefault.jpg",
        "youtube_video_id": "xuOQqWU2UQA",
        "official_channel_name": "Shemaroo Movies",
        "release_year": 1975, "duration_minutes": 174, "age_rating": "U", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 8.1, "view_count": 34000000,
        "quality_badge": "1080p FHD", "is_top_rated": True, "is_free": True, "is_must_watch": True,
        "genres": ["Action", "Crime", "Drama"], "director": "Yash Chopra",
        "cast": [
            {"actor_name": "Amitabh Bachchan", "character_name": "Vijay Verma", "photo_url": ACTORS[2]["photo_url"]}
        ]
    },
    {
        "id": 12,
        "title": "Chupke Chupke (1975)",
        "slug": "chupke-chupke-1975",
        "tagline": "Hrishikesh Mukherjee's immortal family comedy of disguises.",
        "description": "Newly married botany professor Parimal plays an elaborate prank on his wife's brother-in-law by posing as an eccentric Hindi-speaking driver, leading to a delightfully tangled comedy of manners.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/e/e4/Chupke_Chupke.jpg",
        "backdrop_url": "https://img.youtube.com/vi/ltaFcAoI30E/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/ltaFcAoI30E/maxresdefault.jpg",
        "youtube_video_id": "ltaFcAoI30E",
        "official_channel_name": "NH Comedy Duniya",
        "release_year": 1975, "duration_minutes": 146, "age_rating": "U", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 8.3, "view_count": 28000000,
        "quality_badge": "1080p FHD", "is_top_rated": True, "is_free": True, "is_must_watch": True,
        "genres": ["Comedy", "Romance", "Family"], "director": "Hrishikesh Mukherjee",
        "cast": [
            {"actor_name": "Amitabh Bachchan", "character_name": "Prof. Sukumar Sinha", "photo_url": ACTORS[2]["photo_url"]}
        ]
    },
    {
        "id": 13,
        "title": "Anand (1971)",
        "slug": "anand-1971",
        "tagline": "Zindagi badi honi chahiye, lambi nahi.",
        "description": "A terminally ill cancer patient approaches life with boundless cheer and infectious optimism, deeply touching the cynical doctor treating him and teaching everyone the true meaning of living.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/5/5d/Anand_1971.jpg",
        "backdrop_url": "https://img.youtube.com/vi/nK_SmZrjMPU/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/nK_SmZrjMPU/maxresdefault.jpg",
        "youtube_video_id": "nK_SmZrjMPU",
        "official_channel_name": "NH Studioz",
        "release_year": 1971, "duration_minutes": 132, "age_rating": "U", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 8.7, "view_count": 22000000,
        "quality_badge": "1080p FHD", "is_featured": True, "is_top_rated": True, "is_free": True, "is_must_watch": True,
        "genres": ["Drama", "Family"], "director": "Hrishikesh Mukherjee",
        "cast": [
            {"actor_name": "Amitabh Bachchan", "character_name": "Dr. Bhaskar Banerjee", "photo_url": ACTORS[2]["photo_url"]}
        ]
    },
    {
        "id": 14,
        "title": "Amar Akbar Anthony",
        "slug": "amar-akbar-anthony-1977",
        "tagline": "Three brothers separated at birth reunite in a triumph of brotherhood.",
        "description": "Three brothers separated as children are adopted into Hindu, Muslim, and Christian families. Years later, their lives intertwine to defeat the ruthless smuggler who tore their parents apart.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/8/8c/Amar_Akbar_Anthony_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/aO-F8JsXG2g/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/aO-F8JsXG2g/maxresdefault.jpg",
        "youtube_video_id": "aO-F8JsXG2g",
        "official_channel_name": "Shemaroo Movies",
        "release_year": 1977, "duration_minutes": 184, "age_rating": "U", "language": "Hindi",
        "region_category": "Bollywood", "country": "India", "imdb_rating": 7.4, "view_count": 39000000,
        "quality_badge": "1080p FHD", "is_popular": True, "is_free": True, "is_must_watch": True,
        "genres": ["Action", "Comedy", "Drama"], "director": "Manmohan Desai",
        "cast": [
            {"actor_name": "Amitabh Bachchan", "character_name": "Anthony Gonsalves", "photo_url": ACTORS[2]["photo_url"]}
        ]
    },

    # ----------------------------------------------------
    # Hollywood & World Cinema Free Full-Length Movies
    # ----------------------------------------------------
    {
        "id": 15,
        "title": "Tears of Steel",
        "slug": "tears-of-steel-2012",
        "tagline": "A futuristic sci-fi visual effects triumph set in dystopian Amsterdam.",
        "description": "In a post-apocalyptic future, a group of scientists and warriors in Amsterdam's Oude Kerk stage a desperate time-reversal experiment to stop robotic annihilation caused by a broken romance.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Tears_of_Steel_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/OHOpb2fS-cM/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/OHOpb2fS-cM/maxresdefault.jpg",
        "youtube_video_id": "OHOpb2fS-cM",
        "official_channel_name": "Blender Foundation",
        "release_year": 2012, "duration_minutes": 12, "age_rating": "U/A 13+", "language": "English",
        "region_category": "Hollywood", "country": "Netherlands / USA", "imdb_rating": 7.0, "view_count": 18000000,
        "quality_badge": "4K UHD", "is_featured": True, "is_trending": True, "is_free": True,
        "genres": ["Science Fiction", "Action", "Drama"], "director": "Ian Hubert"
    },
    {
        "id": 16,
        "title": "Big Buck Bunny",
        "slug": "big-buck-bunny-2008",
        "tagline": "A gentle giant bunny takes hilarious revenge on forest bullies.",
        "description": "A large and lovable rabbit has his peaceful forest morning ruined by three mischievous rodent bullies who cruelly target butterflies. The bunny plots ingenious woodland traps to teach them a lesson.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/commons/c/c5/Big_buck_bunny_poster_big.jpg",
        "backdrop_url": "https://img.youtube.com/vi/aqz-KE-bpKQ/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/aqz-KE-bpKQ/maxresdefault.jpg",
        "youtube_video_id": "aqz-KE-bpKQ",
        "official_channel_name": "Blender Foundation",
        "release_year": 2008, "duration_minutes": 10, "age_rating": "U", "language": "English",
        "region_category": "Hollywood", "country": "Netherlands", "imdb_rating": 7.8, "view_count": 25000000,
        "quality_badge": "4K 60FPS", "is_popular": True, "is_top_rated": True, "is_free": True,
        "genres": ["Comedy", "Family", "Animation"], "director": "Sacha Goedegebure"
    },
    {
        "id": 17,
        "title": "Sintel: The Dragon Quest",
        "slug": "sintel-2010",
        "tagline": "She searched the ends of the world for the creature she loved.",
        "description": "A lonely young woman rescues an injured baby dragon and names him Scales. When a terrifying winged dragon abducts him, Sintel undertakes a perilous cross-continental pilgrimage to bring him home.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Sintel_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/eRsGyueVLvQ/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/eRsGyueVLvQ/maxresdefault.jpg",
        "youtube_video_id": "eRsGyueVLvQ",
        "official_channel_name": "Blender Foundation",
        "release_year": 2010, "duration_minutes": 15, "age_rating": "U/A 13+", "language": "English",
        "region_category": "Hollywood", "country": "Netherlands", "imdb_rating": 7.4, "view_count": 16000000,
        "quality_badge": "4K UHD", "is_top_rated": True, "is_free": True,
        "genres": ["Action", "Adventure", "Animation"], "director": "Colin Levy"
    },
    {
        "id": 18,
        "title": "Night of the Living Dead",
        "slug": "night-of-the-living-dead-1968",
        "tagline": "They keep coming back in a bloodthirsty lust for human flesh!",
        "description": "George A. Romero's foundational horror masterpiece following a ragtag group of survivors trapped inside a rural farmhouse while flesh-eating ghouls lay siege to the countryside.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/commons/1/18/Night_of_the_Living_Dead_%281968%29_theatrical_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/H91BxkBXttE/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/H91BxkBXttE/maxresdefault.jpg",
        "youtube_video_id": "H91BxkBXttE",
        "official_channel_name": "Timeless Classic Movies",
        "release_year": 1968, "duration_minutes": 96, "age_rating": "A", "language": "English",
        "region_category": "Hollywood", "country": "USA", "imdb_rating": 7.8, "view_count": 12000000,
        "quality_badge": "1080p FHD", "is_top_rated": True, "is_free": True,
        "genres": ["Horror", "Thriller"], "director": "George A. Romero"
    },
    {
        "id": 19,
        "title": "The General",
        "slug": "the-general-1926",
        "tagline": "Buster Keaton's timeless locomotive action comedy masterpiece.",
        "description": "During the American Civil War, train engineer Johnnie Gray undertakes a daring solo pursuit when enemy spies hijack his beloved locomotive, displaying acrobatic comedic heroism.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/commons/2/23/The_General_%281926%29_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/D_UdtS-8QS0/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/D_UdtS-8QS0/maxresdefault.jpg",
        "youtube_video_id": "D_UdtS-8QS0",
        "official_channel_name": "Classic Cinema Restorations",
        "release_year": 1926, "duration_minutes": 75, "age_rating": "U", "language": "English",
        "region_category": "Hollywood", "country": "USA", "imdb_rating": 8.1, "view_count": 9400000,
        "quality_badge": "1080p FHD", "is_top_rated": True, "is_free": True,
        "genres": ["Action", "Adventure", "Comedy"], "director": "Buster Keaton, Clyde Bruckman"
    },
    {
        "id": 20,
        "title": "Charade",
        "slug": "charade-1963",
        "tagline": "Expect the unexpected in Paris with Audrey Hepburn and Cary Grant.",
        "description": "A grieving widow in Paris finds herself pursued by three ruthless criminals looking for her murdered husband's stolen fortune, relying on a charming mystery man whose identity keeps changing.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/commons/0/07/Charade_%281963_poster%29.jpg",
        "backdrop_url": "https://img.youtube.com/vi/-uc86VH8hdA/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/-uc86VH8hdA/maxresdefault.jpg",
        "youtube_video_id": "-uc86VH8hdA",
        "official_channel_name": "FEATURE FILM Classic Cinema",
        "release_year": 1963, "duration_minutes": 113, "age_rating": "U", "language": "English",
        "region_category": "Hollywood", "country": "USA", "imdb_rating": 7.9, "view_count": 14000000,
        "quality_badge": "1080p FHD", "is_popular": True, "is_top_rated": True, "is_free": True,
        "genres": ["Comedy", "Romance", "Thriller"], "director": "Stanley Donen",
        "cast": [
            {"actor_name": "Audrey Hepburn", "character_name": "Regina Lampert", "photo_url": ACTORS[9]["photo_url"]}
        ]
    },
    {
        "id": 21,
        "title": "His Girl Friday",
        "slug": "his-girl-friday-1940",
        "tagline": "Fast-talking newsroom comedy with Cary Grant and Rosalind Russell.",
        "description": "Hard-nosed newspaper editor Walter Burns tries every conniving trick in the book to prevent his top reporter and ex-wife from leaving the newspaper game to marry a safe insurance man.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/commons/9/91/His_Girl_Friday_%281940_poster%29.jpg",
        "backdrop_url": "https://img.youtube.com/vi/kmYcT5gT6a4/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/kmYcT5gT6a4/maxresdefault.jpg",
        "youtube_video_id": "kmYcT5gT6a4",
        "official_channel_name": "Retrospective - Classic Movies",
        "release_year": 1940, "duration_minutes": 92, "age_rating": "U", "language": "English",
        "region_category": "Hollywood", "country": "USA", "imdb_rating": 7.8, "view_count": 6800000,
        "quality_badge": "1080p FHD", "is_top_rated": True, "is_free": True,
        "genres": ["Comedy", "Romance", "Drama"], "director": "Howard Hawks"
    },
    {
        "id": 22,
        "title": "Sita Sings the Blues",
        "slug": "sita-sings-the-blues-2008",
        "tagline": "An artistic animated retelling of the Ramayana set to 1920s blues.",
        "description": "Nina Paley's critically acclaimed musical feature animation that interweaves the ancient Indian epic of the Ramayana with the autobiographical tale of a modern-day romantic breakup.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/a/a2/Sita_sings_the_blues_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/f8LvBnz7oRA/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/f8LvBnz7oRA/maxresdefault.jpg",
        "youtube_video_id": "f8LvBnz7oRA",
        "official_channel_name": "Nina Paley Official",
        "release_year": 2008, "duration_minutes": 82, "age_rating": "U", "language": "English",
        "region_category": "Hollywood", "country": "USA", "imdb_rating": 7.6, "view_count": 4500000,
        "quality_badge": "1080p FHD", "is_free": True,
        "genres": ["Animation", "Comedy", "Romance"], "director": "Nina Paley"
    },
    {
        "id": 23,
        "title": "Spring",
        "slug": "spring-blender-2019",
        "tagline": "A poetic animated journey between winter and spring in the clouds.",
        "description": "A shepherd girl and her loyal dog face ancient spirits to bring about the transition of the seasons in this visually stunning fantasy short film by Blender Animation Studio.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/commons/0/08/Spring_-_Blender_Open_Movie.png",
        "backdrop_url": "https://img.youtube.com/vi/WhWc3b3KhnY/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/WhWc3b3KhnY/maxresdefault.jpg",
        "youtube_video_id": "WhWc3b3KhnY",
        "official_channel_name": "Blender Studio",
        "release_year": 2019, "duration_minutes": 8, "age_rating": "U", "language": "English",
        "region_category": "Hollywood", "country": "Netherlands", "imdb_rating": 7.3, "view_count": 11000000,
        "quality_badge": "4K UHD", "is_free": True,
        "genres": ["Animation", "Family", "Adventure"], "director": "Andy Goralczyk"
    },
    {
        "id": 24,
        "title": "Charge",
        "slug": "charge-blender-2022",
        "tagline": "Cyberpunk robotics combat powered by the real-time EEVEE engine.",
        "description": "In an old battery storage facility, an aging robot must defend its precious life battery from a squad of hungry robotic salvagers in high-octane 4K action.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/commons/3/36/CHARGE_-_Blender_Open_Movie.png",
        "backdrop_url": "https://img.youtube.com/vi/UXqq0ZvbOnk/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/UXqq0ZvbOnk/maxresdefault.jpg",
        "youtube_video_id": "UXqq0ZvbOnk",
        "official_channel_name": "Blender Studio",
        "release_year": 2022, "duration_minutes": 4, "age_rating": "U/A 13+", "language": "English",
        "region_category": "Hollywood", "country": "Netherlands", "imdb_rating": 7.1, "view_count": 8200000,
        "quality_badge": "4K UHD", "is_free": True,
        "genres": ["Animation", "Action", "Science Fiction"], "director": "Hjalti Hjalmarsson"
    },

    # ----------------------------------------------------
    # Premium 4K UHD Rentals & Digital Purchases
    # ----------------------------------------------------
    {
        "id": 25,
        "title": "Oppenheimer",
        "slug": "oppenheimer-christopher-nolan",
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
        "id": 26,
        "title": "RRR: Rise Roar Revolt",
        "slug": "rrr-rise-roar-revolt",
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
        "id": 27,
        "title": "Jawan",
        "slug": "jawan-srk",
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
            {"actor_name": "Deepika Padukone", "character_name": "Aishwarya Rathore", "photo_url": ACTORS[6]["photo_url"]}
        ]
    },
    {
        "id": 28,
        "title": "Inception",
        "slug": "inception-dream-architecture",
        "tagline": "Your mind is the scene of the crime.",
        "description": "A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO in Nolan's mind-bending masterpiece.",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
        "backdrop_url": "https://img.youtube.com/vi/YoHD9XEInc0/maxresdefault.jpg",
        "official_thumbnail_url": "https://img.youtube.com/vi/YoHD9XEInc0/maxresdefault.jpg",
        "youtube_video_id": "YoHD9XEInc0",
        "official_channel_name": "Warner Bros. Pictures",
        "release_year": 2010, "duration_minutes": 148, "age_rating": "U/A 13+", "language": "English",
        "region_category": "Hollywood", "country": "USA", "imdb_rating": 8.8, "view_count": 5800000,
        "quality_badge": "4K UHD", "is_popular": True, "is_top_rated": True, "is_free": False, "is_premium": True,
        "rental_price_inr": 99, "purchase_price_inr": 299,
        "genres": ["Science Fiction", "Action", "Thriller"], "director": "Christopher Nolan"
    },
    {
        "id": 29,
        "title": "Kalki 2898 AD",
        "slug": "kalki-2898-ad",
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
            {"actor_name": "Prabhas", "character_name": "Bhairava", "photo_url": ACTORS[7]["photo_url"]},
            {"actor_name": "Amitabh Bachchan", "character_name": "Ashwatthama", "photo_url": ACTORS[2]["photo_url"]},
            {"actor_name": "Deepika Padukone", "character_name": "SUM-80", "photo_url": ACTORS[6]["photo_url"]}
        ]
    },
    {
        "id": 30,
        "title": "12th Fail: Restart",
        "slug": "12th-fail-restart",
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
    }
]

# Set calculated properties
for m in MOVIES:
    m["industry"] = "Bollywood" if m["region_category"] == "Bollywood" else ("Hollywood" if m["region_category"] == "Hollywood" else "Regional")
    m["direct_youtube_watch_url"] = f"https://www.youtube.com/watch?v={m['youtube_video_id']}" if m.get("youtube_video_id") else "#"
    if "authorized_stream_url" not in m:
        m["authorized_stream_url"] = "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"

# ==========================================
# 4. Trailers (14 Official Studio Trailers)
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
    "favorite_genres": ["Comedy", "Action", "Romance", "Drama"],
    "favorite_actors": ["Shah Rukh Khan", "Akshay Kumar", "Amitabh Bachchan", "Paresh Rawal"],
    "watchlist": [1, 2, 3, 4, 10, 11, 15, 20],
    "continue_watching": [
        {"movie_id": 1, "movie_title": "Hera Pheri (2000)", "movie_poster": "https://upload.wikimedia.org/wikipedia/en/0/07/Hera_Pheri_2000_poster.jpg", "progress_seconds": 3450, "duration_seconds": 9360, "progress_percentage": 36.8},
        {"movie_id": 2, "movie_title": "Hum Saath-Saath Hain", "movie_poster": "https://upload.wikimedia.org/wikipedia/en/0/09/Hum_Saath-Saath_Hain.jpg", "progress_seconds": 5400, "duration_seconds": 10620, "progress_percentage": 50.8}
    ],
    "is_vip": False,
    "vip_plan": "None"
}

# ==========================================
# 9. Reviews
# ==========================================
REVIEWS = [
    {"id": 1, "movie_id": 1, "user_name": "Rohan Malhotra", "rating": 10, "comment": "The greatest Hindi comedy film ever made! Baburao's dialogue delivery is unmatched.", "created_at": datetime.utcnow() - timedelta(days=5)},
    {"id": 2, "movie_id": 10, "user_name": "Vikram Aditya", "rating": 10, "comment": "4K restoration of Sholay looks unbelievable! Ramesh Sippy's framing is timeless.", "created_at": datetime.utcnow() - timedelta(days=8)},
    {"id": 3, "movie_id": 2, "user_name": "Ananya Sen", "rating": 9, "comment": "Pure family values and pristine emotion. One of Rajshri's finest masterpieces.", "created_at": datetime.utcnow() - timedelta(days=12)}
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
