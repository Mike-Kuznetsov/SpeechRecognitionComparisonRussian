# SpeechRecognitionComparisonRussian
UPD: At the time i did this comparison there were no OpenAI Whisper. Now i use it. And for recognizing voice commands for my smart home i use Orange Pi with Vosk.  
Когда я проводил тестирование, OpenAI Whisper еще не существовал, теперь я пользуюсь им, а команды для умного дома распознает Orange Pi с Vosk.

I tested the most popular russian speech recognizers.
Я протестировал наиболее популярные сервисы и библиотеки распознавания русской речи
Video with results: https://www.youtube.com/watch?v=5aXNzigJ0c4
YouTube: https://www.youtube.com/c/MautozTech   
YouTube channel about programming: https://www.youtube.com/@ESPdev

### Links:

Vosk API:  
https://alphacephei.com/vosk/  
https://github.com/alphacep/vosk-api  
https://alphacephei.com/ru/

Google Speech Recognition:  
My GoogleContinuousRecognition App: https://github.com/Mike-Kuznetsov/GoogleContinuousRecognition  
Android: https://developer.android.com/reference/android/speech/SpeechRecognizer  
Google Cloud Speech-to-Text: https://cloud.google.com/speech-to-text  
Python: https://pypi.org/project/SpeechRecognition/  

Yandex SpeechKit: https://cloud.yandex.ru/services/speechkit

WebSpeech API:  
My AndroidWebSpeech App: https://github.com/Mike-Kuznetsov/AndroidWebSpeech  
Usage example: https://codepen.io/harryheman/pen/VwppNgp  
Docs: https://developer.mozilla.org/ru/docs/Web/API/Web_Speech_API  

Mail.ru (VK) Cloud Voice: https://mcs.mail.ru/cloud-voice/

Amazon Transcribe: https://aws.amazon.com/ru/transcribe/

Wav2vec:  
Russian: https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-russian  
wav2vec tutorial: https://www.youtube.com/watch?v=Ivz-E2eBUZM  
Github: https://github.com/pytorch/fairseq/tree/main/examples/wav2vec

Red - Not tested;
Yellow - Tested on phone;
White - Tested on PC;  
Columns in english: Service or toolkit name / Price for an hour / Offline mode / Quality of recognition with 3 different volume levels
![alt text](https://github.com/Mike-Kuznetsov/SpeechRecognitionComparisonRussian/blob/main/spreadsheet.png?raw=true)

I tested some services after i made this comparison, here're the results:   
Sber Smartspeech - 0 0 0  
Tinkoff Voicekit - 0 3.5 4.5  
NLab Speech ASR - 0 3 4   
Silero - NT NT 3  
