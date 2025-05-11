from abc import ABCMeta, abstractmethod
from typing import Callable


class TranslatorBase(metaclass=ABCMeta):
    """翻訳器のメタクラス"""

    info_provider = None
    """ユーザに情報を提供できます
    
    定義は辞書(マップ)形式で、実行する関数と、実行のトリガーを指定します。詳しくはREADME.mdを参照してください。
    
    Example:
        >>> info_provider = {
            "func": calculate_cost,
            "trigger": "onTextChanged"
        }
        
    Note:
        "func"に指定された関数には以下の情報が渡されます。
        text (str): 入力されているテキスト
        len_char (int): 入力されているテキストの文字数
        len_word (int): 入力されているテキストの単語数
        datetime (datetime): 

    Raises:
        NotImplementedError: 
    """

    @abstractmethod
    async def translate(self, text: str) -> str:
        """
        入力されたテキストを指定の言語に翻訳する非同期関数

        Args:
            text (str): 翻訳するテキスト

        Returns:
            str: 翻訳されたテキスト

        Raises:
            TranslationError: 翻訳リクエストが失敗した場合
        """
        raise NotImplementedError()


class TranslationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
