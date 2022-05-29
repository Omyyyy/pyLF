import compiler
import os
import time
import sys
import runner

TEST = False

MESSAGES = False

APPROXTIME = True

TOTALTIME = True

try:
    if sys.argv[-1].endswith(".lf\\"):
        filename = sys.argv[-1].removesuffix(".lf\\")
        
    else:
        filename = sys.argv[-1].removesuffix(".lf")

except IndexError:
    print(compiler.red("LF: error: No file specified."))
    exit(1)

flags = sys.argv[1:-1]

if "-t" in flags:
    TEST = True

    flags.remove("-t")

if "-i" in flags:
    MESSAGES = True

    flags.remove("-i")


print(f"[COMPILING] > Started compiling {filename}.lf;") if MESSAGES else None

start_time = time.process_time()

with open(filename + ".lf", "r") as f:
    for i in f.readlines():
        compiler.Lexer(i.replace("\n", "").replace("\t", "    ").split("#", 1)[0], filename) if i.split("#", 1)[0].isspace() == False and i.startswith("#") == False else None

timecomp = time.process_time() - start_time

if timecomp == 0.0:
    timecomp = 0.0001

if MESSAGES:
    print(f"[COMPILING] > Compilation over in {round(timecomp, 4)}s ({round(timecomp, 4) * 1000}ms)\n") if APPROXTIME else print(f"[COMPILING] > Compilation over in {timecomp}s ({timecomp * 1000}ms)\n")

print(f"[RUNNING] > Running...\n") if MESSAGES else None

program_time = time.process_time()

if TEST:
    with open(filename + ".py", "w") as f:
        f.write(runner.code)

try:
    exec(runner.code.replace("array.Length(", "len(").replace("string.Length(", "len(").replace("interger.Range(", "range(").replace("string.Enum(", "enumerate(").replace("array.Enum(", "enum(").replace("array.Sum(", "sum("))

except TypeError as e:
    if str(e).startswith("can't unbox heterogeneous list:"):
        print(compiler.red("OverflowError: value exceeds 64-bit integer range"))

timeprog = time.process_time() - program_time

if timeprog == 0.0:
    timeprog = 0.0001

if MESSAGES:
    print(f"\n[RUNNING] > Program run in {round(timeprog, 4)}s ({round(timeprog, 4) * 1000}ms)\n") if APPROXTIME else print(f"\n[RUNNING] > Program run in {timeprog}s ({timeprog * 1000}ms)\n") 

if MESSAGES and TOTALTIME:
    print(f"\n[INFO] > Total time of compiling and running was {round(timeprog, 4) + round(timecomp, 4)}s ({round(timeprog, 4) * 1000 + round(timecomp, 4) * 1000}ms)\n") if APPROXTIME else print(f"\n[RUNNING] > Total time of compiling and running was {timeprog + timecomp}s ({timeprog * 1000 + timecomp * 1000}ms)\n")
