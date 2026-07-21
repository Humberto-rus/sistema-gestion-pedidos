import pytest
from src.config.configuracion import ConfiguracionSistema


def test_singleton_instancia_unica():
    config1 = ConfiguracionSistema()
    config2 = ConfiguracionSistema()
    assert config1 is config2


def test_singleton_atributos_compartidos():
    config1 = ConfiguracionSistema()
    config2 = ConfiguracionSistema()
    config1.modo = "produccion"
    assert config2.modo == "produccion"