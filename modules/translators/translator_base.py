from abc import ABCMeta, abstractmethod


class TranslatorBase (metaclass=ABCMeta):
    @abstractmethod
    async def translate(self, text: str, target_lang: str, source_lang: str = "EN") -> str:
        """
        入力されたテキストを指定の言語に翻訳する非同期関数。

        Args:
            text (str): 翻訳するテキスト。
            target_lang (str): 翻訳先の言語コード（例: "EN", "JA", "FR"など）。
            source_lang (str, optional): 翻訳するテキストの言語コード（例: "EN", "JA", "FR"など）。デフォルトは"EN"。

        Returns:
            str: 翻訳されたテキスト。

        Raises:
            TranslationError: 翻訳リクエストが失敗した場合。
        """
        raise NotImplementedError()

class TranslationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)