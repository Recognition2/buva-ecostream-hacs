"""Ecostream API Client."""

import aiohttp


class EcostreamApiClientError(Exception):
    """Exception to indicate general API error."""


class EcostreamApiClient:
    """The actual Ecostream client."""

    def __init__(
        self,
        ipaddr: str,
        session: aiohttp.ClientSession,
    ) -> None:
        """Actual Ecostream client."""
        self._ipaddr = ipaddr
        self._session = session

    async def async_get_data(self) -> any:
        """Get data from API."""
        return {"ONZIN": "DINGEN"}

    async def async_set_title(self, value: str) -> any:
        return {"OK": "True"}
