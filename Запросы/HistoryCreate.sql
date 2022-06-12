CREATE TABLE IF NOT EXISTS History (
ID INT PRIMARY KEY,
Data_Entry DATE NOT NULL,
Data_Exit DATE,
block BOOL,
ID_employeers VARCHAR(255) NOT NULL,
FOREIGN KEY (ID_employeers) REFERENCES Employee (ID_Employee)
);