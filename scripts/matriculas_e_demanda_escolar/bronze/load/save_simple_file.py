from core.loaders.file_system import CkanDfSaver
from pandas import DataFrame
from typing import Union, Generator
from types import GeneratorType

from config import DATA_FOLDER

PKG = 'demanda-e-matriculas'

class SaveFile:

    def __init__(self,)->None:
        
        self.save_file = CkanDfSaver(pkg=PKG, tier='bronze', data_dir=DATA_FOLDER)

    def match_types(self, data:Union[DataFrame, Generator], metadata:Union[dict, Generator]):

        if type(data) is GeneratorType:
            if not type(metadata) is GeneratorType:
                raise ValueError(f'If passing a generator, both data and metadata must be generators')
        
        if type(data) is DataFrame:
            if not type(metadata) is dict:
                raise ValueError(f'If passing a dataframe, metadata must be dict')

    def save_all(self, metadata:Generator, data:Generator)->list:

        files_saved = []

        while True:
            try:
                df = next(data)
                metadata_instance = next(metadata)
                fsaved = self.save_file(metadata_instance, df)
                files_saved.append(fsaved)
            except StopIteration:
                break
        return files_saved
            
    def save_pipeline(self, data:Union[DataFrame, Generator], metadata:Union[dict, Generator])->Union[list, str]:

        self.match_types(data, metadata)
        if type(data) is GeneratorType:
            return self.save_all(metadata, data)
        else:
            return self.save_file(metadata, data)


    def __call__(self, data:Union[DataFrame, Generator], metadata:Union[dict, Generator])->Union[list, str]:
        return self.save_pipeline(data, metadata)
    

    

    