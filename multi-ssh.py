#!/usr/bin/env python3.7

import iterm2
# This script was created with the "basic" environment which does not support adding dependencies
# with pip.

def generate_cmd_list(cmdList):
    with open('UPDATE-THIS-TO-FILE-LOCATION') as my_file:
        for line in my_file:
            cmdList.append("ssh " + line)
    return cmdList

async def main(connection):
    # Your code goes here. Here's a bit of example code that adds a tab to the current window:

    cmdList = []

    cmdList = generate_cmd_list(cmdList)

    app = await iterm2.async_get_app(connection)

    await app.async_activate()

    await iterm2.Window.async_create(connection)

    currentSession = app.current_terminal_window.current_tab.current_session
    newSession = currentSession

    await currentSession.async_send_text(text=cmdList[0])

    if len(cmdList) >= 0:
        index = 0
        while index < len(cmdList):
            if index == 0:
                index += 1
            else:
                if index % 2 == 0:
                    currentSession = await currentSession.async_split_pane()
                    await currentSession.async_send_text(text=cmdList[index])
                    currentSession = app.current_terminal_window.current_tab.current_session
                    index += 1
                else:
                    if index+1 >= len(cmdList):
                        newSession = await newSession.async_split_pane()
                    else:
                        newSession = await newSession.async_split_pane(vertical=True)
                    await newSession.async_send_text(text=cmdList[index])
                    index += 1


iterm2.run_until_complete(main)
