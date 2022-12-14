import queue                            #реализация очереди с разделенными функциями, которые позволяет находящимся в очереди объектам быть
                                        # обработанными параллельно несколькими одновременно работающими процессами
import sounddevice as sd
import vosk        # https://alphacephei.com/vosk/
import json        # стандарт обмена данными. Он позволяет легко сериализовать и десериализовать объекты.

from sklearn.feature_extraction.text import CountVectorizer  #https://scikit-learn.org/stable/
from sklearn.linear_model import LogisticRegression   #используемый для прогнозирования вероятности категориальной зависимой переменной
from skills import *     ##### ПРОРАБОТАТЬ, НЕ ИМОРТИТ ДАННЫЕ ИЗ ФАЙЛА
import voiceBot
import phrases





q = queue.Queue()
model = vosk.Model(r"D:\pythonProject\model_small\vosk-model-small-ru-0.22")

device = sd.default.device          # sd.default.device == 1, 3  /input, output [1, 3]               python -m sounddevice просмотр
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate']) #тут находим нашу частоту микро к примеру 16000




def callback(indata, frames, time, status):
    # Добавляет в очередь семплы из потока. вызывается каждый раз при наполнении blocksize в sd.RawInputStream
    q.put(bytes(indata)) #https://docs-python.ru/standart-library/modul-queue-python/obekty-ocheredi-modulja-queue/#Queue.put




def recognize(data, vectorizer, clf):
    trg = phrases.TRIGGERS.intersection(data.split()) #делает проверку, если тригерных слов нету то ретерн возращает проверку в начало
    if not trg:
        return
    data.replace(list(trg)[0], '')# удаляем имя бота из текста
    text_vector = vectorizer.transform([data]).toarray()[0]# получаем вектор полученного текста
    answer = clf.predict([text_vector])[0]# сравниваем с вариантами, получая наиболее подходящий ответ


    func_name = answer.split()[0]#получение имени функции из ответа из data_set
    voiceBot.speaker(answer.replace(func_name, ''))#озвучка ответа из модели data_set + удаление опозновающ. слова
    exec(func_name + '()')#запуск функции из skills




def main(): #Обучение матрицы на data_set модели
    vectorizer = CountVectorizer()  # преобразовывает входной текст в матрицу
    vectors = vectorizer.fit_transform(list(phrases.data_set.keys())) #получаем ключи списка, метод хэширует фразы и строит по ним векторы, какой либо масив из матрицы цифр.
                                                                    # Похожие фразы, которые и будут содерж похожие слова , то их векторы будут совпадать
                                                                    # => машина будет распозновать слова в любых похожих предложениях

    clf = LogisticRegression()
    clf.fit(vectors, list(phrases.data_set.values())) # берем ответы, а не ключи уже. После идет некая проверка, в которой опред, совпадение ключа и ответа и после выводится ответ :)
    del phrases.data_set

    # постоянная прослушка микрофона
    with sd.RawInputStream(samplerate=samplerate, blocksize=2000, device=device[0], dtype='int16', channels=1, callback=callback): # device[0] == micro  # sd.RawInputStream записывает данные c нашего микро
                                                                                        #callback как он накопит 2000 сиплов, то он их начнет записывать в нашу уже опред очередь (q)

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True: #слушаем голос без перерыва
            data = q.get()
            if rec.AcceptWaveform(data):    # если остановится голос, начнется расшифровка вводимых данных
                data = json.loads(rec.Result())['text']
                recognize(data, vectorizer, clf)
            else:
                print(rec.PartialResult())

if __name__ == '__main__':
    main()  # запускаем код функции

