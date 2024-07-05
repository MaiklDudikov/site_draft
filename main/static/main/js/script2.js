navigator.mediaDevices.getUserMedia({ audio: true, video: true })
    .then(function (stream) {
        console.log("Получен поток с камеры и микрофона.");

        // Сохраняем поток в глобальной переменной для дальнейшего использования
        window.localStream = stream;

        // Открываем страницу видео
        var videoPage = window.open("/video", "_blank");

        if (!videoPage) {
            console.error("Не удалось открыть новую вкладку.");
        }
    })
    .catch(function (error) {
        alert("Произошла следующая ошибка: " + error.name);
        console.error("Ошибка при получении потока:", error);
    });
