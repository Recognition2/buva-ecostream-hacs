"""Add config flow for Buva Ecostream."""


import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers import selector
from homeassistant.const import CONF_IP_ADDRESS
from homeassistant.helpers.aiohttp_client import async_create_clientsession

from .api import (
    EcostreamApiClient,
    EcostreamApiClientError,
)

from .const import DOMAIN, LOGGER


class BuvaEcostreamFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for BuvaEcostream."""

    VERSION = 1

    async def async_step_user(
        self,
        user_input: dict | None = None,
    ) -> config_entries.FlowResult:
        """Handle a flow initialized by the user."""
        _errors = {}
        if user_input is not None:
            return self.async_create_entry(
                title=user_input[CONF_IP_ADDRESS], data=user_input
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_IP_ADDRESS,
                        default=(user_input or {}).get(CONF_IP_ADDRESS),
                    ): selector.TextSelector(
                        selector.TextSelectorConfig(type=selector.TextSelectorType.TEXT)
                    )
                }
            ),
            errors=_errors,
        )

    async def _test_ip_address(self, ip_address: str) -> None:
        """Check IP address."""
        client = EcostreamApiClient(
            ipaddr=ip_address, session=async_create_clientsession(self.hass)
        )
        await client.async_get_data()
