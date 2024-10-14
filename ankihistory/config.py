from pathlib import Path

from genanki import Model

SCRIPT_DIR = Path(__file__).resolve().parent


class History101Config:
    DECK_ID = 2059111110
    DECK_NAME = "History 101"

    MODEL_ID = 1607332339
    MODEL = Model(
        MODEL_ID,
        "History 101 Model",
        fields=[
            {"name": "Question"},
            {"name": "Answer"},
        ],
        templates=[
            {
                "name": "Card 1",
                "qfmt": "{{Question}}",
                "afmt": '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ],
    )

    INPUT_CSV_PATH = f"{SCRIPT_DIR.parent}/data/input/history101_questions.csv"
    OUTPUT_APKG_PATH = f"{SCRIPT_DIR.parent}/data/output/history101.apkg"
