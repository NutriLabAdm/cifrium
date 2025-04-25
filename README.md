# Цифриум. Машинисты 
## MIPT Hackaton Cifrium 2025-04
### Задача 1. "Конспект видео лекций"

2025-03-30 Реализовать сервис для подготовки преподавателем конспекта лекции на основе видео длительностью от 3 до 60 минут.  
Сервис может быть реализован как в Jupyter Notebook, так и в виде веб-сайта или API к сервису.

### Ссылки

* Песочница  [💎⏳ Хакатон ЦК МФТИ. Цифриум. Машинисты](https://docs.google.com/document/d/1Iiq1pSYpAoJTyzz4hFYPD75WkthUZyB7Xq8ktMs_BrQ/edit?tab=t.0#heading=h.twwayrjm6xcy )
* Хакатон.ЦК.2025.drawio [Схема проекта](https://drive.google.com/file/d/1ZNFj6rUf3b-7xbHWv_muyv_2-ZXZ41op/view?usp=drive_link)
* Git [cifrium](https://github.com/NutriLabAdm/cifrium)
* Презентация [МАШИНИСТЫ_Цифриум_образование_вер_6_только_пять_слайдов](https://docs.google.com/presentation/d/1lWOFmtI0cURbFLQREEk86ctSzwNr7OAm/edit?slide=id.g35016723367_1_10#slide=id.g35016723367_1_10)

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
<pre> ```
Структура файлов в репозитории:
├── 01.videos_cut.ipynb
├── 02.jpg
├── 02.videos_trans.ipynb
├── 03.api_proccesing.ipynb
├── 03.local_proccesing.ipynb
├── 04.exports.ipynb
├── 05.ocr.ipynb
├── README.md
├── conspects
│   ├── conspect_API_claude-3-7-sonnet-20250219.md.pptx
│   ├── conspect_API_claude-3-7-sonnet-20250219.txt
│   ├── conspect_gpt-3.5-turbo.txt
│   ├── conspect_gpt-4.txt
│   ├── conspectmodel_claude-3.7-sonnet-reasoning-gemma3-12B.Q8_0.gguf.txt
│   ├── conspectmodel_meta-llama-3-8b-instruct.Q4_K_M.gguf.txt
│   └── conspectmodel_mistral-7b-instruct-v0.1.Q8_0.gguf.txt
├── materials
│   ├── images
│   │   ├── cifrium_conspect_preview.png
│   │   └── cifrium_project_flow.png
│   └── pptx
│       ├── МАШИНИСТЫ_Цифриум_ВК_образование_вер_4.pptx
│       └── Цифриум Frontend.pptx
├── prompt_00.txt
├── results
│   ├── conspects
│   │   ├── conspect_API_claude-3-7-sonnet-20250219.md
│   │   ├── conspect_DeepSeek-R1-Distill-Qwen-14B-IQ4_XS.gguf.md
│   │   ├── conspect_DeepSeek-R1-Distill-Qwen-14B-IQ4_XS.gguf__lap-(1).md
│   │   ├── conspect_Meta-Llama-3.1-8B-Instruct.Q8_0.gguf.md
│   │   ├── conspect_Meta-Llama-3.1-8B-Instruct.Q8_0.gguf__lap-(0).md
│   │   ├── conspect_Meta-Llama-3.1-8B-Instruct.Q8_0.gguf__lap-(1).md
│   │   ├── conspect_Mistral-7B-Instruct-v0.3.Q8_0.gguf.md
│   │   ├── conspect_Mistral-7B-Instruct-v0.3.Q8_0.gguf__lap-(1).md
│   │   ├── conspect_Mistral-7B-Instruct-v0.3.fp16.gguf.md
│   │   ├── conspect_Mistral-7B-Instruct-v0.3.fp16.gguf__lap-(0).md
│   │   ├── conspect_Mistral-7B-Instruct-v0.3.fp16.gguf__lap-(1).md
│   │   ├── conspect_YandexGPT-5-Lite-8B-instruct.md
│   │   ├── conspect_claude-3.7-sonnet-reasoning-gemma3-12B.Q8_0.gguf.md
│   │   ├── conspect_claude-3.7-sonnet-reasoning-gemma3-12B.Q8_0.gguf__lap-(0).md
│   │   ├── conspect_claude-3.7-sonnet-reasoning-gemma3-12B.Q8_0.gguf__lap-(1).md
│   │   ├── conspect_falcon-7b-instruct.md
│   │   ├── conspect_gpt-3.5-turbo.md
│   │   ├── conspect_meta-llama-3-8b-instruct.Q4_K_M.gguf.md
│   │   ├── conspect_meta-llama-3-8b-instruct.Q4_K_M.gguf__lap-(1).md
│   │   ├── conspect_mistral-7b-instruct-v0.1.Q3_K_L.gguf.md
│   │   ├── conspect_mistral-7b-instruct-v0.1.Q3_K_L.gguf__lap-(0).md
│   │   ├── conspect_mistral-7b-instruct-v0.1.Q3_K_L.gguf__lap-(1).md
│   │   ├── conspect_mistral-7b-instruct-v0.1.Q3_K_L.gguf__lap-(2).md
│   │   ├── conspect_mistral-7b-instruct-v0.1.Q8_0.gguf.md
│   │   ├── conspect_mistral-7b-instruct-v0.1.Q8_0.gguf__lap-(0).md
│   │   ├── conspect_mistral-7b-instruct-v0.1.Q8_0.gguf__lap-(1).md
│   │   ├── conspect_mistral-7b-instruct-v0.2.Q4_K_M.gguf.md
│   │   ├── conspect_mistral-7b-instruct-v0.2.Q4_K_M.gguf__lap-(1).md
│   │   ├── conspect_mistral-7b-instruct-v0.2.Q4_K_M.gguf__lap-(2).md
│   │   ├── conspect_model_claude-3.7-sonnet-reasoning-gemma3-12B.Q8_0.gguf.md
│   │   ├── conspect_models_Meta-Llama-3.1-8B-Instruct.Q8_0.gguf.md
│   │   ├── conspect_models_Mistral-7B-Instruct-v0.3.fp16.gguf.md
│   │   ├── conspect_models_claude-3.7-sonnet-reasoning-gemma3-12B.Q8_0.gguf.md
│   │   ├── conspect_models_meta-llama-3-8b-instruct.Q4_K_M.gguf.md
│   │   ├── conspect_models_mistral-7b-instruct-v0.1.Q3_K_L.gguf.md
│   │   ├── conspect_models_mistral-7b-instruct-v0.1.Q8_0.gguf.md
│   │   ├── conspect_mythomax-l2-13b.Q8_0.gguf.md
│   │   ├── conspect_mythomax-l2-13b.Q8_0.gguf__lap-(0).md
│   │   ├── conspect_mythomax-l2-13b.Q8_0.gguf__lap-(1).md
│   │   ├── conspect_phi-2.Q8_0.gguf.md
│   │   ├── conspect_phi-2.Q8_0.gguf__lap-(0).md
│   │   ├── conspect_phi-2.Q8_0.gguf__lap-(1).md
│   │   └── conspect_phi-2.Q8_0.gguf__lap-(2).md
│   ├── docs
│   │   ├── Общественное движение в России 2четверь XIX в_01_base.docx
│   │   ├── Общественное движение в России 2четверь XIX в_01_large-v1.docx
│   │   ├── Общественное движение в России 2четверь XIX в_01_large-v2.docx
│   │   ├── Общественное движение в России 2четверь XIX в_01_large-v3.docx
│   │   ├── Общественное движение в России 2четверь XIX в_01_large.docx
│   │   ├── Общественное движение в России 2четверь XIX в_01_medium.docx
│   │   ├── Общественное движение в России 2четверь XIX в_01_small.docx
│   │   └── Общественное движение в России 2четверь XIX в_01_tiny.docx
│   ├── keyframes
│   │   ├── keyframe_04.jpg
│   │   ├── keyframe_08.jpg
│   │   ├── keyframe_10.jpg
│   │   ├── keyframe_11.jpg
│   │   ├── keyframe_12.jpg
│   │   ├── keyframe_14.jpg
│   │   ├── keyframe_16.jpg
│   │   ├── keyframe_17.jpg
│   │   ├── keyframe_18.jpg
│   │   ├── keyframe_20.jpg
│   │   ├── keyframe_21.jpg
│   │   ├── keyframe_22.jpg
│   │   ├── keyframe_23.jpg
│   │   ├── keyframe_24.jpg
│   │   ├── keyframe_25.jpg
│   │   ├── keyframe_27.jpg
│   │   ├── keyframe_29.jpg
│   │   ├── keyframe_30.jpg
│   │   ├── keyframe_32.jpg
│   │   ├── keyframe_33.jpg
│   │   ├── keyframe_38.jpg
│   │   ├── keyframe_40.jpg
│   │   ├── keyframe_43.jpg
│   │   ├── keyframe_44.jpg
│   │   ├── keyframe_45.jpg
│   │   ├── keyframe_47.jpg
│   │   ├── keyframe_48.jpg
│   │   ├── keyframe_49.jpg
│   │   └── keyframe_50.jpg
│   ├── pptx
│   │   ├── conspect_API_claude-3-7-sonnet-2025021.pptx
│   │   ├── conspect_API_claude-3-7-sonnet-20250219.md.pptx
│   │   ├── conspect_API_claude-3-7-sonnet-20250219.pptx
│   │   ├── conspect_claude-3.7-sonnet-reasoning-gemma3-12B.Q8_0.gguf.md.pptx
│   │   ├── conspect_gpt-3.5-turbo.md.pptx
│   │   ├── conspect_models_claude-3.7-sonnet-reasoning-gemma3-12B.Q8_0.gguf.md.pptx
│   │   ├── conspect_models_meta-llama-3-8b-instruct.Q4_K_M.gguf.md.pptx
│   │   ├── markdown_with_formatting.pptx
│   │   └── markdown_with_formatting_using_template.pptx
│   ├── prompts
│   │   ├── prompt_00.txt
│   │   ├── prompt_01.txt
│   │   ├── prompt_02.txt
│   │   └── prompt_03.txt
│   └── transcripts
│       ├── Общественное движение в России 2четверь XIX в_01_base.txt
│       ├── Общественное движение в России 2четверь XIX в_01_large-v1.txt
│       ├── Общественное движение в России 2четверь XIX в_01_large-v2.txt
│       ├── Общественное движение в России 2четверь XIX в_01_large-v3.txt
│       ├── Общественное движение в России 2четверь XIX в_01_large.txt
│       ├── Общественное движение в России 2четверь XIX в_01_medium.txt
│       ├── Общественное движение в России 2четверь XIX в_01_small.txt
│       └── Общественное движение в России 2четверь XIX в_01_tiny.txt
├── transcript.txt
├── utils.py
└── utils_log.py
```