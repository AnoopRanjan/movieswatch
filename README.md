# CinePulse — Next-Gen AI-Powered Movie Streaming, Trailer Discovery & Cinema Booking Platform (Python Edition)

> **Cinematic Excellence, Everywhere.**  
> An original, production-ready, dark-themed OTT movie streaming, discovery, trailer hub, and location-based cinema ticket booking platform built with **Python 3.12 & Flask**.

---

## 🌟 Architecture & Core Capabilities

CinePulse combines a cinematic, responsive front-end with a high-performance **Python 3.12 & Flask** backend engine, featuring an intelligent movie discovery system, legal YouTube video integration with quota tracking, trailer discovery across freshness windows, nearby cinema multiplex geolocation using the **Haversine formula**, and **authorized ticket booking redirection (BookMyShow & Cinepolis India)**.

```
                               ┌────────────────────────────────────────────────────────┐
                               │                  CinePulse OTT Client                  │
                               │   (Tailwind, Vanilla ES6+, FontAwesome, Location API)  │
                               └───────────────────────────┬────────────────────────────┘
                                                           │
                                             HTTP / Jinja2 / JSON REST APIs
                                                           │
                               ┌───────────────────────────▼────────────────────────────┐
                               │                CinePulse Python Engine                 │
                               │                   (Flask 3.1 & WSGI)                   │
                               └───────┬───────────────────┬───────────────────┬────────┘
                                       │                   │                   │
        ┌──────────────────────────────┼───────────────────┼───────────────────┼──────────────────────────────┐
        │                              │                   │                   │                              │
┌───────▼────────────────┐   ┌─────────▼─────────┐   ┌─────▼─────────────┐   ┌─▼──────────────────┐   ┌───────▼────────────────┐
│ Google OAuth 2.0 /     │   │ YouTube IFrame    │   │ Trailer Discovery │   │ Cinema Discovery & │   │ Ticket Booking         │
│ OpenID Connect Service │   │ Verification &    │   │ Freshness Engine  │   │ Location Services  │   │ Redirect Service       │
│ (Identity & Profiling) │   │ Quota Management  │   │ (48h/7d/30d/rel)  │   │ (Haversine Metro)  │   │ (BookMyShow, Cinepolis)│
└────────────────────────┘   └───────────────────┘   └───────────────────┘   └────────────────────┘   └────────────────────────┘
        │                              │                   │                   │                              │
        └──────────────────────────────┼───────────────────┼───────────────────┼──────────────────────────────┘
                                       │
                           ┌───────────▼────────────────────────────┐
                           │      In-Memory Python Data Store       │
                           │ Users, Movies, Trailers, Cinemas, Logs │
                           └────────────────────────────────────────┘
```

---

## 🚀 Key Features

### 1. Unified Entertainment Experience (Strict UI/UX Compliance)
- **Zero Separate Bollywood/Hollywood Tabs:** All Bollywood, Hollywood, South Indian, and international cinema live together in one unified entertainment catalogue.
- **Dynamic Faceted Filtering:** Language (Hindi, English, Telugu, Tamil, Malayalam) and Industry (Bollywood, Hollywood, Regional) are structured as query/dropdown filters and badges (`/movies/free?industry=...&language=...`), never as separate navigation tabs.
- **Top Navigation Rails:** Unified links: **Home**, **Must Watch** (with flame badge), **Free Movies**, **Movie Trailers** (`/trailers`), **Cinema Tickets** (`/cinemas`), **Rent & Buy** (`/movies/premium`), **Actors** (`/actors`), **Watchlist** (`/account/watchlist`), and **Admin** (`/admin`).

### 2. Dedicated "Must Watch" Bollywood Blockbusters Tab (`/must-watch`)
- **Curated Legal Free Bollywood Blockbusters:** Showcases India's all-time greatest Hindi cinema blockbusters (*Chak De! India*, *Dilwale Dulhania Le Jayenge*, *Sholay*, *Hera Pheri*, *Andaz Apna Apna*, *Hum Saath Saath Hain*, *Vivah*, *Deewaar*, *Don*, *Chupke Chupke*, *Welcome*, *Golmaal*).
- **Dual Playback Actions:**
  - **"Watch Movie":** Seamless in-app streaming with full monetization and controls.
  - **"Watch in New Tab":** Direct link (`target="_blank"`) to the verified official studio YouTube channel.
- **Genre Pill Filters with Live Counts:** Real-time filtering across Action, Comedy, Romance, Drama, Crime, Family with active counter badges.
- **In-Page Keyword Search:** Instant search filter across movie titles, descriptions, and actor names.

### 3. Free Movie Streaming — Verified Legal YouTube Integration
- **Official YouTube IFrame Player API:** 100% compliant player with zero overlay obstruction, embedded with `strict-origin-when-cross-origin` referrer policy, `origin` validation, and `enablejsapi=1`.
- **Zero "Playback ID" Error (150/153):** Handled through verified embeddable video IDs catalogued directly from authorized studio channels (Yash Raj Films, Rajshri, Shemaroo, Ultra Movie Parlour, Universal Pictures, Warner Bros.).
- **Automatic Fallback CDN Player:** One-click backup switch to authorized Content Delivery Network (CDN) MP4 video stream if client network blocks third-party YouTube embeds.
- **Resilient Original Thumbnails:** Direct official studio thumbnails (`img.youtube.com/vi/{id}/maxresdefault.jpg`) with automatic fallback to `hqdefault.jpg`.

### 4. Movie Trailer Discovery Hub (`/trailers`)
- **Unified Trailer Discovery:** Comprehensive trailer catalogue for Bollywood, Hollywood, and regional blockbusters (*Kalki 2898 AD*, *Singham Again*, *Deadpool & Wolverine*, *Gladiator II*, *Stree 2*, *Dune: Part Two*, *Bhool Bhulaiyaa 3*, *Pushpa 2*, *Mission Impossible*, etc.).
- **Freshness Window Filters:**
  - *All Releases*
  - *🔥 Latest (48 Hours)*
  - *Last 7 Days*
  - *Last 30 Days*
  - *🎟️ Upcoming Cinema Releases*
- **Rich Metadata & Actions:** Theatrical release dates, duration stamps, official studio channel names, and direct links to book cinema tickets or watch on YouTube.

### 5. Theatrical Releases & Nearby Cinema Booking (`/cinemas`)
- **Location Permission Protocol:** Transparent 3-option modal (*Use GPS Proximity* | *Manual City Dropdown* | *Dismiss*). Video streaming is never blocked if location permission is denied.
- **Indian Metro City Support:** Mumbai, Delhi-NCR, Bengaluru, Hyderabad, Pune, Chennai, Kolkata, Ahmedabad.
- **Python Haversine Geolocation Engine:** Accurate real-world spherical distance calculation in kilometers between user coordinates and nearby multiplexes:
  $$\Delta\sigma = 2 \arcsin \sqrt{\sin^2\left(\frac{\Delta\phi}{2}\right) + \cos(\phi_1)\cos(\phi_2)\sin^2\left(\frac{\Delta\lambda}{2}\right)}$$
- **Multiplex Venue Details:** Venue names, addresses, screen counts, and audio/visual formats (IMAX 4K Laser, 4DX, Dolby Atmos, Recliners, In-seat dining).
- **Verified Showtime Grid:** Morning, matinee, evening, and night showtimes with pricing in INR and dynamic availability badges (*Available*, *Filling Fast*, *Almost Full*).
- **Authorized Ticketing Redirection:**
  - Direct deep-links to **BookMyShow** (`in.bookmyshow.com/explore/movies-{city}`) and **Cinepolis India** (`cinepolisindia.com`).
  - Prominent **Statutory Partner Disclosures** informing users that transactions and tickets are processed through authorized external ticketing partners.

### 6. Actor & Actress Discovery with Photo Licensing Attribution (`/actors`)
- **Wikimedia Commons Compliance:** Every actor profile features complete copyright attribution records (`Photo Attribution: Wikimedia Commons CC BY-SA / CC BY`).
- **Comprehensive Profiles (`/actors/<slug>`):** High-resolution portraits, detailed biographies, date of birth, place of birth, global follower counts, notable honors, filmographies on CinePulse, and **Upcoming Projects**.

### 7. Main Streaming Page & Monetization Layout (`/watch/<id>`)
- **Prominent 16:9 Video Canvas:** Responsive aspect ratio, zero distortion, with accessible playback controls.
- **Three Distinct Viewing Modes:**
  - **Normal Mode:** 2-column layout with 8-column main video canvas and 4-column right-side monetization sidebar on desktop. Below-player ad slots and metadata are visible.
  - **Theatre Mode:** Expands player to 100% container width (12 columns) for maximum immersion; right sidebar smoothly reflows below the player without breaking layout.
  - **Fullscreen Mode:** Invokes native player canvas fullscreen (`requestFullscreen`). **All external website advertisements, display banners, headers, and sidebars are automatically hidden.** Layout is seamlessly restored upon exit (`fullscreenchange` event).
- **Below-Player Advertising Space:**
  - Configurable Google AdSense horizontal display unit (`ca-pub-7928340192837461`).
  - Sponsored movie recommendation banner.
  - Affiliate entertainment gear carousel (Sony ANC Headphones, Sennheiser Soundbars, Samsung 65" OLED).
- **Desktop Right-Side Monetization Sidebar:**
  - VIP ad-free upgrade banner.
  - Responsive Google AdSense 300x250 slot.
  - Sponsored & featured movie cards.
  - Similar & related movie recommendations.
- **Below-Player Content:** Complete synopsis, director and genres, cast & crew cards with photos, user star ratings, and review submission form.

### 8. Comprehensive Multi-Channel Revenue System
1. **Google AdSense:** Configurable Publisher Account ID and slot IDs for below-player and sidebar responsive display units.
2. **Direct Brand Sponsorship Campaigns:** Contracted promotional banners with verified branding.
3. **Affiliate Marketing:** High-ticket home theatre audio/visual gear with statutory partner disclosure.
4. **VIP Membership Subscriptions:** Ad-Free UI Experience for active VIP subscribers (`₹199/month`).
5. **Digital Movie Rentals:** Pay-per-view rentals from `₹49` to `₹149` with 48-hour viewing window.
6. **Digital Movie Purchases:** Perpetual 4K UHD digital ownership from `₹199` to `₹499`.

### 9. User Authentication — Google Sign-In & Privacy (`/account/profile`)
- **Google Identity Services:** OAuth 2.0 / OpenID Connect profile integration with avatar, display name, and verified email sync.
- **Taste Profile & Preferences:** Multi-select favorite genres, favorite actors, and personalized recommendation weighting.
- **Personalized Continue Watching Rail:** Tracks playback progress percentage and duration across sessions.
- **GDPR & DPDP Privacy Compliance:** 1-click **Delete Account & Erase Data** action providing complete right to erasure under India's Digital Personal Data Protection Act 2023 and GDPR.

### 10. Executive Admin Dashboard (`/admin`)
- **Multi-Channel Financial Overview:** Real-time revenue aggregation across Gross, AdSense Display, Affiliate Commissions, Digital Rentals, UHD Purchases, and VIP Subscriptions.
- **YouTube Data API v3 Daily Quota Meter:** Visual progress gauge tracking consumption against the 10,000 daily quota limit (9,912 units remaining).
- **Live YouTube Video Verification Tool:** Interactive AJAX tool allowing administrators to verify any catalogue movie ID against YouTube embed restrictions with real-time status output.
- **Configured Ad Slots Manager:** Table listing active ad slots with status indicators.
- **Active Video Catalogue Status Table:** Comprehensive listing of catalogue titles with direct link to test playback.

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| **Language & Runtime** | Python 3.12 (64-bit) |
| **Web Framework** | Flask 3.1.3 (WSGI) |
| **Templating Engine** | Jinja2 3.1.6 with template inheritance |
| **Styling & Design System** | Tailwind CSS (CDN), Custom CSS Glassmorphism, FontAwesome 6, Google Fonts Inter & Montserrat |
| **Data Store** | In-Memory Python Data Store (`data/store.py`) with thread-safe persistence |
| **Authentication** | Google Identity Services (OAuth 2.0 / OpenID Connect simulation) + Secure Session Management |
| **Video Playback** | YouTube IFrame Player API v3 (Free/Verified) + HTML5 Video Fallback |
| **Geolocation** | HTML5 Browser Geolocation API + Python Haversine Formula (`math` library) |
| **Monetization** | Google AdSense Responsive Units, Amazon Associates Affiliate Gear, VIP Subscriptions |

---

## 📂 Project Structure

```
C:\Games\CinePulse.Python\
├── app.py                      # Main Flask application with all routes, security headers & APIs
├── requirements.txt            # Python dependencies (flask>=3.0.0)
├── run.bat                     # 1-click Windows batch launcher
├── README.md                   # Complete architectural documentation
├── data\
│   └── store.py                # Thread-safe data store: 45 movies, 14 trailers, 10 superstars, Haversine GPS
├── static\
│   ├── css\
│   │   └── app.css             # OTT dark cinematic theme, glassmorphic nav, theatre mode, ad slots
│   └── js\
│       ├── player.js           # Video player controller, theatre/fullscreen, fallback switch, watchlist AJAX
│       └── cinemas.js          # HTML5 Geolocation protocol & Haversine distance calculator
└── templates\
    ├── base.html               # Responsive glassmorphic layout with disclaimers & footer
    ├── _movie_card.html        # Reusable card with original movie posters & "New Tab" link
    ├── index.html              # Cinematic Hero, Must Watch, Trending, Free, Premium rails
    ├── must_watch.html         # Curated free Bollywood blockbusters with "Watch in New Tab"
    ├── free.html               # Unified catalogue with Industry & Language query filters
    ├── premium.html            # 4K UHD rentals & purchases
    ├── watch.html              # Monetization streaming page (Normal/Theatre/Fullscreen)
    ├── trailers.html           # Freshness windows (48h, 7d, 30d, upcoming)
    ├── cinemas.html            # Multiplexes, Haversine GPS distance, BookMyShow deep links
    ├── actors.html             # Superstar directory
    ├── actor_details.html      # Filmography, biography, Wikimedia attribution
    ├── profile.html            # Google login, user preferences, GDPR deletion
    ├── watchlist.html          # Saved user movies
    ├── admin.html              # Revenue channels, YouTube quota meter, video verifier
    ├── search.html             # Cross-catalogue instant search
    ├── privacy.html            # DPDP & GDPR privacy compliance
    └── terms.html              # Statutory aggregator & YouTube TOS compliance terms
```

---

## ⚡ Quick Start & Running the Platform

### Prerequisites
- **Python 3.12** installed (located at `%LOCALAPPDATA%\Programs\Python\Python312\python.exe` or available in system PATH).

### 1. Install Dependencies
```powershell
cd C:\Games\CinePulse.Python
python -m pip install -r requirements.txt
```

### 2. Launch the Application (Option A — 1-Click Batch)
Double-click [`run.bat`](file:///C:/Games/CinePulse.Python/run.bat) located in `C:\Games\CinePulse.Python\`.

### 3. Launch the Application (Option B — PowerShell / Command Prompt)
```powershell
cd C:\Games\CinePulse.Python
python app.py
```
Open **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your web browser!

---

## 🔑 Pre-Configured Test Credentials

For frictionless review, the default authenticated session is pre-seeded with full viewer and admin capabilities:

| Role | Name | Email | Capabilities |
|---|---|---|---|
| **Viewer** | Priya Sharma | `priya.sharma@gmail.com` | Authenticated via Google OAuth 2.0, active Watchlist, Continue Watching history, favorite genres and actors |
| **Admin** | Administrator | `admin@cinepulse.io` | Full platform control, Monetization Dashboard, AdSense Config, YouTube Quota Meter, Live Video Embed Verifier |

---

## 🔒 Security, Legal & Licensing Compliance

1. **YouTube Compliance:**
   - Free movies and trailers are streamed exclusively via the official YouTube IFrame Player API.
   - All movies are verified to originate from official rights-holder and studio channels.
   - Creator branding and studio channels remain intact; content is never re-hosted or pirated.
2. **Ad Viewing Integrity:**
   - Advertisements are never placed over essential player controls.
   - In Fullscreen mode, all surrounding website ads and banners are completely hidden.
   - Active VIP subscribers receive an automated 100% ad-free experience on all platform-controlled ad slots.
3. **Ticketing Partner Transparency:**
   - Cinema showtime redirects lead directly to authorized ticketing platforms **BookMyShow** and **Cinepolis India** with prominent statutory disclaimers.
4. **GDPR & DPDP Compliance:**
   - Full data privacy controls, transparent location permissions, and complete 1-click account and data deletion.
