import fcntl, termios, struct, signal, sys, time

def read_size(fd):
    rows, cols, _, _ = struct.unpack("HHHH", fcntl.ioctl(fd, termios.TIOCGWINSZ, b"\x00"*8))
    return rows, cols

def on_winch(signum, frame):
    r, c = read_size(sys.stdout.fileno())
    print(f"Nowy rozmiar: {r} x {c}", file=sys.stderr)

signal.signal(signal.SIGWINCH, on_winch)
on_winch(None, None) 
while True:
    time.sleep(1)      
