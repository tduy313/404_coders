#NGUOIDAUTIEN
#CHO XIN 1 FL NHÉ MN
import os, sys, time, math, warnings

warnings.filterwarnings("ignore", category=UserWarning, module="pygame")
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

file = "music.mp3"
trễ = 0.0
speed = 10.0
duration = 31
WIDTH = 60

RESET = "\033[0m" 
CLR = "\033[K"
B = "\033[1m"
HIDE = "\033[?25l"
SHOW = "\033[?25h"
MOVE_HOME = "\033[H"
DIM = "\033[38;5;236m"

ICE = [
    "\033[38;5;17m","\033[38;5;18m","\033[38;5;19m","\033[38;5;20m","\033[38;5;21m",
    "\033[38;5;27m","\033[38;5;33m","\033[38;5;39m","\033[38;5;45m","\033[38;5;51m",
    "\033[38;5;87m","\033[38;5;123m","\033[38;5;159m","\033[38;5;195m","\033[38;5;231m",
    "\033[38;5;255m","\033[38;5;231m","\033[38;5;195m","\033[38;5;159m","\033[38;5;123m",
    "\033[38;5;87m","\033[38;5;51m","\033[38;5;45m","\033[38;5;39m","\033[38;5;33m",
    "\033[38;5;27m","\033[38;5;21m","\033[38;5;20m","\033[38;5;19m","\033[38;5;18m"
]

HEART = [
    "\033[38;5;196m","\033[38;5;197m","\033[38;5;198m","\033[38;5;199m","\033[38;5;200m",
    "\033[38;5;201m","\033[38;5;207m","\033[38;5;213m","\033[38;5;219m","\033[38;5;225m",
    "\033[38;5;225m","\033[38;5;219m","\033[38;5;213m","\033[38;5;207m","\033[38;5;201m",
    "\033[38;5;200m","\033[38;5;199m","\033[38;5;198m","\033[38;5;197m","\033[38;5;196m"
]

lyric = [
    [(0.5,"Chỉ"),(1.0,"có"),(1.5,"anh"),(2.1,"làm"),(2.5,"trái"),(2.9,"tim"),(3.2,"em"),(3.7,"biết"),(4.0,"đập"),(4.50,"nồng"),(4.90,"nàn")],
    [(6.5,"Nỗi"),(6.80,"đau"),(7.00,"hóa"),(7.10,"tiếng"),(7.45,"cười"),(8.00,"rộn"),(8.40,"ràng")],
    [(10.95,"Mọi"),(11.10,"lo"),(11.35,"toan"),(11.60,"cứ"),(11.85,"để"),(12.10,"anh"),(12.35,"mang")],
    [(14.50,"Hay"),(15.00,"là"),(15.40,"em"),(15.70,"đi"),(16.00,"theo"),(16.30,"anh"),(16.65,"đến"),(17.10,"nơi")],
    [(18.60,"Nơi"),(18.85,"mà"),(19.10,"ta"),(19.35,"không"),(19.70,"chia"),(19.85,"đôi"),(20.20,"quãng"),(20.50,"đời")],
    [(22.27,"Nơi"),(22.35,"mà"),(22.50,"có"),(22.90,"anh"),(23.1,"cười"),(23.40,"như"),(23.70,"năm"),(24.00,"tháng"),(24.20,"đôi"),(24.70,"mươi")],
    [(25.50,"Nơi"),(26.10,"mà"),(26.40,"bão"),(26.50,"giông"),(26.80,"đều"),(27.30,"tan"),(27.60,"vì"),(27.80,"có"),(28.20,"nhau"),(28.40,'rồi')]
]

def setup_audio():
    if not os.path.exists(file): return None, False
    try: import pygame
    except: return None, False
    try:
        pygame.mixer.init(frequency=44100, buffer=512)
        pygame.mixer.music.load(file)
        return pygame, True
    except: return None, False

def heart(r, c, R, C):
    y = (R/2-r)/(R/2.5)
    x = (c-C/2)/(C/2.5)
    x*=1.8
    return (x**2+y**2-1)**3-(x**2*y**3)<=0                                              

def color(r,c,shift):
    if heart(r,c,len(lyric),WIDTH):
        return HEART[(c+r-shift)%len(HEART)]
    return ICE[(c+r-shift)%len(ICE)]

def line_str(words, active, ratio, row, freeze=False):
    shift = 0 if freeze else int(time.time()*speed)
    raw = []
    for i,w in enumerate(words): raw.append((" " if i>0 else "")+w)
    full = "".join(raw)
    pad = max(0,(WIDTH-len(full))//2)
    chars = ["."]*pad+list(full)+["."]*(WIDTH-pad-len(full))
    buf=[]
    start=pad
    end=pad+len(full)
    UNSUNG="\033[38;5;240m"
    for col, ch in enumerate(chars):
        c=color(row,col,shift)
        lyric_char = start<=col<end
        if not lyric_char: buf.append(f"{DIM}{c}{ch}{RESET}")
        else:
            rel=col-start
            acc=0
            status="future"
            for wi,wv in enumerate(words):
                wl=len(wv)+(1 if wi>0 else 0)
                if acc<=rel<acc+wl:
                    if wi<active: status="past"
                    elif wi==active:
                        ci=rel-acc-(1 if wi>0 else 0)
                        if ci<0: status="past"
                        elif ci<int(len(wv)*ratio): status="past"
                        else: status="future"
                    else: status="future"
                    break
                acc+=wl
            buf.append(f"{B}{c}{ch}{RESET}" if status=="past" else f"{UNSUNG}{ch}{RESET}")
    return "".join(buf)

def render(lines, cur_line, active_word, ratio, freeze=False):
    out=["\n"*2]
    for i, words in enumerate(lines):
        if i<cur_line: out.append(line_str(words,9999,1.0,i,freeze))
        elif i==cur_line: out.append(line_str(words,active_word,ratio,i,freeze))
        else: continue
    sys.stdout.write(MOVE_HOME+"\n".join([l+CLR for l in out]))
    sys.stdout.flush()

def main():
    os.system("cls" if os.name=="nt" else "clear")
    sys.stdout.write(HIDE)
    pg, music = setup_audio()
    if music:
        try: pg.mixer.music.play()
        except: music=False
    start=time.time()
    all_lines=[[w for _,w in line] for line in lyric]
    try:
        for idx,line in enumerate(lyric):
            first=line[0][0]+trễ
            while True:
                now=time.time()-start
                if now>=first: break
                render(all_lines[:idx+1],idx,-1,0.0)
                time.sleep(0.01)
            for i,(t,_) in enumerate(line):
                next_t=line[i+1][0]+trễ if i<len(line)-1 else t+trễ+(0.8 if idx<len(lyric)-1 else 0)
                dur=next_t-(t+trễ)
                while True:
                    now=time.time()-start
                    if now>=next_t: break
                    elapsed=now-(t+trễ)
                    ratio=min(max(elapsed/dur if dur>0 else 1.0,0.0),1.0)
                    render(all_lines[:idx+1],idx,i,ratio)
                    time.sleep(0.01)
        while True:
            now=time.time()-start
            if now>=duration: break
            render(all_lines,9999,9999,1.0)
            time.sleep(0.01)
        render(all_lines,9999,9999,1.0,freeze=True)
    except KeyboardInterrupt: pass
    if music:
        try: pg.mixer.music.stop()
        except: pass
    sys.stdout.write(SHOW)
    print('\n'+ICE[15]+"~~~~"+RESET+"\n")

if __name__=="__main__":
    main()
