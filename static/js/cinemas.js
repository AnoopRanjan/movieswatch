// CinePulse Location Protocol & GPS Multiplex Proximity Engine

(function () {
    window.CinemaLocator = {
        requestLocation: function () {
            var statusDiv = document.getElementById('location-status-message');
            if (!navigator.geolocation) {
                if (statusDiv) {
                    statusDiv.innerText = 'Geolocation is not supported by your browser. Please select your city manually.';
                    statusDiv.className = 'text-xs text-amber-400 mt-2';
                }
                return;
            }

            if (statusDiv) {
                statusDiv.innerText = 'Detecting your GPS coordinates via HTML5 Geolocation API...';
                statusDiv.className = 'text-xs text-sky-400 mt-2 animate-pulse';
            }

            navigator.geolocation.getCurrentPosition(
                function (position) {
                    var lat = position.coords.latitude;
                    var lng = position.coords.longitude;
                    sessionStorage.setItem('cinepulse_user_lat', lat);
                    sessionStorage.setItem('cinepulse_user_lng', lng);

                    var currentUrl = new URL(window.location.href);
                    currentUrl.searchParams.set('lat', lat);
                    currentUrl.searchParams.set('lng', lng);
                    window.location.href = currentUrl.toString();
                },
                function (error) {
                    if (statusDiv) {
                        statusDiv.innerText = 'Location permission denied or unavailable. You can browse multiplexes by city.';
                        statusDiv.className = 'text-xs text-rose-400 mt-2';
                    }
                },
                { enableHighAccuracy: true, timeout: 10000, maximumAge: 60000 }
            );
        },

        dismissLocationModal: function () {
            var modal = document.getElementById('location-permission-modal');
            if (modal) modal.style.display = 'none';
        }
    };
})();
