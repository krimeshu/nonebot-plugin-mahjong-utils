"""Regression coverage for the vendored engine under Pydantic v2."""


def test_v2_plugin_config():
    from pydantic import BaseModel

    from nonebot_plugin_mahjong_utils.config import Config

    config = Config.model_validate(
        {
            "mahjong_utils_send_image": "false",
            "mahjong_utils_sniff_mode": "false",
            "mahjong_utils_command_mode": "true",
            "unrelated_plugin_setting": "ignored",
        }
    )
    assert isinstance(config, BaseModel)
    assert config.mahjong_utils_send_image is False
    assert config.mahjong_utils_sniff_mode is False
    assert config.mahjong_utils_command_mode is True
    assert "unrelated_plugin_setting" not in config.model_dump()


def test_vendored_furo_analysis():
    from nonebot_plugin_mahjong_utils._vendor.mahjong_utils.models.tatsu import Tatsu
    from nonebot_plugin_mahjong_utils._vendor.mahjong_utils.models.tile import (
        Tile,
        parse_tiles,
    )
    from nonebot_plugin_mahjong_utils._vendor.mahjong_utils.shanten import (
        furo_chance_shanten,
    )

    tiles = parse_tiles("3456778m123457p")
    chance = Tile.by_text("7m")
    result = furo_chance_shanten(tiles, chance)
    assert result.shanten == 0
    assert result.shanten_info.chi[Tatsu.parse("68m")].shanten == 0
    assert result.shanten_info.pon.shanten == 1
    assert result.shanten_info.pass_.shanten == 1

    # A discard from across the table must not offer chi.
    result = furo_chance_shanten(tiles, chance, allow_chi=False)
    assert not result.shanten_info.chi
    assert result.shanten_info.pon.shanten == 1


def test_vendored_hora_with_furo():
    from nonebot_plugin_mahjong_utils._vendor.mahjong_utils.hora import build_hora
    from nonebot_plugin_mahjong_utils._vendor.mahjong_utils.models.furo import Furo
    from nonebot_plugin_mahjong_utils._vendor.mahjong_utils.models.tile import (
        Tile,
        parse_tiles,
    )
    from nonebot_plugin_mahjong_utils._vendor.mahjong_utils.models.wind import Wind
    from nonebot_plugin_mahjong_utils._vendor.mahjong_utils.yaku.common import (
        round_wind,
        self_wind,
    )

    hora = build_hora(
        tiles=parse_tiles("12233466m111z"),
        furo=[Furo.parse("789p")],
        agari=Tile.by_text("1z"),
        tsumo=True,
        dora=4,
        self_wind=Wind.east,
        round_wind=Wind.east,
    )
    assert hora.yaku == {self_wind, round_wind}
    assert (hora.han, hora.hu) == (6, 30)
    assert hora.parent_point == (0, 6000)
    assert hora.child_point == (0, 6000, 3000)
