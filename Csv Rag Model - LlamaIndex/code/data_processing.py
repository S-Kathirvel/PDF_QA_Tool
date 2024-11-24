import os
import json
from loading_csv import df
from pathlib import Path


tableinfo_dir = "TableInfo"

# Check if the directory already exists using os.path.exists()
if not os.path.exists(tableinfo_dir):
  # Create the directory if it doesn't exist
  os.mkdir(tableinfo_dir)
  print(f"Directory '{tableinfo_dir}' created.")
else:
  print(f"Directory '{tableinfo_dir}' already exists. Using existing directory.")


def _get_tableinfo_with_index(idx: int) -> str:
	results_gen = Path(tableinfo_dir).glob(f"{idx}_*")
	results_list = list(results_gen)
	if len(results_list) == 0:
		return None
	elif len(results_list) == 1:
		path = results_list[0]
		return TableInfo.parse_file(path)
	else:
		raise ValueError(
			f"More than one file matching index: {list(results_gen)}"
		)

table_names = set()
table_infos = []
for idx, df in enumerate(df):
	table_info = _get_tableinfo_with_index(idx)
	if table_info:
		table_infos.append(table_info)
	else:
		# Try to generate table info with program (once)
		num_tries = 1
		while num_tries <= 1:  # Limit to one retry
			df_str = df.head(10).to_string(errors = "coerce")

			table_info = program(
				table_str=df_str,
				exclude_table_name_list=str(list(table_names)),
			)
			table_name = table_info.table_name
			print(f"Processed table: {table_name} (Try {num_tries})")
			if table_name not in table_names:
				table_names.add(table_name)
				break  # Success, exit the loop
			else:
				print(f"Table name {table_name} already exists. Moving to next file.")
				num_tries += 1  # Increment retry count

		# If loop finishes without a break (no success), move to next file
		if num_tries > 1:  # Check if we exhausted the retry
			print(f"Failed to generate unique table name for index {idx}. Skipping.")

		# Save table info only if successful
		if table_info:
			out_file = f"{tableinfo_dir}/{idx}_{table_name}.json"
			json.dump(table_info.dict(), open(out_file, "w"))
			table_infos.append(table_info)
