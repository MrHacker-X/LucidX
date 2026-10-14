#!/usr/bin/env python3
# Author: Alex a.k.a. VritraSec
# Project: LucidX — AI-Powered Image Synth Engine
# GitHub: https://github.com/MrHacker-X

from .colors import *
import re, os, time, json
from pathlib import Path

def lucid_exit():
    print()
    print(f"{GRAY}┌────────────────────────────────────┐")
    print(f"{GREEN}│ {GREEN}• {WHITE}Thank you for using {GREEN}LucidX{GRAY}       │")
    print(f"{GREEN}│ {GREEN}• {WHITE}Your vision now lives in code.{GRAY}   │")
    print(f"{GREEN}│ {GREEN}• {WHITE}Keep creating. Stay lucid.{GRAY}       │")
    print(f"{GREEN}│ {GREEN}• {GREEN}Session terminated gracefully.{GRAY}   │")
    print(f"{GRAY}└────────────────────────────────────┘\n\n")
    exit()


def configure_api_key():
    existing_key = None

    config_path = Path.home() / ".config-vritrasecz/lucidx-config.json"
    
    if config_path.exists():
        try:
            with open(config_path, "r") as f:
                config = json.load(f)
                existing_key = config.get('API', '')
        except Exception:
            pass
    
    if existing_key:
        print()
        print(f"{GRAY}┌──────────────────────────────────────────┐")
        print(f"{GREEN}│ {WHITE}• An API key is already configured.      {GRAY}│")
        print(f"{GREEN}│ {WHITE}• Existing key: {VALUE}{existing_key[:5]}*****{existing_key[-3:]}            {GRAY}│")
        print(f"{GREEN}│ {WHITE}• Do you want to {RED}replace{WHITE} it? ({GREEN}y/n{WHITE})       {GRAY}│")
        print(f"{GRAY}└──────────────────────────────────────────┘")
        
        choice = input(f"{QUOTE_BLUE}» {WHITE}Your choice: {GREEN}").strip().lower()
        if choice != "y":
            print(f"\n{GREEN}• Returning to main menu...")
            time.sleep(2)
            return

    print()
    print(f"{GRAY}┌────────────────────────────────────────────────┐")
    print(f"{GREEN}│ {WHITE}• Enter your new {GREEN}Stability AI {WHITE}API Key below.   {GRAY}│")
    print(f"{GRAY}└────────────────────────────────────────────────┘")

    while True:
        user_input = input(f"{QUOTE_BLUE}» {WHITE}API Key: {VALUE}").strip()
        if user_input:
            break
        else:
            print(f"{RED}• Invalid input. API key cannot be empty.")

    try:
        config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(config_path, "w") as file:
            json.dump({'API': user_input}, file)

        print()
        print(f"{GRAY}┌──────────────────────────────────────────────────────┐")
        print(f"{GREEN}│ {WHITE}• API Key successfully updated.                      {GRAY}│")
        print(f"{GREEN}│ {WHITE}• Saved to: {VALUE}~/.config-vritrasecz/lucidx-config.json{WHITE}  {GRAY}│")
        print(f"{GREEN}│ {WHITE}• Returning to main menu...                          {GRAY}│")
        print(f"{GRAY}└──────────────────────────────────────────────────────┘")
        time.sleep(2)

    except Exception as e:
        print()
        print(f"{RED}• Error saving API key: {e}")
        time.sleep(2)


def about_lucidx():
    print()
    print(f"{GRAY}┌{'─' * 60}┐")
    print(f"{GREEN}│ {WHITE}LucidX is an {GREEN}AI-powered image synthesis engine             {GRAY}│")
    print(f"{GREEN}│ {WHITE}crafted for {GREEN}creators{WHITE}, {GREEN}developers{WHITE}, and {GREEN}visionaries{WHITE}.         {GRAY}│")
    print(f"{GREEN}│ {WHITE}Generate stunning, high-res images using pure imagination. {GRAY}│")
    print(f"{GRAY}├{'─' * 60}┤")
    print(f"{GREEN}│ {WHITE}• Tool Name     : {VALUE}LucidX                                   {GRAY}│")
    print(f"{GREEN}│ {WHITE}• Version       : {VALUE}1.0.5                                    {GRAY}│")
    print(f"{GREEN}│ {WHITE}• Engine Mode   : {VALUE}Vision Synthesis Core                    {GRAY}│")
    print(f"{GREEN}│ {WHITE}• Tech Stack    : {VALUE}Stability AI API + Python                {GRAY}│")
    print(f"{GREEN}│ {WHITE}• Platforms     : {VALUE}Linux, Termux (Android)                  {GRAY}│")
    print(f"{GRAY}├{'─' * 60}┤")
    print(f"{GREEN}│ {WHITE}Features:                                                  {GRAY}│")
    print(f"{GREEN}│ {WHITE}› {GREEN}High-quality{WHITE} multi-style image generation                {GRAY}│")
    print(f"{GREEN}│ {WHITE}› {GREEN}Auto-save{WHITE} with timestamps and full logging               {GRAY}│")
    print(f"{GREEN}│ {WHITE}› {GREEN}Interactive CLI{WHITE} interface for smooth control             {GRAY}│")
    print(f"{GREEN}│ {WHITE}› {GREEN}Fully customizable{WHITE} API-based workflow                    {GRAY}│")
    print(f"{GRAY}├{'─' * 60}┤")
    print(f"{GREEN}│ {WHITE}Built by: {VALUE}Alex @ VritraSec                                 {GRAY}│")
    print(f"{GREEN}│ {WHITE}Vision: {GREEN}AI creation should feel like magic—controlled.     {GRAY}│")
    print(f"{GRAY}└{'─' * 60}┘\n")
    input(f"{WHITE}↳ Press {GREEN}Enter{WHITE} to return to main menu... ")


def lucid_connect():
    print()
    print(f"{GRAY}┌───────────────────────────────────────────────┐")
    print(f"{GREEN}│ {WHITE}           CONNECT WITH THE OWNER             {GREEN}│")
    print(f"{GRAY}├───────────────────────────────────────────────┤")
    print(f"{GREEN}│ {GREEN}• {WHITE}Website      : {GRAY}https://vritrasec.com        │")
    print(f"{GREEN}│ {GREEN}• {WHITE}Instagram    : {GRAY}@haxorlex                    │")
    print(f"{GREEN}│ {GREEN}• {WHITE}YouTube      : {GRAY}@Technolex                   │")
    print(f"{GREEN}│ {GREEN}• {WHITE}Telegram     : {GRAY}@LinkCentralX (Channel)      │")
    print(f"{GREEN}│ {GREEN}• {WHITE}Support Bot  : {GRAY}@ethicxbot                   │")
    print(f"{GREEN}│ {GREEN}• {WHITE}GitHub       : {GRAY}github.com/MrHacker-X        │")
    print(f"{GRAY}└───────────────────────────────────────────────┘")
    print()
    input(f"{WHITE}Press {GREEN}Enter{WHITE} to return to main menu...")

def lucid_help():
    print()
    print(f"{GRAY}┌──────────────────────────────────────────────────────────────┐")
    print(f"{GREEN}│ {GRAY}             {GREEN}    HELP / DOCUMENTATION CENTER                 {GRAY}│")
    print(f"{GRAY}├──────────────────────────────────────────────────────────────┤")
    print(f"{GREEN}│ {GREEN}• {WHITE}Image Generation                                           {GRAY}│")
    print(f"{GREEN}│{GRAY}   This is the core feature of LucidX. Simply enter a text    {GRAY}│")
    print(f"{GREEN}│{GRAY}   prompt and the system will generate 4 high-quality images  {GRAY}│")
    print(f"{GREEN}│{GRAY}   based on the selected AI style (e.g., photographic, anime).{GRAY}│")
    print(f"{GREEN}│{GRAY}   The output images are saved automatically with unique      {GRAY}│")
    print(f"{GREEN}│{GRAY}   filenames based on the current timestamp.                  {GRAY}│")
    print(f"{GREEN}│ {GRAY}                                                             │")
    print(f"{GREEN}│ {GREEN}• {WHITE}Configure API Key                                          {GRAY}│")
    print(f"{GREEN}│{GRAY}   Before generating any image, you must configure your       {GRAY}│")
    print(f"{GREEN}│{GRAY}   Stability AI API key. The key is securely stored inside a  {GRAY}│")
    print(f"{GREEN}│{GRAY}   local config file. If a key is already set, you’ll be      {GRAY}│")
    print(f"{GREEN}│{GRAY}   prompted whether you want to replace it.                   {GRAY}│")
    print(f"{GREEN}│ {GRAY}                                                             │")
    print(f"{GREEN}│ {GREEN}• {WHITE}Connect With Us                                            {GRAY}│")
    print(f"{GREEN}│{GRAY}   You can find us across platforms like Telegram, Instagram, {GRAY}│")
    print(f"{GREEN}│{GRAY}   YouTube, and GitHub. We regularly post updates, features,  {GRAY}│")
    print(f"{GREEN}│{GRAY}   and offer community support via these channels.            {GRAY}│")
    print(f"{GREEN}│ {GRAY}                                                             │")
    print(f"{GREEN}│ {GREEN}• {WHITE}Output Storage                                             {GRAY}│")
    print(f"{GREEN}│{GRAY}   All generated images are stored in structured folders.     {GRAY}│")
    print(f"{GREEN}│{GRAY}   For Termux: '/sdcard/lucidx_images'                        {GRAY}│")
    print(f"{GREEN}│{GRAY}   For Linux/PC: './generated_images'                         {GRAY}│")
    print(f"{GREEN}│{GRAY}   File names follow the format: YYYYMMDD_HHMMSS.png          {GRAY}│")
    print(f"{GREEN}│ {GRAY}                                                             │")
    print(f"{GREEN}│ {GREEN}• {WHITE}Session Logging                                            {GRAY}│")
    print(f"{GREEN}│{GRAY}   Every prompt and generated image is logged with its        {GRAY}│")
    print(f"{GREEN}│{GRAY}   corresponding timestamp, style used, and output file name. {GRAY}│")
    print(f"{GREEN}│{GRAY}   These logs are saved in 'lucidx_log.txt'.                  {GRAY}│")
    print(f"{GREEN}│ {GRAY}                                                             │")
    print(f"{GREEN}│ {GREEN}• {WHITE}Keyboard Interrupt Handling                                {GRAY}│")
    print(f"{GREEN}│{GRAY}   If you press Ctrl+C anytime during usage, LucidX will not  {GRAY}│")
    print(f"{GREEN}│{GRAY}   crash or corrupt. Instead, it will gracefully return you   {GRAY}│")
    print(f"{GREEN}│{GRAY}   back to the safe main menu.                                {GRAY}│")
    print(f"{GREEN}│ {GRAY}                                                             │")
    print(f"{GREEN}│ {GREEN}• {WHITE}Reporting Issues                                           {GRAY}│")
    print(f"{GREEN}│{GRAY}   If you face any bug, glitch, or unexpected behavior,       {GRAY}│")
    print(f"{GREEN}│{GRAY}   kindly report it on the official GitHub repo below.        {GRAY}│")
    print(f"{GREEN}│ {WHITE}  → {QUOTE_BLUE}https://github.com/MrHacker-X/LucidX                     {GRAY}│")
    print(f"{GRAY}└──────────────────────────────────────────────────────────────┘")
    print()
    print()
    print(f"{GRAY}┌──────────────────────────────────────────────────────────────┐")
    print(f"{GRAY}│{GREEN}                TIPS & BEST PRACTICES FOR LucidX              {GRAY}{GRAY}│")
    print(f"{GRAY}├──────────────────────────────────────────────────────────────┤")
    print(f"{GRAY}│{GREEN} • {WHITE}Use descriptive prompts — avoid single words.              {GRAY}{GRAY}│")
    print(f"{GRAY}│{GREEN} • {WHITE}Add modifiers: {VALUE}‘high quality’{WHITE}, {VALUE}‘cinematic’{WHITE}, etc.           {GRAY}{GRAY}│")
    print(f"{GRAY}│{GREEN} • {WHITE}Select the right style matching your vision.               {GRAY}{GRAY}│")
    print(f"{GRAY}│{GREEN} • {WHITE}Reuse logs to {GREEN}refine and evolve your creations.            {GRAY}{GRAY}│")
    print(f"{GRAY}│{GREEN} • {WHITE}Ensure API key is active and valid.                        {GRAY}{GRAY}│")
    print(f"{GRAY}│{GREEN} • {WHITE}Facing {GREEN}issues?{WHITE} Try better prompts or check internet.       {GRAY}{GRAY}│")
    print(f"{GRAY}└──────────────────────────────────────────────────────────────┘")
    print()
    input(f"{WHITE}↪ Press {GREEN}Enter{WHITE} to return to main menu...")
