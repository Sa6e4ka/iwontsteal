$(document).ready(function() {
    $.post('/get_ip_info', function(data) {
        $('#ip').text(`IP: ${data.ip}`);
        $('#location').text(`Location: ${data.city}, ${data.state_prov}, ${data.country_name}`);

        const map = L.map('map').setView([data.latitude, data.longitude], 10);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        const marker = L.marker([data.latitude, data.longitude]).addTo(map);
        marker.bindPopup(`<b>${data.city}, ${data.state_prov}, ${data.country_name}</b>`).openPopup();
    });
});
