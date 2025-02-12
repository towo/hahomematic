"""
Module for entities implemented using the
number platform (https://www.home-assistant.io/integrations/number/).
"""
from __future__ import annotations

import logging
from typing import Any

from hahomematic.const import ATTR_HM_VALUE, HmPlatform
import hahomematic.device as hm_device
from hahomematic.entity import GenericEntity

_LOGGER = logging.getLogger(__name__)


class HmNumber(GenericEntity[float]):
    """
    Implementation of a number.
    This is a default platform that gets automatically generated.
    """

    def __init__(
        self,
        device: hm_device.HmDevice,
        unique_id: str,
        address: str,
        parameter: str,
        parameter_data: dict[str, Any],
    ):
        super().__init__(
            device=device,
            unique_id=unique_id,
            address=address,
            parameter=parameter,
            parameter_data=parameter_data,
            platform=HmPlatform.NUMBER,
        )

    async def set_state(self, value: float) -> None:
        """Set the state of the entity."""
        # pylint: disable=no-else-return
        if value is not None and self._min <= value <= self._max:
            await self.send_value(value)
            return
        elif self._special:
            if [sv for sv in self._special.values() if value == sv[ATTR_HM_VALUE]]:
                await self.send_value(value)
                return
        _LOGGER.error(
            "number: Invalid value: %s (min: %s, max: %s, special: %s)",
            value,
            self._min,
            self._max,
            self._special,
        )
