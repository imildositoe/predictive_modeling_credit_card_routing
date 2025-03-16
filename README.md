# __Credit Card Routing System__

This is the main notebook of the project and is divided by 2 files (this and app.py). This file is subdivided by:
- Main Imports: import all the libraries needed for the project
- Read Data: read the data from the excel sheet dataset
- Exploratory Data Analysis: explore the data for consequent analysis and development of the model
- Data Preparation
- Modeling
- Evaluation
- End-user GUI

Below some screenshot results of the project:

- <div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>tmsp</th>
      <th>country</th>
      <th>amount</th>
      <th>success</th>
      <th>PSP</th>
      <th>3D_secured</th>
      <th>card</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>2019-01-01 00:01:11</td>
      <td>Germany</td>
      <td>89</td>
      <td>0</td>
      <td>UK_Card</td>
      <td>0</td>
      <td>Visa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2019-01-01 00:01:17</td>
      <td>Germany</td>
      <td>89</td>
      <td>1</td>
      <td>UK_Card</td>
      <td>0</td>
      <td>Visa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2019-01-01 00:02:49</td>
      <td>Germany</td>
      <td>238</td>
      <td>0</td>
      <td>UK_Card</td>
      <td>1</td>
      <td>Diners</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>2019-01-01 00:03:13</td>
      <td>Germany</td>
      <td>238</td>
      <td>1</td>
      <td>UK_Card</td>
      <td>1</td>
      <td>Diners</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>2019-01-01 00:04:33</td>
      <td>Austria</td>
      <td>124</td>
      <td>0</td>
      <td>Simplecard</td>
      <td>0</td>
      <td>Diners</td>
    </tr>
  </tbody>
</table>
</div>

![image](https://github.com/user-attachments/assets/eb96c869-829f-42f1-af42-a4c39cdf0aec)

![image](https://github.com/user-attachments/assets/0ff48d59-44d5-47b3-849a-106818aa122f)

![image](https://github.com/user-attachments/assets/a7c7a53e-3921-417a-aa9e-439de6eba7a8)

![image](https://github.com/user-attachments/assets/1da9dacf-598c-4ac1-ab6c-897eba966304)

<div>
<br>
  
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>tmsp</th>
      <th>country</th>
      <th>amount</th>
      <th>success</th>
      <th>PSP</th>
      <th>3D_secured</th>
      <th>card</th>
      <th>retry</th>
      <th>hour</th>
      <th>day_of_week</th>
      <th>month</th>
      <th>PSP_code</th>
      <th>transaction_cost</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>9238</th>
      <td>9238</td>
      <td>2019-01-10 03:49:12</td>
      <td>Austria</td>
      <td>6</td>
      <td>0</td>
      <td>Moneycard</td>
      <td>0</td>
      <td>Diners</td>
      <td>0</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>4.5</td>
    </tr>
    <tr>
      <th>9239</th>
      <td>9239</td>
      <td>2019-01-10 03:49:37</td>
      <td>Austria</td>
      <td>6</td>
      <td>0</td>
      <td>Simplecard</td>
      <td>0</td>
      <td>Diners</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>22742</th>
      <td>22742</td>
      <td>2019-01-27 14:01:11</td>
      <td>Austria</td>
      <td>6</td>
      <td>1</td>
      <td>Simplecard</td>
      <td>0</td>
      <td>Master</td>
      <td>0</td>
      <td>14</td>
      <td>6</td>
      <td>1</td>
      <td>3</td>
      <td>1.5</td>
    </tr>
    <tr>
      <th>33737</th>
      <td>33737</td>
      <td>2019-02-08 05:02:33</td>
      <td>Austria</td>
      <td>6</td>
      <td>0</td>
      <td>UK_Card</td>
      <td>0</td>
      <td>Diners</td>
      <td>0</td>
      <td>5</td>
      <td>4</td>
      <td>2</td>
      <td>2</td>
      <td>1.5</td>
    </tr>
    <tr>
      <th>33738</th>
      <td>33738</td>
      <td>2019-02-08 05:02:37</td>
      <td>Austria</td>
      <td>6</td>
      <td>0</td>
      <td>UK_Card</td>
      <td>0</td>
      <td>Diners</td>
      <td>1</td>
      <td>5</td>
      <td>4</td>
      <td>2</td>
      <td>2</td>
      <td>1.5</td>
    </tr>
  </tbody>
</table>
</div>


![image](https://github.com/user-attachments/assets/ba34a7fb-8a28-4c8d-b1dc-d4bb8bce37d8)

![image](https://github.com/user-attachments/assets/efa81410-7d2d-4cd6-8bf6-a163f2c1fb8d)

![image](https://github.com/user-attachments/assets/f6cba7f5-bcff-43bc-8b1b-d8862236d43d)

![image](https://github.com/user-attachments/assets/951f78ff-9d2e-4c55-93c6-b11d232f8d99)








