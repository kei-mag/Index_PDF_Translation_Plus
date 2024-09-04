from translator_base import TranslatorBase, TranslationError

class LlamaCppTranslator(TranslatorBase):
    def __init__(self) -> None:
        super().__init__()
        
    async def translate(self, text: str, target_lang: str, source_lang: str = "EN") -> str:
        raise TranslationError("Failed to translate text with llama.cpp model")
        return "Not Implemented"