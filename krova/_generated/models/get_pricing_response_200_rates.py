from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetPricingResponse200Rates")


@_attrs_define
class GetPricingResponse200Rates:
    """
    Attributes:
        vcpu_per_hour (float):
        ram_gb_per_hour (float):
        disk_gb_per_hour (float):
    """

    vcpu_per_hour: float
    ram_gb_per_hour: float
    disk_gb_per_hour: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vcpu_per_hour = self.vcpu_per_hour

        ram_gb_per_hour = self.ram_gb_per_hour

        disk_gb_per_hour = self.disk_gb_per_hour

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vcpuPerHour": vcpu_per_hour,
                "ramGbPerHour": ram_gb_per_hour,
                "diskGbPerHour": disk_gb_per_hour,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        vcpu_per_hour = d.pop("vcpuPerHour")

        ram_gb_per_hour = d.pop("ramGbPerHour")

        disk_gb_per_hour = d.pop("diskGbPerHour")

        get_pricing_response_200_rates = cls(
            vcpu_per_hour=vcpu_per_hour,
            ram_gb_per_hour=ram_gb_per_hour,
            disk_gb_per_hour=disk_gb_per_hour,
        )

        get_pricing_response_200_rates.additional_properties = d
        return get_pricing_response_200_rates

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
