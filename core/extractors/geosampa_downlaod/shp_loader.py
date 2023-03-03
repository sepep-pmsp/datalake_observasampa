from io import BytesIO
from tempfile import TemporaryDirectory
import geopandas as gpd

from core.utils.file_path import list_files_recursive
from core.utils.io import download_binary_file, unzip_file


class ShpDownloader:
    
    
    domain = 'http://download.geosampa.prefeitura.sp.gov.br/PaginasPublicas/'


    def __init__(self):

        self.tmp_folder = TemporaryDirectory()
        
    def get_file_uri(self, camada_name:str)->str:

        uri = f'downloadArquivo.aspx?orig=DownloadCamadas&arq={camada_name}&arqTipo=Shapefile'

        return self.domain + uri
    
    def download_shp_zip(self, uri:str)->BytesIO:

        content = download_binary_file(uri)

        return BytesIO(content)
    
    def unzip_to_tmp_folder(self, zipped_content:BytesIO)->None:

        unzip_file(zipped_content, self.tmp_folder.name)
    
    
    def get_shape_path(self)->str:

        shps = list_files_recursive(self.tmp_folder.name, '.shp')

        return shps[0]
    
    def open_shp(self, shp_path:str)->gpd.GeoDataFrame:

        return gpd.read_file(shp_path)
    
    def empty_folder(self):

        self.tmp_folder.cleanup()

    def pipe_download_shp(self, camada_name:str)->gpd.GeoDataFrame:

        uri = self.get_file_uri(camada_name)
        zip_bytes = self.download_shp_zip(uri)
        self.unzip_to_tmp_folder(zip_bytes)

        shp_path = self.get_shape_path()
        print(shp_path)
        geodf = self.open_shp(shp_path)
        
        #self.empty_folder()

        return geodf


    def __call__(self, camada_name:str)->None:

        return self.pipe_download_shp(camada_name)