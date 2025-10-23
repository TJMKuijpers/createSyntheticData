import polars as pl
import random
from utils import get_patient_or_sample_identifiers
EXAMPLE_TIMELINE_FILE = "example_data/data_timeline_treatment_msk_chord_2024.txt"
PATIENT_FILE = "data_clinical_patient.txt"
OUTPUT_FILE = "data_timeline_treatment.txt"

def main():
    patient_ids = get_patient_or_sample_identifiers(PATIENT_FILE, sep='\t', select_column='PATIENT_ID')["PATIENT_ID"].to_list()
    timeline_df = pl.read_csv(EXAMPLE_TIMELINE_FILE, separator="\t")
    min_treatments = 1
    max_treatments = 3


    all_rows = []
    for pid in patient_ids:
        n_treatments = random.randint(min_treatments, max_treatments)
        sampled = timeline_df.sample(n_treatments, with_replacement=True).with_columns([
            pl.lit(pid).alias("PATIENT_ID")
        ])
        all_rows.append(sampled)

    result_df = pl.concat(all_rows)
    result_df.write_csv(OUTPUT_FILE, separator="\t")
    print(f"Wrote {result_df.height} rows to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
