const API_KEY = 'YOUR_YOUTUBE_API_KEY'; // YouTube API anahtarını buraya ekle

const fetchVideos = async (query, elementId) => {
    const url = `https://www.googleapis.com/youtube/v3/search?part=snippet&q=${query}&type=video&key=${API_KEY}&maxResults=5`;
    const response = await fetch(url);
    const data = await response.json();
    displayVideos(data.items, elementId);
};

const displayVideos = (videos, elementId) => {
    const container = document.getElementById(elementId);
    container.innerHTML = ''; // önceki içerikleri temizle
    videos.forEach(video => {
        const videoElement = document.createElement('div');
        videoElement.classList.add('video');
        videoElement.innerHTML = `
            <img src="${video.snippet.thumbnails.medium.url}" alt="${video.snippet.title}">
            <h3>${video.snippet.title}</h3>
            <a href="https://www.youtube.com/watch?v=${video.id.videoId}" target="_blank">İzle</a>
        `;
        container.appendChild(videoElement);
    });
};

// Matematik ve Türkçe videolarını çekmek için çağrılar yap
fetchVideos('ortaokul matematik dersi', 'matematik-videolar');
fetchVideos('ortaokul türkçe dersi', 'turkce-videolar');
