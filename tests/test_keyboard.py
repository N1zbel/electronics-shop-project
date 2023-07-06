import pytest
from src.keyboard import KeyBoard


def test_init():
    kb = KeyBoard('razer', 9000, 15)
    assert str(kb) == "razer"
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"
