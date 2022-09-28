from googletrans import Translator
import clipboard


def trans_from_clipbd() :
    translator = Translator()
    clip_txt = clipboard.paste()
    trans_txt = translator.translate(clip_txt, dest='en')
    # print(trans_txt.text)
    clipboard.copy(trans_txt.text)
    # print(clipboard.paste())


if __name__ == "__main__" :
    trans_from_clipbd()
    test_text = clipboard.paste()
    print(test_text)