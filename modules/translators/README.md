# カスタム翻訳方法の追加

デフォルトで用意されている翻訳方法以外に、自分で翻訳方法を定義できます。

## 既存のTranslatorを使った翻訳方法の追加
[config.py](../../config.py)の`trasnlators`の欄にTranslatorの定義を追加します。
REST APIを使った翻訳やllama.cppを使った翻訳等は[translatorsディレクトリ](/modules/translators/)内にある各Pythonファイルで定義してあります。それを使えばPythonに不慣れな方でも比較的簡単に新しい翻訳器を追加できると思います。

新しく`translate.example.com`にHTTP GETして翻訳を行う翻訳器を追加する例：
```diff
# ----- Translator 設定 -----
translators = [
    {
        "category": "コピペ翻訳",
        "label": "DeepL Web",
        "description": "deepl.comでPDF中の文章をコピペ翻訳します．",
        "object": CopyAndPasteTranslator(service="DeepL")
    },
    {
        "category": "コピペ翻訳",
        "label": "Google Web",
        "description": "translate.google.comでPDF中の文章をコピペ翻訳します．",
        "object": CopyAndPasteTranslator(service="Google")
    },
    {
        "category": "コピペ翻訳",
        "label": "Microsoft Web",
        "description": "translator.bing.comでPDF中の文章をコピペ翻訳します．",
        "object": CopyAndPasteTranslator(service="Microsoft")
    },
    {
        "category": "ローカルLLM翻訳",
        "label": "C3TR-Adapter-Q4_k_m.gguf",
        "description": "**【必要RAM:8.3GB】**[webbigdata/C3TR-Adapter_gguf](https://huggingface.co/webbigdata/C3TR-Adapter_gguf)",
        "object": LlamaCppTranslator(
            prompt= """You are a highly skilled professional Japanese-English and English-Japanese translator. Translate the given text accurately, taking into account the context and specific instructions provided. Steps may include hints enclosed in square brackets [] with the key and value separated by a colon:. Only when the subject is specified in the Japanese sentence, the subject will be added when translating into English. If no additional instructions or context are provided, use your expertise to consider what the most appropriate context is and provide a natural translation that aligns with that context. When translating, strive to faithfully reflect the meaning and tone of the original text, pay attention to cultural nuances and differences in language usage, and ensure that the translation is grammatically correct and easy to read. After completing the translation, review it once more to check for errors or unnatural expressions. For technical terms and proper nouns, either leave them in the original language or use appropriate translations as necessary. Take a deep breath, calm down, and start translating.
            <start_of_turn>### Instruction:
            <<Translate Japanese to English. or Translate English to Japanese.>>
            When translating, please use the following hints:
            writing_style: academic-presentation
            
            ### Input:
            {context}
            
            <end_of_turn>
            <start_of_turn>### Response:
            """,
            model_path="C3TR-Adapter.f16.Q4_k_m.gguf",
            temperature=
            
        )
    },
    # さらに独自の翻訳方法を追加できます。
    # フォーマット:
    # {
    #     "category": "GUIでひとまとまりとして表示されるカテゴリを指定します（省略可）"
    #     "label": "GUIで表示される翻訳方法の名前（Markdownに対応）",
    #     "description": "翻訳方法の説明（Markdownに対応）",
    #     "object": 実際に呼び出すPythonオブジェクト（上記の翻訳器は `modules/translators` で定義されています）
    # },
+   {
+       "label": "[translate.example.com](https://translate.example.com)で翻訳",
+       "description": "APIにHTTP GETリクエストを送信して翻訳します。",
+       "object": RestAPITranslator(
+           url="translate.example.com",
+           body={
+               "text": "{text}",
+               "target_language": "en",
+               "translation_language": "ja"
+           }
+       )
+   }
]
```

## カスタムTranslatorクラスの定義
[translatorsディレクトリ](/modules/translators/)内にある各翻訳器では対応できないような翻訳方法を追加したい場合、あなたにPythonの文法知識があれば独自のTranslatorを作ることができます。

例えば、新しいTranslatorクラス`MyTranslator`を作る場合は以下のような手順になります：
1. `modules/translators/`に新規のPythonファイルを作成します。（ここでは`mytranslator.py`）
2. `mytranslator.py`に`TranslatorBase`を継承した`MyTranslator`を定義します。
    ```python
    from .translator_base import TranslatorBase, TranslationError

    class MyTranslator(TranslatorBase):
        def __init__(self) -> None:

            super().__init__()
    
        async def translate(self, text: str) -> str:
            ... # 英語テキスト(text)を日本語に翻訳する処理
            return "translated text"
    ```
3. [modules/translators/\_\_init\_\_.py](/modules/translators/__init__.py)に作成した`MyTranslator`のimportステートメントを追加します。
   ```diff
        from .copy_paste_translator import *
        from .llamacpp_translator import *
        from .rest_api_translator import *
   +    from .mytranslator import *
    ```
4. [既存のTranslatorを使った翻訳方法の追加](#既存のtranslatorを使った翻訳方法の追加)の場合と同じように[config.py](/config.py)にMyTranslatorを使った翻訳方法を追加します。
    ```python
    {
        "category": "自分で追加したTranslator",
        "label": "MyTranslator",
        "description": "定義はmytranslator.pyにある",
        "object": MyTranslator
    }
    ```

### Translatorクラスの仕様
#### フィールド
1. info_provider
   - 型： a
   - 以下のようなdictを指定することで追加情報を提示できます。
        ```python
        {
            "func": function,
            "trigger": "onChanged or onStart"
        }
        ```
#### trigger
| 値 | a |
| --- |

#### 関数
