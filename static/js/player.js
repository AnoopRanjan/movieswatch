// CinePulse Video Player Controller & Monetization Engine

(function () {
    window.CinePulsePlayer = {
        isTheatre: false,
        isFullscreen: false,

        init: function (videoId, fallbackStreamUrl) {
            this.videoId = videoId;
            this.fallbackStreamUrl = fallbackStreamUrl;
            this.setupListeners();
        },

        toggleTheatre: function () {
            var body = document.body;
            var btn = document.getElementById('btn-theatre');
            this.isTheatre = !this.isTheatre;

            if (this.isTheatre) {
                body.classList.add('theatre-mode');
                if (btn) btn.innerHTML = '<i class="fa-solid fa-compress mr-1"></i> Normal View';
            } else {
                body.classList.remove('theatre-mode');
                if (btn) btn.innerHTML = '<i class="fa-solid fa-expand mr-1"></i> Theatre Mode';
            }
        },

        toggleFullscreen: function () {
            var container = document.getElementById('player-wrapper');
            if (!container) return;

            if (!document.fullscreenElement && !document.webkitFullscreenElement) {
                if (container.requestFullscreen) {
                    container.requestFullscreen();
                } else if (container.webkitRequestFullscreen) {
                    container.webkitRequestFullscreen();
                }
                container.classList.add('is-fullscreen');
            } else {
                if (document.exitFullscreen) {
                    document.exitFullscreen();
                } else if (document.webkitExitFullscreen) {
                    document.webkitExitFullscreen();
                }
                container.classList.remove('is-fullscreen');
            }
        },

        switchSource: function (sourceType) {
            var iframe = document.getElementById('main-video-player');
            var videoElem = document.getElementById('html5-fallback-player');
            var banner = document.getElementById('source-status-banner');

            if (sourceType === 'fallback') {
                if (iframe) iframe.style.display = 'none';
                if (videoElem) {
                    videoElem.style.display = 'block';
                    videoElem.play();
                }
                if (banner) {
                    banner.innerHTML = '<i class="fa-solid fa-satellite-dish mr-2 text-emerald-400"></i> Switched to Authorized Content Delivery Network (CDN) backup stream.';
                    banner.className = 'p-3 bg-emerald-950/60 border border-emerald-500/40 rounded-lg text-xs text-emerald-200 mt-3';
                }
            } else {
                if (videoElem) {
                    videoElem.pause();
                    videoElem.style.display = 'none';
                }
                if (iframe) iframe.style.display = 'block';
                if (banner) {
                    banner.innerHTML = '<i class="fa-brands fa-youtube mr-2 text-red-500"></i> Streaming via Official Studio YouTube Channel with strict origin validation.';
                    banner.className = 'p-3 bg-slate-900/80 border border-slate-700/60 rounded-lg text-xs text-slate-300 mt-3';
                }
            }
        },

        setupListeners: function () {
            var self = this;
            document.addEventListener('fullscreenchange', function () {
                var container = document.getElementById('player-wrapper');
                if (!document.fullscreenElement && container) {
                    container.classList.remove('is-fullscreen');
                }
            });
        }
    };

    // Global Watchlist AJAX Toggle
    window.toggleWatchlist = function (movieId, btnElem) {
        fetch('/api/watchlist/toggle', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ movie_id: movieId })
        })
        .then(function (response) { return response.json(); })
        .then(function (data) {
            if (data.success) {
                if (btnElem) {
                    if (data.in_watchlist) {
                        btnElem.classList.add('text-red-500');
                        btnElem.classList.remove('text-slate-400');
                        btnElem.innerHTML = '<i class="fa-solid fa-bookmark"></i> In Watchlist';
                    } else {
                        btnElem.classList.remove('text-red-500');
                        btnElem.classList.add('text-slate-400');
                        btnElem.innerHTML = '<i class="fa-regular fa-bookmark"></i> Add to Watchlist';
                    }
                }
            }
        })
        .catch(function (err) {
            console.error('Watchlist toggle error:', err);
        });
    };
})();
