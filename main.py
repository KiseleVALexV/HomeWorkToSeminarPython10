
from calculation import CalcModule as calc
from logging import LogEntry as logg
from typeselection import IdentifyType as ident
import console as cons

def StartingCalc():
    dt = ident(cons.InputData())
    result = calc(dt)
    cons.OutData(result)
    logg(dt, result)

StartingCalc()