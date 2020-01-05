import os
import sys
from PyQt5.QtWidgets import *
from jinja2 import Environment, FileSystemLoader
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtCore


class SaveToPDF(QWidget):

    def __init__(self, FileName="index.html", Title="WAKACJE W NIEWOLI ", Content="ZAPRASZAMYNAWKACJEWESZWECJIerwerwerwerwerewrwerfdsfdgvdfgdfgdfgdf",Prize="10000", Photo="Zdjecie"):
        super().__init__()

        context = {
            'TitleLabel': Title,
            'phototrawel': Photo,
            'contents': Content,
            'prize': Prize
        }

        PATH = os.path.dirname(os.path.abspath(__file__))
        self.TEMPLATE_ENVIRONMENT = Environment(loader=FileSystemLoader(os.path.join(PATH, 'templates')))

        # Generate the HTML data with the template without creating a file, on-the-fly
        html = self.render_template(FileName, context)

        # add html to a webengine/widget
        self.web = QtWebEngineWidgets.QWebEngineView()
        self.web.setHtml(html)

        self.web.loadFinished.connect(self.emit_pdf)




    def render_template(self,template_filename, context):
        return self.TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

    def emit_pdf(self):
        self.web.show()
        self.web.page().printToPdf("test.pdf")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        app.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    ex = SaveToPDF()
    sys.exit(app.exec_())
