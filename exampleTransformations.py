

unique_values = combined_df['attr_place_subregion'].unique()

filtered_df = combined_df[combined_df['attr_place_subregion'] == 'Tromsø']

print(filtered_df.head(1))
