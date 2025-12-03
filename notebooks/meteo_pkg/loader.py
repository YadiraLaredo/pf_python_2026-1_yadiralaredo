import pandas as pd

class MeteoLoader:
    def __init__(self, path_parquet, rename_dict=None):

        self.df = pd.read_parquet(path_parquet)

        if rename_dict is not None:
            self.df = self.df.rename(columns=rename_dict)

        if not isinstance(self.df.index, pd.DatetimeIndex):
            self.df.index = pd.to_datetime(self.df.index)

        self.inicio = self.df.index.min()
        self.fin = self.df.index.max()

        self.cantidad = len(self.df)

    @property
    def columnas(self):
        """Regresa lista de columnas actuales."""
        return list(self.df.columns)

    def info(self):
        print("Inicio:", self.inicio)
        print("Final :", self.fin)
        print("Cantidad de datos:", self.cantidad)
        print("Columnas:", ", ".join(self.columnas))
