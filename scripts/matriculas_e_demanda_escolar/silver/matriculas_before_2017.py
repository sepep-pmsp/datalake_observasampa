from core.extractors.file_system import DfLoaderGenerator
from pandas import DataFrame

from config import DATA_FOLDER


class MatriculasCleanBefore2017:

    folder = 'demanda_e_matriculas'

    def __init__(self):

        self.load = DfLoaderGenerator(tier='bronze', data_dir=DATA_FOLDER)

    def is_col_matricula(self, col:str)->bool:

        return col.startswith('MAT_') and not 'PROC_' in col

    def get_cols_matricula(self, df:DataFrame)->list:

        cols = []
        for col in df.columns:
            if self.is_col_matricula(col):
                cols.append(col)

        return cols
    
    def clean_col_mat(self, col:str)->str:

        col = col.replace('MAT_', '')
        col = col.lower()

        return col
    

    def clean_other_col(self, col:str)->str:

        col = col.lower()

        return col
    
    def clean_cols(self, df:DataFrame)->str:

        rename_mat = {
            col : self.clean_col_mat(col)
            for col in df.columns if self.is_col_matricula(col)
                }
        
        rename_other = {
            col : self.clean_other_col(col)
            for col in df.columns if not self.is_col_matricula(col)
        }
        
        rename_mat.update(rename_other)

        df.rename(rename_mat, axis=1, inplace=True)
    
    def cols_to_int(self, df:DataFrame, cols_matricula:list)->DataFrame:

        for col in cols_matricula:

            df[col] = df[col].astype(int)

    def subset_cols(self, df:DataFrame, cols_matricula:list)->DataFrame:

        other_cols = ['DISTRITO', 'MES_ANO_REF']

        other_cols.extend(cols_matricula)
        df = df[other_cols].copy()

        return df

    def pipeline(self, df:DataFrame)->DataFrame:

        cols_matricula = self.get_cols_matricula(df)
        df = self.subset_cols(df, cols_matricula)
        self.cols_to_int(df, cols_matricula)

        self.clean_cols(df)

        return df

    def extract_ano(self, df:DataFrame)->None:

        df['ano'] = df['mes_ano_ref'].str.split('-').apply(lambda x: x[1])
        df['ano'] = df['ano'].apply(lambda x: f'20{x}')

        

    def filter_dezembro(self, df:DataFrame)->DataFrame:

        mes = df['mes_ano_ref'].str.split('-').apply(lambda x: x[0])
        mask = mes=='dez'

        return df[mask].copy()

    
    def __call__(self)->DataFrame:

        df = next(self.load(self.folder, extension='.csv', sep=';'))
        df = self.pipeline(df)
        df = self.filter_dezembro(df)
        self.extract_ano(df)
        del df['mes_ano_ref']

        return df

    



        


