from models.wine import Wine
from models.model import db
from PIL import Image
import pytesseract
from service.levenshtein import Levenshtein

class ProcessingPicture:

    def process(self, file):
        img = Image.open(file)
        content = pytesseract.image_to_string(img)
        wines = Wine.query.all()
        score = {}

        for i, wine in enumerate(wines):
            score[i] = Levenshtein.compareString(content, wine.nom)

        wineFound = wines[min(score, key=score.get)]
        return wineFound.to_dict()

