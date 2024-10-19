import logging
import os
import structlog
from structlog import get_logger

import sentry_sdk
from dotenv import load_dotenv

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

if os.environ.get("SENTRY_DSN"):
    sentry_sdk.init(dsn=os.environ["SENTRY_DSN"])

def get_logger(name):
    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.KeyValueRenderer(key_prefix=" "),
            structlog.processors.JSONRenderer(),
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
        wrapper_class=structlog.stdlib.BoundLogger,
        context_class=dict,
        level=LOG_LEVEL,
    )

    return get_logger(name)