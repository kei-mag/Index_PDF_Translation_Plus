import webbrowser

from .translator_base import TranslationError, TranslatorBase


class CopyPasteTranslator(TranslatorBase):
    services = {
        "DeepL": "https://www.deepl.com/ja/translator#/{target_lang}/{text}",
        "Google": "https://translate.google.com/?op=translate&tl={target_lang}&text={text}",
        "Microsoft": "https://www.bing.com/translator?to={target_lang}&text={text}",
    }
    def __init__(self, service="DeepL", **kwargs) -> None:
        """
        原文入力済みの翻訳サービスWebページを開き、ユーザーに訳文のペーストを求める。

        Args:
            service (str, optional): 使用する翻訳サービス。"DeepL"，"Google"，"Microsoft"のいずれか、もしくは"custom"を指定可能。デフォルトは"DeepL"。
            url (str, optional): serviceを"custom"にした場合には、翻訳サイトへ遷移するためのURLを指定する。"{source_lang}"，"{target_lang}"，"{text}"の3種類のプレースホルダーを利用可能。
        
        Examples:
            >>> translator = CopyPasteTranslator(service="DeepL")
            >>> translator = CopyPasteTranslator(service="custom", url="https://mytranslator.com/{source_lang}/{target_lang}/{text}")

        Raises:
            ValueError: serviceの指定が不適切だった場合。
        """
        if service in self.services:
            self.url = self.services[service]
        elif service == "custom":
            self.url = kwargs["url"]
        else:
            raise ValueError(f"argument 'service' must be {",".join(self.services.keys())} or custom (with url).")
        super().__init__()
    
    async def translate(self, text: str, target_lang: str, source_lang: str = "EN") -> str:
        url = self.url.replace("{text}", text).replace("{target_lang}", target_lang).replace("{source_lang}", source_lang)
        webbrowser.open(url)
        return input("ここに訳文をペースト：")