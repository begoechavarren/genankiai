import logging

from config import History101Config
from utils import create_anki_deck, create_notes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_history_101_deck():
    history_101_notes = create_notes(
        csv_path=History101Config.INPUT_CSV_PATH,
        model=History101Config.MODEL,
    )

    create_anki_deck(
        deck_id=History101Config.DECK_ID,
        deck_name=History101Config.DECK_NAME,
        notes=history_101_notes,
        output_path=History101Config.OUTPUT_APKG_PATH,
    )


if __name__ == "__main__":
    create_history_101_deck()
