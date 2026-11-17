from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_pricing_response_200_rates import GetPricingResponse200Rates
    from ..models.pricing_tier import PricingTier


T = TypeVar("T", bound="GetPricingResponse200")


@_attrs_define
class GetPricingResponse200:
    """
    Attributes:
        currency (str):
        rates (GetPricingResponse200Rates):
        tiers (list[PricingTier]):
        note (str):
    """

    currency: str
    rates: GetPricingResponse200Rates
    tiers: list[PricingTier]
    note: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        rates = self.rates.to_dict()

        tiers = []
        for tiers_item_data in self.tiers:
            tiers_item = tiers_item_data.to_dict()
            tiers.append(tiers_item)

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "rates": rates,
                "tiers": tiers,
                "note": note,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_pricing_response_200_rates import GetPricingResponse200Rates
        from ..models.pricing_tier import PricingTier

        d = dict(src_dict)
        currency = d.pop("currency")

        rates = GetPricingResponse200Rates.from_dict(d.pop("rates"))

        tiers = []
        _tiers = d.pop("tiers")
        for tiers_item_data in _tiers:
            tiers_item = PricingTier.from_dict(tiers_item_data)

            tiers.append(tiers_item)

        note = d.pop("note")

        get_pricing_response_200 = cls(
            currency=currency,
            rates=rates,
            tiers=tiers,
            note=note,
        )

        get_pricing_response_200.additional_properties = d
        return get_pricing_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
