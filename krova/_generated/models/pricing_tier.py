from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PricingTier")


@_attrs_define
class PricingTier:
    """
    Attributes:
        min_vcpus (int):
        max_vcpus (int | None):
        multiplier (float):
        label (str):
    """

    min_vcpus: int
    max_vcpus: int | None
    multiplier: float
    label: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_vcpus = self.min_vcpus

        max_vcpus: int | None
        max_vcpus = self.max_vcpus

        multiplier = self.multiplier

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "minVcpus": min_vcpus,
                "maxVcpus": max_vcpus,
                "multiplier": multiplier,
                "label": label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        min_vcpus = d.pop("minVcpus")

        def _parse_max_vcpus(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_vcpus = _parse_max_vcpus(d.pop("maxVcpus"))

        multiplier = d.pop("multiplier")

        label = d.pop("label")

        pricing_tier = cls(
            min_vcpus=min_vcpus,
            max_vcpus=max_vcpus,
            multiplier=multiplier,
            label=label,
        )

        pricing_tier.additional_properties = d
        return pricing_tier

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
