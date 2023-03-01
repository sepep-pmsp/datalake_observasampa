from .transform.matriculas_before_2017 import MatriculasCleanBefore2017
from .transform.matriculas_from_2017 import MatriculasCleanFrom2017

from core.loaders.file_system import DfSaver

from config import DATA_FOLDER

import pandas as pd

def pseudoDag():

    before = MatriculasCleanBefore2017()
    df1 = before()

    after = MatriculasCleanFrom2017()
    df2 = after()

    df_final = pd.concat([df1, df2])

    save = DfSaver(tier='silver', folder='demanda_e_matriculas', data_dir=DATA_FOLDER)

    save(df_final, 'historico_matriculas_anual', how='csv', index=False, sep=';')

