"""Logging pattern examples."""

import logging

LOGGER = logging.getLogger(__name__)


def process_item(item_id: str) -> None:
    """Log structured progress around item processing."""
    LOGGER.info("processing item", extra={"item_id": item_id})
    LOGGER.info("processing complete", extra={"item_id": item_id})
