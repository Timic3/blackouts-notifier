from dotenv import load_dotenv
from importlib import import_module
import sys
import os
from src.notifiers.discord import Discord

from src.infrastructure.utils import to_camel_case

load_dotenv()

def scrape(provider_name, filters={}):
    print("Running scraper %s (%s)..." % (provider_name, to_camel_case(provider_name)))
    provider = load_provider(provider_name)
    handler = provider()
    handler.set_filters(filters)
    data = handler.handle()

    if (os.getenv("DISCORD_WEBHOOK")):
        discord = Discord(os.getenv("DISCORD_WEBHOOK"))
        embeds = []

        for record in data:
            embeds.append({
                "title": "Blackout(s) for " + record["street"],
                "description": "Blackout detected (`%s`) for **%s** between `%s` and `%s`." % (
                    record["type"],
                    record["street"],
                    record["time_start"],
                    record["time_end"]
                ),
                "color": 0xFF0000
            })

        if len(embeds) > 0:
            discord.handle({
                "content": ":warning: Blackout detected!",
                "embeds": embeds
            })

def load_provider(provider_name):
    try:
        provider = import_module("src.providers." + provider_name)
        try:
            _class = getattr(provider, to_camel_case(provider_name))
        except AttributeError:
            print("Class incorrectly configured")
    except ImportError:
        print("Provider not found")

    return _class or None

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) < 1:
        print("Usage: ./main.py provider_name [street]")
        exit(1)

    filters = {}
    if len(args) == 2:
        filters["street"] = args[1]

    scrape(args[0].lower(), filters=filters)
