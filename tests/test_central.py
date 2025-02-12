"""Test the HaHomematic central."""
from typing import Any
from unittest.mock import patch

from conftest import get_value_from_generic_entity, send_device_value_to_ccu
import pytest

from hahomematic.helpers import get_device_address


@pytest.mark.asyncio
async def test_central(central, loop) -> None:
    """Test the central."""
    assert central
    assert central.instance_name == "ccu-dev"
    assert central.model == "PyDevCCU"
    assert central.version == "pydevccu 0.0.9"
    assert central.clients["ccu-dev-hm"].model == "PyDevCCU"
    assert central.get_primary_client().model == "PyDevCCU"
    assert len(central.hm_devices) == 294
    assert len(central.hm_entities) == 2650


@pytest.mark.asyncio
async def test_device_set_data(central, pydev_ccu, loop) -> None:
    """Test callback."""
    assert central
    assert pydev_ccu
    old_value = await get_value_from_generic_entity(
        central, "VCU6354483:1", "SET_POINT_TEMPERATURE"
    )
    assert old_value is None
    send_device_value_to_ccu(pydev_ccu, "VCU6354483:1", "SET_POINT_TEMPERATURE", 19.0)
    new_value = await get_value_from_generic_entity(
        central, "VCU6354483:1", "SET_POINT_TEMPERATURE"
    )
    assert new_value == 19.0
