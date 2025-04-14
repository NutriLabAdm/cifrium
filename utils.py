def tm(txt="", s=0):  # helper для измерений в коде
    import datetime 
    
    global lap,start
    
    try: lap 
    except: start = lap = datetime.datetime.today() 
    
    SUB = str.maketrans(":-+.0123456789", "⡄₋₊.₀₁₂₃₄₅₆₇₈₉")   # https://sanstv.ru/tools/unicode
    SUP = str.maketrans(":0123456789", "⠃⁰¹²³⁴⁵⁶⁷⁸⁹")
    
    txt = str(txt)
    
    if txt == "" or s==1: 
        lap = start =  datetime.datetime.today()
        print(f''' *** Start at: {ps.BLGREEN}{start:%H:%M:%S %Y-%m-%d}{ps.END} {txt} {"*"*60}'''); 
    else: 
        now = datetime.datetime.today()
        nowf = f'{now:%H:%M:%S}'.translate(SUP) if s==2  else ''
        
        print(
              nowf,
              f'{(f"{now-lap}"[:-3]):>12}', 
              f'{(f"{now-start}".translate(SUB)[:-3]):>12}',
              ps.rep(txt)
                 );
        lap =  datetime.datetime.today()
    return lap 


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
    
