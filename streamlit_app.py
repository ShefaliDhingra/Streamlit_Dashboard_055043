# General import section
import pandas as pd 
import streamlit as st 
from io import StringIO 
import os 

# Streamlit main page configuration
st.set_page_config(page_title="DEVP Dashboard",
                    page_icon=None,
                    layout="wide",
                    initial_sidebar_state="expanded",
                    menu_items=None)

# App import
import Welcome_Page
import Data_Preview
import Data_Visualization
import Observations
import Managerial_Insights

# Data object class
class DataObject():
    """
    Data object class holds a dataframe and its byte size.
    """


# Interface class        
class Interface():
    
    def side_bar(cls, dt_obj):
      """Sidebar configuration and file picker

      :param dt_obj: pandas dataframe object
      :type dt_obj: pandas.core.frame.DataFrame
      """
      dt_obj.data = pd.read_csv("import_export_updated.csv")
      # Data Sampling
      dt_obj.df = pd.DataFrame.sample(dt_obj.data, n=3001, random_state=55043)
      dt_obj.filesize = dt_obj.df.size
      dt_obj.Non_Categorical_Variables=dt_obj.df.Quantity+dt_obj.df.Value+dt_obj.df.Weight
      
        # Side bar navigation menu with a select box
      menu = ['Welcome Page','Data Preview','Data Visualization','Observations','Managerial Insights']
      navigation = st.sidebar.selectbox(label="Select menu", options=menu)

        # Runs 'Data Preview' app
      if navigation == 'Data Preview':
        with st.container():
         Data_Preview.data_preview(dt_obj)

      elif navigation == 'Data Visualization':
        with st.container():
          Data_Visualization.data_visualization(dt_obj)

      elif navigation == 'Observations':
        with st.container():
          Observations.observations()

      elif navigation == 'Managerial Insights':
        with st.container():
          Managerial_Insights.managerial_insights()
      
      else:
        Welcome_Page.welcome()
        
def main():
  """
  Main and its Streamlit configuration
  """            
  data_main = DataObject()
  interface = Interface()
  interface.side_bar(data_main)


# Run Main
if __name__ == '__main__':
  main()
