#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#reading data gotten from task 1
summary = pd.read_csv('summary_report.csv')
financials = pd.read_csv('financial_report.csv')


# In[4]:


financials


# In[5]:


summary


# In[8]:


def financial_chatbot():
    print("\n Please entery your query")
    user_query = input()
    if user_query == "what is the total revenue?":
        revenue = financials[(financials['Year'] == fiscal_year) & (financials['Company'] == company_input)]['Total Revenue'].values[0]
        return f"The Total Revenue for {company_input} for fiscal year {fiscal_year} is $ {revenue}"
        
    elif user_query == "what is the Net income?":
        net_income  = financials[(financials['Year'] == fiscal_year) & (financials['Company'] == company_input)]['Net Income'].values[0]
        return f"The Net Income for {company_input} for fiscal year {fiscal_year} is $ {net_income}"
        
    elif user_query == "what is the total assests?":
        total_asset = financials[(financials['Year'] == fiscal_year) & (financials['Company'] == company_input)]['Total Assests'].values[0]
        return f"The Total assests for {company_input} for fiscal year {fiscal_year} is $ {total_asset}"
        
    elif user_query == "what is the total liabilities?":
        tot_lib = financials[(financials['Year'] == fiscal_year) & (financials['Company'] == company_input)]['Total Liabilities'].values[0]
        return f"The Total Liability for {company_input} for fiscal year {fiscal_year} is $ {tot_lib}" 
        
    elif user_query == "what is the cash flow from operating activities?":
        cash_fflow = financials[(financials['Year'] == fiscal_year) & (financials['Company'] == company_input)]['Cash Flow from Operating Activities'].values[0]
        return f"The cash flow from operating activities for {company_input} for fiscal year {fiscal_year} is $ {cash_fflow}"
        
    elif user_query == "what is the revenue growth?":
        revenue_growth = financials[(financials['Year'] == fiscal_year) & (financials['Company'] == company_input)]['Revenue Growth (%)'].values[0].round(3)
        return f"The Revenue growth for {company_input} for fiscal year {fiscal_year} is {revenue_growth}(%)"
        
    elif user_query == "what is the net income growth?":
        ni_growth = financials[(financials['Year'] == fiscal_year) & (financials['Company'] == company_input)]['Net Income Growth (%)'].values[0].round(3)
        return f"The Net Income Growth for {company_input} for fiscal year {fiscal_year} is {ni_growth}(%)"
        
    elif user_query == "what is the total assets growth?":
        ta_growth = financials[(financials['Year'] == fiscal_year) & (financials['Company'] == company_input)]['Total Assests Change (%)'].values[0].round(3)
        return f"The Total assets growth for {company_input} for fiscal year {fiscal_year} is {ta_growth}(%)"
        
    elif user_query == "what is the total liabiities growth?":
        tl_growth = financials[(financials['Year'] == fiscal_year) & (financials['Company'] == company_input)]['Total Liabilities Change (%)'].values[0].round(3)
        return f"The Total liabilities growth for {company_input} for fiscal year {fiscal_year} is {tl_growth}(%)"
        
    elif user_query == "what is the cash from operating activities growth?":
        cash_growth = financials[(financials['Year'] == fiscal_year) & (financials['Company'] == company_input)]['Cash Flow Operating Activities Change (%)'].values[0].round(3)
        return f"The Cash from operating activities growth for {company_input} for fiscal year {fiscal_year} is {cash_growth}(%)"
        
    elif user_query == "what is the average yearly revenue growth?":
        revenue_year_growth = summary[(summary['Company'] == company_input)]['Revenue Growth (%)'].values[0].round(3)
        return f"The average yearly revenue growth for {company_input} form 2021 to 2023 is {revenue_year_growth}(%)"
        
    elif user_query == "what is the average yearly net income growth?":
        ni_year_growth = summary[(summary['Company'] == company_input)]['Net Income Growth (%)'].values[0].round(3)
        return f"The average yearly net income growth for {company_input} form 2021 to 2023 is {ni_year_growth}(%)"
        
    elif user_query == "what is the average yearly total assets growth?":
        ta_year_growth = summary[(financials['Company'] == company_input)]['Total Assets Change (%)'].values[0].round(3)
        return f"The average yearly total assets growth for {company_input} form 2021 to 2023 is {ta_year_growth}(%)"
        
    elif user_query == "what is the average yearly total liabilities growth?":
        tl_year_growth = summary[(financials['Company'] == company_input)]['Total Liabilities Change (%)'].values[0].round(3)
        return f"The average yearly total liabilities growth for {company_input} form 2021 to 2023 is {tl_year_growth}(%)"
        
    elif user_query == "what is the average yearly cash flow from operating activities growth?":
        cash_year_growth = summary[(financials['Company'] == company_input)]['Cash Flow Operating Activities Change (%)'].values[0].round(3)
        return f"The average yearly total assets growth for {company_input} form 2021 to 2023 is {cash_year_growth}(%)"
        
    else:
        return "Sorry, I cannot only provide information on the predetermined query."
# testing the chatbot
while True:
    print("----------------------------------------------------------------------------")
    user_input = input("\nEnter Hi to start the chatbot session; type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    elif user_input.lower() == "hi":
        print("\nHello! Welcome to AI Driven Financial Chatbot!!!")
        print("\nI can help you with your financial queries")
        print("Please select the company name from below: -")
        print("\n1.Microsoft \n2.Tesla \n3.Apple")
        company_input = input("Enter company name : ").capitalize()
        if company_input not in ['Apple', 'Microsoft', 'Tesla']:
            print("Invalid Company Name. Please check and enter correct company name by starting the chatbot session again")
            break
        else:
            print("\nThe data for the fiscal year 2023, 2022, and 2021 is currently available")
            fiscal_year = int(input("The fiscal year for the selected company : "))
            if fiscal_year not in [2023, 2022, 2021]:
                print("Please enter a valid fiscal year by starting the chatbot session again")
                break
            else:
                response = financial_chatbot()
                print(response)
       
    else:
        print("Enter 'Hi' Properly!!!!! by starting the chatbot session again")
        break 


# In[ ]:




