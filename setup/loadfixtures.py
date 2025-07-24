import subprocess

def run_loaddata(fixture):
    """Run the loaddata manage.py command for a given fixture name."""
    print(f"Loading fixture: {fixture} ...")
    result = subprocess.run(
        ["uv", "run", "python", "manage.py", "loaddata", fixture],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print(f"✅ {fixture} loaded successfully.\n")
    else:
        print(f"❌ Error loading {fixture}:\n{result.stderr}\n")

def loadfixtures():
    """Run the full sequence of loaddata commands, organized by section."""
    sections = [
        ("Common Records", [
            # "common_industry",
            # "common_area",
            "common_country",
            "common_currency",
            # "common_state",
            # "common_municipal",
            "common_degree",
            "common_employment_type",
            "common_gender",
            # "common_identification_doc",
            "common_marital_status",
            "common_profile",
        ]),
        ("Company Records", [
            "companies_company_industry",
            # "companies_company_area",
            # "companies_recommendation_status",
        ]),
        ("Custom Field Records", [
            "customfield_fieldclassification",
            "customfield_fieldtype",
        ]),
        ("Job Records", [
            "vacancies_employment_experience",
            "vacancies_salary_type",
            "vacancies_pubdate_search",
            "vacancies_vacancy_status",
        ]),
        ("Candidate Records", [
            "candidates_academic_area",
            # "candidates_academic_career",
            # "candidates_school_type",
            "candidates_academic_status",
            "candidates_language",
            # "candidates_language_level",
            # "candidates_software",
            # "candidates_software_level",
        ]),
        ("Payment Records", [
            "payments_servicecategory",
            "payments_services",
            "payments_package",
            "payments_priceslab",
            "payments_discount",
        ])
    ]

    print("\nStarting Copy of Records...")
    print("-----------------------------------\n")

    for section_title, fixture_list in sections:
        print(f"{section_title}")
        print("Copying...")
        for fixture in fixture_list:
            run_loaddata(fixture)
        print(f"{section_title} Copied\n")
        print("-------------------------------------\n")

    print("Copy of Records Completed.\n")

if __name__ == "__main__":
    loadfixtures()
