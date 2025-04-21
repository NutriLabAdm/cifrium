import os
import datetime
from threading import Thread
from queue import Queue



# === Глобальные переменные ===
lap, start = None, None
_insert_queue = Queue()
_insert_worker_started = False
_gsheet_obj = None


# === Логгер в Jupyter/терминал ===
def tm(txt="", s=0):
    global lap, start
    now = datetime.datetime.now()
    if lap is None:
        start = lap = now

    SUB = str.maketrans(":-+.0123456789", "⡄₋₊.₀₁₂₃₄₅₆₇₈₉")
    SUP = str.maketrans(":0123456789", "⠃⁰¹²³⁴⁵⁶⁷⁸⁹")

    txt = str(txt)

    if txt == "" or s == 1:
        lap = start = now
        print(f''' *** Start at: {start:%H:%M:%S %Y-%m-%d} {txt} {"*"*40}''')
    else:
        nowf = f'{now:%H:%M:%S}'.translate(SUP) if s == 2 else ''
        delta_lap = now - lap
        delta_start = now - start

        print(nowf, f'{f"{delta_lap}"[:-3]:>12}', f'{f"{delta_start}"[:-3].translate(SUB):>12}',  ps.rep(txt))
        lap = now

    return lap


# === Инициализация Google Sheets ===
def init_gsheet(sheet_id='1QCLSait8lExQHwXDkBcPZZ9PYBNtWdorq-vF5hh944E', sheet_name='Transcription Log'):
    import os
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    # Абсолютный путь к текущему файлу (модулю)
    credentials_path = 'credentials.json'

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(sheet_id)

    try:
        worksheet = sheet.worksheet(sheet_name)
    except gspread.WorksheetNotFound:
        worksheet = sheet.add_worksheet(title=sheet_name, rows="10", cols="10")
        worksheet.append_row(['Session ID', 'Time', 'Δ from Last', 'Δ from Start', 'Message', 'Params', 'Tags'])

    return worksheet



# === Асинхронная вставка в Google Sheet ===
def async_insert_row(worksheet, row_data):
    """Асинхронная вставка строки в Google Sheet (новые строки — вверху)"""

    def worker():
        while True:
            ws, data = _insert_queue.get()
            try:
                ws.insert_row(data, index=2)  # Вставка после заголовка
            except Exception as e:
                print("⚠️ Ошибка записи в Google Sheet:", e)
            finally:
                _insert_queue.task_done()

    global _insert_worker_started
    if not _insert_worker_started:
        Thread(target=worker, daemon=True).start()
        _insert_worker_started = True

    _insert_queue.put((worksheet, row_data))


# === Логгер в Google Sheet ===
import datetime

# Хранилище таймеров: {lap_id: (start_time, last_lap_time)}
_lap_timers = {}
_gsheet_obj = None  # Глобальный объект таблицы

import datetime

# Глобальное хранилище таймеров
_lap_timers = {}
_gsheet_obj = None



import datetime

_lap_timers = {}
_gsheet_obj = None
_existing_columns = set()

def tg(txt, sid=None, sheet_name='def', tags=None, params=None, laps=None,
       gsheet_id='1QCLSait8lExQHwXDkBcPZZ9PYBNtWdorq-vF5hh944E',
       lap_id=None, reset=False
      ):
    global _gsheet_obj, _existing_columns
    now = datetime.datetime.now()

    # --- Обработка lap_id и reset ---
    if lap_id:
        if reset or '🚩' in txt or lap_id not in _lap_timers:
            _lap_timers[lap_id] = (now, now)
    else:
        if reset:
            _lap_timers.clear()
        lap_id = 'default'
        if '🚩' in txt or lap_id not in _lap_timers:
            _lap_timers[lap_id] = (now, now)

    # --- Вычисления времени ---
    start, lap = _lap_timers[lap_id]
    delta_lap = now - lap
    delta_start = now - start
    _lap_timers[lap_id] = (start, now)

    # --- Инициализация таблицы ---
    if _gsheet_obj is None:
        _gsheet_obj = init_gsheet(sheet_id=gsheet_id, sheet_name=sheet_name)
        _existing_columns = set(get_column_headers(_gsheet_obj))

    if sid is None:
        sid = str(round(start.timestamp()))

    # --- Базовая строка данных ---
    row_data = [
        sid,
        now.strftime('%Y-%m-%d %H:%M:%S'),
        round(delta_lap.total_seconds(), 3),
        round(delta_start.total_seconds(), 3),
        str(txt),
        params,
        tags
    ]

    # --- Подготовка дополнительных lap-колонок ---
    lap_columns = {}
    for _id, (_start, _lap) in _lap_timers.items():
        col_name = f"lap_{_id}"
        if col_name == "lap_default":  # Пропускаем, так как она уже в row_data
            continue
        lap_columns[col_name] = round((now - _lap).total_seconds(), 3)

        if col_name not in _existing_columns:
            add_column(_gsheet_obj, col_name)
            _existing_columns.add(col_name)

    # --- Добавляем значения счётчиков в таблицу ---
    for col in sorted(_existing_columns):
        if col.startswith("lap_") and col != "lap_default":
            row_data.append(lap_columns.get(col, None))

    async_insert_row(_gsheet_obj, row_data)




def get_column_headers(sheet_obj):
    # Получаем первую строку как список названий колонок
    return sheet_obj.row_values(1)

def add_column(sheet_obj, column_name):
    headers = get_column_headers(sheet_obj)
    if column_name not in headers:
        headers.append(column_name)
        sheet_obj.update('A1', [headers])  # Обновить первую строку (заголовки)




# подсветка текста 
class ps:
    def __init__(self,c = '#000000',b = '#ffffff'):
        hc = c.lstrip('#')
        hb = b.lstrip('#')
        (rc,gc,bc) = tuple(int(hc[i:i+2], 16) for i in (0, 2, 4))
        (rb,gb,bb) = tuple(int(hb[i:i+2], 16) for i in (0, 2, 4))
        res = f'\033[38;2;{rc};{gc};{bc}m\033[48;2;{rb};{gb};{bb}m'
        return res         

    END = '\033[0m'
    E = '\033[0m'
    _ = '\033[0m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLCYAN = '\033[48;2;210;255;240m'
    
    BLUE = '\033[94m'
    BBLUE = '\033[104m'
    LBLUE = '\033[38;2;50;210;255m'
    BLBLUE = '\033[48;2;150;220;255m'
    BLLBLUE = '\033[48;2;220;245;255m'

    
    LMAGENTA = '\033[38;2;250;230;255m'
    BLMAGENTA = '\033[48;2;255;225;255m'

    
    GREEN = '\033[92m'
    BGREEN = '\033[42m'
    
    LGREEN = '\033[38;2;50;255;210m'
    BLGREEN = '\033[48;2;140;255;180m'
    
    
    RED   = '\033[91m'
    BRED  = '\033[41m'
    LRED  = '\033[38;2;255;100;120m'
    BLRED = '\033[48;2;255;190;200m'
    ERR   = '\033[48;2;255;190;200m'
    err   = '\033[48;2;255;190;200m'

    GRAY   = '\033[38;2;100;100;100m'
    BGRAY  = '\033[48;2;220;220;220m'
    LGRAY  = '\033[38;2;200;200;200m'
    BLGRAY = '\033[48;2;245;245;245m'
    
    BLILAC = T = TOTAL = '\033[48;2;245;227;255m'
    
    ORANGE = '\033[38;2;255;75;21m'
    BORANGE = '\033[48;2;255;75;21m'
    
    
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    MAGENTA = '\033[35m'
    BMAGENTA = '\033[45m'
    YELLOW = '\033[33m'
    Y = '\033[43m'
    BYELLOW = BY ='\033[48;2;255;255;150m'
    BLYELLOW = BLY ='\033[48;2;255;255;235m'
    
    reps = [   
       '((BLGRAY))',
       '[!BLRED!]',
       '[[BY]]',
       '[%BLMAGENTA%]',
       '[(BLGREEN)]',
    ]
        
    def rep (s):

        for r in ps.reps:
            s = s.replace(r[:2],getattr(ps,r[2:-2])).replace(r[-2:],ps._)
        
        return s.replace('>>>',f'{ps.BLBLUE}>>>{ps._}')     
    
    def c(rgb):
        h = rgb.lstrip('#')
        (r,g,b) = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        res = f'\033[38;2;{r};{g};{b}m'
        return res 
    
    
    def b(rgb):
        h = rgb.lstrip('#')
        (r,g,b) = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        res = f'\033[48;2;{r};{g};{b}m'
        return res 
    
    def cb(c = '#000000',b = '#ffffff'):
        hc = c.lstrip('#')
        hb = b.lstrip('#')
        (rc,gc,bc) = tuple(int(hc[i:i+2], 16) for i in (0, 2, 4))
        (rb,gb,bb) = tuple(int(hb[i:i+2], 16) for i in (0, 2, 4))
        res = f'\033[38;2;{rc};{gc};{bc}m\033[48;2;{rb};{gb};{bb}m'
        return res 
    