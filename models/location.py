from pydantic import BaseModel, Field
from typing import Optional


class Location(BaseModel):
    """ Location for the transaction """
    address_line_1: str = Field(
        ...,
        description="Address Line 1"
    )
    address_line_2: Optional[str] = Field(
        None,
        description="Address Line 2 for unit (optional)"
    )
    city: str = Field(
        ...,
        description="City of the location"
    )
    state: str = Field(
        ...,
        description="Province / State"
    )
    postal_code: str = Field(
        ...,
        description="Postal code of the location"
    )
    country: str = Field(
        # TODO
        "US",
        description="Country"
    )
