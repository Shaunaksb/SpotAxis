#!/bin/bash
# -*- ENCODING: UTF-8 -*-
# If you are in a virtualenv you need to activate it before you can run ./manage.py 'command'
# source path/to/your/virtualenv/bin/activate
echo " "
echo "Starting Copy of Records..."
echo "-----------------------------------"
echo "Common Records"
echo "Copying..."
# uv run python manage.py loaddata common_industry
# uv run python manage.py loaddata common_area
uv run python manage.py loaddata common_country
uv run python manage.py loaddata common_currency
# uv run python manage.py loaddata common_state
# uv run python manage.py loaddata common_municipal
uv run python manage.py loaddata common_degree
uv run python manage.py loaddata common_employment_type
uv run python manage.py loaddata common_gender
# uv run python manage.py loaddata common_identification_doc
uv run python manage.py loaddata common_marital_status
uv run python manage.py loaddata common_profile
echo "Common Records Copied"
echo " "
echo "-------------------------------------"
echo " "
echo "Company Records"
echo "Copying..."
uv run python manage.py loaddata companies_company_industry
# uv run python manage.py loaddata companies_company_area
# uv run python manage.py loaddata companies_recommendation_status
echo "Company Records copied"
echo " "
echo "-------------------------------------"
echo " "
echo "Custom Field Records"
echo "Copying..."
uv run python manage.py loaddata customfield_fieldclassification
uv run python manage.py loaddata customfield_fieldtype
echo "Custom Field Records copied"
echo " "
echo "-------------------------------------"
echo " "
echo "Job Records"
echo "Copying..."
uv run python manage.py loaddata vacancies_employment_experience
uv run python manage.py loaddata vacancies_salary_type
uv run python manage.py loaddata vacancies_pubdate_search
uv run python manage.py loaddata vacancies_vacancy_status
echo "Job Records Copied"
echo " "
echo "-------------------------------------"
echo " "
echo "Candidate Records"
echo "Copying..."
uv run python manage.py loaddata candidates_academic_area
# uv run python manage.py loaddata candidates_academic_career
# uv run python manage.py loaddata candidates_school_type
uv run python manage.py loaddata candidates_academic_status
uv run python manage.py loaddata candidates_language
# uv run python manage.py loaddata candidates_language_level
# uv run python manage.py loaddata candidates_software
# uv run python manage.py loaddata candidates_software_level
echo "Candidate Records Copied"
echo " "
echo "-------------------------------------"
echo " "
echo "Payment Records"
echo "Copying..."
uv run python manage.py loaddata payments_servicecategory
uv run python manage.py loaddata payments_services
uv run python manage.py loaddata payments_package
uv run python manage.py loaddata payments_priceslab
uv run python manage.py loaddata payments_discount
echo "Payment Records Copied"
echo "-------------------------------------"
echo "Copy of Records Completed."
echo " "