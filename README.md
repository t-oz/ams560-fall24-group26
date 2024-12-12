# ams560-fall24-group26

**Step 1: Setup MIMIC-SPARQL and get access to MIMIC data**

Follow the instructions here: https://github.com/junwoopark92/mimic-sparql to get access to MIMIC and download the code we modified to create our system.

**Step 2: Build MIMIC-IV Database**

The MIMIC-SPARQL system is based on MIMIC-III, but we use MIMIC-IV, so you need to use the import script here: https://github.com/MIT-LCP/mimic-code/tree/main/mimic-iv/buildmimic/sqlite to create a SQLITE database from the raw CSV files.

**Step 3: Build simple and/or complex knowledge graphs**

In build_{complex|simple}_kg_mimic4.py, modify the paths to the MIMIC-IV SQLITE database and patient IDs CSV file to suit your specific setup. We included the patient ID CSVs for ease of use, but you can extract others manually if you'd prefer.
