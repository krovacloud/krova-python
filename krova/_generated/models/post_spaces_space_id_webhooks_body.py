from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_spaces_space_id_webhooks_body_events_item import (
    PostSpacesSpaceIdWebhooksBodyEventsItem,
)

T = TypeVar("T", bound="PostSpacesSpaceIdWebhooksBody")


@_attrs_define
class PostSpacesSpaceIdWebhooksBody:
    """
    Attributes:
        url (str):
        events (list[PostSpacesSpaceIdWebhooksBodyEventsItem]):
    """

    url: str
    events: list[PostSpacesSpaceIdWebhooksBodyEventsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "events": events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        url = d.pop("url")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = PostSpacesSpaceIdWebhooksBodyEventsItem(events_item_data)

            events.append(events_item)

        post_spaces_space_id_webhooks_body = cls(
            url=url,
            events=events,
        )

        post_spaces_space_id_webhooks_body.additional_properties = d
        return post_spaces_space_id_webhooks_body

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
