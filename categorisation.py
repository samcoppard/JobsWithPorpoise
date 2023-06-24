import pandas as pd

# Pull in the scraped jobs as a dataframe
scraped_csv = pd.read_csv('cleaned_jobs.csv')
scraped_jobs = pd.DataFrame(scraped_csv)

""" Map each job to its location(s) first """

# Create a list of possible terms for each location
remote = [
    'Flexible Across England', 'Fully Remote', 'Global', 'Remote-Based',
    '2H From Utc', 'Gmt +-2', 'Homebased', 'Anywhere In The Uk',
    'Remote Working In Europe', 'Remote (Ireland, Uk Or Us Only)',
    'Remote Working', 'Western Europe', 'Uk, With Home Working Possible',
    'Remote (Ireland And Uk)', 'Home Based - Uk', 'Location: Remote',
    'Home Based - With Extensive Travel', 'Home-Based - With Significant Travel',
    'Home-Based With Some Travel', 'Home Working , All, Various',
    'Home Working (Office Facilities Available)', 'Remote, Eu',
    'Home Based - Some National Travel Expected', 'Emea', 'Remote, Uk', 'Flexible Home Working', 'Remote Based With The Ability To Travel Throughout England', 'Remote (Europe', 'Remote (US, UK', 'Remote (UK', 'Remote (US, Europe', 'Home Based With Occasional Travel'
]
london = [
    'London', 'Southwark', 'Bermondsey', 'Brixton', 'Camberwell', 'Hackney Wick', 'Chelsea', 'Fulham',
    'Wimbledon', 'Shoreditch', 'Westminster', 'Kensington', 'Londres', 'Clerkenwell', 'Putney', 'Ealing',
    'John Street Office', 'Streatham', 'Stratford', 'Tottenham', 'Camden', 'Battersea', 'Clapham', 'Harrow',
    'Wembley', 'Whitechapel', 'Chiswick', 'Fulham', 'Wandsworth', 'Acton', 'Hammersmith', 'Hanwell',
    'Twickenham', 'North Woolwich', 'Roehampton', 'Deptford', 'Enfield', 'Park Royal', 'Poplar', 'Fruit Towers', 'Lambeth', 'Sutton', 'Croydon'
]
scotland = [
    'Scotland', 'Solway', 'Argyll', 'Hebrides', 'Dundee', 'East Coast',
    'Dumfries', 'Galloway', 'Perth', 'Kinross', 'Edinburgh', 'Aberdeen',
    'Glasgow', 'Highlands', 'Shetland', 'Orkney', 'Aviemore', 'Inverness',
    'North Berwick', 'Stirling', 'Ayr', 'Moffat', 'Falls Of Clyde', 'Lanark',
    'Loch Of The Lowes', 'Dunkeld', 'Grangemouth', 'Falkirk', 'East Lothian',
    'Lothian', 'Kinneil', "Bo'Ness", 'Borrowstounness', 'Cumbernauld'
]
wales = [
    'Wales', 'Cardiff', 'Machynlleth', 'Powys', 'Snowdonia', 'Pembrokeshire',
    'Radnorshire', 'Abertillery', 'Gwent', 'Radnorshire', 'Montgomeryshire',
    'Newport', 'Swansea', 'Barry'
]
southeast = [
    'Andover', 'Oxford', 'Brighton', 'Guildford', 'Kent', 'Southampton', 'Gravesham',
    'Reading', 'Abingdon', 'Milton', 'Bbowt', 'Hampshire', 'Isle Of Wight',
    'Middlesex', 'Solent', 'Totton', 'Surrey', 'Sussex', 'Henfield', 'New Forest',
    'South East England', 'Banbury', 'Upper Heyford', 'Bicester', 'Leatherhead',
    'Sevenoaks', 'Dartford', 'Maidstone', 'Tonbridge', 'South East', 'Slough',
    'Berkshire', 'Woking', 'Winchester', 'Newbury', 'Wallingford', 'Egham',
    'Aldershot', 'Chichester', 'West Malling', 'Farnham', 'Romsey', 'Worthing',
    'Pevensey', 'Sevenoaks', 'Canterbury', 'Rye', 'Horsham', 'Weybridge', 'Winnersh',
    'South East, Uk', 'Hastings', 'Eastbourne', 'Wokingham', 'Basingstoke',
    'Aylesbury', 'Buckinghamshire', 'Reigate', 'Banstead', 'Maidenhead', 'Lewes',
    'Eastleigh', 'Portsmouth', 'Dymchurch', 'Sittingbourne', 'Ramsdell', 'Hampstead Norreys', 'Smol Warehouse', 'Raf Welford', 'Crawley', 'Sunbury'
]
southwest = [
    'Bristol', 'Barnstaple', 'Bath', 'Cornwall', 'Exeter', 'Plymouth', 'Avon',
    'Somerset', 'Devon', 'Dorset', 'Devizes', 'Wiltshire', 'Gloucester', 'Radstock',
    'Langford', 'Wilton', 'Bude', 'South West England', 'Weston-Super-Mare',
    'Bridgwater', 'Cheltenham', 'Salisbury', 'Yeovil', 'Taunton', 'Poole', 'Midsomer Norton',
    'Bournemouth', 'Bodmin', 'Launceston', 'Chippenham', 'Tewkesbury', 'Somer Valley',
    'Blandford Forum', 'Swindon', 'Cricklade', 'Bruton', 'Redruth', 'Wadebridge', 'South West', 'Scilly', 'Lulworth', 'Tor Bay', 'Torbay', 'Torquay', 'Dorchester'
]
northeast = [
    'Hartlepool', 'Durham', 'Tees Valley', 'Newcastle', 'Tyneside',
    'Northumberland', 'North East England', 'Darlington', 'Northern England'
]
northwest = [
    'Manchester', 'Liverpool', 'Penrith', 'Cumbria', 'Lake District',
    'Isle Of Man', 'Lancashire', 'Wigan', 'North West England', 'Warrington',
    'Cheshire', 'Chester', 'Merseyside', 'Preston', 'Kendal', 'Leigh', 'Leyland',
    'Southport', 'Winsford', 'Workington', 'Abbeytown', 'Brampton',
    'Trafford Park', 'Speke', 'Crewe', 'Carnforth', 'Rochdale', 'Stockport', 'Northern England'
]
eastmidlands = [
    'Ashby', 'East Midlands', 'Derbyshire', 'Leicester', 'Lincoln', 'Nottingham',
    'Northampton', 'Wildlifebcn', 'Silverstone', 'Grantham', 'Newark', 'Gainsborough',
    'Midlands And East', 'Kettering', 'Spalding', 'Scunthorpe', 'Mablethorpe', 'Central England', 'Loughborough', 'Derby'
]
westmidlands = [
    'Birmingham', 'Coventry', 'West Midlands', 'Shropshire', 'Staffordshire',
    'Warwick', 'Worcester', 'Hereford', 'Nuneaton', 'Kenilworth', 'Rugby',
    'Midlands And East', 'Telford', 'Fradley', 'Smethwick', 'Chorley',
    'Henley-In-Arden', 'Kidderminster', 'Shrewsbury', 'Solihull', 'Stafford',
    'Sutton Coldfield', 'Uttoxeter', 'West Bromwich', 'Mira, Gb', 'Wariwckshire',
    'Stoke', 'Wolverhampton', 'Central England', 'Leamington'
]
eastengland = [
    'Cambridge', 'Harpenden', 'Luton', 'Ongar', 'Peterborough', 'Essex',
    'Norfolk', 'Suffolk', 'Herts', 'Hertfordshire', 'Bedford', 'Wildlifebcn',
    'East Of England', 'Ipswich', 'Tilbury', 'Chelmsford', 'Lakenheath',
    'Billericay', 'Mildenhall', 'Alconbury', 'Stevenage', 'St Albans',
    'Hertford', 'Marston Vale', 'Midlands And East', 'Welwyn Garden City',
    'Colchester', 'Ely', 'Norwich', "King's Lynn", 'Great Yarmouth', 'St. Neots',
    'Huntingdon', "King'S Lynn", 'Southend', 'Harlow'
]
yorks = [
    'Doncaster', 'Leeds', 'York', 'Sheffield', 'Humber', 'Yorkshire',
    'Rotherham', 'Yorkshire And The Humber', 'Hull', 'Wetherby', 'Barnsley',
    'Beverley', 'Ilkley', 'Redcar', 'Scarborough', 'The National Forest',
    'Tadcaster', 'Northern England', 'Wakefield', 'Halifax', 'Bradford', 'Harrogate'
]
abroad = [
    'Alderney', 'Ulster', 'Munich', 'Singapore', 'Utrecht', 'Utretch', 'Belfast', 'Oregon',
    'Düsseldorf', 'Duisburg', 'Berlin', 'Sydney', 'New South Wales', 'Australia',
    'Belgium', 'Auckland', 'New Zealand', 'Boston', 'New York', 'Nyc', 'Cluj',
    'Romania', 'Chicago', 'North America', 'Paris', 'Amsterdam', 'San Francisco',
    'California', 'Madagascar', 'Timor-Leste', 'Denmark', 'Remote - Us', 'Ouagadougou',
    'Georgia', 'Belgrade', 'Serbia', 'Apeldoorn', 'Netherlands', 'Remote Usa',
    'Ireland Only', 'Austria', 'France', 'Germany', 'Italy', 'Norway', 'Poland',
    'Portugal', 'Spain', 'Sweden', 'Switzerland', 'Oslo', 'Madrid', 'Lisbon',
    'Vienna', 'Brussels', 'Milan', 'Warsaw', 'Stockholm', 'Zurich', 'Montreal',
    'Washington', 'Turin', 'United States', 'Bengaluru', 'Bangalore', 'India',
    'Helsinki', 'Finland', 'Wellington', 'Mexico', 'Central America', 'Dubai',
    'Asia Pacific', 'Malaysia', 'Salengor', 'Lusaka', 'Zambia', 'Nairobi',
    'Kenya', 'Hanoi', 'Vietnam', 'Kazakhstan', 'Hawaii', 'Nijmegen', 'D.C.',
    'Austin', 'Boulder', 'Raleigh', 'San Juan', 'La Paz', 'Jakarta', 'Nordic Region',
    'New Orleans', 'Bavaria', 'Frankfurt', 'Valencia', 'Tokyo', 'Houston',
    'Ascoli Piceno', 'Portadown', 'Melbourne', 'Gibraltar', 'Rawalpindi',
    'Tando Allayar', 'Northeast Us', 'New England', 'Bayern', 'Tanzania', 'Cameroon',
    'Usa / Remote', 'Japan', 'Ontario', 'Canada', 'Ghana', 'Remote, Us', 'Yaounde',
    'Vilnius', 'Lithuania', 'Leira', 'Coimbra', 'Belize', 'U.S. Remote', 'Logistique',
    'Dusseldorf', 'Alicante', 'Pacific Time Zone', 'Copenhagen', 'Shenzhen', 'Du Projet',
    'Duisberg', 'Athens', 'Greece', 'Dublin', 'Andavadoaka', 'Coslada', 'Sindh', 'Pakistan', 'Detroit', 'Northern Ireland', 'Région', 'Lille', 'Indonesia', 'Tando Allahyar'
]

# Create a dictionary from all those lists so that we can scan them all at once
locations_dict = {
    'Fully Remote': remote,
    'London': london,
    'Scotland': scotland,
    'Wales': wales,
    'South East': southeast,
    'South West': southwest,
    'North East': northeast,
    'North West': northwest,
    'East Midlands': eastmidlands,
    'West Midlands': westmidlands,
    'East of England': eastengland,
    'Yorkshire / Humber': yorks,
    'Abroad': abroad
}

# Check each job / row in scraped_jobs
for ind in scraped_jobs.index:
  # Start off with an empty list that we'll populate with the locations
  a = []
  # For each possible location, check if one of the defining terms for that location appears in the scraped location, then add it to the list if it does
  for area in locations_dict:
    if any(ele in scraped_jobs['Location'][ind]
           for ele in locations_dict[area]):
      a.append(area)
    # Combine all the mapped locations in the dictionary into a single string
    if a != []:
      b = ", ".join(a)
      # Add the string to the 'mapped_location' column of the scraped_jobs dataframe
      # NB if the scraped location didn't match any of the possible mapped locations, this will still read 'unmapped'
      scraped_jobs['mapped_location'][ind] = b

# Deal with awkward scraped locations, starting with Remote jobs
remote_matches = [
    'Remote', 'Fully Remote', 'Remote Job', 'Uk', 'Remote, United Kingdom',
    'Uk, United Kingdom', 'Remote (Ireland Or Uk Only)', 'United Kingdom',
    'Home Based', 'Home-Based', 'Working From Home', 'Europe', 'Nationwide',
    'Flexible/Home Working', 'Uk Wide', 'Flexible'
]
midlands_matches = ['Midlands', 'Midlands, United Kingdom', 'Midlands, Gb']
north_matches = ['Northern England', 'England, North']
england_matches = ['England, United Kingdom']
abroad_matches = ['Ireland', 'Northern Ireland']
all_matches = ['Nearby Any Sustrans Office Hub Across The Uk']

for ind in scraped_jobs.index:
  if any(x == scraped_jobs['Location'][ind] for x in remote_matches):
    scraped_jobs['mapped_location'][ind] = "Fully Remote"
  elif any(x == scraped_jobs['Location'][ind] for x in midlands_matches):
    scraped_jobs['mapped_location'][ind] = "East Midlands, West Midlands"
  elif any(x == scraped_jobs['Location'][ind] for x in north_matches):
    scraped_jobs['mapped_location'][ind] = "North East, North West"
  elif any(x == scraped_jobs['Location'][ind] for x in england_matches):
    scraped_jobs['mapped_location'][
        ind] = "London, South East, South West, North East, North West, East Midlands, West Midlands, East of England, Yorkshire / Humber"
  elif any(x == scraped_jobs['Location'][ind] for x in abroad_matches):
    scraped_jobs['mapped_location'][ind] = "Abroad"
  elif any(x in scraped_jobs['Location'][ind] for x in all_matches):
    scraped_jobs['mapped_location'][
        ind] = "Scotland, Wales, London, South East, South West, North East, North West, East Midlands, West Midlands, East of England, Yorkshire / Humber"

# Sometimes the location only appears in the job title, not where it 'should' be, so let's deal with that by checking job titles for locations IF the normal way hasn't worked

for ind in scraped_jobs.index:
  if scraped_jobs['mapped_location'][ind] == "not mapped":
    a = []
    for area in locations_dict:
      if any(ele in scraped_jobs['Job Title'][ind]
             for ele in locations_dict[area]):
        a.append(area)
      if a != []:
        b = ", ".join(a)
        scraped_jobs['mapped_location'][ind] = b

# Ensure that Remote jobs are only tagged as Remote, not other locations as well
for ind in scraped_jobs.index:
  if "Fully Remote" in scraped_jobs['mapped_location'][ind]:
    scraped_jobs['mapped_location'][ind] = "Fully Remote"

# NB - What to do with jobs like ones from EVenergy that are e.g. 'New York - Fully Remote'? Need to exclude, not class as remote

# Print out any jobs that haven't been mapped to any area (for easy review)
print("These jobs haven't been mapped to any location:")
print(scraped_jobs[scraped_jobs['mapped_location'] == 'not mapped'])

# Remove jobs in non-UK locations
for ind in scraped_jobs.index:
  # NB Check that the job has only been mapped to 'Abroad' so that we don't accidentally exclude jobs with a scraped location like 'Brussels, London, Amsterdam'
  if scraped_jobs['mapped_location'][ind] == 'Abroad':
    scraped_jobs.drop(index=ind, inplace=True)


""" Now map each job to its job type(s) """


# Create a list of terms for each kind of job, which will be used to map jobs to the right kind of job
admin = [
    'Admin', 'Executive Assistant', 'Business Support', 'Personal Assistant',
    'Management Team Assistant', 'Administrative', 'Executive Support', 'Development Assistant',
    'Engagement Executive', 'Team Assistant', 'Receptionist', 'PA', 'Enquiries Officer', 'Secretary', 'Environment Assistant',
    'Technical Support Officer', 'Department Assistant', 'Venues Co-ordinator', 'Travel Experience Freelancer',
    'Parts Supervisor', 'Secretariat', 'Support Assistant', 'Membership Assistant', 'Office Manager', 'Office Coordinator', 'Organisational Resilience Team Member', 'Finance Support Officer'
]
advocacy = [
    'Advocacy', 'Policy', 'Political', 'Public Affairs', 'Proposals EMEA',
    'Parliamentary', 'APPG', 'Convenor', 'Politics'
]
bizdev = [
    'Business Development', 'Bizdev', 'BizDev', 'Account Manager', 'Commercial Lead',
    'Account Executive', 'Donor Relations', 'Commercial Manager', 'OEM Partnerships',
    'Corporate Partnerships', 'Prospect Research', 'Commercial Officer',
    'Client Relationship Manager', 'Partnership Manager', 'Bid Development',
    'Aftersales Manager', 'Partnership Executive', 'PSP', 'Head of Commercial',
    'Head Of Nature Based Investment', 'Independent Partners', 'Partnerships and Alliances',
    'Corporate Programme', 'Account Handler', 'Estimator', 'Director of Development',
    'Growth and Strategic Planning', 'Account Officer', 'Business Evangelist',
    'Senior Engagement Officer', 'Account Go-To-Market Manager', 'Director of Transformation',
    'Commercial Coordinator', 'Market Design', 'Investor Relations', 'MBA',
    'Portfolio Associate', 'Associate - Development', 'Client Onboarding',
    'Development Officer', 'Partnership Advisor', 'Key Account Manager',
    'Corporate Relations Officer', 'Commercial Strategy', 'Stakeholder Manager',
    'Associate Director', 'Partner Enablement', 'Partnerships Manager', 'VP of Partnerships',
    'Business Change Manager', 'BD Director', 'Enterprise Account Director', 'PSO',
    'Licensing', 'Channel Manager', 'Managing Director', 'MD', 'Carbon Portfolio',
    'Associate Director', 'Private Sector Engagement', 'Director of Change',
    'External Relations', 'Strategic Partnerships', 'Strategic Alliance', 'Country Manager',
    'Head of Partnerships', 'Account Management', 'Client Success', 'Lead Generation',
    'Commercial Partner', 'Commercial Director', 'Commercial Analyst', 'Relationship Manager', 'Chief Executive Officer', 'CEO', 'Partnerships -', 'Kielder Team Manager', 'Novel CDR Business', 'Business Planning', 'Strategy Associate', 'Partnerships Director', 'Climate Strategy and Development', 'Chief Executive', 'Land Advice Service Manager', 'Partnerships Officer', 'Awards Manager', 'Partner Manager', 'Director of Client Services', 'ERP', 'Enterprise Resource', 'Partnership Enablement', 'Head of Change Enablement', 'Corporate Development', 'Portfolio Manager', 'Client Lead', 'Trading Development', 'Climate Contribution Fund', 'Director of Advisory', 'Global Director', 'Innovation Lead', 'Regional Manager', 'Commercial Operations', 'Partnerships Marketing', 'Trade Marketing', 'Key Partner', 'Supplier Manager'
]
campaigning = [
    'Campaign', 'Community Action', 'Climate Action', 'Partnerships Executive', 'Activist',
    'Campaigner', 'Actions Coordinator', 'Action for Nature', 'Head of Action', 'Head Of Action', 'Investigator'
]
climate = [
    'Sustainability', 'Environmental Manager', 'Climate Change Adviser',
    'Climate Change Advisor', 'Carbon Footprint', 'Climate Advisor',
    'Carbon Consultant', 'Sustainable Development', 'Climate Analyst', 'ESG',
    'GHG', 'Greenhouse Gas', 'Climate Action', 'Carbon Impact', 'Methane',
    'Climate Finance', 'Climate Change', 'HS2', 'Green Growth & Delivery',
    'Fisheries Officer', 'Sustainable Places', 'Environment Planning Officer',
    'Environment Planning Specialist', 'Water Resources Officer', 'Carbon Portfolio',
    'Water Resources Specialist', 'Water Resources Senior Technical Specialist',
    'Carbon Reduction', 'Zero Carbon', 'Low Carbon', 'Sequestration',
    'Farming Advisor', 'Agriculture Specialist', 'Decarbonisation',
    'Environmental Impact', 'Climate Risk', 'Climate Targets', 'Half Hourly Settlement',
    'Climate Strategies', 'REDD', 'Carbon Market', 'Climate Program',
    'Metric Senior Specialist', 'Metric Specialist', 'Carbon Project',
    'Carbon Management', 'Carbon Inventory', 'Sustainable Diets', 'Clean Power',
    'Sustainable Business Partner', 'Sustainable Business Manager', 'Green Infrastructure',
    'Climate Methodologies', 'EHS', 'Environmental Health', 'EIA', 'Carbon Funds',
    'Environmental Impact Assessment', 'Environmental Consultant', 'Net Zero',
    'E&B', 'Carbon Registry', 'Climate Services', 'Carbon Services', 'Head of Food System Transformation',
    'Nature Strategy', 'Renewable Energy Solutions', 'Area Environment Manager', 'Head of Resilience', 'Environment Adviser', 'Air Quality', 'Environment Officer', 'LCA', 'EPD', 'Sustainable Standards', 'Climate Strategy', 'Carbon Projects', 'NEAS', 'Carbon Partnership', 'Renewables', 'Climate Digitalization', 'Climate Science', 'Tropical Cyclones', 'Renewable Energy', 'Life Cycle Assessment', 'Life Cycle Analys', 'Climate Intern', 'Energy Attribute Certificates', 'EAC', 'Impact Manager', 'Offshore Wind', 'Onshore Wind', 'Wind Energy', 'Sustainable Travel'
]
community = [
    'Community', 'Communities', 'Wilder Nottinghamshire Officer',
    'Stakeholder Engagement', 'Engagement Coordinator', 'Engagement Manager', 'Engagement Advisor', 'Engagement Projects Officer', 'Wilder Lives', 'Wilder Childhood', 'Nature Connection Manager'
]
conservation = [
    'Conservation', 'Field Officer', 'Project Officer', 'River', 'Wye',
    'Ocean Campaign', 'Wild Spaces Officer', 'Reserves Manager', 'Farm Advice',
    'Reserves Officer', 'Reserve Officer', 'Warden', 'Wilder Marches',
    'Nature Recovery', 'Ranger', 'Wild Ingleborough', 'Three Dales Project',
    'Wilder Nottinghamshire', 'Work Party', 'Habitat Biodiversity Assessment',
    'Landscape Recovery', 'Ponds Officer', 'Environmental Impact',
    'Planning Advisor', 'Environment Lead Advisor', 'Environment Lead Adviser',
    'Environment Advisor', 'Protected Sites', 'Farming Lead Adviser',
    'Farming Lead Advisor', 'ELM', 'Environmental Land Management',
    'Freshwater Lead Advisor', 'Strategic Plans for Places', 'DAS/PSS',
    'Tree Action Plan', 'Marine Specialist', 'NCEA', 'Nutrient Markets',
    'Natural Capital & Ecosystem Assessment', 'Natural England Adviser',
    'Agricultural Advisor', 'Land Advisor', 'Biodiversity Planning', 'Keeper',
    'Nature-Based', 'Nature Based', 'NBS', 'Nature Restoration', 'Reserve Trainee',
    'Great Crested Newt', 'Greener Farming', 'Greener Fisheries', 'Beaver',
    'Biodiversity', 'Wildcat', 'Pine Marten', 'Reintroduction', 'Bat Advisor',
    'Treescapes', 'Eelscapes', 'Forest Creation', 'Freshwater Scientist',
    'Invasive Species', 'Glasshouse', 'INNS', 'Restoring', 'Natural History',
    'Trillion Trees', 'Species Specialist', 'Contaminated Land', 'Landscape Partnership',
    'Environment Management Incident', 'Nautral Course', 'Natural Course',
    'GWCL', 'Groundwater', 'Advisor for Trees', 'Marine Monitoring', 'Landscape Advice',
    'Environment Monitoring', 'Environmental Monitoring', 'Field Monitoring',
    'Polar Oceans Specialist', 'Marine Senior Adviser', 'Marine Adviser',
    'Farm Adviser', 'Grey Squirrel', 'Species Protection Officer', 'Reserves Trainee',
    'Fisheries Technical Specialist', 'Estate Manage', 'Animal Care', 'REDD',
    'Kelp', 'Strategic Environment Planning', 'Waterways Workforce', 'Fish',
    'Restoration', 'Squirrel', 'Pool Frog', 'Woodland Hope', 'Farming Adviser',
    'Land Management Scheme Development', 'Fresh Water & Air', 'Urban Forestry',
    'Stork', 'Mussel', 'Species and Recording Officer', 'Pollution', 'Farm Officer',
    'Environmental Internship', 'Seabird', 'New To Nature', 'Watercress',
    'Marine Lead Adviser', 'Environmental Quality', 'Corncrake', 'Land Use',
    'Landscape Project Officer', 'Park Manager', 'Coastal Habitat', 'Seagrass',
    'Atlantic Rainforest', 'Get The Marches Buzzing', 'Freshwater', 'Natural Solutions',
    'Major Marine Developments', 'Environment Officer - Agriculture', 'Environmental Practitioner',
    'Wigan Greenheart', 'Habitat Survey', 'Saving Sites', 'Working Wetlands',
    'Habitats Officer', 'Reserves Assistant', 'Woodland Assistant', 'Catchment Coordinator',
    'Land Manage', 'Estuarine And Coastal', 'Marine Technical Officer',
    'DNA Based Monitoring', 'Reserve Manager', 'Woodland Lead Adviser', 'Ringer', 'Marine Future', 'Wilder Landscapes', 'Botanical Surveyor', 'Coast Explorer', 'Water Quality', 'Agriculture Technical Assistant', 'Managing Moors', 'Wilder Lives', 'Wilder Childhood', 'UK Habs Surveyor', 'Landscape Officer', 'Mammals', 'Carnivore', 'Woodland Creation', 'Estate Officer', 'Forestry Intern', 'Tree Nursery', 'Action for Nature', 'Local Wildlife Sites', 'Wetlands Expert', 'HabiMap', 'Wilder Ouse', 'New to Nature', 'Catchment Manager', 'Microplastic', 'Chemicals of Emerging Concern', 'Monitoring Systems', 'NPP', 'Northumberland Peat Partnership', 'Wildlife Care'
]
customer_service = [
    'Customer Service', 'Energy Advisor', 'Solution Advisor', 'Customer Support',
    'Customer Experience', 'Green Home Tech Advisor', 'Customer Care',
    'Complaints', 'Customer Delighter', 'Energy Caseworker', 'Development Assistant',
    'Visitor Services Manager', 'Visitor Experience', 'Call Centre',
    'Aftersales Manager', 'Customer Success', 'Payments and Collection Advisor',
    'Experience Assistant', 'Software Support Executive', 'Visitor Engagement',
    'Customer Technical Support', 'Customer and Engagement Specialist',
    'Engagement Lead', 'Customer Contact', 'Customer Operations', 'Energy Helper',
    'Credit Specialist', 'Energy Specialist', 'Solution Analyst', 'Engagement Placement',
    'Solution Engineer', 'Solutions Engineer', 'Client Onboarding', 'Supporter Care Officer',
    'Customer Advisor', 'Driver Support', 'Technical Support Engineer',
    'Customer Satisfaction', 'Installation Coordinator', 'Customer Excellence',
    'Energy Support Social Worker', 'Visitor Reception Officer', 'Customer and Operations',
    'Wildlife Centre Officer', 'Green Home Installation Manager', 'Digital Services Agent',
    'Technical Support Manager', 'Domestic Surveyor', 'Service Assistant',
    'Visitor Centre Assistant', 'Solar Onboarding', 'Domestic Energy Assessor',
    'Centre Assistant', 'Travel Experience Intern', 'Travel Experience Freelancer',
    'Energy Independence Advisor', 'Client Success', 'Customer Onboarding',
    'Visitor Officer', 'Customer Manager', 'Customers & Engagement', 'Collections', 'Resolution Advisor', 'Resolutions Manager', 'Customer Liaison', 'Trip Experience', 'Vulnerability Support'
]
data = [
    'Data', 'Business Analyst', 'Remote Sensing', 'Evidence and Learning', 'MEL',
    'Monitoring, Evaluation & Learning', 'Monitoring & Evaluation', 'GIS',
    'Geospatial', 'Analyst', 'Business Intelligence', 'BI', 'EDA', 'Records Centre',
    'Engineering Analyst', 'Biodiversity Assessment Manager', 'ETRM',
    'Analytics', 'Earth Observation', 'Modeller', 'Modelling', 'Principal BA',
    'Evidence Specialist', 'Hydrometry', 'Telemetry', 'Survey Specialist',
    'Scientist -Data', 'Field Monitoring', 'Reporting Manager', 'DBRC',
    'Integrated Environment Planning Specialist', 'Technical Services Officer',
    'Survey Advisor', 'Forecasting', 'Business Analysis', 'Statistics',
    'Energy Optimis', 'Analytical', 'Commercial Analyst', 'DNA Based Monitoring', 'Statistician', 'Evidence/Evaluation', 'Geomatics', 'Survey', 'Tropical Cyclones', 'Analysis', 'Monitoring Systems'
]
design = [
    'Design', 'Graphic', 'Video', 'Photo', 'Image', 'UX', 'UI', 'Art Director',
    'Studio Manager', 'Creative', 'Artworker', 'Animator', 'Filmmaker',
    'Landscape Planner', 'Label Art', 'Studio Assistant', 'Artist', 'Visual Merchandiser'
]
ecology = [
    'Ecologist', 'Ecology', 'Ecological', 'Ponds Officer', 'Marine Specialist',
    'Bat Advisor', 'Field Surveyor', 'Biodiversity Technician'
]
engineering = [
    'Mechanical', 'Electric', 'Electrical', 'Manufacturing', 'Electronics',
    'Automotive', 'Hydrogen', 'Calibration', 'Control Systems',
    'Process Engineer', 'Charger', 'Structural', 'Crashworthiness', 'Durability',
    'Fault', 'Powertrain', 'Thermal', 'Refrigeration', 'Suspension',
    'Composites', 'NVH', 'Tooling Engineer', 'Functional Validation',
    'Safety Engineer', 'Materials', 'Project Engineer', 'BIM', 'Civil',
    'Mechatronics', 'Controls Engineer', 'Control Engineer', 'Extrusion Technician',
    'Tendering Engineer', 'Field Service Engineer', 'Fuel Cell Engineer',
    'Charging Validation', 'Packaging Engineer', 'Engineering Technician',
    'Engineer, Northern Ireland', 'Engineer - Highways', 'Engineer, Scotland',
    'Engineer, Wales', 'CAD', 'Power Systems', 'RF Control', 'Superconduct',
    'Data Acquisition Engineer', 'Test Engineer - Control Systems',
    'RF Engineer', 'Magnet Systems Engineer', 'Engineering Analyst',
    'Magnet Instrumentation', 'Physicist/Engineer', 'Design Engineer',
    'Safety Case', 'Modelling Engineer', 'Cryogenic Engineer', 'Extrusion Engineer',
    'Integration Engineer', 'Charging Infrastructure', 'Engineer - Vehicle',
    'Frame Engineer', 'CAE', 'Development Engineer', 'Diagnostic',
    'Voltage Engineer', 'EE', 'Analysis Engineer', 'Body Systems Concepts',
    'Aerothermal', 'Chassis', 'Quality Engineer', 'Network Engineer',
    'Network Architect', 'System Engineering Practitioner', 'Vehical Programme',
    'Tooling Engineer', 'Voltage System Engineer', 'Validation Test Engineer',
    'EDS Rework Technician', 'HV Engineer', 'Site Services Engineer',
    'Workshop Supervisor', 'Propulsion', 'Electrified', 'Test Technician',
    'Prototype', 'Reactor Fuel', 'Machinist', 'EC&I', 'R&D Technician', 'GDA',
    'Balance of Plant', 'BoP', 'Site Layout', 'Installation Technician',
    'Serviceability Engineer', 'Magnet Engineer', 'Technical Support Specialist',
    'System Calibration', 'Launch Engineer', 'High Voltage', 'MEICA',
    'Catchment Engineer', 'Electric Charging', 'Research & Development Engineer',
    'Smart Meter Engineer', 'R&D Product Development', 'Cell Projects',
    'Hardware Engineer', 'Technical Support Engineer', 'Magnet Technician',
    'Engineering Project Manager', 'Structures', 'Technical Support Manager',
    'Concepts Manager', 'Technical Design', 'Technical Support Lead',
    'Change Management Engineer', 'Cab Structure', 'Concepts Engineer', 'BMS',
    'Battery', 'Plant Engineer', 'Plant Technologist', 'Maintenance Manager',
    'PV Technical Engineer', 'Aftermarket Engineer', 'Graduate Engineer',
    'Failure Mode', 'FMEA', 'Integrated Launch', 'Launch Parts', 'HTS',
    'Integration Architect', 'Circuit Engineer', 'Robot Installation',
    'Site Assessment Engineer', 'Energy Engineer', 'Asset Maintenance', 'Service Engineer', 'Chemical Engineering', 'Instrumentation Engineer', 'Conventional Island', 'Instrumentation Lead', 'Regulation Engineer', 'Landfill Engineer', 'Weight Attribute', 'Heating Engineer', 'Body & Trim', 'Chief Engineer', 'Geometry Engineer', 'Interiors', 'DVP Planning', 'BoM', 'Bill of Materials', 'Engineering Manager (Nuclear)', 'Heat Pump Installer'
]
finance = [
    'Accountant', 'Accounts', 'Finance', 'Financial', 'Invest', 'ETF', 'FP&A',
    'Tax', 'Capital', 'Trader', 'Treasury', 'Economist', 'Fintech', 'Invoicing',
    'Payroll', 'CFO', 'Chief Financial Officer', 'Accounts Admin', 'Money Laundering',
    'Credit Controller', 'Quantity Surveyor', 'Securities', 'Lending', 'Audit',
    'Income', 'Credit Specialist', 'Credit Risk', 'Accounting', 'Carbon Deals',
    'Middle Office', 'Carbon Market', 'Integrated Compensation', 'Originator',
    'Purchase Ledger', 'Credit Manager', 'Capital Marketplace', 'Carbon Funds',
    'Credit Control Officer', 'Banking', 'Economy', 'Credit Underwriter', 'Fund Manager', 'Affordability', 'M&A', 'Procure to Pay', 'Trading', 'Billing', 'Funding Manager'
]
hr = [
    'People', 'HR', 'Recruitment', 'Recruiter', 'Human Resources', 'Training', 'Induction Officer',
    'Talent', 'Culture', 'Resourcing Consultant', 'Volunteer Co-ordinator', 'Total Reward',
    'Learning and Development', 'Compensation', 'Benefits', 'Workforce Planning',
    'Resource Advisor', 'Equality, Diversity and Inclusion', 'EDI', 'Shift Coordinator', 'Shift Manager',
    'Safeguarding', 'Wellbeing', 'Head of Reward', 'Health, Safety & Wellbeing', 'Organisational Development', 'Career Entry', 'Skills Advisor', 'Team Manager', 'Head of Change Enablement', 'Learning & Development', 'Professional Development', 'Skills Officer', 'Anti-Racism'
]
it = [
    'IT', '365', 'Microsoft', 'Information Systems', 'ICT', 'Cloud Architect',
    'Applications Support', 'Security Project Manager', 'NetOps',
    'Network Operations', 'Moodle', 'Business Systems', 'DBRC',
    'Technical Support Officer', 'Salesforce', 'Technical Solutions Specialist',
    'TechOps', 'Enterprise Architecture', 'Technology Strategy',
    'Business Applications Technology', 'Technical Product Manager',
    'Network Infrastructure Engineer', 'CSIRT', 'Technical Architect',
    'Scrum Master', 'Business Applications, Technology', 'Implementation Lead',
    'Digital Strategy Manager', 'Resilience Manager', 'Tech Support',
    'Technology & Systems Manager', 'Web & Digital', 'Information Security', 'Cybersecurity', 'Data Architect', 'Wordpress', 'Digitalization', 'Head of Technology', 'Digital Threats', 'Cloud Admin', 'Colleague Technology', 'Systems Development Manager'
]
legal = [
    'Legal', 'Regulation', 'Regulator', 'Law', 'Certification', 'Compliance',
    'Risk', 'Functional Safety', 'GRC', 'Protected Sites Senior Adviser', 'In-House Counsel',
    'District Level Licensing', 'Regional Counsel', 'Paralegal', 'Planning Consent',
    'Standards Manager', 'Assurance', 'Area Incident', 'Monitoring Assessor',
    'Waste Assessor', 'Environment Management Incident', 'Head of Contracts',
    'Permitting', 'Enforcement', 'Disclosure', 'Crime', 'EIR', 'COMAH', 'DCO', 'Development Consent Order',
    'Senior Advisor - Refineries and Fuels', 'Corporate Counsel', 'Solicitor', 'Business Counsel', 'Consents Expert', 'Renewable Certificate', 'Regulated'
]
marketing = [
    'Marketing', 'Marketer', 'Comms', 'Communication', 'Content', 'Growth',
    'Social Media', 'Demand Generation', 'Branding', 'PR', 'Outreach', 'CRM',
    'Digital Acquisition', 'SEO', 'Search Engine Optimisation', 'Advertising',
    'PPC', 'Copywriter', 'Copy Writer', 'Copywriting', 'Press Officer',
    'Head of Ecommerce', 'Media Officer', 'Head of Press', 'Promotions Officer',
    'Head of Creative Production', 'CMO', 'Consumer Insight', 'E-Commerce Promotions',
    'Digital Engagement', 'Brand Manager', 'Engagement Manager',
    'Engagement Specialist', 'Engagement Lead', 'User Research', 'Paid Ads',
    'Brand Executive', 'Paid Social', 'E-Commerce Associate', 'Membership Manager',
    'User Acquisition', 'Brand Strategy', 'Ecommerce Manager', 'Promoter',
    'Youth Ambassador', 'Storytelling', 'Brand Rep', 'Stories',
    'B2B Demand Specialist', 'Travel Experience Intern', 'Lead Generation',
    'Brand Ambassador', 'Engagement Advisor', 'Influencer', 'Brand Sponsor', 'Pr Manager', 'Media Relations', 'Media Manager', 'Martech'
]
operations = [
    'Operations', 'Ops', 'Logistics', 'Quality Assistant', 'Planner',
    'Head of Land', 'Dataflow', 'MEL', 'Fulfilment', 'Knowledge and Research',
    'Knowledge & Research', 'O&M', 'Project Officer', 'Operator', 'Planning Assistant',
    'Business Process Analyst', 'Volunteer Co-ordinator', 'Skills Co-ordinator',
    'Technical Manager', 'Global Resilience Programme', 'Impact Coordinator',
    'Building Standards Manager', 'Warehouse Support Lead', 'Facilities Manager',
    'Smart Meter', 'Supply Chain', 'Food Safety', 'Client Services Manager',
    'Business Executive', 'Facilities Coordinator', 'Asset Compliance Officer',
    'D365', 'Business Central', 'Aftersales Solutions Specialist',
    'Claim Manager', 'Pricing', 'Accountability Officer', 'Business Management',
    'Team Leader', 'Trust and Safety', 'Technical Consultant', 'Field Planning',
    'Asset Management', 'General Manager', 'Planning & Performance', 'Fleet Advisor',
    'Strategic Plans and Green Infrastructure', 'Optimisation Lead',
    'Customer Infrastructure Partner', 'Import', 'Export', 'COO',
    'Chief Operating Officer', 'Delivery Officer', 'Chief of Staff',
    'Infleet Coordinator', 'Build Coordinator', 'Order Scheduler',
    'Refill Scheme Assistant', 'Shipping', 'Executive Coordination Manager',
    'Asset Performance', 'Programme Officer', 'Planning Specialist',
    'Technical Services Manager', 'Development Planning', 'Incident Management',
    'FOI', 'Flood & Coastal Risk Management', 'FCRM', 'AIT Officer',
    'Flood and Coastal Risk Management', 'Flood and Coastal Risk Manager',
    'Inspection Officer', 'Incident Advisor', 'Incident Management Officer',
    'Fisheries Officer', 'Biodiversity Net Gain', 'Flood Resilience Officer',
    'Director - Strategy', 'Readiness and Response', 'Places Planning',
    'Integrated Environment Planning Specialist', 'Asset Officer',
    'Delivery Manager', 'Service Continuity', 'Asset Manager', 'Planning Consent',
    'Stock Coordinator', 'Asset Coordinator', 'Stock Manager', 'DCO', 'Development Consent Order',
    'Flood Resilience Team Member', 'Technical Advisor (Incident Systems)',
    'Hazardous Waste Installations', 'Estate Manage', 'Quality Control',
    'Due Diligence', 'Flood Resilience', 'Flood Adviser', 'Estates Surveyor',
    'Project Support Officer – Residential Team', 'Feed In Tariff Technician',
    'Scheduler', 'Change Officer', 'Process Technologist', 'Director of Transformation',
    'Solutions Consultant', 'Quality Protocol', 'Installation Coordinator',
    'Technical Review Coordinator', 'Claim Handler', 'Technical Specialist',
    'Warehouse Manager', 'Supply and Deployment', 'Operational Excellence',
    'Inventory Manager', 'Associate Director', 'Project Installation Manager',
    'Quality and Performance', 'Fleet Manager', 'Customer Demand Manager',
    'Manager - Vehicle Development Workshop', 'Spare Parts Manager',
    'Vehicle Development Workshop Manager', 'Claims Handler', 'Depot Liaison',
    'Operational Delivery', 'Performance Monitoring', 'Process Development',
    'Access All Areas Trainee', 'Managing Director', 'MD', 'Associate Director',
    'HSE', 'EHS', 'SHE', 'HSQE', 'Health & Safety', 'Health and Safety',
    'Safety, Health', 'Wholesale Co-ordinator', 'Grocery Technologist',
    'Project Support Coordinator', 'Contract Coordinator', 'Corporate Services',
    'Wholesale & Consessions Co-ordinator', 'Merchandising', 'Country Manager',
    'Domestic Energy Assessor', 'Regional Manager', 'Project Support Assistant',
    'Quality Partner', 'Quality Specialist', 'Quality Coordinator',
    'Portfolio Officer', 'Contract Supervisor', 'Portfolio (Senior) Associate',
    'Portfolio Associate', 'Installation Manager', 'Flood Incident',
    'Technical Support Coordinator', 'Buildings Manager', 'Shift Coordinator',
    'Business Application Manager', 'Secretariat', 'Governance', 'Change Control Coordinator',
    'Executive Co-ordination Manager', 'Operational Manager', 'Contracts Officer', 'Delivery Lead', 'Head of Delivery', 'CI Practitioner', 'Process Lead', 'Metering Specialist', 'Operational Unit Manager', 'Head of Scheme Delivery', 'Charging Solutions Energy Lead', 'Implementation Specialist', 'Implementation Manager', 'Operational Readiness', 'Fund Manager', 'Membership Assistant', 'Depot Manager', 'Portfolio Delivery', 'Fresh Produce Technologist', 'Dispatch Associate', 'Quality Manager', 'Support Services Specialist', 'Collections', 'ERP', 'Enterprise Resource', 'Quality Systems Engineer', 'Venues Co-Ordinator', 'Consents Expert', 'Standards & Methodology', 'Head of Action', 'Head Of Action', 'ECO Specialist', 'Global Director', 'Quality Executive', 'Change Lead', 'Retrofit Coordinator', 'BoM', 'Bill of Materials', 'Operational Support', 'Supplier Manager', 'Events Officer'
]
other = [
    'Editor', 'Educator', 'Seasonal Staff', 'Author', 'Gender', 'Writer',
    'UAV Pilot', 'Drone Pilot', 'Employment Coach', 'Packaging Technologist',
    'Roofer', 'Board Member', 'School Streets Officer', 'Site Servies Engineer',
    'Charity Shop Manager', 'Engagement Officer', 'Centre Manager', 'Education',
    'Nature Nursery', 'HGV Technician', 'HGV Truck Technician', 'Test Driver',
    'Service Support', 'Historic Environment', 'Social Science', 'Bike Rider',
    'Synthesis and Learning', 'Veterinary', 'Maintenance Officer', 'Warehouse Staff',
    'Sustainable Development Programme - Senior Adviser', 'Strategist', 'Engagement Placement',
    'Healthy Travel Officer', 'Schools Officer', 'Retail Manager', 'Cargobike Rider',
    'Site Manager', 'Senior Adviser – Business & Capability', 'Event', 'E-Cyclist',
    'Learning Designer', 'Digital Learning', 'Chef', 'Strategic Solution',
    'Team Member 3', 'Navigation Moorings', 'Navigation Enforcement', 'NFM',
    'Facilities Officer', 'Navigation Senior Advisor', 'Packaging Cleaner',
    'Recoveries Technical', 'Smart Meter Apprentice', 'Site Supervisor',
    'Insulation Installer', 'Heating Surveyor', 'Solar Surveyor', 'Warehouse Shift',
    'Delivery Driver', 'Delivery Rider', 'Warehouse Operative', 'Caretaker',
    'Pot Washer', 'Senior Contract Support Officer', 'Chemicals Future Funding',
    'Environment & Business Adviser', 'Evidence Advisor', 'AIT Officer',
    'Waterways Business Officer', 'Water Resources Security of Supply',
    'Manufacturing Operative', 'Warehouse Supervisor', 'Inspector', 'Teaching',
    'Building Surveyor', 'Learning Officer', 'Cleaner', 'Heat Pump Engineer',
    'Field Support Specialist', 'Waterways Advisor', 'Hazardous Waste',
    'I Bike Officer', 'Definition of Waste', 'Adviser - Coastal Programme',
    'Coastal Planning', 'Water Quality Officer', 'Water Quality Advisor',
    'Chartered Surveyor', 'Store Manager', 'Cambridge Assistant Manager',
    'Warehouse Recycling Operative', 'Driver', 'Proforest Graduate', 'Beverage Assistant',
    'Graduate Scheme 2023', 'Domestic Surveyor', 'Project Delivery Assistant',
    'Kitchen', 'Water Resource', 'Environment Incident', 'Camp Manager', 'Dryliner',
    'Lecturer', 'Bike Mechanic', 'Bicycle Mechanic', 'Bike Builder', 'Sports',
    'Office Manager', 'Office Coordinator', 'Private Client Work', 'Waterways Business',
    'Resources From Waste', 'Active Travel Officer', 'Schools Streets Officer',
    'Water Company', 'Thames Estuary 2100', 'Humber Strategy', 'Maintenance Manager',
    'Incident Planning Officer', 'Publisher', 'Field Technician', 'Facilities Support',
    'Recycling Advisor', 'Site Care Assistant', 'Planning Officer', 'Activity Support',
    'Landscape Architect', 'Solar Technical Executive', 'Flood Inciedent', 'Shop Assistant',
    'Food Industry Team Coordinator', 'Textiles', 'Publishing', 'Facilities Technician',
    'Hospitality Assistant', 'Catering Assistant', 'Recycling Service Operative',
    'HGV', 'Maintenance Technician', 'Warehouse Associate', 'Courier',
    'Sortation Support', 'Retail Assistant',
    'Retail Sales Associate', 'Retail Supervisor',
    'Cafe', 'Café', 'Housekeeping', 'Cook', 'Mechanisation Arb',
    'Mechanised Arb', 'Key Holder', 'Cleaning Technician',
    'Gas Industry Expert', 'Boston Barrier', 'Water Level', 'Flood Strategy', 'Deputy Manager At Weddings',
    'Outdoor Learning', 'Skomer Visitor Officer', 'Barista', 'Housekeeper', 'Plumber', 'Forest School', 'Construction Manager', 'Construction Supervisor', 'Appraisal Senior Advisor', 'Archivist', 'Reservoir', 'Knowledge Specialist', 'Gas Shipper Expert', 'Area Director', 'Area Manager', 'Fens 2100+', 'Depot Assistant', 'Sweeper Driver', 'Flood Warning Officer', 'Technical Officer', 'Technical Advisor', 'Laundry Assistant', 'Laundry Supervisor', 'Tour Guide', 'Machine Operator', 'Contract Senior Advisor', 'Health Specialist', 'Waste Treatment', 'Waste Storage', 'Catering', 'Packing Assistant', 'Tactical Drought', 'Organisational Resilience', 'Information Management', 'Corporate Strategy', 'Incident Officer', 'Journalist', 'Plasterer', 'Amenity Maintenance', 'Associate - Offshore Wind', 'MMO Support Officer'
]
outdoorsy = [
    'Horticultural', 'Field Data', 'Field Ecologist', 'Ranger',
    'Wild Spaces Officer', 'Reserves Manager', 'Biological Recorder',
    'Farm Advice Officer', 'Reserves Officer', 'Reserve Officer',
    'Landscape Operative', 'Warden', 'Conservation Officer', 'Reserves Trainee',
    'Grazing Officer', 'Work Party', 'Walled Garden', 'Wildlife Care',
    'Habitat Biodiversity Assessment', 'Ponds Officer', 'Stocksperson', 'NCEA',
    'Natural Capital & Ecosystem Assessment', 'Keeper', 'Arborist',
    'Arb Surveyor', 'Landscaping', 'Litter Picker', 'Arb Site Supervisor',
    'Arb Team Leader', 'Glasshouse', 'Field Operations', 'Operations Field',
    'Marine Monitoring', 'Field Monitoring', 'Fencing Site Supervisor',
    'SA Exchange Technician', 'Grey Squirrel', 'Species Protection Officer',
    'Waterways Workforce', 'Landscaper', 'Gardener', 'Reserve Trainee',
    'Species and Recording Officer', 'Field Worker', 'Field Surveyor',
    'Camp Manager', 'Habitat Survey', 'Arboricultural Surveyor', 'Environmental Practitioner',
    'Habitats Officer', 'Reserves Assistant', 'Woodland Assistant', 'Engagement Placement',
    'Land Manage', 'Field Technician', 'Wildlife Boat Guide', 'Reserve Manager',
    'Field Team', 'Outdoor Learning', 'Ringer', 'Horticulture', 'Botanical Surveyor', 'Acorn Farm', 'UK Habs Surveyor', 'Grounds Maintenance', 'Grounds Person', 'Landscape Officer', 'Woodland Creation Officer', 'Estate Officer', 'HabiMap', 'Amenity Maintenance', 'Survey Contractor'
]
procurement = [
    'Procurement', 'Buyer', 'Buying', 'Commodity Lead', 'Sourcing',
    'Category Manager', 'Purchasing', 'Launch Readiness Lead', 'Parts Supervisor', 'Procure'
]
product = [
    'Product', 'CPO', 'Climate Methodologies Lead', 'Ecommerce Manager',
    'Retention', 'Packaging Manager', 'Platform Owner', 'Solution Owner'
]
project_mgmt = [
    'Project Manager', 'Programme Manager', 'Programme Lead', 'Project Director',
    'Programme Director', 'Project Coordinator', 'Project Co-Ordinator', 'Delivery Coordinator',
    'Nature Recovery Manager', 'Head of Nature Recovery', 'Head of Food System Transformation',
    'Wild Ingleborough Manager', 'Three Dales Project Development Manager',
    'Project Leader', 'Workstream Lead', 'Project Lead', 'Service Manager',
    'Network Development Coordinator', 'Director of Services', 'Programmes',
    'Monitoring Coordinator', 'Planning Senior Adviser - Major Casework',
    'Senior Reserves Manager', 'Projects Manager', 'Nature Restoration Manager',
    'Strategic Plans and Green Infrastructure', 'Impact Coordinator',
    'Customer Infrastructure Partner', 'Schools Development Coordinator',
    'Infrastructure Planning', 'Programme Management', 'Contract Manager',
    'Contracts Manager', 'Contracts Supervisor', 'Contract Management',
    'Project Surveyor', 'Senior Programme Specialist', 'Build Coordinator',
    'Events Coordinator', 'INNS Coordinator', 'Risk Management Officer',
    'Catchment Lead', 'Project Team Manager', 'Places Planning Specialist',
    'HS2 Manager', 'Programme Delivery Advisor', 'Manager Smarth Growth',
    'Delivery Manager', 'Estate Manage', 'Senior Managing Consultant',
    'Manager Business Applications Technology', 'Global Director',
    'Programs Coordinator', 'Publishing Systems Coordinator', 'Group Planning',
    'Coordinator – Climate Program', 'Customer Excellence Lead',
    'Programme Coordination', 'National Monitoring Technical Officer',
    'Project Controls Manager', 'Project Development Coordination',
    'Carbon Inventory - Manager', 'Carbon Management - Senior Manager',
    'Wilder Childhood Manager', 'Manager - Vehicle Development Workshop',
    'Vehicle Development Workshop Manager', 'Project Management',
    'Network Co-ordinator', 'Planning Manager', 'Alne Wood Park Manager',
    'Director of Green Infrastructure', 'Head of Forests', 'Development Manager',
    'Scotland Manager', 'Ireland Manager', 'Contract Coordinator',
    'Packaging Manager', 'Director of Change', 'Programme Co-ordinator',
    'Healthy Streets Officer', 'Installation Manager', 'Woodland Lead Adviser', 'Head of Delivery', 'CI Practitioner', 'Head of Scheme Delivery', 'Charging Solutions Energy Lead', 'Land Advice Service Manager', 'Awards Manager', 'Head of Behaviour Change', 'PMO', 'Project Development Lead', 'Head of Change Enablement', 'Resilience Manager', 'Design Authority', 'Project Co-ordinator', 'Global Director', 'Director of Environment', 'Innovation Lead', 'Retrofit Coordinator', 'Regional Manager', 'Project Planner', 'Project Development'
]
research = [
    'Researcher', 'Research', 'Evaluation Senior Specialist', 'Asset Manager',
    'Evidence Officer', 'Evaluation Officer'
]
rewilding = [
    'Rewilding', 'Wild Spaces Officer', 'Wilder Marches', 'Nature Recovery',
    'Nature-Based', 'Nature Based', 'NBS', 'Nature Restoration',
    'Wild Ingleborough', 'Three Dales Project', 'Wilder Nottinghamshire',
    'Landscape Recovery', 'Ponds Officer', 'Tree Action Plan',
    'Natural Capital & Ecosystem Assessment', 'Beaver', 'Reintroduction',
    'Bison', 'Wildcat', 'Pine Marten', 'Treescapes', 'Eelscapes',
    'Forest Creation', 'Natural Capital', 'Peatland Code', 'Landscape Partnership',
    'Wilder Engagement', 'Wilder Rivers', 'Restoring', 'Trillion Trees',
    'Nature North', 'Advisor for Trees', 'Kelp', 'Restoration', 'Pool Frog',
    'Woodland Hope', 'Urban Forestry', 'Stork', 'Mussel', 'Corncrake',
    'Seagrass', 'Atlantic Rainforest', 'Get the Marches Buzzing', 'Natural Solutions',
    'Wigan Greenheart', 'Working Wetlands', 'Woodland Lead Adviser', 'Wilder Landscapes', 'Managing Moors', 'Woodland Creation', 'Forestry Intern', 'Tree Nursery', 'Local Wildlife Sites', 'Wilder Ouse', 'Wilder', 'NPP', 'Northumberland Peat Partnership'
]
sales = [
    'Sales', 'Fundraising', 'Commercial Lead', 'Account Executive', 'Donor', 'Membership Manager',
    'Commercial Manager', 'Fundraiser', 'Individual Giving', 'Bid Development',
    'Philanthropy', 'Legacy Giving', 'Membership Recruiter', 'Grant', 'Trusts',
    'In Memory', 'In Memoriam', 'Membership Officer', 'Electrical Estimator', 'Philanthropy Manager',
    'Revenue Operations', 'Development Officer', 'Head of Independent Partners',
    'Supporter Experience', 'Client Associate', 'Development Manager', 'Development Assistant',
    'Income Generation', 'Information Officer', 'Bid Manager', 'Wholesale Lead',
    'Public Funding', 'Charges Team', 'Licensing', 'Development Coordinator', 'Lead Generation',
    'Major Giving', 'Legacies', 'Field Activation', 'Novel CDR Business', 'Income Advisor', 'Climate Contribution Fund', 'Funding', 'SDR'
]
science = [
    'Science', 'R&D', 'Bioinformatics', 'Hydrologist', 'Scientific', 'Scientist',
    'Research and Development', 'Innovation Researcher', 'Aquarist', 'Plasma',
    'Physicist', 'Spectroscopy', 'Cryogenic', 'Geomorphology', 'Hydrology',
    'Contaminated Land', 'Groundwater Quality', 'Radiolog', 'Nuclear',
    'Radioactiv', 'Hydrometry', 'Telemetry', 'Environment Monitoring',
    'Environmental Monitoring', 'Hydrogeologist', 'Geomorphologist',
    'Lab Tech', 'Evaluation Senior Specialist', 'Cell Projects', 'Assay Develop',
    'Laboratory Technician', 'Process Technologist', 'Summer Placement',
    'Academic Internship', 'Stem Cell', 'Geochemical', 'Biolog', 'Bioprocess',
    'Field Technician', 'DNA', 'Physics', 'Chemical Engineering', 'Entomology', 'Bid Coordinator'
]
software = [
    'Software', 'Firmware', 'Android', 'Java', 'Python', 'Backend',
    'Back End', 'Back-End', 'Frontend', 'Front End', 'Front-End',
    'Javascript', 'Data Engineer', 'CTO', 'Developer', 'Data Science',
    'Data Scientist', 'ML', 'Machine Learning', 'AI', 'Artificial Intelligence',
    'Remote Sensing', 'Algorithm', 'Cloud Services', 'DevOps', 'Dev Ops',
    'Devops', 'Full Stack', 'Full-Stack', 'Fullstack', 'Agile', 'QA Tester',
    'QA Engineer', 'Mobile', 'iOS', 'Platform Engineer', 'SQA', 'SW Engineer',
    'SW Developer', 'SW Test', 'Agile Lead', 'Technical Lead', 'SRE',
    'Site Reliability Engineer', 'BI Engineer', 'Business Intelligence Engineer',
    '.NET', 'Support Engineer', 'C++', 'React Native', 'Next.js', 'QA Lead',
    'Security Engineer', 'Rust', 'TypeScript', 'Haskell', 'Data Acquisition',
    'Test Engineer - Control Systems', 'Cloud Architect', 'Security Analyst',
    'Security Architect', 'Infotainment', 'ETRM Developer', 'Enterprise Architect',
    'Chief Technical Officer', 'Tech Lead', 'NetOps', 'Network Operations',
    'Golang', 'Data Warehouse', 'Kafka', 'Web Developer', 'Network Cloud',
    'Windows', 'App Developer', 'App Development', 'Web Engineer',
    'Web Development', 'Product Engineer', 'Automation', 'Salesforce Developer',
    'Scala', 'Node', 'Solution Engineer', 'Solutions Engineer', 'Research Scientist (Staff',
    'Quantitative Analyst', 'Platform Architect', 'Enterprise Architecture',
    'Embedded Module Architect', 'Ruby', 'Embedded System Engineer', 'Kotlin',
    'Graduate Developer', 'Technical Architect', 'BMS', 'Energy Optimis',
    'Cloud', 'Network Infrastructure Lead', 'Vice President of Technology',
    'VP of Technology', 'Scrum Master', 'Blockchain', 'QA Manager',
    'Solutions Architect', 'Embedded Engineer', 'Cybersecurity', 'Security Lead', 'Senior Principal Engineer', 'Data Architect', 'Geomatics', 'Head of Technology', 'Digital Threats', 'Release Engineer'
]
sw_or_eng = [
    'Lead Engineer', 'Test Engineer', 'Systems Engineer', 'Head of Engineering',
    'Engineering Manager', 'Senior Engineer', 'Director of Engineering', 'Principal Engineer'
]
trustees = [
    'Trustee', 'Honorary', 'Treasurer', 'Chair of the Board',
    'Member of Bonsucro Board', 'Non Executive Director',
    'Non-Executive Director', 'NED', 'Committee Chair'
]
volunteering = ['Unpaid', 'Volunteer', 'Voluntary']
weird_other_ignore = [
    'Invitation to Tender', 'Your Dream Job',
    'Speculative', 'General Application', 'Talent Pool',
    'Inheritance Tax Exemption Heritage Senior Adviser', 'Open Application',
    'Internal Applicants Only', 'Insert Your Future Role Here',
    'Arborist & Team Leader Opportunities', 'Join Us',
    'General Interest', 'Internal Only', 'Tender', "If You Don'T See the Role You'Re Looking for",
    'There Are Currently No Vacancies', 'Spontaneous Application',
    'No Jobs Openings', 'Future Positions', 'Future Opportunities', 'Have Any Vacancies',
    'Member of Technical Staff', 'Consultancy Opportunity', 'Call for',
    'Internal Applicants Only', 'All Departments', 'No Internal Positions', 'We Do Not Have Any Vacancies', 'Follow Us',
    'Us Director', 'US Director', 'CV Database', 'Copy of', 'All Advert Template', 'Looking to Get the New Board Set up', 'Careeers', 'Chargé', 'Restauration'
]

# Create a dictionary from all those lists so that we can scan them all at once
job_types_dict = {
    '✂️ Admin': admin,
    '✍️ Advocacy & Policy': advocacy,
    '📈 Business Development': bizdev,
    '✊ Campaigning': campaigning,
    '🌍 Climate & Sustainability': climate,
    '👫 Community': community,
    '🐝 Conservation': conservation,
    '🎧 Customer Service': customer_service,
    '📊 Data & Analysis': data,
    '🎨 Design & Creative': design,
    '🐞 Ecology': ecology,
    '⚙️ Engineering': engineering,
    '💰 Finance': finance,
    '👋 HR & Recruitment': hr,
    '💻 IT': it,
    '🧐 Legal & Regulatory': legal,
    '📣 Marketing & Comms': marketing,
    '⏰ Operations & Logistics': operations,
    '❓ Other': other,
    '🍁 Outdoorsy': outdoorsy,
    '🛒 Procurement': procurement,
    '🚀 Product': product,
    '🎯 Project Management': project_mgmt,
    '🤔 Research': research,
    '🌳 Rewilding': rewilding,
    '💵 Sales & Fundraising': sales,
    '🧪 Science': science,
    '🤖 Software': software,
    '⭐️ Trustee': trustees,
    'sw_or_eng': sw_or_eng,
    'Volunteering': volunteering,
    'Weird other': weird_other_ignore
}

# Check each job / row in scraped_jobs
for ind in scraped_jobs.index:
  # Start off with an empty list that we'll populate with the job types
  a = []
  # For each job type, check if one of the defining terms for that job type appears in the job title, then add it to the list if it does
  for type in job_types_dict:
    if any(ele in scraped_jobs['Job Title'][ind]
           for ele in job_types_dict[type]):
      a.append(type)
    # Combine all the job types in the dictionary into a single string
    if a != []:
      b = ", ".join(a)
      # Add the string to the 'job_types' column of the scraped_jobs dataframe
      # NB if the job title didn't match any job types, this will still read 'unmapped'
      scraped_jobs['job_types'][ind] = b

# Print out any jobs that haven't been mapped to any job types (for easy review)
print("These jobs haven't been mapped to any job type:")
print(scraped_jobs[scraped_jobs['job_types'] == 'not mapped'])

# Remove jobs that have been categorised as Weird other, or Volunteering
for ind in scraped_jobs.index:
  if any(x in scraped_jobs['job_types'][ind]
         for x in ['Weird other', 'Volunteering']):
    scraped_jobs.drop(index=ind, inplace=True)

""" Now map each job to its seniority level """

# Create a list of terms for each seniority level, which will be used to map jobs to the right seniority
entry_level = [
    'Junior', 'Assistant', 'Intern', 'Trainee', 'Apprentice', 'Student',
    'Water Engineer', 'intern', 'Graduate', 'Industrial Placement', 'Jr',
    'New to Nature', 'New To Nature', 'Summer Placement', 'Youth Ambassador',
    'Industrial Placement', 'Energy Adviser', 'Energy Advisor', 'Placement',
    'Home Tech Advisor', 'Complaints Advisor', 'Customer Care Advisor',
    'Part Qualified', 'Part-Qualified', 'Customer Service Team Member',
    'Gas Operations Specialist', 'Customer Support Executive', 'Tour Guide', 'Brand Ambassador', 'Packing Operator'
]
management = [
    'Senior', 'Manager', 'Director', 'CEO', 'CTO', 'CMO', 'CPO', 'CFO', 'COO',
    'Head of', 'Leader', 'Lead', 'Controller', 'Chair', 'Principal', 'President',
    'VP', 'Vice President', 'Managing Director', 'MD', 'Management',
    'Board Member', 'Team Leader', 'Chief Executive', 'Chief Technical Officer',
    'Chief Marketing Officer', 'Chief Product Officer', 'Chief of Staff',
    'Chief Financial Officer', 'Chief Operating Officer', 'Foreman', 'Head Of',
    'Staff Product Manager', 'Staff / Sr Staff', 'Sr / Staff',
    'Team Coordinator', 'Governance', 'Recruitment Coordinator', 'Solution Architect', 'Chief Engineer', 'Trustee', 'NED', 'Managing Editor', 'Solutions Architect'
]

# Create a dictionary from those lists so that we can scan them at the same time
seniority_dict = {'👶 Entry Level': entry_level, '👵🏻 Senior': management}

# Check each job / row in scraped_jobs
for ind in scraped_jobs.index:
  # Start off with an empty list that we'll populate with the seniority level (this should eventually be unnecessary when you've improved the mappings enough that nothing gets tagged as both entry level and senior)
  y = []
  # For each seniority level, check if one of the defining terms for that seniority level appears in the job title, then add it to the list if it does
  for seniority in seniority_dict:
    if any(ele in scraped_jobs['Job Title'][ind]
           for ele in seniority_dict[seniority]):
      y.append(seniority)
    # Combine all the job types in the dictionary into a single string
    if y != []:
      z = ", ".join(y)
      # Add the string to the 'seniority' column of the scraped_jobs dataframe
      scraped_jobs['seniority'][ind] = z

# Remove seniority tags that aren't actually correct
# Same procedure as above - start by making the lists of terms that should be used for exclusion
not_entry_level = [
    'International', 'Business Partner', 'Marketing Manager', 'Senior',
    'Contract Manager', 'Development Manager', 'Assistant Manager', 'Internal',
    'Account Manager', 'Accounts Manager', 'Retail Manager',
    'Communications Manager', 'Sales Manager'
]
not_management = [
    'Assistant', 'Junior', 'Graduate', 'Trainee', 'Project Manage',
    'Account Manager', 'Management Accountant', 'Social Media Manage',
    'Office Manager', 'Change Management Engineer', 'Relationship Manager',
    'Relationships Manager', 'Database Manager', 'Product Manager',
    'Contracts Manage', 'Nursery Manager', 'Nature Connection Manager'
]
definitely_management = [
    'Senior', 'Director', 'Head of', 'Lead', 'Chair', 'Team Leader', 'Foreman',
    'Key Account Manager'
]

# Then make a dictionary from those lists
not_seniority_dict = {
    'Not Entry Level': not_entry_level,
    'Not Management': not_management,
    'Definitely Management': definitely_management
}

# Now for each job, check if the job title contains any of the terms that would mean it's not actually entry level, then remove the entry level tag if it was given one erroneously
for ind in scraped_jobs.index:
  if any(ele in scraped_jobs['Job Title'][ind]
         for ele in not_seniority_dict['Not Entry Level']):
    scraped_jobs['seniority'][ind] = scraped_jobs['seniority'][ind].replace(
        "👶 Entry Level", "mid level")
  # And then same deal for the management tag
  if any(ele in scraped_jobs['Job Title'][ind]
         for ele in not_seniority_dict['Not Management']):
    # But make sure we're not removing the management tag from any that definitely are management
    if not any(ele in scraped_jobs['Job Title'][ind]
               for ele in not_seniority_dict['Definitely Management']):
      scraped_jobs['seniority'][ind] = scraped_jobs['seniority'][ind].replace(
          "👵🏻 Senior", "mid level")

# Occasionally we can end up with a job where the seniority has now been classed as "mid level, mid level" which causes an error due to duplication when we try to send it to Airtable later on
for ind in scraped_jobs.index:
  scraped_jobs['seniority'][ind] = scraped_jobs['seniority'][ind].replace(
      "mid level, mid level", "mid level")

# Export all the jobs (with their new locations and job type categorisations and seniority levels) as csv
scraped_jobs.to_csv('categorised_jobs.csv', index=False)
