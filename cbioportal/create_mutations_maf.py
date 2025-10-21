import polars as pl
import random


EXAMPLE_MUTATIONS_FILE = "example_data/data_mutations_msk_ch_2023.txt"
SAMPLE_FILE = "data_clinical_sample.txt"
OUTPUT_FILE = "data_mutations.txt"

# Fraction/integer to duplicate the sample mutations rows
DUPLICATE_FRACTION = 4

CUSTOM_NAME_OPTIONS = ["custom_annotation_1", "custom_annotation_2", ""]
CUSTOM_TYPE_OPTIONS = ["custom_type_1", "custom_type_2", ""]


def get_sample_ids(sample_file):
    df = pl.read_csv(sample_file, separator="\t")
    return df["SAMPLE_ID"].to_list()

def main():
    mutations_df = pl.read_csv(EXAMPLE_MUTATIONS_FILE, separator="\t")
    sample_ids = get_sample_ids(SAMPLE_FILE)
    n_samples = len(sample_ids)
    n_mutations = mutations_df.height

    # Replace Tumor_Sample_Barcode with sample IDs, recycle if needed
    if "Tumor_Sample_Barcode" not in mutations_df.columns:
        raise ValueError("Tumor_Sample_Barcode column not found in example mutations file.")
    mutations_df = mutations_df.with_columns([
        pl.Series("Tumor_Sample_Barcode", [sample_ids[i % n_samples] for i in range(n_mutations)])
    ])

    n_duplicate = int(DUPLICATE_FRACTION * n_mutations)
    if n_duplicate > 0:
        duplicate_rows = mutations_df.sample(n_duplicate, with_replacement=True)
        mutations_df = pl.concat([mutations_df, duplicate_rows])
        mutations_df = mutations_df.sample(mutations_df.height, shuffle=True)

    # Add custom annotation columns
    custom_name_col = [random.choice(CUSTOM_NAME_OPTIONS) for _ in range(mutations_df.height)]
    custom_type_col = [random.choice(CUSTOM_TYPE_OPTIONS) for _ in range(mutations_df.height)]
    mutations_df = mutations_df.with_columns([
        pl.Series("CUSTOM.name", custom_name_col),
        pl.Series("CUSTOM.type", custom_type_col)
    ])

    mutations_df.write_csv(OUTPUT_FILE, separator="\t")
    print(f"Wrote {mutations_df.height} rows to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
