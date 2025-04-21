# Цифриум. Машинисты 
## MIPT Hackaton Cifrium 2025-04
### Задача 1. "Конспект видео лекций"

2025-03-30 Реализовать сервис для подготовки преподавателем конспекта лекции на основе видео длительностью от 3 до 60 минут.  
Сервис может быть реализован как в Jupyter Notebook, так и в виде веб-сайта или API к сервису.

### Ссылки

* Песочница  [💎⏳ Хакатон ЦК МФТИ. Цифриум. Машинисты](https://docs.google.com/document/d/1Iiq1pSYpAoJTyzz4hFYPD75WkthUZyB7Xq8ktMs_BrQ/edit?tab=t.0#heading=h.twwayrjm6xcy )
* Хакатон.ЦК.2025.drawio [Схема проекта](https://drive.google.com/file/d/1ZNFj6rUf3b-7xbHWv_muyv_2-ZXZ41op/view?usp=drive_link)
* Git [cifrium](https://github.com/NutriLabAdm/cifrium)
* Презентация 

### Файлы

* transcript.txt - 🎦 файл транскрибации видео 
* utils_log.py - утилиты 
* 01.videos_cut.ipynb - сегментация видео для транскрибации
* 02.videos_trans.ipynb - транскрибации видео
* 03.local_proccesing.ipynb - подкготовка конспекта с использорванием LLM
* 03.api_proccesing.ipynb - конспекта с он-лайн LLM при наличии API_KEY
* 04.exports.ipynb - экспорт конспекта в форматированный файл
* 05.ocr.ipynb - извлечение текста из кадров 

### Результаты обработки 

* 📃 results/transcripts/
* 📄 results/conspects/
* 📁 results/docs/
* 📜 results/prompts/
* 📷 results/keyframes/
* 📊 results/pptx/


# материалы проекта 
* 📊 materials/pptx/  презентации
* 🖼 materials/images/  изображения




### Logs

Логи обработки в гугл таблицах [tm_loging](https://docs.google.com/spreadsheets/d/1QCLSait8lExQHwXDkBcPZZ9PYBNtWdorq-vF5hh944E/edit?gid=164268903#gid=164268903 )

### Modules

```
pip install ipynbname
pip install gspread
pip install oauth2client
```

```import cv2
import numpy as np
import whisper
```

```
from docx import Document
from docx.shared import Inches
from PIL import Image
import subprocess
import glob
```

```
from PIL import Image
import pytesseract
```