from datetime import datetime
from pandas import DataFrame
from typing import Generator, Union, Callable
from core.extractors.ckan_api_reader import Ckan


class ExtractXlsFrom2017:
    '''Extract data from 2017. Earlier data must use other class'''
    
    domain = 'http://dados.prefeitura.sp.gov.br/api/3'
    pkg = 'demanda-e-matriculas'
    earliest_year = 2017
    accepted_extraction_types = {'all', 'latest', 'current'}
    
    def __init__(self):
        
        self.ckan = Ckan(self.domain)
        
    def get_resources(self, regex:str, extract:bool=False)->Generator:
        
        resources = self.ckan(
                    self.pkg,
                    format_=['XLS', 'XLSX'],
                    search_string=regex,
                    how='regex',
                    attr='name',
                    case_sensitive=True,
                    extract=extract,
                )
        
        return resources
        
    def lst_all_resources(self, extract:bool=False)->Generator:
        
        return self.get_resources('Dez/\d{4}', extract)
    
    @property
    def current_year(self)->int:
        
        return datetime.now().year
    
    def get_current_resource(self, extract:bool=False)->Union[DataFrame, dict]:
        
        regex = f'Dez/{self.current_year}'
        return next(self.get_resources(regex, extract))
    
    def get_latest_resource(self, extract:bool=False)->Union[DataFrame, dict]:
        
        year = self.current_year
        while year >= self.earliest_year:
            regex = f'Dez/{year}'
            resource = self.get_resources(regex, extract)
            try:
                resource = next(resource)
                return resource
            except StopIteration:
                year -=1
        return None
    
    @property
    def extract_type_mapper(self):
        
        mapper = {
            'latest' : self.get_latest_resource,
            'current' : self.get_current_resource,
            'all' : self.lst_all_resources
        } 
        
        return mapper
    
    def solve_extraction(self, extraction_type:str)->Callable:
        
        if extraction_type not in self.accepted_extraction_types:
            raise ValueError(f'extraction_type must be in {self.accepted_extraction_types}')
        
        return self.extract_type_mapper[extraction_type]
    
    def __call__(self, how:str, extract:bool=False)->Union[DataFrame, dict, Generator]:
        
        extract_func = self.solve_extraction(how)
        
        return extract_func(extract)