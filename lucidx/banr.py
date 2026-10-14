#!/usr/bin/env python3
# Author: Alex a.k.a. VritraSec
# Project: LucidX — AI-Powered Image Synth Engine
# GitHub: https://github.com/MrHacker-X

from datetime import datetime
import random
import os
from .colors import *

def lucid_logo_banner():

    session_id = f"0x{random.randint(0x100000, 0xFFFFFF):06X}"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    banner = f"""
{GREEN}           ▄█▀▄            ▄▀▄▄
               ▀▄        ▄▀
          ▄▄▄    █▄▄▄▄▄▄█    ▄▄▄
         ▀   ▀█ █▀  ▐▌  ▀█ █▀   ▀
               ██  ▀▐▌▀  ██
          ▄█▀▀▀████████████▀▀▀█
         █      ██████████     ▀▄
         █▄   █▀  ▀▀▀▀▀▀  ▀█   ▄█
          ▀█   █ v.1.0.5  █   █▀{RESET}

{GRAY}┌─────────────────────────────────────────┐
│ {GRAY}•  SESSION ID    : {VALUE}{session_id}          {GRAY}   │
│ {GRAY}•  TIMESTAMP     : {VALUE}{timestamp}  {GRAY}│
│ {GRAY}•  MODE          : {MODE}VISION SYNTHESIS    {GRAY} │
│ {GRAY}•  CORE GREEN    : {GREEN}ONLINE{GRAY}               │
└─────────────────────────────────────────┘

{QUOTE_BLUE}❝ I don’t paint dreams.
   I compute realities yet to be rendered. ❞{RESET}

{GREEN}┌────────────────────────────────────────────┐
│ 🧠  LucidX awaits your imagination...      │
└────────────────────────────────────────────┘{RESET}"""
    return banner


def lucid_Main_logo():
    session_id = f"0x{random.randint(0x100000, 0xFFFFFF):06X}"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    banner = f"""
{GREEN}           ▄█▀▄            ▄▀▄▄
               ▀▄        ▄▀
          ▄▄▄    █▄▄▄▄▄▄█    ▄▄▄
         ▀   ▀█ █▀  ▐▌  ▀█ █▀   ▀
               ██  ▀▐▌▀  ██
          ▄█▀▀▀████████████▀▀▀█
         █      ██████████     ▀▄
         █▄   █▀  ▀▀▀▀▀▀  ▀█   ▄█
          ▀█   █ v.1.0.5  █   █▀{RESET}

{GRAY}┌─────────────────────────────────────────┐
│ {GRAY}•  SESSION ID    : {VALUE}{session_id}          {GRAY}   │
│ {GRAY}•  TIMESTAMP     : {VALUE}{timestamp}  {GRAY}│
│ {GRAY}•  MODE          : {MODE}VISION SYNTHESIS    {GRAY} │
│ {GRAY}•  CORE GREEN    : {GREEN}ONLINE{GRAY}               │
└─────────────────────────────────────────┘"""
    return banner