class Stocks():
    def __init__(self):
        self._stock_list = {'CSNA3': 9.06, 'RADL3': 61.70, 'BVMF3': 17.50, 'MULT3': 60.22,
            'SBSP3': 29.09, 'CPFE3': 22.10, 'BBDC4': 25.70, 'BRML3': 12.62, 'BBDC3': 26.85,
            'EQTL3': 49.07, 'CSAN3': 34.29, 'PETR4': 9.50, 'SMLE3': 46.42, 'LREN3': 24.23,
            'KROT3': 13.57, 'PETR3': 11.69, 'USIM5': 2.07, 'CMIG4': 7.56, 'QUAL3': 18.00, 
            'MRVE3': 11.39}

    def get_stocks(self):
        return self._stock_list

def return_stocks():
    stocks = Stocks()
    return stocks.get_stocks()