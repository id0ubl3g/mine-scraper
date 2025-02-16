from config.colors_config import BRIGHT_YELLOW, GREEN, RED, RESET, BOLD

usage_mine_scraper = f"""{GREEN}{BOLD}MineScraper{RESET} - Web Scraping for data extraction and processing.
GitHub: {GREEN}github.com/id0ubl3g/mine-scraper{RESET}

{BRIGHT_YELLOW}Usage:{RESET}
    python3 run.py --localhost [OPTIONS]

{BRIGHT_YELLOW}Options:{RESET}
    {GREEN}-l, --localhost <True/False>{RESET}
        Configure proxy behavior:
        - Use {GREEN}True{RESET}  → Connect directly via localhost (no proxy)
        - Use {RED}False{RESET} → Enable proxy (settings from config/proxies_config.py)

{BRIGHT_YELLOW}Examples:{RESET}
    python3 run.py --localhost {GREEN}True{RESET}    # Direct connection (localhost)
    python3 run.py --localhost {RED}False{RESET}   # Use proxy settings

{BRIGHT_YELLOW}Misc Options:{RESET}
    {GREEN}-h, --help{RESET}
        Show this help message and exit.
    """