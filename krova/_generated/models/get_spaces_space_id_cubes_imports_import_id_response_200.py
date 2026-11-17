from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_spaces_space_id_cubes_imports_import_id_response_200_import import (
        GetSpacesSpaceIdCubesImportsImportIdResponse200Import,
    )


T = TypeVar("T", bound="GetSpacesSpaceIdCubesImportsImportIdResponse200")


@_attrs_define
class GetSpacesSpaceIdCubesImportsImportIdResponse200:
    """
    Attributes:
        import_ (GetSpacesSpaceIdCubesImportsImportIdResponse200Import | Unset):
    """

    import_: GetSpacesSpaceIdCubesImportsImportIdResponse200Import | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        import_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.import_, Unset):
            import_ = self.import_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if import_ is not UNSET:
            field_dict["import"] = import_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_spaces_space_id_cubes_imports_import_id_response_200_import import (
            GetSpacesSpaceIdCubesImportsImportIdResponse200Import,
        )

        d = dict(src_dict)
        _import_ = d.pop("import", UNSET)
        import_: GetSpacesSpaceIdCubesImportsImportIdResponse200Import | Unset
        if isinstance(_import_, Unset):
            import_ = UNSET
        else:
            import_ = GetSpacesSpaceIdCubesImportsImportIdResponse200Import.from_dict(
                _import_
            )

        get_spaces_space_id_cubes_imports_import_id_response_200 = cls(
            import_=import_,
        )

        get_spaces_space_id_cubes_imports_import_id_response_200.additional_properties = d
        return get_spaces_space_id_cubes_imports_import_id_response_200

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
