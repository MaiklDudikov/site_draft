window.addEventListener('load', function () {
    var videoElement = document.getElementById('remoteVideo');

    // Проверяем, что поток сохранен в локальном хранилище
    if (window.opener && window.opener.localStream) {
        // Устанавливаем источник видео потока
        videoElement.srcObject = window.opener.localStream;
        videoElement.play();
    } else {
        console.error("Нет доступа к локальному потоку.");
    }
});
