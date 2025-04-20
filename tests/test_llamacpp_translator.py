import pytest

from modules.translators import LlamaCppTranslator


@pytest.mark.asyncio
async def test_translation():
    import config_copy
    translator = config_copy.translators[3]["object"]
    result = await translator.translate("こんにちは", "EN")
    print(f"{result=}")
    assert result != ""