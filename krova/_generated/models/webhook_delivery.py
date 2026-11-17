from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.webhook_delivery_status import WebhookDeliveryStatus

T = TypeVar("T", bound="WebhookDelivery")


@_attrs_define
class WebhookDelivery:
    """
    Attributes:
        id (str):
        event (str):
        status (WebhookDeliveryStatus):
        attempts (int):
        last_attempt_at (datetime.datetime | None):
        response_status (int | None):
        created_at (datetime.datetime):
    """

    id: str
    event: str
    status: WebhookDeliveryStatus
    attempts: int
    last_attempt_at: datetime.datetime | None
    response_status: int | None
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        event = self.event

        status = self.status.value

        attempts = self.attempts

        last_attempt_at: None | str
        if isinstance(self.last_attempt_at, datetime.datetime):
            last_attempt_at = self.last_attempt_at.isoformat()
        else:
            last_attempt_at = self.last_attempt_at

        response_status: int | None
        response_status = self.response_status

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "event": event,
                "status": status,
                "attempts": attempts,
                "lastAttemptAt": last_attempt_at,
                "responseStatus": response_status,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        event = d.pop("event")

        status = WebhookDeliveryStatus(d.pop("status"))

        attempts = d.pop("attempts")

        def _parse_last_attempt_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_attempt_at_type_0 = isoparse(data)

                return last_attempt_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_attempt_at = _parse_last_attempt_at(d.pop("lastAttemptAt"))

        def _parse_response_status(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        response_status = _parse_response_status(d.pop("responseStatus"))

        created_at = isoparse(d.pop("createdAt"))

        webhook_delivery = cls(
            id=id,
            event=event,
            status=status,
            attempts=attempts,
            last_attempt_at=last_attempt_at,
            response_status=response_status,
            created_at=created_at,
        )

        webhook_delivery.additional_properties = d
        return webhook_delivery

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
