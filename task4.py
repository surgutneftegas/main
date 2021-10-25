#!/usr/bin/env python3
import socket

servers = {"drive.google.com" : "108.177.14.194", "mail.google.com" : "64.233.162.18", "google.com" : "173.194.220.113"}
for i, y in servers.items():
    if y != socket.gethostbyname(i):
        print(f'[ERROR] {i} IP mismatch: {y} - {socket.gethostbyname(i)}')
    else:
        print(f'{i} {y} - {socket.gethostbyname(y)}')