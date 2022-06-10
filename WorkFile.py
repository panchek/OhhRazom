from openpyxl import *

class WorkFile:

    def __init__(self, NameFile):
        self.book = load_workbook(NameFile)


class BodyWork(WorkFile):

    def chooseSheet(self, nameSheet):
        self.sheetWork = self.book.get_sheet_by_name(nameSheet)

    def getElement(self, cell):
        return self.sheetWork[cell].value
