"""Platform for light integration"""
from __future__ import annotations
import sys
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import DOMAIN

sys.path.append("custom_components/new_light")
from new_light import NewLight

ceiling_entity = "light.logan_s_room_ceiling_group"
lamps_entity = "light.logan_s_room_lamps_group"
# light_entity = "light.logans_room_group"
# strip_entity = "light.logans_light_strip"
# lamp_entity = "light.repeater_test_lamp"


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the light platform."""
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return
    ent = LogansRoomLight()
    add_entities([ent])


class LogansRoomLight(NewLight):
    """LogansRoom Light."""

    def __init__(self) -> None:
        """Initialize LogansRoom Light."""
        super(LogansRoomLight, self).__init__(
            "Logan's Room", domain=DOMAIN, debug=False, debug_rl=False
        )
        self.entities[lamps_entity] = None
        self.entities[ceiling_entity] = None
        self.entities_below_threshold = [lamps_entity]
        self.entities_above_threshold = [ceiling_entity]
        self.has_brightness_threshold = True
        self.switch = "Logan's Switch"
