***********
 csv-merge
***********


Problem Description
-------------------
Read a list of csv files and merge them into one file.

There are three provided csv files in ./data, with an
inconsistent format. Normalize the data before merging
them.

Headers from the CSV files::

  # data/yellowtail_fcu.csv
  Department,Host,IP Address,OS,Function
  #data/yellowtail_financial_services.csv
  Name,IP,Dept,Operating System,Function
  #data/yellowtail_national_bank.csv
  hostname,IPAddress,Department,OS,Function

The consolidated csv file should look like this::

  Host Name,IP Address,Department,OS,Function
  ny-res-fw,192.250.29.243,Research,Cisco,firewall
  la-sec-sw,172.46.97.47,Security,Cisco,switch
  sf-res-fw,172.11.180.248,Research,Cisco,firewall
  ny-fin-sw,10.50.216.77,Finance,Cisco,switch
  ...


Implementation
--------------
This is implemented as a cli utility. To run it, use::

    ∿ csv-merge \
        --input data/yellowtail_fcu.csv \
        --input data/yellowtail_financial_services.csv \
        --input data/yellowtail_national_bank.csv \
        --output data/output.csvN

    ∿ head -n2 data/output.csv
    Department,Host Name,IP Address,OS,Function
    Finance,was-fin-web,172.57.191.179,Mac,web

