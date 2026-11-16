from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.backup_config_domains_item import BackupConfigDomainsItem
    from ..models.backup_config_tcp_ports_item import BackupConfigTcpPortsItem


T = TypeVar("T", bound="BackupConfig")


@_attrs_define
class BackupConfig:
    """The Cube configuration captured with the backup, used by redeploy. A shared copy carries no domains.

    Attributes:
        vcpus (float | None):
        ram_mb (int | None):
        disk_limit_gb (int | None):
        image_id (None | str):
        region_id (None | str):
        region_name (None | str):
        domains (list[BackupConfigDomainsItem]):
        tcp_ports (list[BackupConfigTcpPortsItem]):
    """

    vcpus: float | None
    ram_mb: int | None
    disk_limit_gb: int | None
    image_id: None | str
    region_id: None | str
    region_name: None | str
    domains: list[BackupConfigDomainsItem]
    tcp_ports: list[BackupConfigTcpPortsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vcpus: float | None
        vcpus = self.vcpus

        ram_mb: int | None
        ram_mb = self.ram_mb

        disk_limit_gb: int | None
        disk_limit_gb = self.disk_limit_gb

        image_id: None | str
        image_id = self.image_id

        region_id: None | str
        region_id = self.region_id

        region_name: None | str
        region_name = self.region_name

        domains = []
        for domains_item_data in self.domains:
            domains_item = domains_item_data.to_dict()
            domains.append(domains_item)

        tcp_ports = []
        for tcp_ports_item_data in self.tcp_ports:
            tcp_ports_item = tcp_ports_item_data.to_dict()
            tcp_ports.append(tcp_ports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vcpus": vcpus,
                "ramMb": ram_mb,
                "diskLimitGb": disk_limit_gb,
                "imageId": image_id,
                "regionId": region_id,
                "regionName": region_name,
                "domains": domains,
                "tcpPorts": tcp_ports,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.backup_config_domains_item import BackupConfigDomainsItem
        from ..models.backup_config_tcp_ports_item import BackupConfigTcpPortsItem

        d = dict(src_dict)

        def _parse_vcpus(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        vcpus = _parse_vcpus(d.pop("vcpus"))

        def _parse_ram_mb(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ram_mb = _parse_ram_mb(d.pop("ramMb"))

        def _parse_disk_limit_gb(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        disk_limit_gb = _parse_disk_limit_gb(d.pop("diskLimitGb"))

        def _parse_image_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_id = _parse_image_id(d.pop("imageId"))

        def _parse_region_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        region_id = _parse_region_id(d.pop("regionId"))

        def _parse_region_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        region_name = _parse_region_name(d.pop("regionName"))

        domains = []
        _domains = d.pop("domains")
        for domains_item_data in _domains:
            domains_item = BackupConfigDomainsItem.from_dict(domains_item_data)

            domains.append(domains_item)

        tcp_ports = []
        _tcp_ports = d.pop("tcpPorts")
        for tcp_ports_item_data in _tcp_ports:
            tcp_ports_item = BackupConfigTcpPortsItem.from_dict(tcp_ports_item_data)

            tcp_ports.append(tcp_ports_item)

        backup_config = cls(
            vcpus=vcpus,
            ram_mb=ram_mb,
            disk_limit_gb=disk_limit_gb,
            image_id=image_id,
            region_id=region_id,
            region_name=region_name,
            domains=domains,
            tcp_ports=tcp_ports,
        )

        backup_config.additional_properties = d
        return backup_config

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
