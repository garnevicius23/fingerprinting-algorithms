import os, csv, sqlite
import csv_to_sqlite 

options = csv_to_sqlite.CsvOptions(typing_style="full", encoding="windows-1250") 
input_files = ["data/data.csv"] # pass in a list of CSV files
csv_to_sqlite.write_csv(input_files, "output.db", options)

con = sqlite3.connect("sqlite/raw_data.db")
cur = con.cursor()
cur.execute("create table raw_data (time,id,lat,lon,C2:9B:38:AF:12:75/09b1e796-8c3b-3475-9e45-a8d31f93649b,C2:9B:38:AF:12:75/0e55db4e-b72e-3e9c-9468-d4ef44cb069c,C2:9B:38:AF:12:75/2ab77db3-5669-3f2c-842a-760e4ae0ef4c,C2:9B:38:AF:12:75/3af9ac1c-c3a5-36f7-a737-4868789e2832,C2:9B:38:AF:12:75/c697eede-6a0a-3d21-8936-3a7f86a830ee,C2:9B:38:AF:12:75/f9c1476f-1603-397a-a451-2a30c91dbe5c,D7:85:88:F5:88:4C/0e55db4e-b72e-3e9c-9468-d4ef44cb069c,D7:85:88:F5:88:4C/3af9ac1c-c3a5-36f7-a737-4868789e2832,D7:85:88:F5:88:4C/66bd8860-6e87-3544-b022-1abaf04ce4ca,D7:85:88:F5:88:4C/c697eede-6a0a-3d21-8936-3a7f86a830ee,D7:85:88:F5:88:4C/c77e7cf1-12bc-36be-9270-c8d56e131eac,D7:85:88:F5:88:4C/d3eedeb6-a50a-35bb-9a2c-d9626d3d4b3e,DA:B5:6B:DD:72:60/09b1e796-8c3b-3475-9e45-a8d31f93649b,DA:B5:6B:DD:72:60/0e55db4e-b72e-3e9c-9468-d4ef44cb069c,DA:B5:6B:DD:72:60/3af9ac1c-c3a5-36f7-a737-4868789e2832,DA:B5:6B:DD:72:60/4552091f-a928-358f-8ae8-be7f9b8d89fe,DA:B5:6B:DD:72:60/66bd8860-6e87-3544-b022-1abaf04ce4ca,DA:B5:6B:DD:72:60/c697eede-6a0a-3d21-8936-3a7f86a830ee,E5:53:1E:24:96:2F/09b1e796-8c3b-3475-9e45-a8d31f93649b,E5:53:1E:24:96:2F/0e55db4e-b72e-3e9c-9468-d4ef44cb069c,E5:53:1E:24:96:2F/18eb2042-91cf-38e6-b280-8bef570522d7,E5:53:1E:24:96:2F/3af9ac1c-c3a5-36f7-a737-4868789e2832,E5:53:1E:24:96:2F/a3ad12b7-06e9-31be-bcc9-4cd0249b5562,E5:53:1E:24:96:2F/c697eede-6a0a-3d21-8936-3a7f86a830ee,E8:97:A0:6C:3B:24/0e55db4e-b72e-3e9c-9468-d4ef44cb069c,E8:97:A0:6C:3B:24/3af9ac1c-c3a5-36f7-a737-4868789e2832,E8:97:A0:6C:3B:24/5cc80f56-5657-302f-80a2-769e378f37f2,E8:97:A0:6C:3B:24/c697eede-6a0a-3d21-8936-3a7f86a830ee,E8:97:A0:6C:3B:24/d3eedeb6-a50a-35bb-9a2c-d9626d3d4b3e,E8:97:A0:6C:3B:24/da2c6c1a-c379-3ccb-8392-3a816b474af2,EB:78:55:87:E9:E5/09b1e796-8c3b-3475-9e45-a8d31f93649b,EB:78:55:87:E9:E5/0e55db4e-b72e-3e9c-9468-d4ef44cb069c,EB:78:55:87:E9:E5/1201aae4-b97c-3ec7-8ad3-869e3a8a1d25,EB:78:55:87:E9:E5/3af9ac1c-c3a5-36f7-a737-4868789e2832,EB:78:55:87:E9:E5/6090e946-3b7f-3f74-aeae-e7202f6c8d69,EB:78:55:87:E9:E5/c697eede-6a0a-3d21-8936-3a7f86a830ee)")

with open('data/data.csv', 'r') as file:
    dr = csv.DictReader(file)
    to_db = [(
        i['time'],
        i['id'],
        i['lat'],
        i['lon'],
        i['C2:9B:38:AF:12:75/09b1e796-8c3b-3475-9e45-a8d31f93649b'],
        i['C2:9B:38:AF:12:75/0e55db4e-b72e-3e9c-9468-d4ef44cb069c'],
        i['C2:9B:38:AF:12:75/2ab77db3-5669-3f2c-842a-760e4ae0ef4c'],
        i['C2:9B:38:AF:12:75/3af9ac1c-c3a5-36f7-a737-4868789e2832'],
        i['C2:9B:38:AF:12:75/c697eede-6a0a-3d21-8936-3a7f86a830ee'],
        i['C2:9B:38:AF:12:75/f9c1476f-1603-397a-a451-2a30c91dbe5c'],
        i['D7:85:88:F5:88:4C/0e55db4e-b72e-3e9c-9468-d4ef44cb069c'],
        i['D7:85:88:F5:88:4C/3af9ac1c-c3a5-36f7-a737-4868789e2832'],
        i['D7:85:88:F5:88:4C/66bd8860-6e87-3544-b022-1abaf04ce4ca'],
        i['D7:85:88:F5:88:4C/c697eede-6a0a-3d21-8936-3a7f86a830ee'],
        i['D7:85:88:F5:88:4C/c77e7cf1-12bc-36be-9270-c8d56e131eac'],
        i['D7:85:88:F5:88:4C/d3eedeb6-a50a-35bb-9a2c-d9626d3d4b3e'],
        i['DA:B5:6B:DD:72:60/09b1e796-8c3b-3475-9e45-a8d31f93649b'],
        i['DA:B5:6B:DD:72:60/0e55db4e-b72e-3e9c-9468-d4ef44cb069c'],
        i['DA:B5:6B:DD:72:60/3af9ac1c-c3a5-36f7-a737-4868789e2832'],
        i['DA:B5:6B:DD:72:60/4552091f-a928-358f-8ae8-be7f9b8d89fe'],
        i['DA:B5:6B:DD:72:60/66bd8860-6e87-3544-b022-1abaf04ce4ca'],
        i['DA:B5:6B:DD:72:60/c697eede-6a0a-3d21-8936-3a7f86a830ee'],
        i['E5:53:1E:24:96:2F/09b1e796-8c3b-3475-9e45-a8d31f93649b'],
        i['E5:53:1E:24:96:2F/0e55db4e-b72e-3e9c-9468-d4ef44cb069c'],
        i['E5:53:1E:24:96:2F/18eb2042-91cf-38e6-b280-8bef570522d7'],
        i['E5:53:1E:24:96:2F/3af9ac1c-c3a5-36f7-a737-4868789e2832'],
        i['E5:53:1E:24:96:2F/a3ad12b7-06e9-31be-bcc9-4cd0249b5562'],
        i['E5:53:1E:24:96:2F/c697eede-6a0a-3d21-8936-3a7f86a830ee'],
        i['E8:97:A0:6C:3B:24/0e55db4e-b72e-3e9c-9468-d4ef44cb069c'],
        i['E8:97:A0:6C:3B:24/3af9ac1c-c3a5-36f7-a737-4868789e2832'],
        i['E8:97:A0:6C:3B:24/5cc80f56-5657-302f-80a2-769e378f37f2'],
        i['E8:97:A0:6C:3B:24/c697eede-6a0a-3d21-8936-3a7f86a830ee'],
        i['E8:97:A0:6C:3B:24/d3eedeb6-a50a-35bb-9a2c-d9626d3d4b3e'],
        i['E8:97:A0:6C:3B:24/da2c6c1a-c379-3ccb-8392-3a816b474af2'],
        i['EB:78:55:87:E9:E5/09b1e796-8c3b-3475-9e45-a8d31f93649b'],
        i['EB:78:55:87:E9:E5/0e55db4e-b72e-3e9c-9468-d4ef44cb069c'],
        i['EB:78:55:87:E9:E5/1201aae4-b97c-3ec7-8ad3-869e3a8a1d25'],
        i['EB:78:55:87:E9:E5/3af9ac1c-c3a5-36f7-a737-4868789e2832'],
        i['EB:78:55:87:E9:E5/6090e946-3b7f-3f74-aeae-e7202f6c8d69'],
        i['EB:78:55:87:E9:E5/c697eede-6a0a-3d21-8936-3a7f86a830ee']
    ) for i in dr]

cur.executemany("insert into raw_data  values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", to_db)
con.commit()
con.close()
