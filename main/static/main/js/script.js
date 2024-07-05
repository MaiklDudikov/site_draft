navigator.getUserMedia(
    { audio: true, video: true },
    function (stream) {
      console.log("Получен поток с камеры и микрофона.");

      // Создаем элемент video
      var video = document.createElement('video');

      // Устанавливаем источник для элемента video как полученный поток
      video.srcObject = stream;

      // Добавляем обработчик для события onloadedmetadata
      video.onloadedmetadata = function (e) {
        console.log("Метаданные загружены. Воспроизведение начинается.");
        video.play(); // Начинаем воспроизведение видео
      };

      // Добавляем обработчики для различных событий
      video.onplaying = function () {
        console.log("Видео воспроизводится.");
      };

      video.onpause = function () {
        console.log("Видео на паузе.");
      };

      video.onerror = function (e) {
        console.error("Произошла ошибка при воспроизведении видео:", e);
      };

      // Добавляем элемент video в тело документа
      document.body.appendChild(video);
      console.log("Видео добавлено на страницу.");
    },
    function (error) {
      alert("Произошла следующая ошибка: " + error.name);
      console.error("Ошибка при получении потока:", error);
    }
  );
