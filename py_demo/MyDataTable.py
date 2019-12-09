import wx.grid as grid

class MyDataTable(grid.PyGridTableBase):
    def __init__(self,data,colLabels=None):
        grid.PyGridTableBase.__init__(self)
        self.colLabels = colLabels
        self.data = data

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data[0])

    def GetValue(self,row,col):
        if self.data[row][col] is None:
            return ''
        else:
            return self.data[row][col]

    def SetValue(self,row,col,value):
        pass

    def GetColLabelValue(self,col):
        if self.colLabels:
            return self.colLabels[col]




class ShowData:
    @classmethod
    def showSqlData(self,data,grid):
        table = MyDataTable(data[1],data[0])
        grid.SetTable(table)
        grid.AutoSize()
        grid.Refresh()