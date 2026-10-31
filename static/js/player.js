// CinePulse Video Player Controller & Multi-Source Monetization Engine

(function () {
    window.CinePulsePlayer = {
        isTheatre: false,
        isFullscreen: false,
        currentSource: 'youtube',
        ytPlayer: null,

        init: function (videoId, fallbackStreamUrl) {
            this.videoId = videoId;
            this.fallbackStreamUrl = fallbackStreamUrl;
            this.setupListeners();
            this.setupYouTubeMessageListener();
        },

        toggleTheatre: function () {
            var body = document.body;
            var btn = document.getElementById('btn-theatre');
            this.isTheatre = !this.isTheatre;

            if (this.isTheatre) {
                body.classList.add('theatre-mode');
                if (btn) btn.innerHTML = '<i class="fa-solid fa-compress text-[11px]"></i> Normal View';
            } else {
                body.classList.remove('theatre-mode');
                if (btn) btn.innerHTML = '<i class="fa-solid fa-expand text-[11px]"></i> Theatre Mode';
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
            this.currentSource = sourceType;
            var iframe = document.getElementById('main-video-player');
            var videoElem = document.getElementById('html5-fallback-player');
            var overlay = document.getElementById('player-error-overlay');
            var banner = document.getElementById('source-status-banner');
            var tabYt = document.getElementById('tab-source-yt');
            var tabCdn = document.getElementById('tab-source-cdn');

            // Hide error overlay whenever user switches sources
            if (overlay) overlay.style.display = 'none';

            if (sourceType === 'fallback') {
                if (iframe) iframe.style.display = 'none';
                if (videoElem) {
                    videoElem.style.display = 'block';
                    videoElem.play().catch(function(e) { console.log('Autoplay deferred:', e); });
                }
                if (tabYt) {
                    tabYt.className = 'px-3 py-1.5 rounded-lg text-xs font-medium transition-all bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white border border-slate-700 flex items-center gap-1.5';
                }
                if (tabCdn) {
                    tabCdn.className = 'px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-amber-500 text-slate-950 flex items-center gap-1.5 shadow';
                }
                if (banner) {
                    banner.innerHTML = '<div class="flex items-center gap-2"><span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span><span>Now streaming via <strong>High-Speed Authorized CDN Backup</strong> (Full HD).</span></div><button onclick="CinePulsePlayer.switchSource(\'youtube\')" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded text-[11px] font-semibold">Switch back to YouTube</button>';
                }
            } else {
                if (videoElem) {
                    videoElem.pause();
                    videoElem.style.display = 'none';
                }
                if (iframe) {
                    iframe.style.display = 'block';
                }
                if (tabYt) {
                    tabYt.className = 'px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-red-600 text-white flex items-center gap-1.5 shadow';
                }
                if (tabCdn) {
                    tabCdn.className = 'px-3 py-1.5 rounded-lg text-xs font-medium transition-all bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white border border-slate-700 flex items-center gap-1.5';
                }
                if (banner) {
                    banner.innerHTML = '<div class="flex items-center gap-2"><span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span><span>Streaming official studio release via YouTube Player.</span></div><div class="flex items-center gap-2"><button onclick="CinePulsePlayer.switchSource(\'fallback\')" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white border border-slate-700 rounded text-[11px] font-medium"><i class="fa-solid fa-tower-broadcast text-amber-400 mr-1"></i>Backup Stream</button></div>';
                }
            }
        },

        showErrorOverlay: function (reason) {
            var overlay = document.getElementById('player-error-overlay');
            if (overlay) {
                overlay.style.display = 'flex';
            }
        },

        hideErrorOverlay: function () {
            var overlay = document.getElementById('player-error-overlay');
            if (overlay) {
                overlay.style.display = 'none';
            }
        },

        setupYouTubeMessageListener: function () {
            var self = this;
            window.addEventListener('message', function (event) {
                // Listen to YouTube postMessage events
                try {
                    var data = typeof event.data === 'string' ? JSON.parse(event.data) : event.data;
                    if (data && data.event === 'onError') {
                        console.warn('YouTube Player reported error:', data.info);
                        self.showErrorOverlay(data.info);
                    }
                } catch (e) {
                    // Ignore non-JSON postMessages
                }
            });
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

    // Auto-initialize when DOM is ready
    document.addEventListener('DOMContentLoaded', function () {
        if (window.CinePulsePlayer) {
            window.CinePulsePlayer.setupListeners();
            window.CinePulsePlayer.setupYouTubeMessageListener();
        }
    });

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
                        btnElem.classList.remove('text-slate-300');
                        btnElem.innerHTML = '<i class="fa-solid fa-bookmark"></i> In Watchlist';
                    } else {
                        btnElem.classList.remove('text-red-500');
                        btnElem.classList.add('text-slate-300');
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