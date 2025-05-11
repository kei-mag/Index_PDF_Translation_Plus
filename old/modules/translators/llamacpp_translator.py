import re

from llama_cpp import Llama

from .translator_base import TranslationError, TranslatorBase

placeholder_pattern = re.compile(r"{([a-zA-Z_]+[a-zA-Z0-9_]*)}")

class LlamaCppTranslator(TranslatorBase):
    model_download_dir = None # Path or None for default
    
    def __init__(self,
                 prompt: str,
                 repo_id: str,
                 filename: str,
                 output_pattern: str = ".*",
                 n: int = -1,
                 temp: float=0.8,
                 repeat_penalty:float = 1,
                 top_p: float = 0.9,
                 **llama_generation_args
                ) -> None:
        """
        llama.cppモデルをllama_cpp_python経由で呼び出して、翻訳を実行する。

        Args:
            prompt (str): llama.cppモデルに与えるプロンプト（下記Notesも参照）
            output_pattern: モデルの出力のどの部分を翻訳結果として使用するかを正規表現で指定する。キャプチャを使用する場合には1個目の括弧内の文字列が使用されます。デフォルトで出力をそのまま翻訳結果として使用します。
            repo_id (str): Hugging Faceのリポジトリ名, "local"を指定することでローカル上のファイルを指定可能
            filename (str): Hugging Faceリポジトリ内のモデルファイル名, もしくはローカル上のモデルファイルのパス
            n (int): モデルが生成する単語数(max_tokens), -1=無限大, -2=文脈が満たされるまで, デフォルト-1
            temp (float): この値を小さくすることで、高い確率の出力が選ばれやすくなり、回答の一貫性が高まる。デフォルト0.8
            repeat_penalty (float): この値を大きくすることで、モデルが繰り返しまたは単調なテキストを生成するのを防ぐのに役立つ。デフォルト1
            top_p (float): この値を小さくすることで、選ばれる回答候補が少なくなり、結果として出力の回答が一貫性を持つようになる。デフォルト0.9
            llama_generation_args (**kwargs): Llama.cppの生成時の他パラメータも指定できます。（参考：https://github.com/ggerganov/llama.cpp/tree/master/examples/main#generation-flags）
            
        Notes:
            prompt内の文字列には{args}形式のプレースホルダーが使用できる。
            次のプレースホルダーは事前定義済み
                `{context}`: 翻訳対象の文章
                `{translation_lang}`: 
            また事前に定義されていない任意の値もプレースホルダーとしてkwargs経由で利用可能
                `{kwargs}`: translate関数で与えられたkwargsに置き換えられる（当該のkwargsが与えられなかった場合は空文字に置き換え）
        """
        super().__init__()
        if repo_id == "local":
            self.model = Llama(model_path=filename)
        else:
            self.model = Llama.from_pretrained(repo_id, filename, local_dir=self.model_download_dir)
        self.prompt = prompt
        self.output_pattern = re.compile(".*")
        self.n = n
        self.temp = temp
        self.repeat_penalty = repeat_penalty
        self.top_p = top_p
        self.other_args = llama_generation_args
        
    async def translate(self, text: str, target_lang: str, source_lang: str = "EN", **kwargs) -> str:
        output = self.model(self.prompt.replace(r"{text}", text),
                   max_tokens=self.n,
                   temperature=self.temp,
                   repeat_penalty=self.repeat_penalty,
                   top_p=self.top_p,
                   echo=False, **self.other_args)
        result = self.output_pattern.search(output["choices"][0]["text"])
        if not result:
            raise TranslationError("モデルの実行は完了しましたが翻訳結果が出力されていません。（output_patternが間違っていませんか？）")
        else:
            groups = result.groups()
            if groups:
                return result.group(1)
            else:
                return result.group(0)
        
    
    def replace_placeholders(self, text, target_lang, source_lang, **kwargs):
        """カスタムプレースホルダーを実際の値に置き換え"""
        prompt = self.prompt
        placeholders = placeholder_pattern.findall(prompt)
        for ph in placeholders:
            if ph[1] in kwargs:
                prompt = prompt.replace(f"{{{ph[1]}}}", "")
            else:
                prompt = prompt.replace(f"{{{ph[1]}}}", kwargs[ph[1]])
        return prompt