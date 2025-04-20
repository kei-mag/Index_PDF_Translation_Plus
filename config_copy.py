"""Local_Index_PDF_Translation設定ファイル


"""

import os

from modules.translators import *

default_output_folder_path = "./output/"

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
            repo_id="webbigdata/C3TR-Adapter_gguf",
            filename="C3TR-Adapter-Q4_k_m.gguf",
            n=-2,
            temp=0,
            repeat_penalty=1.0,
            # top_p=0.75
        )
    },
    # さらに独自の翻訳方法を追加できます。
    # フォーマット:
    # {
    #     "category": "GUIでひとまとまりとして表示されるカテゴリを指定します（省略可）"
    #     "label": "GUIで表示される翻訳方法の名前（Markdownに対応）",
    #     "description": "翻訳方法の説明（Markdownに対応）",
    #     "object": 実際に呼び出すPythonオブジェクト（上記の翻訳器は `modules/translators` で定義されています）
    # }
]



# ----- 以下 API用 設定 --------

# 接続許可リスト
CORS_CONFIG = [
    'https://indqx-demo-front.onrender.com',
    'http://localhost:5173'
]

#URLリスト
URL_LIST = {
    'papers_link':'https://indqx-demo-front.onrender.com/abs/'
}

# 翻訳設定
TRANSLATION_CONFIG = {
    'ALLOWED_LANGUAGES':['en', 'ja']
}

#token 計算用
SPACY_CONFIG = {
    'supported_languages': {
        'en': 'en_core_web_sm',
        'ja': 'ja_core_news_sm'
        }
}

# デバッグ用ファイル位置
Debug_folder_path = "./debug/"
bach_process_path = "./Test Bench/result/"
