import sys
import glob
PUZZLES=[
"fake-surveillance-camera-",
"animated-esports-sign-",
"diagnostic-pulse-generator-",
"harmonic-maximization-engine-",
"pollution-sensing-smart-window-",
"passive-infrared-sensor-",
"personal-sandwich-maker-",
"haunted-doll-",
"token-based-payment-kiosk-",
"color-changing-vape-pen-",
"wireless-game-controller-",
"precision-food-scale-",
"cryptocurrency-deposit-terminal-",
"carbine-target-illuminator-",
"unknown-optimization-device-",
"remote-kill-switch-",
"pocket-i-ching-oracle-",
"color-coordinating-shoes-",
"spoiler-blocking-headphones-",
"airline-cocktail-mixer-",
"deep-sea-sensor-grid-",
"meat-based-printer-",
"aquaponics-maintenance-robot-",
"smart-grid-control-router-",
"traffic-signal-",
"safetynet-tracking-badge-",
"drinking-game-scorekeeper-",
"control-signal-amplifier-",
"electronic-door-lock-",
"virtual-reality-buzzer-",
"cold-storage-robot-",
"scientific-chronometer-",
"automatic-pet-feeder-",
"electronic-practice-target-",
"kelp-harvesting-robot-",
"sushi-making-robot-",
"thorium-reactor-status-monitor-",
"brain-computer-interface-",
"cellular-scaffold-printer-",
"laser-tag-equipment-"]
def read_solution(path):
    c,p,l=(None,None,None)
    with  open(path,"r") as f:
        lines=[l.strip() for l in f.readlines()]
        c,p,l=None,None,None
        for line in lines:
            if "[production-cost]" in line and c is None:
                c=int(line.split()[-1])
            if "[power-usage]" in line and p is None:
                p=int(line.split()[-1])
            if "[lines-of-code]" in line and l is None:
                l=int(line.split()[-1])
    return c,p,l
def read_scores(path):
    report=[]
    for n in PUZZLES:
        scores=[]
        for spath in glob.glob(path+"/"+n+"*.txt"):
            scores.append(read_solution(spath))
        c=[s[0] for s in scores if s[0] is not None]
        p=[s[1] for s in scores if s[1] is not None]
        l=[s[2] for s in scores if s[2] is not None]
        if len(c):
            report.append((n[:-1],(min(c)//100,min(p),min(l))))
        else:
            report.append((n[:-1],None))
    return report
def print_scores(rpt):
    out=""
    for n,s in rpt:
        out+=n+"\n"
        if s is None:
            out+="unsolved\n"
        else:
            out+="cost\t{:d}\npower\t{:d}\nlines\t{:d}\n".format(*s)
    print(out.strip())
            
if __name__=='__main__':
    if len(sys.argv)==0:
        print("usage: get_scores.py path_to_scores")
    report=read_scores(sys.argv[1])
    print_scores(report)
