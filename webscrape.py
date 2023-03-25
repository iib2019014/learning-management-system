import pygsheets
import pandas as pd


gc = pygsheets.authorize(service_file='https://docs.google.com/spreadsheets/d/1QQj8gAD9jexgz2OoYEyQOIe7xVSG-0r0FyTDHSAYYg0/edit')


df = pd.DataFrame()