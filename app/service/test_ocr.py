from PIL import Image
import pytesseract
import easyocr

class TestOcr:
    def test_pytesseract(self) :
        print("azert")
        # In order to bypass the image conversions of pytesseract, just use relative or absolute image path
        # NOTE: In this case you should provide tesseract supported images or tesseract will return error
        test = pytesseract.image_to_string('/home/user/Bureau/alternance/Cours/urbanisation/images/test.png')
        test1 = pytesseract.image_to_string('/home/user/Bureau/alternance/Cours/urbanisation/images/test1.png')
        test2 = pytesseract.image_to_string('/home/user/Bureau/alternance/Cours/urbanisation/images/test2.png')
        test3 = pytesseract.image_to_string('/home/user/Bureau/alternance/Cours/urbanisation/images/test3.png')
        test4 = pytesseract.image_to_string('/home/user/Bureau/alternance/Cours/urbanisation/images/test4.png')
        print(test)
        print(test1)
        print(test2)
        print(test3)
        print(test4)
        return 'test'

    def test_easyocr(self) :
        print("azert")
        reader = easyocr.Reader(['fr'], gpu=False) # this needs to run only once to load the model into memory
        # In order to bypass the image conversions of pytesseract, just use relative or absolute image path
        # NOTE: In this case you should provide tesseract supported images or tesseract will return error
        texte = ""
        texte1 = ""
        texte2 = ""
        texte3 = ""
        texte4 = ""
        
        test = reader.readtext('/home/user/Bureau/alternance/Cours/urbanisation/images/test.png')
        test1 = reader.readtext('/home/user/Bureau/alternance/Cours/urbanisation/images/test1.png')
        test2 = reader.readtext('/home/user/Bureau/alternance/Cours/urbanisation/images/test2.png')
        test3 = reader.readtext('/home/user/Bureau/alternance/Cours/urbanisation/images/test3.png')
        test4 = reader.readtext('/home/user/Bureau/alternance/Cours/urbanisation/images/test4.png')
        for x in test:
            texte += x[1] + " "
        
        for x in test1:
            texte1 += x[1] + " "
        
        for x in test2:
            texte2 += x[1] + " "

        for x in test3:
            texte3 += x[1] + " "
        
        for x in test4:
            texte4 += x[1] + " "

        print(texte)
        print(texte1)
        print(texte2)
        print(texte3)
        print(texte4)
        return 'test2'