arcpy.management.SelectLayerByAttribute(
    in_layer_or_view=r"Standard Working Data\OwnerParcel",
    selection_type="NEW_SELECTION",
    where_clause="PARCELID = '25005401101010000'",
    invert_where_clause=None
)