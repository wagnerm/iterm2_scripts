#!/usr/bin/env python3
#
# Reads a flat file of hostnames as an argument. Each hostname on a new line.
# In a new tab, SSH to each server and run a command.
# Useful to look at logs or something on a group of servers.

import iterm2
import sys


async def main(connection):
    app = await iterm2.async_get_app(connection)
    window = app.current_terminal_window

    with open(sys.argv[1]) as f:
        for line in f.readlines():
            hostname = line.strip("\n")
            await window.async_create_tab(command="ssh {} -C \"whoami\"".format(hostname))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: launch_host_cmds.py <hosts-file>")
        exit(1)

    iterm2.run_until_complete(main)
