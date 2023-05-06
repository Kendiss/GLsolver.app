import streamlit as st


st.set_page_config(
    page_title='GlSolver', 
    page_icon=':money_with_wings:',
    layout = "wide",)


st.markdown(
    """
    <style>
    [data-testid = "stAppViewContainer"] {
    background-image: url(https://png.pngtree.com/thumb_back/fh260/background/20210526/pngtree-black-and-white-high-end-line-network-technology-background-image_720925.jpg);
    background-size: cover;
    }

    [data-testid = "stHeader"]{
    background-color: rgba(0, 0, 0, 0);
    }

    [data-testid ="stMarkdownContainer"]{
    background-color: rgba(0, 0, 0, 0);
    }

    [data-baseweb = "tab"]{
    background-color: rgba(0, 0, 0, 0);
    }
 

    </style>
    """,
    unsafe_allow_html=True
)




# Homepage
st.markdown("<h1 style='font-size: 48px; font-family: Arial, sans-serif;'>GSolver</h1>", unsafe_allow_html=True)
st.markdown("###")




with st.container():
    left_column, middle_column, right_column = st.columns([1, 5, 1])

with middle_column:

    st.header("Home")
    st.subheader("About us")

    st.divider()

    
    st.markdown( 
        """
        
    :grey[Our team of experienced accounting professionals brings a combined experience of over 35 years in the manufacturing and service industry. With expertise in financial and management accounting, systems,  and more, we provide strategic financial solutions for clients across diverse sectors.]
        
    :grey[We stay up-to-date with the latest developments in the field and leverage cutting-edge technology for accuracy and efficiency. Committed to exceptional customer service, we build long-term relationships based on trust and professionalism.]
    """, unsafe_allow_html=True
    )
    
    st.divider()
    
    st.markdown("###")
    st.markdown("###")


    st.title("Services")
    
    #Container for the buttons
    with st.container():
        left_column, middle_column, right_column = st.columns([1, 1, 1])
        button1 = left_column.button("BookKeeping & Financial Account")
        button2 = right_column.button("Costing and Inventory Accounting")
        middle_column.write("###")
        button3 = middle_column.button("Process Improvement & Automation")
        button4 = left_column.button("Forecast & Budgeting")
        button5 = right_column.button("Coaching and Training")
            
        
            
    

    if button1: 
        st.header("BookKeeping & Financial Accounting")
        st.markdown("""
    1.) Recording financial transactions (QBO, Xero, SAP, NetSuite)


    2.) Maintaining general ledgers

        
    3.) Reconciling accounts 
        
    
    4.) Managing accounts payable and accounts receivable
        
        
    5.) Generating financial reports and analysis



    """)
        
    if button2: 
        st.header("Costing & Inventory Accounting")
        tab1, tab2= st.tabs(["Costing", "Inventory Management",])
        with tab1:
            st.header("Costing")
            st.markdown("""
           
           1.) Calculating standard cost
           
           2.) Developing Analyzing cost behavior (variable and fixed)
           
           3.) Cost accounting systems
           
           4.) Identifying cost savings opportunities
           
           5.) Conducting cost-benefit analysis
           
           """)
        with tab2:
            st.header("Inventory Management")
            st.markdown(""" 
            1.) Tracking inventory levels
            
            2.) Managing inventory replenishment 
            
            3.) Optimize periodic inventory audits/count
            
            4.) Analyzing inventory turnover
            
            5.) Optimizing inventory control systems

            """)
    
    

    if button3:
        st.header("Process Improvement & Automation")
        st.markdown("""
        1.) Comprehensive budget and financial forecast
        
        2.) Financial analysis and reporting
        
        3.) Conducting variance analysis
        
        4.) Financial planning and strategy
        
        5.) Cost optimization and efficiency
        
        6.) Risk management and mitigation
        
        7.) Financial modeling and scenario planning

        
        """)
    

    if button4:
        st.header("Forecast & Budgeting")
        st.markdown("""
        
        1.) Implement accounting software:
        
        &rarr; Accounting software (QBO, Xero, SAP, NetSuite, can automate many tasks, including data entry, reconciliation, and financial reporting. Standardize processes
        
        &rarr; Streamline workflows
        
        2.) Integrate electronic payment systems within the Invoicing module
        
        3.) Implement document management systems
        
        4.) Use data analytics technologies

        
        
        
        """)

    if button5:
        st.header("Coaching & Training")
        st.markdown("""
        1.) Advance Excel Automation
        
        2.) Quick Books Online (QBO)
        
        3.) Xero 
        
        4.) SAP
        
        5.) NetSuite

        
        
        """)
        excel_icon = 'https://upload.wikimedia.org/wikipedia/commons/8/86/Microsoft_Excel_2013_logo.svg'
        st.image(excel_icon, width=20)
    
    st.divider()
    st.markdown("###")
    st.markdown("###")
    st.markdown("###")
    st.markdown("###")
    st.markdown("###")
    
    st.header("Contact Us")
    st.markdown("""
                
Need professional accounting services? 
Contact our experienced team at GL SOLVER for comprehensive financial solutions tailored to your needs. 

Call +63 9955360941, email glsolver@gmail.com, or visit our website at [Website URL]. 

Partner with us for exceptional customer service and expert financial management. 
Contact us now and take the first step towards financial success!

    
""")    

