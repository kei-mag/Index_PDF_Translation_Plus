"""TransformersとFuguMTを使った英日翻訳

追加の環境構築が必要なため、config.pyで使うとエラーになります。主にサンプルコードとしての側面が強いです。

Note:
    Local_Index_PDF_TranslationのDockerfileには、FuguMTを使うための環境は構築されていません。FuguMTTranslatorを使うにはDockerやご自身のPCに追加の環境構築が必要です。
    環境構築についてはこちらの記事等が参考になります：
    
"""
from .translator_base import TranslatorBase, TranslationError

class FuguMTTranslator(TranslatorBase):
    def __init__(self) -> None:
        super().__init__()
    
    async def translate(self, text: str) -> str:
        return "translated text"