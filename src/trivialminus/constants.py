# TODO: Validate
"""Path and site constants for trivialminus."""

from pathlib import Path

TRIVIALMINUS_PATH = Path(__file__).parent
FILES_PATH = TRIVIALMINUS_PATH / "_files"

WEB_DOMAIN = "www.paramountplus.com"

# Default location parameters the search lookup requires. Paramount+ scopes
# search to a US market; these mirror the values the web client sends and can be
# overridden per call.
DEFAULT_DMA = "807"
DEFAULT_STATION_ID = "16533"
DEFAULT_LATITUDE = "37.99"
DEFAULT_LONGITUDE = "-121.71"
DEFAULT_TIME_ZONE = "America/Los_Angeles"
