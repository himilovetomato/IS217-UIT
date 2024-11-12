import pandas as pd 

mental_health_replacement = {
	"I have a concentration and/or memory disorder (e.g. ADHD)": "I have a concentration and/or memory disorder (e.g., ADHD, etc.)",
    "I have a mood or emotional disorder (e.g. depression, bipolar disorder)": "I have a mood or emotional disorder (e.g., depression, bipolar disorder, etc.)",
    "I have autism / an autism spectrum disorder (e.g. Asperger's)": "I have autism / an autism spectrum disorder (e.g. Asperger's, etc.)",
    "Or, in your own words:": "In your own words"
}
employment_replacement = {
    "Employed full-time": "Employed, full-time",
    "Employed part-time": "Employed, part-time",
    "Student": "Student, full-time",
    "I prefer not to say": "Prefer not to say"
}
jobtitle_replacement = {
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
    "Cobol": "COBOL"
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
    "Digital Ocean": "DigitalOcean"
}
database_replacement = {
    "Dynamodb": "DynamoDB",
    "Neo4j": "Neo4J",
    "Couch DB": "CouchDB"
}
misc_tech_tools_replacement = {
    "Scikit-learn": "Scikit-Learn",
    "Spring": "Spring Framework"
}
collab_tools_replacement = {
    "Goland": "GoLand",
    "IntelliJ": "IntelliJ IDEA",
    "IPython": "IPython/Jupyter",
    "Jupyter Notebook/JupyterLab": "IPython/Jupyter",
    "NetBeans": "Netbeans",
    "PhpStorm": "PHPStorm",
    "Rad Studio (Delphi, C++ Builder)": "RAD Studio (Delphi, C++ Builder)",
    "WebStorm": "WebStorm"
}

office_stack_async_replacement = {
    "Clickup": "ClickUp",
    "Dingtalk (Teambition)": "DingTalk (Teambition)",
    "Jira Work Management": "Jira",
    "monday.com": "Monday.com",
    "Ringcentral": "RingCentral"
}
web_framework_replacement = {
    "Angular": "Angular.js",
    "AngularJS": "Angular.js",
    "Angular/Angular.js": "Angular.js",
    "ASP.NET Core": "ASP.NET CORE",
    "React": "React.js"
}

def standardize_values(column, replacement_dict):
    def replace_values(cell):
        if pd.isna(cell):
            return cell
        values = cell.split(';')
        replaced_values = [replacement_dict.get(value.strip(), value) for value in values]
        return ';'.join(replaced_values)
    return column.apply(replace_values)

def standardize_column(df, column_name, replacement_dict):
    df[column_name] = standardize_values(df[column_name], replacement_dict)
    
def main():
    input_path = "your_path"
    output_path = "your_path"
    
    try:
        df = pd.read_csv(input_path, encoding='UTF-8', low_memory=False)
	    
        standardize_column(df, "Employment", employment_replacement)
        standardize_column(df, "PlatformHaveWorkedWith", platform_replacement)
        standardize_column(df, "LanguageHaveWorkedWith", programming_language_replacement)
        standardize_column(df, "DatabaseHaveWorkedWith", database_replacement)
        standardize_column(df, "MiscTechHaveWorkedWith", misc_tech_tools_replacement)
        standardize_column(df, "NEWCollabToolsHaveWorkedWith", collab_tools_replacement)
        standardize_column(df, "OfficeStackAsyncHaveWorkedWith", office_stack_async_replacement)
        standardize_column(df, "WebFrameHaveWorkedWith", web_framework_replacement)
        standardize_column(df, "MentalHealth", mental_health_replacement)
        standardize_column(df, "DevType", jobtitle_replacement)

        df.to_csv(output_path, index=False)
    except Exception as e:
        print(f"Error processing file: {e}")
        
if __name__ == "__main__":
    main()
