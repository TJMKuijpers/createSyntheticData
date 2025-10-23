import polars as pl
import argparse
from utils import get_patient_or_sample_identifiers, replace_sample_ids, duplicate_rows, add_custom_namespace_cols


def main():
    parser = argparse.ArgumentParser(description="Create synthetic mutation or SV data from an example file.")
    parser.add_argument("--example_file", required=True, help="Path to example input file (MAF or SV)")
    parser.add_argument("--sample_file", default="data_clinical_sample.txt", help="Path to clinical sample file")
    parser.add_argument("--output_file", required=True, help="Path to output file")
    parser.add_argument("--sample_col", default="Sample_Id", help="Column name for sample IDs in the example file")
    parser.add_argument("--duplicate_fraction", type=float, default=3, help="Fraction of rows to duplicate")
    args = parser.parse_args()

    df = pl.read_csv(args.example_file, separator="\t")
    sample_ids = get_patient_or_sample_identifiers(args.sample_file,sep='\t', select_column='SAMPLE_ID')["SAMPLE_ID"].to_list()
    if args.sample_col not in df.columns:
        raise ValueError(f"{args.sample_col} column not found in example file.")
    df = replace_sample_ids(df, sample_ids, sample_col=args.sample_col)
    df = duplicate_rows(df, args.duplicate_fraction)
    df = add_custom_namespace_cols(df)
    df.write_csv(args.output_file, separator="\t")
    print(f"Wrote {df.height} rows to {args.output_file}")

if __name__ == "__main__":
    main()
