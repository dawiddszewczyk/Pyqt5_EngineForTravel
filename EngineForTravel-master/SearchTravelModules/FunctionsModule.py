from PyQt5.Qt import QLabel
from PyQt5.QtGui import QFont

def SetFont(Size, FontFamily="DukeFill"):
    fFontSize = Size

    Font = QFont()
    Font.setFamily(FontFamily)
    Font.setPointSize(fFontSize)

    return Font

def TextSize(Text, Size):
    TMP_QL = QLabel()
    TMP_QL.setText(Text)
    TMP_QL.setFont(SetFont(Size))
    Px_TextSize = TMP_QL.fontMetrics().boundingRect(TMP_QL.text()).width()

    return Px_TextSize