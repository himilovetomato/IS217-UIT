import pandas as pd 

def replace_multiple_values(column, replacement_dict):
    def replace_values(cell):
        if pd.isna(cell):
            return cell
        values = cell.split(';')
        replaced_values = [replacement_dict.get(value.strip(), value) for value in values]
        return ';'.join(replaced_values)
    
    return column.apply(replace_values)

mental_health_replace_dict = {
	"I have a concentration and/or memory disorder (e.g. ADHD)": "I have a concentration and/or memory disorder (e.g., ADHD, etc.)",
    "I have a mood or emotional disorder (e.g. depression, bipolar disorder)": "I have a mood or emotional disorder (e.g., depression, bipolar disorder, etc.)",
    "I have autism / an autism spectrum disorder (e.g. Asperger's)": "I have autism / an autism spectrum disorder (e.g. Asperger's, etc.)",
    "Or, in your own words:": "In your own words"
}

employment_replacement_dict = {
    "Employed full-time": "Employed, full-time",
    "Employed part-time": "Employed, part-time",
    "Student": "Student, full-time",
    "I prefer not to say": "Prefer not to say"
}

jobtitle_replacement_dict = {
    "Data engineer": "Data Engineer",
    "Engineer, data": "Data Engineer",
    "Senior Executive (C-Suite, VP, etc.)": "Senior Executive",
    "Senior executive/VP": "Senior Executive",
    "System administrator": "Systems Administrator",
    "Security professional": "Security Specialist",
    "Developer, AI": "AI Developer",
    "Developer, back-end": "Back-End Developer",
    "Developer, desktop or enterprise applications": "Desktop/Enterprise Applications Developer",
    "Developer, embedded applications or devices": "Embedded Applications Developer",
    "Developer, front-end": "Front-End Developer",
    "Developer, full-stack": "Full-Stack Developer",
    "Developer, game or graphics": "Game/Graphics Developer",
    "Developer, mobile": "Mobile Developer",
    "Developer, QA or test": "QA/Test Developer",
    "Engineer, site reliability": "Site Reliability Engineer",
    "Other (please specify):": "Others"
}
programming_language_replacement = {
    "Bash/Shell (all shells)": "Bash/Shell",
    "LISP": "lisp",
    "Cobol": "COBOL",
    "Other(s):": "Others"
}

platform_replacement = {
    "Matlab": "MATLAB",
    "Amazon Web Service": "AWS",
    "Amazon Web Services (AWS)": "AWS",
    "Google Cloud": "Google Cloud Platform",
    "IBM Cloud Or Watson": "IBM Cloud Or Watson",
    "Linode, now Akamai": "Akamai",
    "Linode": "Akamai",
    "Oracle Cloud Infrastructure (OCI)": "Oracle Cloud Infrastructure",
    "Digital Ocean": "DigitalOcean",
    "Other(s):": "Others"
}
database_replacement = {
    "Dynamodb": "DynamoDB",
    "Neo4j": "Neo4J",
    "Couch DB": "CouchDB",
    "Other(s):": "Others"
}
misc_tech_tools_replacement = {
    "Scikit-learn": "Scikit-Learn",
    "Spring": "Spring Framework",
    "Other(s):": "Others"
}
collab_tools_replacement = {
    "Goland": "GoLand",
    "IntelliJ": "IntelliJ IDEA",
    "IPython": "IPython/Jupyter",
    "Jupyter Notebook/JupyterLab": "IPython/Jupyter",
    "NetBeans": "Netbeans",
    "PhpStorm": "PHPStorm",
    "Rad Studio (Delphi, C++ Builder)": "RAD Studio (Delphi, C++ Builder)",
    "WebStorm": "WebStorm",
    "Other(s):": "Others"
}
office_stack_async_replacement = {
    "Clickup": "ClickUp",
    "Dingtalk (Teambition)": "DingTalk (Teambition)",
    "Jira Work Management": "Jira",
    "monday.com": "Monday.com",
    "Ringcentral": "RingCentral",
    "Other(s):": "Others"
}
web_framework_replacement = {
    "Angular": "Angular.js",
    "AngularJS": "Angular.js",
    "Angular/Angular.js": "Angular.js",
    "ASP.NET Core": "ASP.NET CORE",
    "React": "React.js",
    "Other(s):": "Others"
}

ai_tool_currently_using_replacement = {
    "Other (please describe)": "Others",
    "Other (please specify):": "Others",
    "Other(s):": "Others"
}

df = pd.read_csv("../6years_preprocessing.csv", low_memory=False)

df["Employment"] = replace_multiple_values(df["Employment"], employment_replacement_dict)
df["PlatformHaveWorkedWith"] = replace_multiple_values(df["PlatformHaveWorkedWith"], platform_replacement)
df["LanguageHaveWorkedWith"] = replace_multiple_values(df["LanguageHaveWorkedWith"], programming_language_replacement)
df["DatabaseHaveWorkedWith"] = replace_multiple_values(df["DatabaseHaveWorkedWith"], database_replacement)
df["MiscTechHaveWorkedWith"] = replace_multiple_values(df["MiscTechHaveWorkedWith"], misc_tech_tools_replacement)
df["NEWCollabToolsHaveWorkedWith"] = replace_multiple_values(df["NEWCollabToolsHaveWorkedWith"], collab_tools_replacement) 
df["OfficeStackAsyncHaveWorkedWith"] = replace_multiple_values(df["OfficeStackAsyncHaveWorkedWith"], office_stack_async_replacement)
df["WebFrameHaveWorkedWith"] = replace_multiple_values(df["WebFrameHaveWorkedWith"], web_framework_replacement)
df["MentalHealth"] = replace_multiple_values(df["MentalHealth"], mental_health_replace_dict)
df["DevType"] =replace_multiple_values(df["DevType"], jobtitle_replacement_dict)
df["AIToolCurrently Using"] = replace_multiple_values(df["AIToolCurrently Using"], ai_tool_currently_using_replacement)

df.to_csv("../6years_preprocessing.csv", index=False)
