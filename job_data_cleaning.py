""" Clean up the scraped jobs so that you can effectively categorise them later """

import pandas as pd

# Pull in the scraped jobs as a dataframe
scraped_csv = pd.read_csv('scraped_jobs.csv')
scraped_jobs = pd.DataFrame(scraped_csv)

# Remove all rows with a missing value (job title, location, etc), then reset the index
scraped_jobs.dropna(how='any', axis=0, inplace=True)
scraped_jobs.reset_index(drop=True, inplace=True)

# Get all the locations in title case
scraped_jobs['Title Location'] = scraped_jobs['Location'].str.title()

# Remove mentions of New York and New South Wales (they mess up location mapping)
scraped_jobs['Title Location'] = scraped_jobs['Title Location'].str.replace("New York", "").str.replace("New South Wales", "")

# Change to "Manchester" if location is "Sale" or "Bury" (they mess up location mapping)
# Create a boolean mask, then update the values for rows where the mask is True
mask = scraped_jobs['Title Location'].isin(["Sale", "Bury"])
scraped_jobs.loc[mask, 'Title Location'] = "Manchester"


# Tidy up the scraped job titles

# Remove references included in job titles
scraped_jobs['Job Title'] = [
    i.split("Ref :")[0] for i in scraped_jobs['Job Title']
]
# Tidy up hyphens
scraped_jobs['Job Title'] = [
    i.replace("- ", " - ").replace("  ",
                                   " ").replace(" -", " - ").replace("  ", " ")
    for i in scraped_jobs['Job Title']
]
# Tidy up colons
scraped_jobs['Job Title'] = [
    i.replace(" :", ": ").replace("  ", " ") for i in scraped_jobs['Job Title']
]
# Get rid of punctuation that's never needed
scraped_jobs['Job Title'] = [
    i.replace(".", "").replace("!", "").replace(
        "?", "").replace("→", "").replace("🌿", "")
    for i in scraped_jobs['Job Title']
]

# Replace a weird apostrophe with a normal one
scraped_jobs['Job Title'] = [
    i.replace("’", "'") for i in scraped_jobs['Job Title']]

# Get rid of extra phrases that aren't needed
scraped_jobs['Job Title'] = [
    i.replace("(All Genders)", "").replace("(all genders)", "").replace("all genders", "").replace(" - Permanent (no closing date – apply now)",
                                           "").replace("/ ANNUM ", "").replace("docx", "").replace("Job Description", "")
    for i in scraped_jobs['Job Title']
]

# Remove extra spaces at the end
scraped_jobs['Job Title'] = [i.strip() for i in scraped_jobs['Job Title']]
# Get rid of trailing punctuation
scraped_jobs['Job Title'] = [
    i[:-1] if i[-1] in ["-", ":"] else i for i in scraped_jobs['Job Title']
]
# Remove extra spaces again (including mid-string this time)
scraped_jobs['Job Title'] = [
    i.strip().replace("  ", " ") for i in scraped_jobs['Job Title']
]

# Now we need to tidy everything up with title case, but with exceptions for words that should stay capitalised
# Define a list of words to exclude from being title cased
exclusions = ["PA", "EMEA", "APPG", "BizDev", "PSP", "BD", "MD", "CEO", "ESG", "GHG", "HS2", "REDD", "EHS", "EIA", "ELM", "DAS/PSS", "NCEA", "INNS", "GWCL", "MEL", "GIS", "BI", "BA", "EDA", "ETRM", "DNA", "UX", "UI", "UX/UI", "UI/UX", "NVH", "BIM", "CAD", "RF", "CAE", "EE", "EDS", "HV", "EC&I", "GDA", "BoP", "MEICA", "BMS", "PV", "FMEA", "ETF", "FP&A", "CFO", "HR", "EDI", "IT", "ICT", "NetOps", "TechOps", "CSIRT", "GRC", "EIR", "COMAH", "PR", "CRM", "SEO", "PPC", "CMO", "COO", "FOI", "FCRM", "HSE", "EHS", "SHE", "UAV", "HGV", "SA", "CPO", "CTO", "ML", "AI", "DevOps", "QA", "iOS", "SQA", "SW", "IT", "SRE", ".NET", "TypeScript", "NetOps", "BMS", "VP", "NED", "US", "QHSE", "LCA", "EPD", "CDR", "CI", "CD", "CI/CD", "LEF", "HSQE", "UK", "UK)", "NPP", "SG3", "MMO", "UX/", "/UI", "API", "USA)", "(NY", "(HR)", "MEICA)", "(MEICA", "(MEICA)", "FSGo", "SIG", "AIT", "OEM", "FTE", "DBRC", "HTS", "BES", "FCERM", ")FCERM", "(FCERM", "(FCERM)", "MBA", "(s)",
              "(UK", "(UK)", "(UK-)", "UK/EU", "UK/EU)", "(UK/EU", "(UK/EU)", "POS", "NNR", "FTC", "EU", "EMEA", "EMEA)", "(EMEA", "(EMEA)", "EV", "IoT", "NEAS", "CV", "GMT", "VCF", "UK/I", "SDR", ")SDR", "(SDR", "(SDR)", "FTC)", "(FTC", "(FTC)", "EV)", "(EV", "(HSE", "(EHS", "(SHE", "(QHSE", "HSE)", "EHS)", "SHE)", "QHSE)", "(HSE)", "(EHS)", "(SHE)", "(QHSE)", "(CI)", "(GMT", "GMT)", "HMNB", "RAF", "(AWS)", "AWS", "NRG", "(NRG)", "EPR", "(PM1)", "(PM2)", "PM", "(IEP)", "IEP", "(FCRM)", "BoP", "(UK&IE)", "UK&IE", "TCAF", "(TCAF)", "ZCL", "HQ", "ERP", "OPEX", "PMO", "PDME", "SQL", "ECO", "HabiMap", "FP&A", "DACH", "EAN", "LNA", "TaaS", "(TaaS)", "PSO", "NFM", "(NFM)", "DVP", "NE", "SE", "NW", "SW", "SWE", "PDM", "KAM", "BOM", "BoM", "CFD/MHD", "CFD", "MHD", "EAC", "UKPN", "or", "x", "x2", "x3", "x4", "'s", "s", "CSM)", "(CSM)", "(CSM", "DCO", "DCO/", "DCO/Planning", "VPP", "Co-ordinator", "Co-ordination", "the", "and", "of", "to", "for", "up"]


# Make a function to convert strings to title case, excluding the words in the exclusions list above
def convert_to_title_case(text):
  words = text.split()  # Split the string into a list of words
  # List comprehension to convert each word to title case unless it's in the exclusions list
  title_words = [
      word.title() if word not in exclusions else word for word in words]
  # Combine the converted words back into a single string
  return ' '.join(title_words)


# Apply the new function to all job titles
scraped_jobs['Job Title'] = [
    convert_to_title_case(i) for i in scraped_jobs['Job Title']
]

# Fix a weird edge case with apostrophes, and another with Next.js
scraped_jobs['Job Title'] = [
    i.replace("'S", "'s").replace("Nextjs", "Next.js") for i in scraped_jobs['Job Title']]

# Limit the 'Job Title' column to 255 characters (the maximum allowed in the jobs PSQL table)
scraped_jobs['Job Title'] = scraped_jobs['Job Title'].str[:255]


# Create a new column for concatenating org-role-location
scraped_jobs['concat'] = scraped_jobs['Company'] + " - " + scraped_jobs[
    'Job Title'] + " - " + scraped_jobs['Title Location']
# Limit this column to 255 characters (the maximum allowed in the jobs PSQL table)
scraped_jobs['concat'] = scraped_jobs['concat'].str[:255]

# Create new columns for the jobs' mapped locations, job types, and seniorities
scraped_jobs['mapped_location'] = "not mapped"
scraped_jobs['job_types'] = "not mapped"
scraped_jobs['seniority'] = "mid level"