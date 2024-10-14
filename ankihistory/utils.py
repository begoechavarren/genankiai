import logging
from datetime import datetime
from pathlib import Path
from typing import List

import genanki
import pandas as pd
from genanki import Note

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_notes(input_path: str, model: genanki.Model) -> list[Note]:
    """Create Anki notes from a CSV file using the provided model.

    Args:
        input_path (str): Path to the CSV file containing the questions.
        model (genanki.Model): Anki note model to use for the notes.
    """
    questions_df = pd.read_csv(input_path)
    questions = questions_df.values.tolist()
    notes = []
    for question in questions:
        note = Note(model=model, fields=question)
        notes.append(note)
    return notes


def create_anki_deck(
    deck_id: int, deck_name: str, notes: List[Note], output_path: str
) -> None:
    """
    Create an Anki deck from the provided parameters and save it to an apkg file.

    Args:
        deck_id (int): Unique identifier for the deck.
        deck_name (str): Name of the deck.
        notes (List[Note]): List of notes to add to the deck.
        output_path (str): Path where the output .apkg file will be saved.
    """
    try:
        deck = genanki.Deck(deck_id, deck_name)

        for note in notes:
            deck.add_note(note)

        current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
        output_path = Path(output_path)
        new_filename = f"{output_path.stem}_{current_datetime}{output_path.suffix}"
        new_output_path = output_path.with_name(new_filename)
        new_output_path.parent.mkdir(parents=True, exist_ok=True)

        package = genanki.Package(deck)
        package.write_to_file(new_output_path)
        logger.info(f"Successfully created Anki package: {new_output_path}")
    except Exception as e:
        logger.error(f"An error occurred while creating the Anki deck: {str(e)}")
