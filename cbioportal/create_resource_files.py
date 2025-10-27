import polars as pl
import random

PATIENT_FILE = "data_clinical_patient.txt"
SAMPLE_FILE = "data_clinical_sample.txt"
FRACTION = 0.01 # fraction of patients/samples to use
RESOURCE_DEF_FILE = "data_resource_definition.txt"
RESOURCE_PATIENT_FILE = "data_resource_patient.txt"
RESOURCE_SAMPLE_FILE = "data_resource_sample.txt"
RESOURCE_STUDY_FILE = "data_resource_study.txt"
RESOURCE_DEFINITIONS = """RESOURCE_ID\tDISPLAY_NAME\tDESCRIPTION\tRESOURCE_TYPE\tOPEN_BY_DEFAULT\tPRIORITY
PATHOLOGY_SLIDE\tPathology Slide\tThe pathology slide for the sample\tSAMPLE\tTRUE\t1
PATIENT_NOTES\tPatient Notes\tNotes about the patient\tPATIENT\tFALSE\t2
STUDY_SPONSORS\tStudy Sponsors\tSponsors of this study\tSTUDY\tTRUE\t3
CHROMOSCOPE\tChromoscope\tiframe for chromoscope\tSAMPLE\tTRUE\t1
"""
with open(RESOURCE_DEF_FILE, "w") as f:
    f.write(RESOURCE_DEFINITIONS)


patients = pl.read_csv(PATIENT_FILE, separator="\t")["PATIENT_ID"].to_list()
samples_df = pl.read_csv(SAMPLE_FILE, separator="\t")
samples = samples_df["SAMPLE_ID"].to_list()

n_patients = int(len(patients) * FRACTION)
selected_patients = random.sample(patients, n_patients)
n_samples = int(len(samples) * FRACTION)
selected_samples = random.sample(samples, n_samples)

# patient resource file
with open(RESOURCE_PATIENT_FILE, "w") as f:
    f.write("PATIENT_ID\tRESOURCE_ID\tURL\n")
    for i, pid in enumerate(selected_patients):
        url = f"http://fake-url-to-patient-notes-{pid}"
        f.write(f"{pid}\tPATIENT_NOTES\t{url}\n")

# sample resource file
with open(RESOURCE_SAMPLE_FILE, "w") as f:
    f.write("PATIENT_ID\tSAMPLE_ID\tRESOURCE_ID\tURL\n")
    for i, sid in enumerate(selected_samples):
        #find patient for samples
        pid = samples_df.filter(pl.col("SAMPLE_ID") == sid)[0, "PATIENT_ID"]
        url_slide = f"http://fake-url-to-slide-{sid}"
        f.write(f"{pid}\t{sid}\tPATHOLOGY_SLIDE\t{url_slide}\n")
        url_chromo = f"http://fake-url-to-chromoscope-{sid}"
        f.write(f"{pid}\t{sid}\tCHROMOSCOPE\t{url_chromo}\n")

# study resource file
with open(RESOURCE_STUDY_FILE, "w") as f:
    f.write("RESOURCE_ID\tURL\n")
    f.write("STUDY_SPONSORS\thttp://fake-url-to-study-sponsors\n")
