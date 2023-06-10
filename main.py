import streamlit as st
import requests
import pandas as pd
import numpy as np
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from matplotlib import pyplot as plt
import matplotlib
import json


matplotlib.use('TkAgg')


class Project:
    def __init__(self, saleDate):

        self.saleDate1 = saleDate


    def set_ownerName(self, value):
        self.ownername = value

    def get_ownerName(self):
        return self.ownername


    def set_saleDate(self, value):
        self.saleDate1 = value

    def get_saleDate(self):
        return self.saleDate1

    def set_welcomeDate(self, value):
        self.welcomeCallCompleteDate2 = value

    def get_welcomeDate(self):
        return self.welcomeCallCompleteDate2

    def set_installer(self, value):
        self.installer = value

    def get_installer(self):
        return self.installer
    def set_qualityCheckDate(self, value):
        self.qualityCheckDate5 = value

    def get_qualityCheckDate(self):
        return self.qualityCheckDate5

    def set_siteSurveyComplete(self, value):
        self.siteSurveyCompleteDate3 = value

    def get_siteSurveyComplete(self):
        return self.siteSurveyComplete3

    def set_NTPDate(self, value):
        self.NTPDate4 = value

    def get_NTPDate(self):
        return self.NTPDate4

    def set_solarPlans(self, value):
        self.solarPlans6 = value

    def get_solarPlans(self):
            return self.solarPlans6

    def set_solarInstall(self, value):
        self.solarInstall7 = value

    def get_solarinstall(self):
     return self.solarInstall7

    def set_FinalInspection(self, value):
      self.FinalInspection = value

    def get_FinalInspection(self):
         return self.FinalInspection

    def set_PTO(self, value):
      self.PTO = value

    def get_PTO(self):
         return self.PTO

    def set_Address(self, value):
       self.address = value

    def get_Address(self):
       return self.address

    def set_Completed(self, value):
        self.Completed = value

    def get_Compelted(self):
        return self.Completed



# Set the base URL for the QuickBase API
base_url = "https://api.quickbase.com/v1"

# Setting QuickBase realm and application tokens
realm = "voltaic.quickbase.com"
app_token = "b7738j_qjt3_0_dkaew43bvzcxutbu9q4e6crw3ei3"

# Setting the API endpoint for the desired QuickBase table
table_id = "your_table_id"


# user token:
#   QB-USER-TOKEN b7738j_qjt3_0_dkaew43bvzcxutbu9q4e6crw3ei3

#    private static final String QB_DOMAIN = "voltaic.quickbase.com";

#https://api.quickbase.com/v1/reports/321/run?tableId=br5cqr4r3
# api_endpoint = f"/tables/{table_id}/records"

api_endpoint = f"/reports/520/run?tableId=br5cqr4r3"

# Setting the headers with the required authentication and content type
headers = {
    "QB-Realm-Hostname": realm,
    "Authorization": f"QB-USER-TOKEN {app_token}",
    "Content-Type": "application/json"
}

# Setting the data to be sent in the request
# data = {
#     "fields": {
#         "Field1": "Value1",
#         "Field2": "Value2",
#         "Field3": "Value3"
#     }
# }

# Sending a POST request to create a new record in the QuickBase table
response = requests.post(f"{base_url}{api_endpoint}", headers=headers)

# Checking the response status code
if response.status_code == 200:
    st.write("Loaded Volatic Data Successfully!")
    records_json = response.json()
    # Creating a list to hold project models
    project_models = []

    parsed_response = json.loads(response.text)
    pretty_response = json.dumps(parsed_response, indent=4)
    # print(pretty_response)
    try:
        for record in  records_json.get("data", []):

            # print("RECORD!")
            # print(record)
            homeownerName = record.get("105").get("value")
            saleDate = record.get("102").get("value")
            address = record.get("92").get("value")
            welcomeDate = record.get("1377").get("value")
            siteSurveyDate = record.get("1641").get("value")
            NTPDate = record.get("862").get("value")
            QualityControlCheckDate = record.get("856").get("value")
            SolarPlansDate = record.get("1445").get("value")
            SolarPermitDate = record.get("1346").get("value")
            SolarInstallDate = record.get("877").get("value")
            FinalInspectionDate = record.get("883").get("value")
            PTODate = record.get("889").get("value")
            instaler = record.get("634").get("value")
            CompletedDate = record.get("889").get("value")
            #
            # print(saleDate)
            # print(welcomeDate)


            # Create project model and add it to the list

            project_model = Project(saleDate)
            project_model.set_ownerName(homeownerName)
            project_model.set_welcomeDate(welcomeDate)
            project_model.set_siteSurveyComplete(siteSurveyDate)
            project_model.set_NTPDate(NTPDate)
            project_model.set_qualityCheckDate(QualityControlCheckDate)
            project_model.set_solarPlans(SolarPlansDate)
            project_model.set_solarInstall(SolarInstallDate)
            project_model.set_installer(instaler)
            project_model.set_Address(address)
            project_model.set_FinalInspection(FinalInspectionDate)
            project_model.set_PTO(PTODate)
            project_model.set_Completed(CompletedDate)



            project_models.append(project_model)


        # Convert project models into a DataFrame
        data = {
            "homeownerName": [project.ownername for project in project_models],
            "installer": [project.installer for project in project_models],
            "address": [project.address for project in project_models],
            "SaleDate1": [project.saleDate1 for project in project_models],
            "WelcomeCallDate2": [project.welcomeCallCompleteDate2 for project in project_models],
            "siteSurveyDate3": [project.siteSurveyCompleteDate3 for project in project_models],
            "noticeToPermitDate4": [project.NTPDate4 for project in project_models],
            "QualityCheckDate5": [project.qualityCheckDate5 for project in project_models],
            "SolarPlansReceivedDate6": [project.solarPlans6 for project in project_models],
            "SolarPermitReceiveDate7": [project.solarPlans6 for project in project_models],
            "SolarInstallCompleteDate8": [project.solarInstall7 for project in project_models],
            "FinalInspectionDate9": [project.FinalInspection for project in project_models],
            "PermissionToOperateApprovedDate10": [project.PTO for project in project_models],
            "ProjectCompleteDate11": [project.Completed for project in project_models]


        }
        df = pd.DataFrame(data)

        # Convert date columns to datetime format
        date_cols = [ "SaleDate1", "WelcomeCallDate2", "siteSurveyDate3", "noticeToPermitDate4", "QualityCheckDate5",
                     "SolarPlansReceivedDate6", "SolarPermitReceiveDate7", "SolarInstallCompleteDate8", "FinalInspectionDate9", "PermissionToOperateApprovedDate10",
                     "ProjectCompleteDate11"]

        df[date_cols] = df[date_cols].apply(pd.to_datetime)

        # Calculate duration for each stage
        duration_cols = []
        for i in range(1, len(date_cols)):
            duration_col = f"StageDuration{i}"
            df[duration_col] = (df[date_cols[i]] - df[date_cols[i - 1]]).dt.days
            duration_cols.append(duration_col)

        # Create a new DataFrame with durations
        new_df = df[[ "homeownerName","address", "installer"] + duration_cols]

        # Display the DataFrame in Streamlit
        # st.write(df)

        st.write("Date Dataframe")
        # Print the DataFrame
        st.dataframe(df)

        # st.write("Duration Dataframe")
        # st.dataframe(new_df)


        # Create three separate dataframes based on unique identifiers
        df_1 = df[df['installer'] == 'Voltaic Construction']
        df_2 = df[df['installer'] == 'Greenspire']
        df_3 = df[df['installer'] == 'AC/DC']
        df_4 = df[df['installer'] == 'Proclaim Solar']
        df_5 = df[df['installer'] == 'Titanium Solar']
        df_6 = df[df['installer'] == 'Energy Service Partners']

        #installer dataframes =========================
        # st.write("Voltaic Construction")
        # st.dataframe(df_1)
        # st.write("Greenspire")
        # st.dataframe(df_2)
        # st.write("AC/DC")
        # st.dataframe(df_3)
        # st.write("Proclaim Solar")
        # st.dataframe(df_4)
        # st.write("Energy Service Partners")
        # st.dataframe(df_5)
        # st.write("Voltaic Construction")
        # st.dataframe(df_6)

        installers_df = [df_1, df_2, df_3,df_4,df_5,df_6]


        # =====================-===========================-TESTING-===========================-===========================
        original_addresses = []
        original_homeowners = []
        original_installers = []
        original_saleDates = []


        # Create an empty DataFrame to store the combined data
        combined_df = pd.DataFrame()

        for installer in installers_df:


            df = installer
            # first_value = df.iloc[0, 1]
            original_addresses.append(df['address'].copy())
            original_homeowners.append(df['homeownerName'].copy())
            original_installers.append(df['installer'].copy())
            original_saleDates.append(df['SaleDate1'].copy())

            # Removing "installer", "homeownerName", "address" columns
            duration_df = df[duration_cols]
            # st.write("Duration Dataframe")
            # st.dataframe(duration_df)

            # Calculate column-wise averages
            column_averages = duration_df.mean()

            try:
                # Fill missing values with column averages and replace negatives with the average
                for column in duration_df.columns:
                    duration_df[column].fillna(column_averages[column], inplace=True)
                    duration_df[column] = duration_df[column].apply(lambda x: column_averages[column] if x < 0 else x)

                # st.write(f'{first_value} injected Avg std deviation')
                # st.dataframe(duration_df)

                # Add original columns back to duration_df
                duration_df['installer'] = original_installers[-1]
                duration_df['address'] = original_addresses[-1]
                duration_df['homeownerName'] = original_homeowners[-1]
                duration_df['SaleDate'] = original_saleDates[-1]


                # Combine the duration_df with the combined_df
                combined_df = pd.concat([combined_df, duration_df])

                # st.write("Updated DataFrame:")
                # st.dataframe(duration_df)


            except Exception as e:
                st.write("Error occurred:", str(e))
            finally:
                print("Completed")

                # st.dataframe(duration_df)



        # Display the combined DataFrame
        st.write("Combined DataFrame:")
        st.dataframe(combined_df)

        # =====================-^^^===========================-TESTING-===========================-^^^===========================

    #    AI stuff

        OPENAI_KEY = "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"
        matplotlib.use('TkAgg')
        llm = OpenAI(OPENAI_KEY)
        # pandas_ai = PandasAI(llm, verbose=True, conversational=False)
        pandas_ai = PandasAI(llm)
        # response = pandas_ai.run(df, "What is the average project duration for each stage by installer?")
        # print(response)

        prompt = st.text_area('What do you want to know about voltaic? ')

        if st.button('Generate'):
            if prompt:
                with st.spinner("Analyzing Voltaic...."):
                    res = pandas_ai.run(combined_df, prompt=prompt)
                    print(res)
                    st.write(res)

            else:
                st.warning("Enter a prompt.")










    except json.JSONDecodeError:
        print("Unable to parse response as JSON.")
    # st.write(response.text)

else:
    st.write(f"Error: {response.status_code} - {response.text}")

