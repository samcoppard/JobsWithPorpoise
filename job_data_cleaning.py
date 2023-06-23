""" Clean up the scraped jobs so that you can effectively categorise them later """

import pandas as pd

# Pull in the scraped jobs as a dataframe
scraped_csv = pd.read_csv('scraped_jobs.csv')
scraped_jobs = pd.DataFrame(scraped_csv)

def remove_incomplete_rows(df):
    """Remove all rows with a missing value anywhere, then reset the index"""
    df.dropna(how='any', axis=0, inplace=True)
    df.reset_index(drop=True, inplace=True)


def clean_locations(df, column):
    """Create a new column to store locations in title case, and deal with a couple
        of edge cases that mess up location mapping"""
    df[column] = (df[column].str.title()
    # Remove mentions of New York and New South Wales
    .str.replace("New York", "").str.replace("New South Wales", ""))
    # Change "Sale" & "Bury" to "Manchester" (by using a boolean mask)
    mask = df[column].isin(["Sale", "Bury"])
    df.loc[mask, column] = "Manchester"


def clean_job_titles(df, column):
    """Remove useless phrases & characters; limit to 255 chars; tidy up punctuation"""

    # Get rid of extra phrases that aren't needed
    phrases_to_remove = ["(All Genders)", "(all genders)", "all genders", " - Permanent (no closing date – apply now)", "/ ANNUM ", "docx", "Job Description"]
    for phrase in phrases_to_remove:
        df[column] = df[column].str.replace(phrase, "")

    # Get rid of punctuation that's never needed
    chars_to_remove = [".", "!", "?", "→", "🌿"]
    for char in chars_to_remove:
        df[column] = df[column].str.replace(char, "")

    # Limit the 'Job Title' column to 255 characters (the maximum allowed in the jobs PSQL table)
    df[column] = df[column].str[:255]

    # Tidy up hyphens
    df[column] = (df[column].str.replace("- ", " - ").str.replace(" -", " - ").str.replace("  ", " ")

    # Tidy up colons
    .str.replace(" :", ": ").str.replace("  ", " "))

    # Replace a weird apostrophe with a normal one
    df[column] = df[column].str.replace("’", "'")

    # Remove whitespace at the end
    df[column] = (df[column].str.strip()

    # Get rid of trailing punctuation
    .str.replace(r'[:,(/-]+$', '', regex=True)
    
    # Remove extra spaces again (including mid-string this time)
    .str.strip().str.replace("  ", " "))





# Convert job titles to title case, excluding certain words
exclusions = ["PA", "EMEA", "APPG", "BizDev", "PSP", "BD", "MD", "CEO", "ESG", "GHG", "HS2", "REDD", "EHS", "EIA", "ELM", "DAS/PSS", "NCEA", "INNS", "GWCL", "MEL", "GIS", "BI", "BA", "EDA", "ETRM", "DNA", "UX", "UI", "UX/UI", "UI/UX", "NVH", "BIM", "CAD", "RF", "CAE", "EE", "EDS", "HV", "EC&I", "GDA", "BoP", "MEICA", "BMS", "PV", "FMEA", "ETF", "FP&A", "CFO", "HR", "EDI", "IT", "ICT", "NetOps", "TechOps", "CSIRT", "GRC", "EIR", "COMAH", "PR", "CRM", "SEO", "PPC", "CMO", "COO", "FOI", "FCRM", "HSE", "EHS", "SHE", "UAV", "HGV", "SA", "CPO", "CTO", "ML", "AI", "DevOps", "QA", "iOS", "SQA", "SW", "IT", "SRE", ".NET", "TypeScript", "NetOps", "BMS", "VP", "NED", "US", "QHSE", "LCA", "EPD", "CDR", "CI", "CD", "CI/CD", "LEF", "HSQE", "UK", "UK)", "NPP", "SG3", "MMO", "UX/", "/UI", "API", "USA)", "(NY", "(HR)", "MEICA)", "(MEICA", "(MEICA)", "FSGo", "SIG", "AIT", "OEM", "FTE", "DBRC", "HTS", "BES", "FCERM", ")FCERM", "(FCERM", "(FCERM)", "MBA", "(s)",
              "(UK", "(UK)", "(UK-)", "UK/EU", "UK/EU)", "(UK/EU", "(UK/EU)", "POS", "NNR", "FTC", "EU", "EMEA", "EMEA)", "(EMEA", "(EMEA)", "EV", "IoT", "NEAS", "CV", "GMT", "VCF", "UK/I", "SDR", ")SDR", "(SDR", "(SDR)", "FTC)", "(FTC", "(FTC)", "EV)", "(EV", "(HSE", "(EHS", "(SHE", "(QHSE", "HSE)", "EHS)", "SHE)", "QHSE)", "(HSE)", "(EHS)", "(SHE)", "(QHSE)", "(CI)", "(GMT", "GMT)", "HMNB", "RAF", "(AWS)", "AWS", "NRG", "(NRG)", "EPR", "(PM1)", "(PM2)", "PM", "(IEP)", "IEP", "(FCRM)", "BoP", "(UK&IE)", "UK&IE", "TCAF", "(TCAF)", "ZCL", "HQ", "ERP", "OPEX", "PMO", "PDME", "SQL", "ECO", "HabiMap", "FP&A", "DACH", "EAN", "LNA", "TaaS", "(TaaS)", "PSO", "NFM", "(NFM)", "DVP", "NE", "SE", "NW", "SW", "SWE", "PDM", "KAM", "BOM", "BoM", "CFD/MHD", "CFD", "MHD", "EAC", "UKPN", "or", "x", "x2", "x3", "x4", "s", "CSM)", "(CSM)", "(CSM", "DCO", "DCO/", "DCO/Planning", "VPP", "the", "and", "of", "to", "for", "up"]


def convert_to_title_case(string):
    """ Change the string to title case, except where you wouldn't actually want to """
    words = string.split()
    capitalized_words = [
        word.capitalize() if word not in exclusions else word for word in words]
    capitalized_string = ' '.join(capitalized_words)
    # Fix an edge case with Next.js
    capitalized_string = capitalized_string.replace("Nextjs", "Next.js")
    return capitalized_string


def convert_df_column_to_title_case(df, column):
    """ Change a df column of string values to title case """
    df[column] = df[column].str.apply(convert_to_title_case)

remove_incomplete_rows(scraped_jobs)
clean_locations(scraped_jobs, 'Location')
clean_job_titles(scraped_jobs, 'Job Title')
convert_df_column_to_title_case(scraped_jobs, 'Job Title')



# Create a new column for concatenating org - role - location, and limit it to 255 chars
scraped_jobs['concat'] = (scraped_jobs['Company'] + " - " + scraped_jobs[
    'Job Title'] + " - " + scraped_jobs['Location']).str[:255]


# Create new columns for the jobs' mapped locations, job types, and seniorities
scraped_jobs['mapped_location'] = "not mapped"
scraped_jobs['job_types'] = "not mapped"
scraped_jobs['seniority'] = "mid level"